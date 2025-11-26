import streamlit as st
from jamaibase import JamAI, types as t
import time

# ==========================================
# 1. SETUP & KEYS 
# ==========================================
# Our API Keys. This connects our Python code to the JamAI brain
# API_KEY = The password. PROJECT_ID = The house. TABLE_ID = The specific room
API_KEY = "PASTE_YOUR_API_KEY_HERE"
PROJECT_ID = "PASTE_YOUR_PROJECT_ID_HERE"
TABLE_ID = "biasiwabuddy"

# TIP: We use @st.cache_resource here
# Why? So Streamlit doesn't reconnect to JamAI every time we click a button
# Keeps the app fast and smooth
@st.cache_resource 
def get_jamai_client():
    return JamAI(token=API_KEY, project_id=PROJECT_ID)

# Try to connect. If fail, show error immediately
try:
    jamai = get_jamai_client()
except Exception as e:
    st.error(f"Alamak! Connection failed: {e}")
    st.stop()

# ==========================================
# 2. DESIGN & CSS (Bagi Cantik Sikit)
# ==========================================
# Set layout to 'wide' so the dashboard looks like a pro app, not a blog
st.set_page_config(
    page_title="Biasiswa Buddy", 
    page_icon="🎓", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS overrides. 
# We want a Dark Blue sidebar to look premium + High contrast text.
st.markdown("""
<style>
    /* Make sidebar Dark Blue */
    [data-testid="stSidebar"] { background-color: #0F172A ; }
    
    /* Force sidebar text to White (otherwise cannot see anything) */
    [data-testid="stSidebar"] * { color: #F8FAFC !important; }
    
    /* Fix the input boxes so they are white with black text */
    [data-testid="stSidebar"] input, [data-testid="stSidebar"] div[data-baseweb="select"] > div { 
        color: #000000 !important; 
        background-color: #ffffff !important; 
        -webkit-text-fill-color: #000000 !important; 
    }
    
    /* Style the main button to be Gradient Blue (More 'Ong') */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #2563EB 0%, #1D4ED8 100%);
        color: white;
        border-radius: 8px;
        font-weight: bold;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. SIDEBAR INPUTS (User Data)
# ==========================================
with st.sidebar:
    st.title("🎓 Biasiswa Buddy")
    
    # Input 1: Language Preference (For Local Impact)
    language = st.radio("Language / Bahasa", ["English", "Bahasa Malaysia"], index=1)
    
    # Input 2: State (Crucial for filtering state-specific scholarships like Yayasan Sarawak)
    origin = st.selectbox("Negeri / State", ["Johor", "Kedah", "Kelantan", "Malacca", "Negeri Sembilan", "Pahang", "Penang", "Perak", "Perlis", "Sabah", "Sarawak", "Selangor", "Terengganu", "Other"])
    
    # Input 3: Results (e.g., 6A) - AI will use this to filter requirements
    result = st.text_input("Keputusan SPM / SPM Result", placeholder="e.g., 6A 2B")
    
    st.markdown("---")
    
    # The Big Button to trigger the AI
    btn_label = "🚀 Generate Strategy" if language == "English" else "🚀 Hasilkan Pelan"
    btn_search = st.button(btn_label, type="primary")

# ==========================================
# 4. BACKEND LOGIC (The Brain)
# ==========================================
# Initialize session state so data doesn't disappear when we switch tabs
if 'scholarship_res' not in st.session_state:
    st.session_state['scholarship_res'] = None
if 'essay_res' not in st.session_state:
    st.session_state['essay_res'] = None

# LOGIC A: User clicks "Generate Strategy" on Sidebar
# Goal: Retrieve the list of scholarships from JamAI Action Table
if btn_search:
    msg = "AI is analyzing database..." if language == "English" else "AI sedang menganalisis data..."
    
    with st.spinner(f'🤖 {msg}'):
        try:
            # Sending data to JamAI Action Table (Phase 1)
            completion = jamai.table.add_table_rows(
                table_type=t.TableType.ACTION,
                request=t.RowAddRequest(
                    table_id=TABLE_ID,
                    data=[{
                        "User_Input": f"Result: {result}, State: {origin}", # Combine info for RAG
                        "Language": language,
                        "key_strength&achievement": "N/A" # Empty for now, we just want the list first
                    }],
                    stream=False
                )
            )
            
            # Get the result from the 'Scholarship_Data' LLM column
            res = completion.rows[0].columns["Scholarship_Data"].text 
            
            # Save to memory
            st.session_state['scholarship_res'] = res
            st.session_state['essay_res'] = None # Clear old essay if any
            
        except Exception as e:
            st.error(f"Connection Error: {e}")

# ==========================================
# 5. DASHBOARD DISPLAY (The Output)
# ==========================================
st.markdown(f"## Your Strategy Dashboard" if language == "English" else f"## Papan Pemuka Strategi Anda")

# Divide into Tabs for better UX
t1, t2 = st.tabs(["💰 Scholarship Match"if language == "English" else "💰 Biasiswa Sesuai", "✍️ Essay Assistant"if language == "English" else "✍️ Asisten Esei"])

# --- TAB 1: SCHOLARSHIP LIST ---
with t1:
    if st.session_state['scholarship_res']:
        # Render the AI response as Markdown (It includes formatting & emojis)
        st.markdown(st.session_state['scholarship_res'])
    else:
        # Placeholder if no data yet
        st.info("👈 Please fill in the information on the left to begin" if language == "English" else "👈 Sila isi maklumat di sebelah kiri untuk mula")

# --- TAB 2: AI ESSAY WRITER ---
with t2:
    st.subheader("Essay Draft Generator" if language == "English" else "Penjana Draf Esei")
    
    # We ask for extra info here: Key Strengths
    st.markdown("**Key Strengths / Kekuatan Utama**")
    user_strengths = st.text_area("List achievements:"if language == "English" else "Senaraikan Pencapaian:", height=120)
    
    draft_label = "✨ Draft Personal Statement" if language == "English" else "✨ Jana Draf Esei"
    
    # LOGIC B: User clicks "Draft Essay" inside Tab 2
    if st.button(draft_label):
        # Check if user ran the main search first
        if not st.session_state['scholarship_res']:
            st.warning("⚠️ Generate Strategy first!")
        else:
            with st.spinner("AI writing..."if language == "English" else "AI sedang menulis..."):
                try:
                    # Call JamAI again (Phase 2), but this time WITH 'user_strengths'
                    completion = jamai.table.add_table_rows(
                        table_type=t.TableType.ACTION,
                        request=t.RowAddRequest(
                            table_id=TABLE_ID,
                            data=[{
                                "User_Input": f"Result: {result}, State: {origin}",
                                "Language": language,
                                "key_strength&achievement": user_strengths # Pass the strengths to LLM
                            }],
                            stream=False
                        )
                    )
                    # Get result from the 'essay_writter' LLM column
                    essay_draft = completion.rows[0].columns["essay_writter"].text
                    st.session_state['essay_res'] = essay_draft
                except Exception as e:
                    st.error(f"Error: {e}")

    # Display the generated essay
    if st.session_state['essay_res']:
        st.success("Done!"if language == "English" else "Siap!")
        st.markdown("### 📄 Your AI Draft"if language == "English" else "### 📄 Draf AI Anda")
        st.text_area("Copy below:"if language == "English" else "Rujuk kandungan di bawah:", st.session_state['essay_res'], height=400)
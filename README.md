# 🎓 Biasiswa-Buddy
An AI-powered scholarship strategist for Malaysian students. Built with JamAI Base &amp; Streamlit


<div align="center">
  <h3>📊 1. Smart Scholarship Dashboard</h3>
  <p><i>Automatically matches scholarships based on your SPM results and state.</i></p>
  <img src="https://github.com/user-attachments/assets/077dc8b9-c9ec-4639-ad01-8188b79264c9" width="95%" />
  
  <br/><br/> <h3>✍️ 2. AI Essay Assistant</h3>
  <p><i>Generates personalized personal statement drafts based on your achievements.</i></p>
  <img src="https://github.com/user-attachments/assets/948c1e1e-bd56-40c6-bbce-e900b1665b7b" width="95%" />
</div>

---
## 🎥 Demo Video
https://youtu.be/pSTqQ7U6_t0
---

## Table of Contents
- [🌟 The Problem](#-the-problem)
- [🚀 The Solution](#-the-solution-biasiswa-buddy)
- [🛠️ Tech Stack](#️-tech-stack)
- [💻 Installation & Setup Guide](#-installation--setup-guide)

---
  
## 🌟 The Problem

- **Scattered Information:** Scholarship details are **not in one place**. Students must check dozens of different websites
- **Wasted Time:** The search process is **long and confusing**, leading students to waste time filtering irrelevant options.
- **Missed Deadlines:** Many students **lose opportunities** because application windows close before they find them.
- **Financial Stress:** Difficulty finding financial aid creates **unnecessary worry and stress**.

---

## 🚀 The Solution: *Biasiswa Buddy*

**Biasiswa Buddy** is more than a search tool, it is an **AI Scholarship Strategist** designed to help Malaysian students secure funding effortlessly.

### What It Does:
1. **All Scholarships in One Place:** Centralizes every major Malaysian scholarship.
2. **AI Matching by Results:** Instantly ranks scholarships based on the student's actual grades.
3. **Deadline Tracking:** Automatically lists upcoming closing dates.
4. **Essay Assistant:** Provides templates, guidance, and AI-generated drafts.
5. **Video Resources:** Curates the best scholarship tips and experiences shared by seniors.

---

## 🛠️ Tech Stack

**Frontend**
- Streamlit (UI, input forms, dashboard)

**Backend**
- JamAI Base (LLM engine, embeddings, RAG)
- Python (Streamlit ↔ JamAI API connector)
- REST API (data communication)

**Data Layer**
- CSV file (scholarship dataset)
- JamAI Knowledge Table (embeddings + retrieval)

---

## 💻 Installation & Setup Guide
Follow these steps to run **Biasiswa Buddy** on your local machine.

### 1. Prerequisites
Ensure you have **Python 3.13** (or compatible version) installed.

### 2. Clone the Repository
```bash
git clone https://github.com/zoeywongzixin/Biasiswa-Buddy.git
cd Biasiswa-Buddy
```

### 3. Setup JamAI Backend 
You need to import our pre-configured "Brain" (Tables, Prompts & Data) into your JamAI account.

1. Download the file **biasiswabuddy.parquet** in this repository (folder jamaibase).
2. Log in to JamAI Base.
3. Click "Import Project".
4. Upload the biasiswabuddy.parquet file.
5. Once imported, go to Settings > API Keys to generate a new Personal Access Token (PAT).
6. Copy your New Project ID (found in the URL or Project Settings) and your PAT.

### 4. ⚙️ Configure Credentials
Open **app.py** in your code editor (VS Code, etc.) and update Lines 10 & 11:

```python
# app.py
API_KEY = "PASTE_YOUR_NEW_PAT_HERE"
PROJECT_ID = "PASTE_YOUR_NEW_PROJECT_ID_HERE"
```

### 5. Setup Environment & Install Dependencies
Run the following commands in your terminal :

```
# 1. Create a virtual environment (if you haven't)
python -m venv myenv

# 2. Allow script execution (Important for Windows)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

# 3. Activate the environment
.\myenv\Scripts\Activate.ps1
```python

# 4. Install required libraries
pip install -r requirements.txt

# 5. Run the App
streamlit run app.py
```





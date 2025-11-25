# 🎓 Biasiswa-Buddy
An AI-powered scholarship strategist for Malaysian students. Built with JamAI Base &amp; Streamlit


## 💻 Installation & Setup Guide
Follow these steps to run **Biasiswa Buddy** on your local machine.

### 1. Prerequisites
Ensure you have **Python 3.13** (or compatible version) installed.

### 2. Clone the Repository
```bash
git clone https://github.com/zoeywongzixin/Biasiswa-Buddy.git
cd Siswa-Buddy
```

### 3. Run this command to install Streamlit and JamAI SDK:
```bash
pip install -r requirements.txt
```

### 4. CONFIGURATION 
This app requires a JamAI Base API Key to function.
Open app.py in your code editor.
Locate the configuration section at the top (Lines 10):
**API_KEY = "PASTE_YOUR_JAMAI_PAT_HERE"**

### 5. Run the App
Launch the application:
```bash
streamlit run app.py
```
> **💡 Tip for Windows Users:**
> If you see a "script execution" error, try running this command in PowerShell first:
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process`
> .\myenv\Scripts\Activate.ps1
> streamlit run app.py



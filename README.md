# 🤖 Telegram ATS Resume Analyzer

An AI-powered Telegram bot that analyzes multiple resumes against a Job Description (JD), calculates an ATS (Applicant Tracking System) score, identifies missing skills and keywords, and recommends relevant courses to improve resume quality.

---

## 🚀 Features

- 📄 Upload multiple resumes (PDF/DOCX)
- 📋 Upload a Job Description (PDF/DOCX)
- 🎯 ATS Score calculation for each resume
- ✅ Skill matching with the Job Description
- ❌ Missing skills detection
- 📝 AI-powered resume improvement suggestions
- 🔑 Missing keyword identification
- 🎓 Personalized course recommendations using Google Gemini AI
- 🤖 Interactive Telegram Bot interface

---

## 🛠️ Tech Stack

- **Language:** Python
- **Framework:** Aiogram
- **AI Model:** Google Gemini API
- **Machine Learning:** Scikit-learn (TF-IDF & Cosine Similarity)
- **Document Parsing:** PyPDF2, python-docx
- **Version Control:** Git & GitHub

---

## 📂 Project Structure

```text
telegram-ats-bot/
│
├── ai/
│   └── ai_service.py
│
├── handlers/
│   ├── analyze.py
│   ├── start.py
│   └── upload.py
│
├── parsers/
│   └── extractor.py
│
├── services/
│   ├── ats_service.py
│   └── skill_matcher.py
│
├── states/
│   └── upload_state.py
│
├── uploads/
│
├── bot.py
├── config.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Rahul-prog839/telegram-ats-resume-analyzer.git
```

### 2. Navigate to the project

```bash
cd telegram-ats-resume-analyzer
```

### 3. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create a `.env` file

```env
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

### 6. Run the bot

```bash
python bot.py
```

---

## 📌 How It Works

1. Start the Telegram bot.
2. Upload one or more resumes.
3. Type `/done`.
4. Upload the Job Description.
5. The bot:
   - Extracts text from resumes and the JD.
   - Computes the ATS score.
   - Identifies matched and missing skills.
   - Uses Google Gemini to generate improvement suggestions.
   - Recommends relevant courses based on missing skills.

---

## 📊 Sample Output

```text
📄 Resume: Rahul.pdf

🎯 ATS Score: 78.42/100

✅ Matched Skills
Python, SQL, AWS

❌ Missing Skills
Power BI, Tableau

📌 Summary
Strong software engineering profile with good backend development skills.

📝 Resume Improvements
• Add analytics-based projects
• Quantify achievements
• Include relevant certifications

🔑 Missing Keywords
• Power BI
• Tableau
• Dashboard
• Business Analytics

🎓 Recommended Courses
• Microsoft Power BI Data Analyst (Coursera)
• Excel Skills for Business (Coursera)

🏆 Final Verdict
Good fit with minor resume improvements.
```

---

## 🔮 Future Enhancements

- 📈 Resume ranking dashboard
- 📊 Skill gap visualisation
- 📄 Export ATS report as PDF
- 🌐 Web dashboard using React or Streamlit
- 📧 Email report generation
- 🌍 Multi-language support
- 📦 Docker support for deployment

---

## 👨‍💻 Author

**Rahul Aakiri**

- GitHub: https://github.com/Rahul-prog839

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
import os
import shutil

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.upload_state import UploadState
from parsers.extractor import extract_text
from services.ats_service import ATSAnalyzer
from services.skill_matcher import find_missing_skills
from ai.ai_service import analyze_resume as ai_analyze_resume

router = Router()


@router.message(
    UploadState.waiting_for_jd,
    F.document
)
async def analyze_jd(message: Message, state: FSMContext):

    user_id = str(message.from_user.id)

    # Save Job Description
    jd_folder = os.path.join(
        "uploads",
        "jd",
        user_id
    )
    os.makedirs(jd_folder, exist_ok=True)

    jd_path = os.path.join(
        jd_folder,
        message.document.file_name
    )

    file = await message.bot.get_file(
        message.document.file_id
    )

    await message.bot.download_file(
        file.file_path,
        jd_path
    )

    await message.answer(
        "🤖 Analyzing resumes...\n\nPlease wait..."
    )

    jd_text = extract_text(jd_path)

    resume_folder = os.path.join(
        "uploads",
        "resumes",
        user_id
    )

    analyzer = ATSAnalyzer()

    # Analyze each resume
    for resume in os.listdir(resume_folder):

        resume_path = os.path.join(
            resume_folder,
            resume
        )

        resume_text = extract_text(
            resume_path
        )

        score = analyzer.calculate_score(
            resume_text,
            jd_text
        )

        matched, missing = find_missing_skills(
            resume_text,
            jd_text
        )

        ai_report = ai_analyze_resume(
            resume_text,
            jd_text,
            score,
            matched,
            missing
        )

        summary = ai_report.get(
            "summary",
            "Not Available"
        )

        resume_improvements = "\n".join(
            f"• {item}"
            for item in ai_report.get(
                "resume_improvements",
                []
            )
        ) or "None"

        missing_keywords = "\n".join(
            f"• {item}"
            for item in ai_report.get(
                "missing_keywords",
                []
            )
        ) or "None"

        courses = "\n".join(
            f"• {course.get('course')} ({course.get('platform')})"
            for course in ai_report.get(
                "recommended_courses",
                []
            )
        ) or "None"

        final_verdict = ai_report.get(
            "final_verdict",
            "Not Available"
        )

        await message.answer(
            f"""📄 Resume: {resume}

🎯 ATS Score: {score:.2f}/100

✅ Matched Skills
{', '.join(matched) if matched else 'None'}

❌ Missing Skills
{', '.join(missing) if missing else 'None'}

📌 Summary
{summary}

📝 Resume Improvements
{resume_improvements}

🔑 Missing Keywords
{missing_keywords}

🎓 Recommended Courses
{courses}

🏆 Final Verdict
{final_verdict}
"""
        )

    # Delete uploaded resumes after analysis
    if os.path.exists(resume_folder):
        shutil.rmtree(resume_folder)

    # Delete uploaded job description after analysis
    if os.path.exists(jd_folder):
        shutil.rmtree(jd_folder)

    # Clear FSM state
    await state.clear()
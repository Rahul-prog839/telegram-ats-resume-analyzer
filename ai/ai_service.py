import json
from google import genai
from google.genai.errors import ClientError
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def analyze_resume(
    resume_text,
    jd_text,
    ats_score,
    matched_skills,
    missing_skills
):

    prompt = f"""
You are an expert ATS Resume Analyzer.

Analyze the resume against the Job Description and provide a concise ATS evaluation.

Resume:
{resume_text}

Job Description:
{jd_text}

ATS Score:
{ats_score}

Matched Skills:
{', '.join(matched_skills)}

Missing Skills:
{', '.join(missing_skills)}

Return ONLY valid JSON.

JSON Format:

{{
  "summary": "",
  "strengths": [],
  "weaknesses": [],
  "resume_improvements": [],
  "missing_keywords": [],
  "recommended_courses": [
    {{
      "course": "",
      "platform": ""
    }}
  ],
  "final_verdict": ""
}}

Rules:
1. Return ONLY valid JSON.
2. Do NOT use markdown or ```json.
3. Do NOT recalculate the ATS score.
4. Explain the ATS score in at most 2 short sentences.
5. Keep the entire response under 150 words.
6. Summary: maximum 2 sentences.
7. Strengths: maximum 3 short bullet points.
8. Weaknesses: maximum 3 short bullet points.
9. Resume Improvements: maximum 3 short bullet points.
10. Missing Keywords: maximum 5 keywords only.
11. Recommend exactly 2 relevant courses.
12. For each course return only:
    - course
    - platform
13. Recommend courses only for missing skills.
14. Final Verdict: one short sentence (maximum 15 words).
15. Do not repeat information across sections.
16. Use concise bullet points (5-8 words each).
17. Focus only on the highest-impact improvements.
"""

    try:

        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )

        text = response.text.strip()

        if text.startswith("```json"):
            text = text.replace("```json", "").replace("```", "").strip()

        elif text.startswith("```"):
            text = text.replace("```", "").strip()

        return json.loads(text)

    except ClientError as e:

        return {
            "summary": f"Gemini API Error: {str(e)}",
            "strengths": [],
            "weaknesses": [],
            "resume_improvements": [],
            "missing_keywords": [],
            "recommended_courses": [],
            "final_verdict": ""
        }

    except json.JSONDecodeError:

        return {
            "summary": text if 'text' in locals() else "Gemini returned invalid JSON.",
            "strengths": [],
            "weaknesses": [],
            "resume_improvements": [],
            "missing_keywords": [],
            "recommended_courses": [],
            "final_verdict": ""
        }

    except Exception as e:

        return {
            "summary": f"Unexpected Error: {str(e)}",
            "strengths": [],
            "weaknesses": [],
            "resume_improvements": [],
            "missing_keywords": [],
            "recommended_courses": [],
            "final_verdict": ""
        }
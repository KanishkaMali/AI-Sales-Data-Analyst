# ==========================================================
# ai_explainer.py
# AI Business Explanation Engine
# ==========================================================

from google import genai
from config import GOOGLE_API_KEY

client = genai.Client(api_key=GOOGLE_API_KEY)


def explain_result(question, analysis):

    if not analysis["success"]:
        return analysis["message"]

    result = analysis["result"].reset_index()

    prompt = f"""
You are a Senior Business Data Analyst.

The user asked:

{question}

Python has already calculated the answer.

Here is the result:

{result.to_string(index=False)}

Your job:

1. Answer the user's question.
2. Explain the business meaning.
3. Mention important numbers.
4. Give one business recommendation.
5. Keep the answer under 200 words.
6. Use simple English.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text
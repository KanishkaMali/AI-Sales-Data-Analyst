# ==========================================================
# ai_router.py
# Intelligent AI Query Router
# ==========================================================

import json
from google import genai
from config import GOOGLE_API_KEY

# ==========================================================
# Gemini Client
# ==========================================================

client = genai.Client(api_key=GOOGLE_API_KEY)


def route_question(question):

    prompt = f"""
You are an AI Query Router.

Your ONLY job is to convert the user's business question into JSON.

DO NOT explain anything.

DO NOT calculate anything.

Return ONLY valid JSON.

------------------------------------------------

Dataset Columns

Sales
Profit
Quantity
Discount
Category
Sub-Category
Region
State
City
Segment
Ship Mode
Customer Name
Product Name
Order Date
Year
Month

------------------------------------------------

Allowed Metrics

Sales
Profit
Quantity
Discount

------------------------------------------------

Allowed Dimensions

State
Region
Category
Sub-Category
City
Customer Name
Product Name
Segment
Ship Mode
Year
Month

------------------------------------------------

Allowed Operations

max
min
sum
average
top
bottom

------------------------------------------------

top_n

If user says

Top 10

return

10

If user says

Top 5

return

5

Otherwise return

1

------------------------------------------------

Filters

Examples

Region = West

State = California

Category = Technology

Segment = Consumer

Year = 2017

------------------------------------------------

User Question

{question}

------------------------------------------------

Return ONLY JSON

Example

{{
    "metric":"Sales",
    "dimension":"State",
    "operation":"max",
    "top_n":1,
    "filters":{{
        "Region":"West",
        "Year":2017
    }}
}}

"""

    response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)

    text = response.text.strip()

    # Remove Markdown if Gemini returns it
    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    try:

        data = json.loads(text)

    except Exception:

        data = {
            "metric": None,
            "dimension": None,
            "operation": None,
            "top_n": 1,
            "filters": {}
        }

    return data
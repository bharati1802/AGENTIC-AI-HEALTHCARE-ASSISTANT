from google import genai
import os
import json
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def planner_agent(user_query):

    prompt = f"""
    You are a planner agent.

    Available actions:
    - claim_status
    - general_query

    Return ONLY JSON:
    {{
        "action": "action_name",
        "input": "user input"
    }}

    Query: {user_query}
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    text = response.text.strip()

    try:
        decision = json.loads(text)
    except:
        decision = {
            "action": "general_query",
            "input": user_query
        }

    return decision
from google import genai
import os
from dotenv import load_dotenv
from tools.claims_api import check_claim_status

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def executor_agent(plan):

    action = plan.get("action")
    user_input = plan.get("input")

    if action == "claim_status":
        return check_claim_status(user_input)

    elif action == "general_query":

        prompt = f"""
        You are a helpful healthcare assistant.

        Answer clearly:
        {user_input}
        """

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    else:
        return "Unknown action"
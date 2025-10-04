import os
from fastapi import APIRouter, HTTPException
import google.generativeai as genai
from .. import schemas

router = APIRouter()

# Configure the Gemini API
try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    print(f"Error configuring Gemini: {e}")
    model = None

@router.post("/generate-plan")
async def generate_event_plan(input_data: schemas.AIEventInput):
    if not model:
        raise HTTPException(status_code=500, detail="AI model is not configured. Check API Key.")

    # Create a detailed prompt for the LLM
    prompt = f"""
    Based on the following event details, act as an expert event planner and generate a list of suggestions for vendors and a sample timeline.

    Event Details:
    - Type: {input_data.eventType}
    - Audience Size: {input_data.audienceSize} people
    - Budget: ${input_data.budget:,.2f}
    - Location: {input_data.location or 'Not specified'}
    - Special Requirements: {input_data.specialRequirements or 'None'}

    Provide suggestions for these vendor categories:
    1.  **Venues**: Suggest 2 venue types suitable for this event.
    2.  **Catering**: Suggest 2 catering styles.
    3.  **Entertainment**: Suggest 2 entertainment options.

    Also, provide a simple, 4-item sample timeline for the event.
    Format your response clearly with headings.
    """

    try:
        response = await model.generate_content_async(prompt)
        return {"plan": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI plan generation failed: {str(e)}")

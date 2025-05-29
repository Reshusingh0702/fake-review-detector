# gemini_utils.py

from google import genai

def get_response(review_text):
    client = genai.Client(api_key="AIzaSyBMdGObIpXvm1lPiTBmBD3bldoPhEUQVYw")
    
    prompt = f"""Classify the following review as GENUINE or FAKE.

Rules:
- GENUINE reviews have proper language, structure, and meaning.
- FAKE reviews contain excessive punctuation, random characters, gibberish, or lack clear intent.

Respond with:
Label: GENUINE or FAKE
Reason: One short sentence. No special characters.

Review:
{review_text}
"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    
    return response.text

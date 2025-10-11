from google import genai
import os

def generate_horoscope(zodiac_sign):
    api_key = os.getenv('GEMINI_API_KEY')
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Készíts egy napi horoszkópot a {zodiac_sign} csillagjegy számára magyar nyelven",
    )
    return response.text
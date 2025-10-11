from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

def generate_horoscope(zodiac_sign, name):
    api_key = os.getenv('GEMINI_API_KEY')
    client = genai.Client(api_key=api_key)
    
    prompt = f"""
    Készíts egy professzionális, személyre szabott napi horoszkópot {name} számára, aki {zodiac_sign} csillagjegy.
    
    A horoszkópnak tartalmaznia kell:
    - Személyes megszólítást ({name} nevével)
    - Inspiráló bevezetőt
    - Részletes horoszkóp szöveget emojikkal
    - Napi tanácsot
    - Szép lezárást
    
    Csakis az első köszönésben használhatod a teljes nevet, a továbbiakban csak a keresztnevet.
    A HTML-t és a CSS-t úgy formázd meg, hogy férfinak és nőknek külön-külön legyen formázva maga a szöveg és a HTML/CSS kinézete, ezt név alapján döntsd el.
    Ne jelentsen problémát a Gmail-ben és a többi email kliensben való megjelenés sem a CSS-ben.
    Formázd HTML-ben, használj <h1>, <h2>, <p>, <strong> tageket és emojokat.
    Használj CSS stílusokat, ami nagyon pompás és szép.
    A válasz CSAK a HTML, CSS tartalom legyen, semmilyen magyarázat vagy kódblokk (```
    """
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    
    text = response.text
    text = text.replace(r'```html\s*', '', text)
    text = text.replace(r'```','',text)
    text = text.strip()
    
    return text

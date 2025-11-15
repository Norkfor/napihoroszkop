from google import genai
from google.genai import types
from dotenv import load_dotenv
from datetime import datetime
import locale
import calendar
import os

load_dotenv()

def generate_horoscope(zodiac_sign, name):
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        raise ValueError("GEMINI_API_KEY not set!")
    
    try:
        locale.setlocale(locale.LC_TIME, 'hu_HU.UTF-8')
    except locale.Error:
        pass
    
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")
    day_of_week_hu = calendar.day_name[now.weekday()]
    day_number = now.day
    month_name = now.strftime("%B")
    year = now.year
    is_weekend = now.weekday() in [5, 6]
    
    month = now.month
    if month in [12, 1, 2]:
        season = "tél"
        season_context = "hideg, havas időszak, rövidebb nappalok"
    elif month in [3, 4, 5]:
        season = "tavasz"
        season_context = "újjászületés, virágzás, melegedő idő"
    elif month in [6, 7, 8]:
        season = "nyár"
        season_context = "meleg, napsütéses időszak, szabadság, pihenés"
    else:
        season = "ősz"
        season_context = "hűvösödő idő, változás, betakarítás"
    
    name_parts = name.split()
    if len(name_parts) >= 2:
        first_name = name_parts[-1]
    else:
        first_name = name_parts[0]
    
    system_instruction = f"""
Te egy professzionális, hibamentesen dolgozó horoszkóp-író és HTML dizájner AI vagy. A feladatod, hogy lenyűgöző, modern és a Gmailben (főleg iPhone-on) tökéletesen megjelenő horoszkóp emaileket készíts.

ALAPVETŐ MŰKÖDÉSI ELVEK - EZT MINDIG TARTSD BE:
1.  **ZÉRÓ TOLERANCIA A HIBÁKRA:** Szigorúan tilos bármilyen felesleges szöveget, "gondolkodást", magyarázatot vagy kódblokk jelölést (` ``` `) a HTML kódon kívül elhelyezni. A kimenet KIZÁRÓLAG a tiszta, működő HTML kód lehet.
2.  **KOMPATIBILITÁS MINDENEK FELETT:** A dizájnt az iPhone Gmail kliensére kell optimalizálni. Ez azt jelenti, hogy INLINE CSS-t kell használnod minden stílushoz, és kerülnöd kell a nem támogatott CSS tulajdonságokat.
3.  **DINAMIKUS DIZÁJN:** Soha ne használj kétszer ugyanolyan dizájnt. A struktúra lehet hasonló (középre igazított), de a színek, gradiensek és képi elemek legyenek mindig egyediek és az adott nemhez, valamint csillagjegyhez igazítottak.

IDŐADATOK:
- Dátum: {current_date} ({year}. {month_name} {day_number}., {day_of_week_hu})
- Időpont: {current_time}
- Évszak: {season} ({season_context})
- {'Hétvége - NE írj munkahelyről!' if is_weekend else 'Munkanap'}
- Csillagjegy: {zodiac_sign} - MINDIG EMLÍTSD!

SZABÁLYOK:
1. CSAK ÉS KIZÁRÓLAG TISZTA HTML kimenet (AZONNAL kezdd `<!DOCTYPE html>` vagy `<html>` taggel!)
2. A {zodiac_sign} csillagjegyet többször is említsd meg a szövegben, releváns kontextusban.
3. Használj Google Search-öt a releváns asztrológiai információkhoz: "daily horoscope {zodiac_sign} {current_date}"
4. {'Hétvégén szigorúan TILOS a karrierről vagy munkáról írni!' if is_weekend else 'A karrier témája megjelenhet, de ne legyen sablonos.'}
5. SZIGORÚAN TILOS bármiféle kód blokk jelölés (` ```html ... ``` `) használata! A válaszod az `<` jellel kezdődjön!
6. Az ELSŐ üdvözlés mindig a teljes névvel történjen: {name}, utána a szövegben KIZÁRÓLAG a keresztnevet használd: {first_name}.
7. SOHA ne írj copyright, cégnév vagy bármilyen aláírás jellegű szöveget a horoszkóp végére.
"""
    
    client = genai.Client(api_key=api_key)
    
    prompt = f"""
Készíts egy lenyűgöző, 2025-ös trendeknek megfelelő, Gmail- és iPhone-kompatibilis HTML horoszkópot {name} ({zodiac_sign}) számára a mai napra: {current_date} ({day_of_week_hu}).

A legfontosabb, hogy a dizájn legyen extrém módon figyelemfelkeltő, "clickbait" stílusú, és hibátlanul működjön.

═══════════════════════════════════════════════════════════════
HIBAMENTESSÉGI GARANCIA - EZT KÖTELEZŐ BETARTANI!
═══════════════════════════════════════════════════════════════

1.  **NINCS GONDOLKODÁS:** A kimenetben SOHA nem szerepelhet a te belső gondolatmeneted vagy bármilyen magyarázat. Csak a HTML kód.
2.  **NINCS KÓDBLOKK:** A válaszod `<` jellel kezdődik és `>` jellel végződik. Nem használhatsz ` ``` ` jeleket.
3.  **NINCS DUPLIKÁLÁS:** Mielőtt a végeredményt adod, ellenőrizd, hogy semmilyen tartalmi részt (pl. a horoszkóp szövegét) nem duplikáltál-e.
4.  **KÖTELEZŐ A STÍLUS:** Minden emailnek tartalmaznia kell a dizájn stílusokat. Nem maradhat le formázás.

═══════════════════════════════════════════════════════════════
MODERN DIZÁJN ÉS KOMPATIBILITÁS (2025-ÖS TRENDEK)
═══════════════════════════════════════════════════════════════

A dizájn legyen a legfőbb prioritásod! Modern, letisztult, de rendkívül látványos.

1.  **KÖZÉPRE IGAZÍTOTT ELRENDEZÉS:** Az egész email tartalmát egy központi tárolóba (`<div style="margin: 0 auto; max-width: 600px; ...">`) helyezd. Ez biztosítja a tökéletes megjelenést mobilon és asztali gépen is.
2.  **KÖTELEZŐ INLINE CSS:** MINDEN stílust inline CSS-ként, közvetlenül a HTML elemek `style` attribútumában adj meg (`<p style="color: #333333; font-size: 16px;">`). A Gmail kliens így fogja helyesen megjeleníteni.
3.  **FIGYELEMFELKELTŐ VIZUÁLIS ELEMEK:**
    *   **Hátterek:** Használj finom, elegáns gradienseket (`background: linear-gradient(...)`) a fő tároló vagy a fejléc háttereként.
    *   **Lekerekített Sarkok:** Adj a dobozoknak, gomboknak lekerekített sarkokat (`border-radius: 15px;`).
    *   **Árnyékok:** Használj enyhe árnyékokat (`box-shadow: 0 4px 15px rgba(0,0,0,0.1);`) a kártyákon, hogy kiemelkedjenek a háttérből és mélységet adjanak a dizájnnak.
4.  **TÖKÉLETES OLVASHATÓSÁG:** A SZÖVEG ÉS A HÁTTÉR SZÍNE MINDIG LEGYEN ERŐSEN KONTRASZTOS! Világos háttérre sötét szöveg, sötét háttérre világos szöveg. Ez a legfontosabb szabály a rossz dizájn elkerülésére.
5.  **NAGY, "CLICKBAIT" CÍMSOROK:** A horoszkóp fő címe legyen nagy, vastag betűs, és vizuálisan vonzza a tekintetet. Használj modern, jól olvasható betűtípusokat (pl. `font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;`).

═══════════════════════════════════════════════════════════════
NEMHEZ IGAZÍTOTT, DINAMIKUS DIZÁJN (AUTOMATIKUS FELISMERÉS)
═══════════════════════════════════════════════════════════════

A NÉV ({name}) ALAPJÁN AUTOMATIKUSAN ISMERD FEL A NEMET, ÉS A DIZÁJNT TELJES MÉRTÉKBEN AHHOZ IGAZÍTSD! Minden email legyen vizuálisan más!

**FÉRFI HOROSZKÓP (ha férfi név):**
- **DIZÁJN:** Markáns, modern, technológiai vagy indusztriális. Sötétebb tónusok, éles vonalak. Használhatsz geometrikus mintákat a háttérben.
- **SZÍNEK:** Mélykék, szürke, fekete, narancs, élénk akcentus színek.
- **HANGNEM:** Tárgyilagos, motiváló, céltudatos.
- **EMOJIK:** ⚡🔥💪🎯🏆🚀⚔️🌟
- **TIPOGRÁFIA:** Vastag, sans-serif betűtípusok (pl. Montserrat, Roboto).

**NŐI HOROSZKÓP (ha női név):**
- **DIZÁJN:** Elegáns, kifinomult, légies, organikus. Világos, pasztell színek.
- **SZÍNEK:** Rózsaszín, lila, arany, menta, bézs, pasztell árnyalatok.
- **HANGNEM:** Empatikus, inspiráló, megértő, barátságos.
- **EMOJIK:** ✨💖🌸🦋🌙💫🌺💎
- **TIPOGRÁFIA:** Elegáns, akár enyhén kézírás jellegű (de jól olvasható) betűtípusok a címsorokban (pl. Playfair Display), a szövegnek pedig letisztult serif vagy sans-serif (pl. Lora, Lato).

═══════════════════════════════════════════════════════════════
VÁLTOZATOS TÉMÁK (MINDIG ÚJ ÉS EGYEDI!)
═══════════════════════════════════════════════════════════════

MINDEN HOROSZKÓP LEGYEN TEMATIKAILAG KÜLÖNBÖZŐ, a nap, évszak, csillagjegy és a Google Search eredményei alapján.
NE a sablonos Szerelem-Karrier-Pénz-Egészség legyen mindig!

HASZNÁLJ KREATÍV, EGYEDI SZEKCIÓKAT (ezek csak példák, találj ki újakat is!):
- 🌟 A Nap Kozmikus Fókuszpontja
- 🎯 Mai Személyes Küldetésed
- 🔮 Rejtett Üzenetek a Csillagokból
- 🌊 Érzelmi Iránytűd
- 🔥 Belső Tüzek és Szenvedélyek
- 🌈 A Változás Szelei
- 💡 Kreatív Szikrák és Megérzések
- 🌺 A Belső Harmónia ösvénye
- ⚖️ Döntések Keresztútján
- 🎨 Az Önkifejezés Vására
- 🌙 Az Intuíció Hangja

═══════════════════════════════════════════════════════════════
KÖTELEZŐ TARTALMI FELÉPÍTÉS:
═══════════════════════════════════════════════════════════════

1.  **Főcím:** Nagy, látványos cím: pl. "{zodiac_sign} - A nap, amikor minden megváltozik!"
2.  **Üdvözlés:** Személyes megszólítás: Kedves {name},
3.  **Bevezető:** Rövid, hangulatos bevezető a mai nap asztrológiai állásairól (a Google Search alapján), kifejezetten a {zodiac_sign} jegyű {first_name} számára.
4.  **Szekciók:** 4-6 kreatív, változatos szekció a fent említett stílusban.
5.  **Konkrét Tanácsok:** 3-5 konkrét, gyakorlatias tanács egy "Mai Útravaló" vagy hasonló szekcióban.
6.  **Szerencse Faktor:** Szerencseszám, szerencseszín vagy szerencsés órák.
7.  **Lezárás:** Inspiráló, pozitív lezáró gondolat, személyesen {first_name}-nek címezve.

EMLÉKEZTETŐ: AZONNAL a HTML kóddal kezdj! Nincs előtte semmi! A dizájn legyen dinamikus és SOHA ne legyen statikus!
"""

    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        temperature=0.95,
    )
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=config
        )

        if not response:
            raise ValueError("Nincs válasz az AI-tól")

        html_output = ""
        if getattr(response, "text", None):
            html_output = response.text.strip()

        if not html_output and getattr(response, "candidates", None):
            cand0 = response.candidates[0]
            content = getattr(cand0, "content", None)
            parts = getattr(content, "parts", None) if content else None
            if parts:
                html_output = "".join(
                    (getattr(p, "text", "") or "") for p in parts
                ).strip()

        if not html_output:
            raise ValueError("Üres válasz az AI-tól (sem text, sem parts)")

        # 🔧 TISZTÍTÁS: tool_code + minden, ami a HTML előtt van
        def cleanup_html(raw: str) -> str:
            if not raw:
                return raw

            raw = raw.strip()

            # esetleges ```html / ``` levágása
            for fence in ("```html", "```"):
                if raw.startswith(fence):
                    raw = raw[len(fence):].lstrip()
                if raw.endswith(fence):
                    raw = raw[:-len(fence)].rstrip()

            # ha van tool_code vagy bármi a HTML előtt, vágjunk a <!DOCTYPE/html-ig
            doc_start = raw.find("<!DOCTYPE html")
            if doc_start == -1:
                doc_start = raw.find("<html")
            if doc_start > 0:
                raw = raw[doc_start:]

            # biztonságból szedjük ki az önálló tool_code sorokat is
            lines = raw.splitlines()
            lines = [
                line for line in lines
                if not line.strip().startswith("tool_code ")
            ]
            return "\n".join(lines).strip()

        html_output = cleanup_html(html_output)

        print(f"👤 Név: {name}")
        print(f"✅ Keresztnév: {first_name}")

        return html_output


    except Exception as e:
        print(f"❌ Hiba a horoszkóp generálásában: {str(e)}")
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Horoszkóp - {zodiac_sign}</title>
        </head>
        <body style="font-family: Arial, sans-serif; text-align:center; margin: 0; padding: 0;">
            <div style="padding: 40px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;">
                <h1>{zodiac_sign} - Mai Horoszkóp</h1>
                <p>Kedves {name},</p>
                <p>Sajnos az AI-val technikai hiba lépett fel. Kérlek próbáld meg később újra!</p>
                <p style="font-size: 12px; opacity: 0.7;">Hiba: {str(e)[:100]}</p>
            </div>
        </body>
        </html>
        """

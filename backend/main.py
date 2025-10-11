from horoscope_generator import generate_horoscope
from email_sender import send_email

def main():
    zodiac_sign = input() #csillagjegy ide api-ból
    horoscope_text = generate_horoscope(zodiac_sign)
    print(horoscope_text)

if __name__ == "__main__":
    main()
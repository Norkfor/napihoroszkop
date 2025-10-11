import datetime

def get_zodiac_sign(month: int, day: int) -> str:
    zodiac_signs = [
        ((3, 21), (4, 19), "Kos"),
        ((4, 20), (5, 20), "Bika"),
        ((5, 21), (6, 20), "Ikrek"),
        ((6, 21), (7, 22), "Rák"),
        ((7, 23), (8, 22), "Oroszlán"),
        ((8, 23), (9, 22), "Szűz"),
        ((9, 23), (10, 22), "Mérleg"),
        ((10, 23), (11, 21), "Skorpió"),
        ((11, 22), (12, 21), "Nyilas"),
        ((12, 22), (12, 31), "Bak"),
        ((1, 1), (1, 19), "Bak"),
        ((1, 20), (2, 18), "Vízöntő"),
        ((2, 19), (3, 20), "Halak"),
    ]
    
    for start, end, sign in zodiac_signs:
        start_month, start_day = start
        end_month, end_day = end
        
        if start_month == end_month:
            if month == start_month and start_day <= day <= end_day:
                return sign
        else:
            if (month == start_month and day >= start_day) or (month == end_month and day <= end_day):
                return sign
    
    raise ValueError("Invalid date")

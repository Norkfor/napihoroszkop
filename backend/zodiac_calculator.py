def get_zodiac_sign(month: int, day: int) -> str:
    """
    Calculates zodiac sign based on birth month and day.
    """
    # Validate month and day ranges
    if not (1 <= month <= 12):
        raise ValueError(f"Invalid month: {month}. Must be between 1 and 12.")
    
    if not (1 <= day <= 31):
        raise ValueError(f"Invalid day: {day}. Must be between 1 and 31.")
    
    # Month-specific day validation
    days_in_month = {
        1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    
    if day > days_in_month[month]:
        raise ValueError(f"Invalid day {day} for month {month}. Month {month} has only {days_in_month[month]} days.")
    
    # Zodiac sign determination
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Kos"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Bika"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Ikrek"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Rák"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Oroszlán"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Szűz"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Mérleg"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Skorpió"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Nyilas"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Bak"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Vízöntő"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Halak"
    else:
        raise ValueError(f"Could not determine zodiac sign for month {month}, day {day}")
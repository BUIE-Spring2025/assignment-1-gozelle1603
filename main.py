def int_to_roman(num):
    roman_letters = {
        1000: "M", 900: "CM", 500: "D", 400: "CD",
        100: "C", 90: "XC", 50: "L", 40: "XL",
        10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
    }

    roman_value = []
    
    for value, symbol in roman_letters.items():
        count = num // value  
        roman_value.append(symbol * count)  
        num %= value 

    return "".join(roman_value)




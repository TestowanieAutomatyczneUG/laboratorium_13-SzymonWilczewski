class Roman:
    def number(self, num):
        numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        i = 0
        roman_number = ""

        while num:
            for _ in range(num // numbers[i]):
                roman_number += symbols[i]
                num -= numbers[i]
            i += 1
        return roman_number

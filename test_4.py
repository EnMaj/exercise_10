class RomanNumber:
    all_roman = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }

    def __init__(self, rom_value):
        if RomanNumber.is_roman(rom_value):
            self.rom_value = rom_value
        else:
            print('ошибка')
            self.rom_value = None

    def decimal_number(self):
        dec = 0
        temp_rom_value = self.rom_value
        for r, i in RomanNumber.all_roman.items():
            while temp_rom_value[:2] == r or temp_rom_value[:1] == r:
                dec += i
                temp_rom_value = temp_rom_value[len(r):]
        return dec

    @staticmethod
    def is_roman(value):
        for _ in range(3):
            if value[:1] == 'M':
                value = value[1:]
        if 0 <= value[:2].count('CM') <= 1 or 0 <= value[:2].count('CD') <= 1 or 0 <= value[:1].count('D') <= 1:
            value = value[value[:2].count('CM') * 2:]
            value = value[value[:2].count('CD') * 2:]
            value = value[value[:1].count('D'):]
        for _ in range(3):
            if value[:1] == 'C':
                value = value[1:]
        if 0 <= value[:2].count('XC') <= 1 or 0 <= value[:2].count('XL') <= 1 or 0 <= value[:1].count('L') <= 1:
            value = value[value[:2].count('XC') * 2:]
            value = value[value[:2].count('XL') * 2:]
            value = value[value[:1].count('L'):]
        for _ in range(3):
            if value[:1] == 'X':
                value = value[1:]
        if (0 <= value.count('IX') <= 1 or 0 <= value.count('IV') <= 1 or 0 <= value.count('V') <= 1):
            value = value[value[:2].count('IX') * 2:]
            value = value[value[:2].count('IV') * 2:]
            value = value[value[:1].count('V'):]
        for _ in range(3):
            if value[:1] == 'I':
                value = value[1:]
        if value == '':
            return True
        return False


    def __repr__(self):
        return f'{self.rom_value}'

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

    def __init__(self, value):
        if value.__class__.__name__ == 'int':
            if RomanNumber.is_int(value):
                self.int_value = value
                self.rom_value = RomanNumber.roman_number(self)
            else:
                print('ошибка')
                self.int_value = None
                self.rom_value = None
        elif value.__class__.__name__ == 'str':
            if RomanNumber.is_roman(value):
                self.rom_value = value
                self.int_value = RomanNumber.decimal_number(self)
            else:
                print('ошибка')
                self.rom_value = None
                self.int_value = None
        else:
            print('ошибка')
            self.rom_value = None
            self.int_value = None

    def decimal_number(self):
        dec = 0
        temp_rom_value = self.rom_value
        for r, i in RomanNumber.all_roman.items():
            while temp_rom_value[:2] == r or temp_rom_value[:1] == r:
                dec += i
                temp_rom_value = temp_rom_value[len(r):]
        return dec

    def roman_number(self):
        roman = ''
        num_int = self.int_value
        while num_int > 0:
            for r, i in RomanNumber.all_roman.items():
                while num_int >= i:
                    roman += r
                    num_int -= i
        return roman

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

    @staticmethod
    def is_int(value):
        if 1 <= int(value) <= 3999:
            return True
        return False

    def __add__(self, other):
        x = RomanNumber(self.int_value + other.int_value)
        return x

    def __sub__(self, other):
        x = RomanNumber(self.int_value - other.int_value)
        return x

    def __mul__(self, other):
        x = RomanNumber(self.int_value * other.int_value)
        return x

    def __truediv__(self, other):
        if self.int_value % other.int_value == 0:
            x = RomanNumber(int(self.int_value / other.int_value))
        else:
            x = RomanNumber(self.int_value / other.int_value)
        return x

    def __floordiv__(self, other):
        x = RomanNumber(self.int_value // other.int_value)
        return x

    def __mod__(self, other):
        x = RomanNumber(self.int_value % other.int_value)
        return x

    def __pow__(self, power, modulo=None):
        x = RomanNumber(self.int_value ** power.int_value)
        return x

    def __iadd__(self, other):
        x = RomanNumber(self.int_value + other.int_value)
        return x

    def __isub__(self, other):
        x = RomanNumber(self.int_value - other.int_value)
        return x

    def __imul__(self, other):
        x = RomanNumber(self.int_value * other.int_value)
        return x

    def __itruediv__(self, other):
        if self.int_value % other.int_value == 0:
            x = RomanNumber(int(self.int_value / other.int_value))
        else:
            x = RomanNumber(self.int_value / other.int_value)
        return x

    def __ifloordiv__(self, other):
        x = RomanNumber(self.int_value // other.int_value)
        return x

    def __imod__(self, other):
        x = RomanNumber(self.int_value % other.int_value)
        return x

    def __ipow__(self, other):
        x = RomanNumber(self.int_value ** other.int_value)
        return x

    def __str__(self):
        return f'{self.rom_value}'

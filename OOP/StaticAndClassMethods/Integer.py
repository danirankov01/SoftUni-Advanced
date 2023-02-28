from math import floor


class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"

        return cls(floor(float_value))

    @classmethod
    def from_roman(cls, value):
        integer = Integer.print_number(value)
        return cls(int(integer))

    @staticmethod
    def print_number(number):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
                 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        i = 0
        num = 0
        while i < len(number):
            if i + 1 < len(number) and number[i:i + 2] in roman:
                num += roman[number[i: i + 2]]
                i += 2
            else:
                num += roman[number[i]]
                i += 1
        return num

    @classmethod
    def from_string(cls, value):
        is_the_value_int = isinstance(value, str)
        if not is_the_value_int:
            return "wrong type"

        return cls(int(value))


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))

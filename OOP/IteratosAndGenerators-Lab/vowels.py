class vowels:
    def __init__(self, text):
        self.vowels = ['a', 'e', 'i', 'u', 'y', 'o']
        self.text = [x for x in text if x.lower() in self.vowels]

    def __iter__(self):
        return self

    def __next__(self):
        if self.text:
            return self.text.pop(0)
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

print("Greeting")

class PersonA:
    def __init__(self, name, age):
        self._name = name
        self._age = age

class PersonB(PersonA):
    def __str__(self):
        return '%sは%d歳です' % (self._name, self._age)

a = PersonA('太郎', 10)
b = PersonB('花子', 20)
c = PersonB('太郎', 10)

print(a)
print(b)
print(c)
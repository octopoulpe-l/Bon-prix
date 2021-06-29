import random
number = random.randint(0,100)
rep = int(input('Donne un nombre entre un 0 et 100'))
number = int(number)
def a():
    if rep > number:
        print('Moins')
    else:
        print('Plus')
while not rep == number:
    a()
    rep = int(input('reessaie'))
print('Bravo')
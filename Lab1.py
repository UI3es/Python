print(2+3)
print(4*5)
print(40/2)
print(2**3)
print("UI3")
print("Hi there" + "UI3")
print("UI3"*3)
print("Running' down the hill")
print('Running\' down the hill')
print("UI3".upper())
print(len("UI3"))
print("длина строки :53475783475: " + str(len(str(53475783475))))
print("Переменные")
name = "UI3"
print(name)
print(len(name))
a = 4
b = 6
print(a*b)
print("Лист")
print([])
lottery = [3, 42, 12, 19, 30, 59]
print(lottery)
print(len(lottery))
lottery.sort()
print(lottery)
lottery.reverse()
print(lottery)
lottery.append(199)
print(lottery)
print(lottery[0])
print(lottery[1])
lottery.pop(0)
print(lottery)
print("Словари")
print({})
participant = {'name': 'Ola', 'country': 'Poland', 'favorite_numbers': [7, 42, 92]}
print(participant)
print(participant['name'])
participant['favorite_language'] = 'Python'
print(participant)
print(len(participant))
participant.pop('favorite_numbers')
print(participant)
participant['country'] = 'Germany'
print(participant)
print("Сравнение вещей")
print(5 > 2)
print(3 < 1)
print(5 > 2 * 2)
print(1 == 1)
print(5 != 2)
print(6 >= 12 / 2)
print(3 <= 2)
print(6 > 2 and 2 < 3)
print(3 > 2 and 2 < 1)
print(3 > 2 or 2 < 1)
print("Логические значения ")
a = True
print(a)
a = 2 > 5
print(a)
print("If...elif...else")
if 3 > 2:  print('It works!')

if 5 > 2:
    print('5 is indeed greater than 2')
else:
    print('5 is not greater than 2')
    
name = 'Sonja'
if name == 'Ola':
    print('Hey Ola!')
elif name == 'Sonja':
    print('Hey Sonja!')
else:
    print('Hey anonymous!')

volume = 57
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")

# Change the volume if it's too loud or too quiet
if volume < 20 or volume > 80:
    volume = 50
    print("That's better!")
    
print("Твоя собственная функция!")
def hi():
    print('Hi there!')
    print('How are you?')
hi()    

def hi(name):
    if name == 'Ola':
        print('Hi Ola!')
    elif name == 'Sonja':
        print('Hi Sonja!')
    else:
        print('Hi anonymous!')
hi(name)

def hi(name):
    print('Hi ' + name + '!')
hi("Rachel")

print("Циклы")
girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hi(name)
    print('Next girl')

for i in range(1, 6):
    print(i)



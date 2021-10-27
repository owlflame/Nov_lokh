#A)
School = { }
for i in range(5):
    School.update( { input(f'Название класса №{i+1}: '): int(input(f'КОЛИЧЕСТВО УЧЕНИКОВ № {i+1}: ')) } )
print(School)
#B)
ClassName = input('Введите класс: ')
if ClassName in School:
    print(f'Количество учеников в классе { ClassName } : { School[ClassName] } ')
else:
    print('Такого класса на существует')
#C)
for i in range(3):
    School.update( { input(f'Название изменяемого класса { i + 1 } : '): int(input(f'Количество учеников изменяемого класса { i + 1 } : ')) } )
print(School)
#D)
for i in range(2):
    School.update( { input(f'Название нового класса { i + 1 } : '): int(input(f'Количество учеников нового класса { i + 1 } : ')) } )
print(School)
#E)
del School[input(f'Название расформировываемого класса: ')]
print(School)






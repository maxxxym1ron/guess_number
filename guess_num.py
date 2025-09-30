from random import randint

a = randint(1, 100)

print('\nИГРА "Guess number 0-100"\n')

print('Выберите сложность игры:')
print('easy - 10 попыток угадать число')
print('medium - 7 попыток угадать число')
print('hard - 5 попыток угадать число')

difficult = str(input('\nВведите сложность игры (easy/medium/hard): '))


attempts = 10
while True:
    if difficult == 'easy':
        print('\nВыбрана сложность easy.')
        attempts = 10
        break

    elif difficult == 'medium':
        print('\nВыбрана сложность medium.')
        attempts = 7
        break

    elif difficult == 'hard':
        print('\nВыбрана сложность hard.')
        attempts = 5
        break

    else:
        print('\nНекорректно введена сложность игры.\nПовторите попытку: ')
        difficult = str(input())



while attempts:
    guess = int(input('Введите число: '))
    
    if guess < a:
        print('\nВаше число меньше загаданного\n')
        attempts -= 1
    
    elif guess > a:
        print('\nВаше число больше загаданного\n')
        attempts -= 1
        
    elif guess == a:
        print('\n-------------- ПОБЕДА -------------')
        print(f'Вы отгадали число загаданное число: {a}\n')
        break

    print(f'Осталось {attempts} попыток')

if attempts == 0:
    print('\n-------------- ПОРАЖЕНИЕ -------------')
    print(f'Вы не отгадали загаданное число: {a}\n')
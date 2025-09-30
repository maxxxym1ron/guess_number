from random import randint

a = randint(1, 100)

print('\nУгадай число от 1 до 100\n')

while True:
    guess = int(input('Введите число: '))
    
    if guess < a:
        print('\nВаше число меньше загаданного\n')
    
    elif guess > a:
        print('\nВаше число больше загаданного\n')
        
    else:
        print('\nВы отгадали число!\n')
        break
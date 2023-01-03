import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Adivinhe um número entre 1 e {x}: '))
        if guess < random_number:
            print('Tente novamente, muito abaixo! ')
        elif guess > random_number:
            print('Tente novamente, muito alto! ')
    print(f'Parabéns! Você acertou o número, {random_number}')


if __name__ == '__main__':
    guess(10)

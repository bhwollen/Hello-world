from random import randint
guess_count = 0

print('The point of this game is to guess the random number in the number of tries you choose')
range = int(input('The number will be randomly chosen between 1 and '))
secret_number = randint(1, range)

guess_limit = int(input('How many guesses would you like? '))
print(f'Ok, you get {guess_limit} tries')

print(secret_number)

while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You win!')
        break
    elif guess < secret_number:
        print('The number is higher')
        print(f'You have {guess_limit - guess_count} tries left')
    else:
        print('The number is lower')
        print(f'You have {guess_limit - guess_count} tries left')
else:
    print('You lose')

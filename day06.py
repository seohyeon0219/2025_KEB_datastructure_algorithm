# Assignment day06
# v1.5) https://github.com/inhadeepblue/2024_KEB_datastructure_algorithm 의
# v0.7 guess number 예제를 자동화하고 로그파일(guess.txt)을 남기도록 코드를 수정하시오.
# 단, 해당 프로그램이 로그시간을 갖도록 한다
import random

answer = random.randint(1, 100)
chance = 7

while chance != 0:
    guess = int(input("Input guess number : "))
    if guess == answer:
        print(f'You win. Answer is {answer}')
        break
    elif guess > answer:
        chance = chance - 1
        print(f'{guess} is bigger. Chance left : {chance}')
    else:
        chance = chance - 1
        print(f'{guess} is lower. Chance left : {chance}')
else:
    print(f'You lost. Answer is {answer}')

# with open('guess.txt', 'w') as fp:
#     fp.write("Inha universty")
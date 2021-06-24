def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    for curr in range(num + 1):
        print(curr, '!')


def test(correct=None):
    print("Let's test your programming knowledge.")
    print("Is learning Python fun?")
    print("1. Yes")
    print("2. No")
    print("3. No")
    print("4. No")
    
    answer = int(input())
    if answer == 4:
        print('Completed, have a nice day!')
        correct == 1
    else:
        print("Please, try again.")
    


def end():
    print('Congratulations, have a nice day!')


greet('Aid', '2020')  # change it as you need
remind_name()
guess_age()
count()
test()
# ...
end()

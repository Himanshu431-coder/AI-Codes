# Title: Elementary Chatbot for Customer Interaction

def greet(bot_name, birth_year):
    print("Hello! My name is {0}.".format(bot_name))
    print("I was created in {0}.".format(birth_year))

def remind_name():
    print("Please, remind me your name.")
    name = input()
    print("What a great name you have, {0}!".format(name))

def guess_age():
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")
    rem3 = int(input("Remainder when divided by 3: "))
    rem5 = int(input("Remainder when divided by 5: "))
    rem7 = int(input("Remainder when divided by 7: "))
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print("Your age is {0}; that's a good time to start programming!".format(age))

def count():
    print("Now I will prove to you that I can count to any number you want.")
    num = int(input("Enter a number: "))
    for i in range(num + 1):
        print("{0} !".format(i))

def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    answer = 2
    while True:
        guess = int(input("Your answer (1-4): "))
        if guess == answer:
            break
        print("Please, try again.")
    print("Completed, have a nice day!")
    print("." * 33)

def end():
    print("Congratulations, have a nice day!")
    print("." * 33)
    input("Press Enter to exit...")

# Main chatbot flow
greet('TE-Chatbot', '2025') 
remind_name()
guess_age()
count()
test()
end()

import random


def number_picker(min, max):
    # This function chooses random integer from a range of number given by user 
    return random.randint(min, max)


def operator():
    # This function chooses picks up a random operator for calculations
    return random.choice(['+', '-', '*'])


def calculate(n1, n2, o):
    # This does the computation and calculates the answer
    problem = f"{n1} {o} {n2}"
    if o == '+': answer = n1 + n2
    elif o == '-': answer = n1 - n2
    else: answer = n1 * n2
    return problem, answer

def userinput():
    # This function validates if the answer is correct
    try:
        user_answer = input("Your answer: ")
        return int(user_answer)
    except ValueError:
        print("Please enter a valid integer value only.")
        return userinput()

def math_quiz():

    """ This function inputs the answer from user and compares with the actual computed answer if its correct or not?
        There are total 3 number of question denoted by total_questions and each correct one will award you with one point. """
    
    points = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        n1 = number_picker(1, 10)
        n2 = number_picker(1, 5)
        o = operator()

        PROBLEM, ANSWER = calculate(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        
        useranswer = userinput()

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            points += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {points}/{total_questions}")

if __name__ == "__main__":
    math_quiz()

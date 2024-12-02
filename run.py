import random
import os
import time
from rich.console import Console
console = Console()


class The_options:
    """
    Defines the options
    """
    def __init__(self, number, country, capital, incorrect_1, incorrect_2):
        self.number = number
        self.country = country
        self.capital = capital
        self.incorrect_1 = incorrect_1
        self.incorrect_2 = incorrect_2

    def the_question(self):
        """
        Shows the structure of question and randomly allocates the capital
        and two incorrect options to A, B and C
        """
        print(f"\nQuestion {self.number}: What is the capital of", end=" ")
        print(f"{self.country}?\n")
        options = [self.capital, self.incorrect_1, self.incorrect_2]
        random.shuffle(options)
        print('A: ', options[0])
        print('B: ', options[1])
        print('C: ', options[2])
        return options


def the_instructions():
    """
    Welcome message and instructions on how to play the game
    """
    message = "Welcome to the capitals quiz, press Enter to continue"
    console.input(f"\n[bold]{message}\n")
    print("You shall be asked for the capital of 10 countries\n")
    print("You shall be given a choice of 3 cities in that country", end=" ")
    print("listed as A, B and C\n")
    print("Please select either A, B or C\n")
    print("You shall be advised if that is the correct answer or not\n")
    print("You shall be awarded 1 point for each correct answer\n")
    print("If you select anything other than A, B or C, you shall", end=" ")
    print("be asked to make a choice again until you select A, B or C\n")
    input("Press Enter to continue\n")
    clear_screen()


def the_quiz():
    """
    Data for the questions generating the question,
    inputting a selected answer and giving a score.
    """
    dictionary = [
        {
            'country': 'the United States',
            'capital': 'Washington DC',
            'incorrect_1': 'Los Angeles',
            'incorrect_2': 'New York'
        },
        {
            'country': 'China',
            'capital': 'Beijing',
            'incorrect_1': 'Hong Kong',
            'incorrect_2': 'Shanghai'
        },
        {
            'country': 'Germany',
            'capital': 'Berlin',
            'incorrect_1': 'Hamburg',
            'incorrect_2': 'Munich'
        },
        {
            'country': 'Japan',
            'capital': 'Tokyo',
            'incorrect_1': 'Hiroshima',
            'incorrect_2': 'Osaka'
        },
        {
            'country': 'India',
            'capital': 'New Dheli',
            'incorrect_1': 'Chennai',
            'incorrect_2': 'Mumbai'
        },
        {
            'country': 'the United Kingdom',
            'capital': 'London',
            'incorrect_1': 'Birmingham',
            'incorrect_2': 'Manchester'
        },
        {
            'country': 'France',
            'capital': 'Paris',
            'incorrect_1': 'Lyon',
            'incorrect_2': 'Nice'
        },
        {
            'country': 'Italy',
            'capital': 'Rome',
            'incorrect_1': 'Milan',
            'incorrect_2': 'Naples'
        },
        {
            'country': 'Canada',
            'capital': 'Ottawa',
            'incorrect_1': 'Montreal',
            'incorrect_2': 'Toronto'
        },
        {
            'country': 'Brazil',
            'capital': 'Brasilia',
            'incorrect_1': 'Rio de Janerio',
            'incorrect_2': 'Sao Paulo'
        }
    ]

    score = 0

    for index, question in enumerate(dictionary):
        question = The_options(
            number=index + 1,
            country=question['country'],
            capital=question['capital'],
            incorrect_1=question['incorrect_1'],
            incorrect_2=question['incorrect_2']
        )
        options = question.the_question()
        while True:
            msg = "Please select an option of A, B or C then press Enter:"
            available_options = input(f"\n{msg}\n\n")
            if available_options.upper() not in ['A', 'B', 'C']:
                error = "That is not a valid option, please select A, B or C"
                console.print(f"[bold]{error}\n\n", style="blue")
            else:
                break

        if available_options.upper() == 'A' and options[0] == question.capital:
            console.print("[bold]\nWell done, that is the correct option",
                          style="green")
            score += 1
            print("\nYour score is currently:", score)
        elif (available_options.upper() == 'B'
              and options[1] == question.capital):
            console.print("[bold]\nWell done, that is the correct option",
                          style="green")
            score += 1
            print("\nYour score is currently:", score)
        elif (available_options.upper() == 'C'
              and options[2] == question.capital):
            console.print("[bold]\nWell done, that is the correct option",
                          style="green")
            score += 1
            print("\nYour score is currently:", score)
        else:
            console.print("[bold]\nSorry, that was not the correct option",
                          style="red")
            print("\nYour score remains at:", score)

        time.sleep(2)
        clear_screen()

    console.print("\n[bold]Thank your for playing the capitals quiz")
    console.print("\n[bold]You scored:", score, "[bold]points out of 10\n")


def clear_screen():
    """Clears the screen"""
    os.system("cls" if os.name == "nt" else "clear")


the_instructions()
the_quiz()

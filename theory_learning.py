"""
-----------------------------------------------------------
@project: Theory learning
@file: theory_learning.py
@author: Adam Dzurilla
-----------------------------------------------------------
"""

import random
import os
import sys
import xml.etree.ElementTree as ET
import re

NO_ERROR = 0
ERROR_NON_EXIST_FILE = 10
ERROR_WRONG_PROGRAM_ARGUMENTS = 11
ERROR_WRONG_XML_STRUCTURE = 20


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    return "   "


def print_help_message():
    print("Usage:")
    print("\tpython3.8 theory_learning.py [FILE | help]")
    print()
    print("Options:")
    print("FILE - Input xml file")
    print("help | h - prints this message")
    print()

    print_choices_help()

    print("Exit status:")
    print("\t0\t\tOK,")

    print("\t10\t\tUnknown file passed as an argument,")
    print("\t11\t\tWrong program arguments count,")

    print("\t20\t\tWrong XML structure,")
    print()
    print("This is help message for the program \"theory_learning.py\"")
    print()


def print_choices_help():
    print("Choices:")
    print("\tr | random - random question")
    print("\t[NUMBER] - gets question from position, indexing starts from one (e.g. 20)")
    print("\ta | answer - show answer")
    print("\tc | count - number of questions")
    print("\tclear - clear the terminal")
    print("\tall - print all questions")
    print("\th | help - print this message")
    print("\tquit - quit")
    print()


class Subject:
    list_of_quest_and_answer = {}
    value = None

    def __init__(self, input_file):
        self.load_from_file(input_file)

    def load_from_file(self, input_file):
        tree = ET.parse(input_file)
        root = tree.getroot()

        if root.tag != 'data':
            print('Wrong xml structure')
            exit(ERROR_WRONG_XML_STRUCTURE)
            
        for element in root.findall('element'):
            question = element.find('question').text
            answer = element.find('answer').text
            self.list_of_quest_and_answer[question] = answer

    def get_question(self):
        return self.value

    def get_answer(self):
        return self.list_of_quest_and_answer[self.value]

    def get_count(self):
        return len(self.list_of_quest_and_answer)

    def get_question_from_position(self, position: int):
        if self.get_count() >= position > 0:
            keys_list = list(self.list_of_quest_and_answer)
            key = keys_list[position - 1]
            return key

    def select_random(self):
        self.value = random.choice(list(self.list_of_quest_and_answer))

    def print_ran_choice(self):
        self.select_random()
        print(self.get_question())

    def print_from_position(self, position):
        key = self.get_question_from_position(position)
        if key is None:
            print('Wrong index (indexing starts from 1 to ' + str(self.get_count()) + ')')
        else:
            self.value = key
            print(key)

    def print_answer(self):
        if self.value is not None:
            print(self.get_answer())
        else:
            print('No question was generated yet, see \'help\' for how to generate a question')

    def print_count(self):
        print(self.get_count())

    def print_all(self):
        num = 1
        for key in self.list_of_quest_and_answer:
            print(str(num) + ":\t" + key)
            num += 1


if __name__ == "__main__":
    file = None
    # Loading arguments
    if len(sys.argv) != 2:
        # Wrong program input arguments
        print("Error in program arguments count")
        print()
        print_help_message()
        exit(ERROR_WRONG_PROGRAM_ARGUMENTS)
    elif sys.argv[1] == 'h' or sys.argv[1] == 'help':
        print_help_message()
        exit(NO_ERROR)
    else:
        file = sys.argv[1]
        if not os.path.exists(file):
            print("Error: File passed as an argument doesn't exists")
            exit(ERROR_NON_EXIST_FILE)

    subject = Subject(file)

    clear()
    run = True
    while run:
        choice = None
        try:
            choice = input("Select choice: ").lower()
        except KeyboardInterrupt:
            run = False
            continue

        if choice == 'r' or choice == 'random':
            clear()
            subject.print_ran_choice()
        elif choice == 'a' or choice == 'answer':
            subject.print_answer()
        elif re.match("[0-9]+", choice):
            clear()
            subject.print_from_position(int(choice))
        elif choice == 'c' or choice == 'count':
            clear()
            subject.print_count()
        elif choice == 'clear':
            clear()
        elif choice == 'all':
            subject.print_all()
        elif choice == 'quit':
            run = False
        elif choice == 'h' or choice == 'help':
            print_choices_help()
        else:
            print("I don't understand the choice, see \'help\' for known choices")

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


def clear_terminal():
    """
    The function clears the terminal
    :return:
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    return "   "


def print_help_message():
    """
    The function prints the help message
    :return:
    """
    print("Usage:")
    print("\tpython3.8 theory_learning.py [-f FILE | -h | --help]")
    print()
    print("Options:")
    print("\tFILE - Input xml file")
    print("\t-h | --help - prints this message")
    print()

    print("Example run:")
    print("\tpython.exe main.py -f questions/nmal/2sem/sur.xml")
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
    """
    The function prints the help for choices
    :return:
    """
    print("Choices:")
    print("\tr | random - random question")
    print("\t[NUMBER] - gets question from position, indexing starts from one (e.g. 20)")
    print("\ta | answer - show answer")
    print("\tc | count - number of questions")
    print("\tclear - clear the terminal")
    print("\tall - print all questions")
    print("\th | help - print this message")
    print("\tq | quit | exit - quit")
    print()


def process_arguments(argv: list) -> str:
    """
    The function gets file name from program arguments and returns its path
    :return: Path of the XML file
    """
    if len(argv) < 1:
        # Wrong program input arguments
        print("Error in program arguments count")
        print()
        print_help_message()
        exit(ERROR_WRONG_PROGRAM_ARGUMENTS)
    elif argv[0] == '-h' or argv[0] == '--help':
        # Prints help message
        print_help_message()
        exit(NO_ERROR)
    elif (argv[0] == '-f' or argv[0] == '--file') and len(argv) > 1:
        filePath = argv[1]
        if not os.path.exists(filePath):
            print("Error: File passed as an argument doesn't exists")
            exit(ERROR_NON_EXIST_FILE)
        else:
            return filePath
    else:
        print("Error: Unknown argument:", argv[0])
        print()
        print_help_message()
        exit(ERROR_WRONG_PROGRAM_ARGUMENTS)


class Subject:
    """
    Class for loading xml and handling with data
    """
    list_of_quest_and_answer = {}
    value = None

    def __init__(self, input_file):
        """
        The constructor class
        :param input_file: Xml file which contains data
        """
        self.load_from_file(input_file)

    def load_from_file(self, input_file):
        """
        Loads XML file into list
        :param input_file: Input file which contains data
        :return:
        """
        tree = ET.parse(input_file)
        root = tree.getroot()

        # Checks root attribute
        if root.tag != 'data':
            print('Wrong xml structure')
            exit(ERROR_WRONG_XML_STRUCTURE)

        # Iterates through elements in tree and add them to the list
        for element in root.findall('element'):
            question = element.find('question').text
            answer = element.find('answer').text
            self.list_of_quest_and_answer[question] = answer

    def get_question(self):
        """
        Gets question by value
        :return: Value from class
        """
        return self.value

    def get_answer(self):
        """
        Gets answer from question
        :return: Answer from concrete question
        """
        return self.list_of_quest_and_answer[self.value]

    def get_count(self):
        """
        Gets number of questions in list
        :return: Integer count number
        """
        return len(self.list_of_quest_and_answer)

    def get_value_index(self):
        """
        Gets index of the value in list
        :return: Index + 1 (due selecting by position) as string
        """
        return str(list(self.list_of_quest_and_answer).index(self.value) + 1)

    def get_question_from_position(self, position: int):
        """
        Gets question from concrete position, if position is valid
        :param position: Integer position
        :return: Question
        """
        if self.get_count() >= position > 0:
            keys_list = list(self.list_of_quest_and_answer)
            key = keys_list[position - 1]
            return key

    def select_random(self):
        """
        Selects random question from the list, and sets the value by the choice
        :return:
        """
        self.value = random.choice(list(self.list_of_quest_and_answer))

    def print_ran_choice(self):
        """
        Selects random choice and then prints it
        :return:
        """
        self.select_random()
        print(self.get_value_index() + ". " + self.get_question())

    def print_from_position(self, position):
        """
        Prints the question from selected position
        :param position: Position
        :return:
        """
        key = self.get_question_from_position(position)

        # Checks position validity
        if key is None:
            print('Wrong index (indexing starts from 1 to ' + str(self.get_count()) + ')')
        else:
            self.value = key
            print(self.get_value_index() + ". " + key)

    def print_answer(self):
        """
        Prints the answer of question in value
        :return:
        """

        # Checks if value is not None
        if self.value is not None:
            print(self.get_answer())
        else:
            print('No question was generated yet, see \'help\' for how to generate a question')

    def print_count(self):
        """
        Prints the number of questions
        :return:
        """
        print(self.get_count())

    def print_all(self):
        """
        Prints the all questions from the list
        :return:
        """
        num = 1
        for key in self.list_of_quest_and_answer:
            print(str(num) + ":\t" + key)
            num += 1


if __name__ == "__main__":
    """
    Main function of the program
    :return:
    """
    file = process_arguments(sys.argv[1:])

    subject = Subject(file)

    clear_terminal()
    print_choices_help()
    run = True
    while run:
        choice = None
        try:
            choice = input("Select choice: ").lower()
        except KeyboardInterrupt:
            run = False
            continue

        if choice == 'r' or choice == 'random':
            clear_terminal()
            subject.print_ran_choice()
        elif choice == 'a' or choice == 'answer':
            subject.print_answer()
        elif re.fullmatch("[0-9]+", choice):
            clear_terminal()
            subject.print_from_position(int(choice))
        elif choice == 'c' or choice == 'count':
            clear_terminal()
            subject.print_count()
        elif choice == 'clear':
            clear_terminal()
        elif choice == 'all':
            subject.print_all()
        elif choice == 'q' or choice == 'quit' or choice == 'exit':
            run = False
        elif choice == 'h' or choice == 'help':
            print_choices_help()
        else:
            print("I don't understand the choice, see \'help\' for known choices")

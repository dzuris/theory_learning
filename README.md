# Theory Learning

## About The Project

This project is intended to help you with learning theoretical questions and formulas. You are going to have file with questions and program random choose question, then you will have time to think about the answer and when you will want to see it, you can easily show the answer text. Also you have an overview of all the questions same as the count of the all questions which you have in the file.

With project also come concise help message which helps you to navigate in the program.

## Getting started

This is overview of instructions which you will need to work with the program locally.

### Prerequisities

- python compiler

### Installation

There is no need to install program in any way to your computer. You can just start the program through your terminal.

## Usage

Running program through your terminal:

1. Navigate to your repository where you have the project main file.
2. Run one of the following commands:
- `python main.py help` - to show help message,
- `python main.py -f FILE_PATH/FILE.XML` - to run the program.

After starting your program, the console will show you some choices options with brief notes. Here are all the potential choices:

- r | random - choose random question and print its text
- [NUMBER] (eg. 28) - gets question from chosen position, the number has to be greater or equal to zero and has to be less than questions count in your file
- a | answer - prints answer to your chosen question
- c | count - number of questions in your file
- clear - clear the console
- all - print all the questions without answers
- h | help - prints help message with choices
- q | quit - terminate the running program

## XML organization

Here you have XML template which you can use in your questions file:

```XML
<data>
    <element>
        <question>Question num 1</question>
        <answer>Answer num 1</answer>
    </element>
    <element>
        <question>Question num 2</question>
        <answer>Answer num 2</answer>
    </element>
</data>
```

## Author

Adam Dzurilla  
adamdzurilla19@gmail.com

import random

class Answer:
    # динанический атрибут создаем
    def __init__(self, answer_txt):
        self.answer_txt = answer_txt

# 2 динамических атрибута создаем
class Question:
    def __init__(self, question_txt, list_answers):
        self.question_txt = question_txt
        self.list_answers = list_answers

class Test:
    # статический атрибут
    list_question = []

    # динамические атрибут
    def __init__(self):
        self.amount_answers = 0
        self.questionGenerator()

    def questionGenerator(self):
        question_txt = input("Введите текст вопроса: ")

        self.amount_answers = int(input("Введите количество ответов: "))

        myAnswers = []# создаем список с ответами

        for i in range(self.amount_answers):
            answer_txt = input(f"Введите текст варианта ответа {i+1}: ")
            myAnswers.append(Answer(answer_txt))

        random.shuffle(myAnswers)
        new_question = Question(question_txt, myAnswers)
        Test.list_question.append(new_question)


    @classmethod
    def getTest(cls):
        for question in cls.list_question:
            print(f"\n{question.question_txt}")
            random.shuffle(question.list_answers)
            for answer in question.list_answers:
                print(f" - {answer.answer_txt}")





test = Test() #создание экземляра класса
test2 = Test()
Test.getTest()
Test.getTest()







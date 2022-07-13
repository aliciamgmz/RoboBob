import numpy as np
import operator


def is_question(sentence):
    """
    This function takes a string variable and returns a boolean whether the sentence can be converted to a mathematical operation or not.
    """
    return False


def answer(question):
    return question


# meter algun "por siempre"
question = input('Question: ')
if is_question(question):
    print('Answer' + answer(question))

else:
    print(float(question))

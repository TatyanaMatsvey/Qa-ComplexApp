import datetime
import random
from time import sleep

from pages.utils import wait_until_ok


# def decorator(func):  # func = time_sleeper
# def wrap(*args, **kwargs):  # *args, **kwargs - вид конструкции, когда мы не знаем, сколько аргументов будет у
#     # декорируемой функции. Args - tuple, Kwargs - dict. В данном случае мы принимаем аргумент функции
#     # time_sleeper(name), которая вызывает заданное нами имя "John".
#     print(f"Before: {datetime.datetime.now()}")
#     result = func(*args, **kwargs)  # получаем результат функции time_sleeper
#     print(f"After: {datetime.datetime.now()}")
#     return result  # возвращаем результат выполнения функции time_sleeper
#
# return wrap  # возвращаем результат выполнения функции декоратора


@wait_until_ok()
def time_sleeper(name):
    sleep(0.5)
    assert random.choice([0, 1])


time_sleeper("John")

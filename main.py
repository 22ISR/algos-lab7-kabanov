"""
Задание №1

Задание: Написать программу, которая принимает на вход слово и проверяет, является ли оно палиндромом.
Условия:

    Программа должна быть нечувствительна к регистру.
    Игнорировать пробелы и знаки пунктуации.
Пример использования:
    isPalindrom("level") # True
    isPalindrom("hello") # False
"""

def isPalindrom(s):
    s_lower = s.lower()
    return s_lower == s_lower[::-1]

print(isPalindrom("level"))
print(isPalindrom("hello"))

"""        
Задание №2

Задание: Написать программу, которая принимает список слов и проверяет, какие из них являются палиндромами.
Условия:

    Слова передаются в виде списка через ввод пользователя.
    Программа должна вывести все палиндромы из списка.

Пример использования:
    isPalindromList(["hello", "list", "level"]) # ["level"]

"""

def isPalindromList(s):
    my_list = []
    for i in s:
        if isPalindrom(i) == True:
            my_list.append(i)

    return my_list

print(isPalindromList(["hello", "list", "level"])) # ["level"]

"""
Задание №3

Задание: Написать программу, которая ищет все палиндромы в строке текста.
Условия:

    Программа должна игнорировать регистр и знаки пунктуации.
    Если палиндромы повторяются, выводить их только один раз.

Пример использования isPalindromString("Madam, Anna went to the civic center") # ["madam", "anna", "civic"]
"""
def isPalindromString(b):
    my_new_list = []
    for i in b:
        if isPalindrom(i) == True:
            my_new_list.append(i.lower())

    return my_new_list        
      

print(isPalindromString("Madam, Anna went to the civic center"))

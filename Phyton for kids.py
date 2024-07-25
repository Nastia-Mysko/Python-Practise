# Define the variables
#found_coin = 10  # Example value
#magic_coin = 5   # Example value
#stole_coin = 2   # Example value

# Calculate the result
#result = found_coin + magic_coin * 365 - stole_coin * 52

# Print the result
#print(result)

#spaces = '' * 25
#print ('%s BlACK STREET' % spaces)
#print ('%s The same street blue' % spaces)
#print ('%s The 12' % spaces)
#print ()
#print()
#print('My dear')
#print()
#print('I have interesting information about youe husbent')
#print()
#print()
#print()
#print('If your interested just call me 9999999')
#print()
#print()
#print('Your New friend')'''
#wizard_list = 'popato, tomato, tuna, bulgur'
#print(wizard_list)


#wizard_list1 = ['popap', 'tomato', 'tuna', 'bulgur']
#print(wizard_list1[2])
#wizard_list1 = ['popap', 'tomato', 'tuna', 'bulgur']
#number = ('1,2,3,4,5,6')
#додає вкінці нове значеннч
#wizard_list1.append ('apple')
#wizard_list1.append ('beans')
# можна видалити значення в списку
#del wizard_list1 [3]
#поєднує 2 списки
#wizard_list1.extend(number)
#додало текст авокадо як 5 тий в списку
#wizard_list1.insert (5, 'avocado')

#print (wizard_list1)
#numbers = [1, 2, 3, 5, 2, 6, 9, 2]
#count = numbers.count(2)
#print (count)
#numbers.reverse ()
#print('reverse list:', numbers)

#cities = ['London', 'Lviv', 'Krakow' ]
#cities.sort()
#print(f"Dictionary order:{cities}")
#cities.sort (reverse = True)
#print (f"Reverce dictionary order:{cities}")


#prime_numbers = [2, 3, 5, 7, 9, 11]

# remove all elements
#prime_numbers.clear()

# Updated prime_numbers List
#print('List after clear():', prime_numbers)

#Словник
#favorite_sport = ['Kally, football',
#'Anna, chess',
#'Kate, baseball',
#'Den, Kriket']
#print(favorite_sport)


#favorite_sport = {'Kally': 'football',
#'Anna':'chess',
#'Kate': 'baseball',
#'Den': 'Kriket'}
#print(favorite_sport)
#print(favorite_sport['Anna'])
#del(favorite_sport['Kate'])
#print (favorite_sport)
#favorite_sport['Anna']= ('Pingpong')
#print (favorite_sport)'''

#Завдання з книжки
#Створіть список улюблених розваг і збережіть його в змінній games.
# Тепер створіть список улюблених ласощів, зберігши його у 
#змінній foods. Об'єднайте два списки, зберігши результат у 
#змінній favorites, і надрукуйте значення цієї змінної.

#games = [' football', 'voleiball', 'bascketball', 'watherpolo', 
       #'othergame']
#food = ['ice_cream','hotdog', 'cheescake', 'macaroon']
#games.extend(food)
#print("favorite:", games)'''


#Є 3 будинки, на даху кожного з яких ховаються по 25 ніндзя, 
#і є 2 тунелі, у кожному з яких ховається по 40 самураїв. 
#Скільки всього воїнів вирішили влаштувати заварушку?
# (Відповідь можна знайти, ввівши в оболонці Python арифметичний вираз.)
#houses = 3
#ninja = 25
#tunel = 2
#samurai = 40

#ningia_sum = (houses*ninja)+(tunel*samurai)
#print (ningia_sum)'''


#Створіть дві змінні: нехай одна зберігає ваше ім'я, а друга прізвище. 
#Тепер за допомогою рядка з мітками %s надрукуйте привітання на кшталт 
#такого: «Привіт, Брандо Ікетт!».


#Задача 1: Робота зі змінними
#Напишіть програму, яка запитує у користувача його ім'я та вік, а потім виводить повідомлення:
#"Привіт, [ім'я]! Тобі [вік] років."


#name1 = input("Add your first name:")
#ages1 = input("Add your age:")
#print(f'Your name is {name1}!!Your {ages1} old' )


#Задача 2: Список чисел
#Створіть програму, яка запитує у користувача п'ять чисел, 
#додає їх у список, а потім виводить суму та середнє значення цих чисел.
#first_data = input ('Enter first data:')
#second_data = input('Enter second data:')
#thrid_data = input('Enter thrid data:')
#fourth_data = input('Enter fourth data:')
#fifth_data = input('Enter fifth data:')
#result_sum = (int(first_data) + int(second_data) + int(thrid_data) +int(fourth_data) + int(fifth_data))
#printn int(result_sum) 
#average_value = int(result_sum)/5
#print (average_value)


### Задача 3: Робота зі словником
#Напишіть програму, яка створює словник з трьох пар "ключ-значення", 
#де ключами є назви предметів, а значеннями — їхні ціни. 
#Потім програма повинна вивести загальну суму цін всіх предметів.

#Price1 = 5
#Price2 = 7
#Price3 = 12


#item1 = {'Apple':Price1}
#item2 = {'Banana':Price2}
#item3 = {'Grape':Price3}
#item_sum = Price1 + Price2 + Price3
#print (item1, item2, item3)
#print ("Total sum of price",item_sum)

#Задача 4: Сортування списку
#Напишіть програму, яка запитує у користувача 
#п'ять імен, додає їх у список, а потім виводить відсортований список 
#імен в алфавітному порядку.

#name1 = input("Enter name 1:")
#name2 = input("Enter name 2:;")
#name3 = input ("Enter name 3:")
#name4 = input("Enter name 4:")
#name5 = input("Enter name 5:")
#name6 = input("Enter name 6:")
#all_name = [name1,name2,name3,name4,name5,name6]
#all_name.sort()
#print(all_name)

### Задача 5: Підрахунок елементів
#Напишіть програму, яка запитує у користувача рядок тексту і підраховує,
#скільки разів кожне слово зустрічається в цьому рядку. 
#Використовуйте словник для зберігання результатів.


# Запитуємо у користувача рядок тексту
#text = input("Введіть рядок тексту: ")

# Розбиваємо рядок на окремі слова
#words = text.split()

# Ініціалізуємо словник для зберігання підрахунків
#word_count = {}

# Підраховуємо кількість появ кожного слова
#for word in words:
    # Приводимо слово до нижнього регістру для уникнення різниці між "Слово" і "слово"
  #  word = word.lower()
 #   if word in word_count:
   #     word_count[word] += 1
    #else:
     ##   word_count[word] = 1

# Виводимо результати
#print("Підрахунок слів у тексті:")
#for word, count in word_count.items():
    #print(f"{word}: {count}")

# Завдання на умови if, else
#age = int(input("Enter your age:"))  # Convert the input to an integer
# if int(age) < 18:  # Compare the integer value of age with 18
 #   print("No access")  # The user should not have access if they are under 18
#else:
 #   print("You have access")


'''a = 4
v = 6
if a + v >100:
  print('sum more >100')
else:
 print('sum less <100')'''

'''age = '18'
if int(age) == 25 or int(age) == 18:
    print('ok')
elif int(age) <= 18:
    print('kid')
else:
    print('vintage')'''

'''twinkeys = 700
if twinkeys < 100:
 print ("Very little")
elif twinkeys > 500:
 print ("To much")'''

'''twinkeys = 50
if twinkeys <100:
 print ("Little" )
else:
 print("To much")'''

'''twinkies = int(input("Enter quantity of twinkies: "))

# Проверка условия
if twinkies < 100 or twinkies > 500:
    print("To much or less")'''

'''data1 = int(input("Enter first data:"))
data2 = int(input("Enter second data"))
sum_data = data1 + data2
if sum_data > 100 and  sum_data< 500:
    print("Amount in range 100 - 500")
elif sum_data > 1000 and sum_data< 5000:
    print("Amount in range 1000 - 5000")
else:
    print(" No range")'''


#Створіть конструкцію if, яка друкує рядок «Їх надто багато»,
#якщо кількість ніндзя (задана в змінній ninjas) менше 50,
#друкує «Буде непросто, але я з ними впораюся»,
#якщо ця кількість менше 30, і друкує «Я здолаю цих ніндзя!»,
#Якщо кількість менше 10.
'''ninja = int(input("Enter ninjas quantity:" ))
if ninja <10:
    print ("I'll beat these ninjas")
elif ninja <30:
    print("It won't be easy, but I'll handle them")
elif ninja <50:
    print("It's too many ninjas")'''




    ### Завдання 1: Перевірка позитивного числа
#Напишіть програму, яка приймає число від користувача і перевіряє, чи є
#це число позитивним. Якщо число позитивне, програма має вивести "Число позитивне".
#posetive =int(input("Enter number:"))
#if posetive > 0:
 #   print(" Number is posetive") 

 ### Завдання 2: Визначення найбільшого числа
#Напишіть програму, яка приймає три числа від користувача і визначає
# найбільше з них. Виведіть найбільше число.
#num1 = int(input("Enter  first number"))
#num2 = int(input("Enter second number"))
#num3 = int(input("Enter one more number"))
#if num1 >num2 and num1> num2:
 #   print(num1)
#elif num2>num1 and num2>num3:
 #print (num2)
#elif num3 >num1 and num3>num2:
 #  print (num3)
### Завдання 3: Перевірка року на високосний
#Напишіть програму, яка приймає рік від користувача і перевіряє, 
#чи є цей рік високосним. Високосний рік ділиться на 4, 
#але не ділиться на 100, якщо тільки не ділиться на 400.

'''year = int(input("Enter year"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} рік є високосним")
else:
    print(f"{year} рік не є високосним")'''


### Завдання 4: Перевірка на парність
#Напишіть програму, яка приймає число від користувача і перевіряє, 
#чи є це число парним. Якщо число парне, програма має вивести 
#"Число парне", інакше — "Число непарне".


# Запит числа від користувача
'''number = int(input("Введіть число: "))

# Перевірка на парність
if number % 2 == 0:
    print("Число парне")
else:
    print("Число непарне")'''
### Завдання 5: Перевірка оцінки
#Напишіть програму, яка запитує у користувача оцінку (число від 1 до 100)
#і виводить відповідне повідомлення:
#- 90-100: "Відмінно"
#- 70-89: "Добре"
#- 50-69: "Задовільно"
#- 0-49: "Не задовільно"


# Запит оцінки від користувача
'''score = int(input("Введіть оцінку (число від 1 до 100): "))

# Перевірка оцінки та виведення відповідного повідомлення
if 90 <= score <= 100:
    print("Відмінно")
elif 70 <= score <= 89:
    print("Добре")
elif 50 <= score <= 69:
    print("Задовільно")
elif 0 <= score <= 49:
    print("Не задовільно")
else:
    print("Некоректна оцінка. Введіть число від 1 до 100.")



#Цикл повторення for
#range - діапазон
#for x in range (0,5):
# print(" Hello")'''

#print (list(range(10,20)))

'''found_coins = 20
magic_coins = 70
stolen_coins = 3
coins = found_coins
for week in range (1,10):
    coins = magic_coins + coins - stolen_coins
    print ('Weekend %s = %s' % (week, coins)) '''


#цикли
# друкує лише 1 значення бо 0 меще 9
'''for x in range(0, 20):
    print('hey  %s' % x)
    if x < 9: 
        break'''
#якщо змінити код на х >= bilshe рівне, то буде 9 значень
'''for x in range(0, 20):
    print('hey  %s' % x)
    if x >= 9: 
        break'''


# Для парних цифер
'''for i in range (2,30):
 if i % 2 ==0:
  print( ' %s' % i)'''
# Для непарних цифер
'''for i in range (1,31):
 if i % 2 !=0:
  print( ' %s' % i )'''


'''ingredients = ['chees', 'butter', 'bread','cutlet', 'salat']
for index, ingredient in enumerate(ingredients, start=1):
    print(f"{index}. {ingredient}")'''


'''# Запрос начального земного веса пользователя
earth_weight = float(input("Введите ваш текущий земной вес в килограммах: "))

# Константа для расчета лунного веса
moon_weight_factor = 0.165

# Цикл для расчета лунного веса в течение 15 лет
for year in range(1, 16):
    moon_weight = (earth_weight + year - 1) * moon_weight_factor
    print(f"Год {year}: Your  moon weight  {moon_weight:.2f} кг")'''

# Перебір списку чисел
#Напишіть програму, яка перебирає список чисел та виводить тільки парні числа.
'''numbers = [1,2,3,4,5,6,7,8,9,10]
for i in range (1,11):
 if i %2 ==0:
  print ('Парні числа %s' %i)'''

#Напишіть програму, яка знаходить суму всіх чисел у списку.
#numbers = [1,2,3,4,5]
'''sum_numbers = sum(numbers) 
print( sum_numbers)'''

'''total = 0
for number in numbers:
    total+=number
    print ('Sum of numbers in list', total)'''

'''total = sum(number for number in numbers)
print("Сума значень у списку:", total)'''


#Перебір рядка
#Напишіть програму, яка перебирає символи у рядку і виводить тільки 
#голосні літери. hello world
'''word = "Hello, World"
vowels = "aiueoy"  # Голосні літери без ком

vowel_letters = ""

for letter in word:
    if letter.lower() in vowels:
        vowel_letters += letter

print("Голосні літери у слові:", vowel_letters)'''
 #Напишіть програму, яка обчислює факторіал числа, використовуючи цикл for.
 
 # Число для обчислення факторіалу
#number = 5

# Ініціалізація змінної для збереження результату факторіалу
#factorial = 1

# Цикл для обчислення факторіалу
#for i in range(1, number + 1):
    #factorial *= i

# Виведення результату
#print(f"Факторіал числа {number} дорівнює {factorial}")

### Завдання 1: Виведення чисел від 1 до 10
#Напишіть програму, яка використовує цикл while для виведення чисел від 1 до 10.

# Ініціалізація змінної
'''number = 1

# Цикл while для виведення чисел від 1 до 10
while number <= 10:
    print(number)
    number += 1'''


'''leftNumber = 3
rightNumber = 6

def calculate(a, b):
    return a + b

result = calculate(leftNumber, rightNumber)

print('Sum %d+%d=%d' % (leftNumber, rightNumber, result))'''
#Сума чисел до заданого числа
#Напишіть програму, яка використовує цикл while для обчислення суми чисел від 1 до n. Значення n вводиться користувачем.
'''n = int(input('Enter some data:'))
sum_number = 0
number = 1
while number <= n:
    sum_number += number
    number += 1

# Виведення результату
print(f"Сума чисел від 1 до {n} дорівнює {sum_number}")'''

#Обчислення факторіалу числа
#Напишіть програму, яка використовує цикл while для обчислення
# факторіалу заданого числа n. Значення n вводиться користувачем.

'''n = int(input("Введіть значення n: "))
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
    print(f"Факторіал числа {n} дорівнює {factorial}")'''

#Вгадування числа
#Напишіть програму, яка просить користувача вгадати випадкове число 
#від 1 до 10. Програма продовжує запитувати, поки користувач не вгадає 
#правильне число. Використовуйте цикл while.


'''n = int(input("Вгадування числа, введіть число: "))
a = 9
b = 0
while n != a:
    b += 1
    print(" Guessed wrong")
    n = int(input())
print("Try agan")'''

'''import random

# Генерація випадкового числа від 1 до 10
random_number = random.randint(1, 10)

# Ініціалізація змінної для збереження вгадування користувача
guess = 0

# Цикл while для запитування вгадування, поки не буде вгадано правильне число
while guess != random_number:
    # Запит у користувача вгадування
    guess = int(input("Вгадайте число від 1 до 10: "))
    
    # Перевірка вгадування
    if guess < random_number:
        print("Занадто мало! Спробуйте ще раз.")
    elif guess > random_number:
        print("Занадто багато! Спробуйте ще раз.")
    else:
        print("Вітаємо! Ви вгадали правильне число.")'''

#Функції
'''firstdata = 17.11

def data (aaa):
    print('Totay, %s' % (firstdata))


data(1213)

import random

secretNumber = random.randint(1, 10)
userAnswer = 0
attempts = 0


def guessMe(value):
    if value == secretNumber:
        print('Congrats!')
        return True
    elif value > secretNumber:
        print('Too large')
    else:
        print('Too low')
    return False


while attempts < 3:
    userAnswer = int(input('Guess number from 1 to 10'))
    result = guessMe(userAnswer)
    if result:
        break

else:
    print('Try again')'''

'''def summa():
    first = 40
    second = 40
    return first * second
print ("Full summa", summa())'''

'''import time
print(" Current time")
print (time.asctime())'''

'''import sys

def commonage():
    print('How old are u?')
age = int(sys.stdin.readline())
if age >=18:
    print ("Access")
else:
    print ("No access")'''

'''import sys
def weight():
    print('What is your weight?')
weight= int(sys.stdin.readline())
cof = 0.25
for year in range(1, 16):
    moon_weight = (weight) + year - 1 * cof
    print(f"Year {year}: Your  moon weight  {moon_weight:.2f} ")'''


'''class Cat:
    def black_cat(self):
        print(f"This is black cat named {self.catName}")
    
    def white_cat(self):
        print(f"This is white cat named {self.catName}")
    
    def red_cat(self):
        print(f"This is red cat named {self.catName}")


myCat1 = Cat()
myCat1.catName = input('What is your first cat name? ')

myCat2 = Cat()
myCat2.catName = input('What is your second cat name? ')

myCat3 = Cat()
myCat3.catName = input('What is your thirth cat name? ')

# Виклик методів для кожного екземпляра
myCat1.black_cat()
myCat2.red_cat()
myCat3.white_cat()'''


#Створіть клас Car, який буде мати наступні атрибути: марка, модель та рік випуску.
# Додайте метод display_info, який буде виводити інформацію про автомобіль у форматі 
#"Марка: X, Модель: Y, Рік: Z".
'''class Car:
    marka = ""
    model = ""
    year = 0

car1 = Car ()
car1.marka = 'mazda'
car1.model = 'new'
car1.year = 1992
print(f" Marka: {car1.marka}, Model: {car1.model},Year:{car1.year}")'''



'''class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Марка: {self.make}, Модель: {self.model}, Рік: {self.year}")

# Приклад використання
my_car = Car('Toyota', 'Camry', 2020)
my_car.display_info()'''

 
class BankAccount:
    def __init__(self,) -> None:
        pass
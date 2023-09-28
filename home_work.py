'''У нас є список показань заборгованостей з комунальних послуг наприкінці місяця. 
Заборгованості можуть бути від'ємними — у нас переплата, чи додатними, якщо необхідно сплатити за рахунками. 
Напишіть функцію amount_payment, яка приймає на вхід список платежів, підсумовує додатні значення 
та повертає суму платежу наприкінці місяця.'''

# def amount_payment(payment):
#     sum = 0
#     for value in payment:
#         if value > 0:
#             sum += value
#     return sum  
    
# print(amount_payment([1, -3, 4]))

'''При аналізі даних часто виникає необхідність позбавитися екстремальних значень, перш ніж почати працювати 
з даними далі. Напишіть функцію prepare_data, яка видаляє з переданого списку найбільше та найменше значення, 
сортує його в порядку зростання і повертає змінений список як результат.'''
    
# def prepare_data(data):
#     res = sorted(data)
#     res.pop(0)
#     res.pop()

#     return res

# print(prepare_data([4, 1, 3, 5, 2]))

'''Ми розробляємо кулінарний блог. І в рецептах, при написанні списку інгредієнтів, ми розділяємо їх комами, 
а перед останнім ставимо союз "and", як у прикладі нижче:

2 eggs, 1 liter sugar, 1 tsp salt and vinegar

Напишіть функцію format_ingredients, яка прийматиме на вхід список з інгредієнтів 
["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"] та повертатиме рядок зібраний з його елементів 
в описаний вище спосіб. Ваша функція має вміти обробляти списки будь-якої довжини.'''

# def format_ingredients(items):
#     if len(items) > 2:
#         items_1 = ', '.join(items[: -1])
#         items_2 = ''.join(items[-1])
#         items_f = (f"{items_1} {'and'} {items_2}")
#         return items_f
    
#     elif len(items) == 0:
#         items_f = ''.join(items)
#         return items_f
    
#     else:
#         items = items[0]
#         items_f = ''.join(items)
#         return items_f
    
# print(format_ingredients([]))








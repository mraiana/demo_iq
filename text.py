'''
IQ = (умственный возраст / хронологический возраст)*100
Возрастной диапазон	   Средний показатель IQ
от 16 до 17 лет 	        108
от 18 до 19 лет	            105
от 20 до 24 лет	            99
от 24 до 34 лет	            97
от 35 до 44 лет	            101
от 45 до 54 лет	            106
Старше 65 лет	            114

Диапазон IQ («отклонение IQ»)	    Классификация IQ
130 и выше	                            Очень превосходный
от 120 до 129	                        Превосходный
от 110 до 119	                        Высокий Средний
от 90 до 109	                        Средний
с 80 до 89	                            Низкий Средний
от 70 до 79	                            Пограничный
69 и ниже	                            Чрезвычайно низкий
'''



txt_iq = "Ваш результат IQ: "
txt_res = [] 
txt_res.append('''низкая. Вам стоит улучшить свое мышление.''')
txt_res.append('''удовлетворительная. 
Продолжайте улучшать мышление.''')
txt_res.append('''средняя. 
Продолжайте улучшать мышление.''')
txt_res.append('''
выше среднего''')
txt_res.append('''
высокая''')

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions = [
    Question("2x+65=77, x=?\n(a) 4\n(b) 6\n(c) 5\n", "b"),
    Question("Если самолет упадет на границе США и Канады, где будут похоронены выжившие?\n(a) США\n(b) Канада\n(c) Ни то, ни другое\n", "c"),
    Question("У отца Мэри есть 5 дочерей: Лейла, Николь, Оливия, Памела. Как зовут пятую дочь?\n(a) Ребекка\n(b) Мэри\n(c) Селена\n", "b"),
    Question("Какое число лучше всего завершает аналогию: 8:4 как 10:?\n(a) 5\n(b) 3\n(c) 2\n", "a"),
    Question("Какое число должно быть следующим в ряду? 1, 1, 2, 3, 5, 8, 13...\n(a) 28\n(b) 21\n(c) 26\n", "b"),
    Question("Если умножить меня на 4, а затем вычесть 5, получится 47. Какое я число?\n(a) 14\n(b) 17\n(c) 13\n", "c")
]

def run_test(questions, age):
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 3
            global iq
            iq = (score*6/age)*100
    print("IQ результат:", iq)

run_test(questions)

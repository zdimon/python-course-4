'''
print('Инициализация')
q = 'Какой у вас вес?'
print(q)
print("Сбор данных")
ves = input()
print("Анализ данных")
print("Вы весите " + ves + " кг.")
ves = int(ves)
if ves < 30:
    print("Вы худой")

elif ves >30 and ves<60:
    print("Так держать!")

else:
    print("Многовато однако!")
'''

def mf():
    print("haha")

d = {
    "say": mf
}

d["say"]()

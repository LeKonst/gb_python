#"""
#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать #значение `n`

#При отправке решения на Проверку закомментируйте эту строку обратно - система #автоматически подставит разные значения `n` для проверки
#"""

#n = 6

# Введите ваше решение ниже
#Катя сделала 2midCountCranes, петя и Сережа midCountCranes, вычисляем midCountCranes
midCountCranes = n/3;
print(midCountCranes%2)
if midCountCranes%2 != 0:
    midCountCranes+=1

countCranesKate = midCountCranes * 2
countCranesMan = midCountCranes/2
print("(%d, %d, %d)"% (countCranesMan, countCranesKate, countCranesMan))
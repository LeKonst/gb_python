#"""
#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать #значение `n`

#При отправке решения на Проверку закомментируйте эту строку обратно - система #автоматически подставит разные значения `n` для проверки
#"""

n = 385911

# Введите ваше решение ниже

stringTicket = str(n)

tryFoundLuckyTicket = True
if len(stringTicket) != 6:
    print("no")
    tryFoundLuckyTicket = False
if tryFoundLuckyTicket and (stringTicket[0] + stringTicket[1] + stringTicket[2] == 
        stringTicket[3] + stringTicket[4] + stringTicket[5]):
    print("yes")
elif stringTicket.__len__ == 6:
    print("no")
    

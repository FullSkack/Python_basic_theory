# Блок else выполняется, когда основное 
# тело цикла перестает работать самостоятельно. 
i = 0
while i < 5:
    # конструкция if break прерывает цикл 
    # при выполнение условия
    if i == 3:
        break
    i = i + 1
# блок else не работает тк цикл был перван
else:
    print('Пожалуй')
    print('хватит )')
print(i)

# Пример где цикл завершается самостоятельно
n = 423
summa = 0
while n > 0:
    x = n % 10
    summa = summa + x
    n = n // 10
# Тк цикл завершился самостоятельно, работает блок else
else:
    print('Пожалуй')
    print('хватит )')
print(summa)

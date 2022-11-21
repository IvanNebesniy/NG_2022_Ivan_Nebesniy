#Калькулятор+

what = input ( "Що робимо? (+,-,*,/): " )

a = float (input ( "Введи перше число: "))
b = float (input ( "Введи друге число: "))

if what == "+":
    c = a + b
    print ("Результат:" + str(c) )
elif what == "-":
    c = a - b
    print ("Результат:" + str(c) )
if what == "*":
    c = a * b
    print ("Результат:" + str(c) )
elif what == "/":
    c = a / b
    print ("Результат:" + str (c) )
    
else:
    print ("Вибрана не вірно операція!! " )
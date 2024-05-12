#question 8
Unit = int(input("enter the unit "))
if Unit <= 100:
    print("no charge")
elif Unit <= 200:
    print(Unit * 5)
elif Unit > 200:
    print(Unit * 10)
else: print("invaled")

#question 1
degree = int (input("enter your degree "))
if degree > 90:
    print("D")
elif degree > 80:
    print("B")
elif degree >=60 <=80: 
    print("C")
elif degree <60: 
    print("D")       
else: print("invaled")

#question 2
cost_price_of_pike = int(input("enter the cost "))
if cost_price_of_pike > 100000:
    print("tax is"),print(cost_price_of_pike*0.15)
elif 50000< cost_price_of_pike <=100000:
    print("tax is"),print(cost_price_of_pike*0.10)
elif cost_price_of_pike <=50000:
    print("tax is"),print(cost_price_of_pike*0.05) 
else:print("invaled")

# question 5
number1= int(input("enter your no. "))
number2= int(input("enter your no. "))
print(number1) if number1>number2 else print(number2)


#question 6 
number5 = float(input("enter your number "))
print("the number is positive") if number5 >0 else print("the number is negative")


#question 7
number6 = int(input("enter the number :"))
print("the number is even") if (number6%2)==0 else print("the number is odd")

#question 9
number1= int(input("enter your no. "))
number2= int(input("enter your no. "))
number3= int(input("enter your no. "))
if number1>(number2):
    print(number1)
elif number2>number3:
    print(number2)
elif number3>number1:
    print(number3)
else: print(None)

#part2 
#question1
working_days = int(input("enter number of working days :"))
absent_days = int(input("enter number of absent days :"))
if absent_days/working_days>0.75:
    print("student able to sit in exam")
elif absent_days/working_days<0.75:
    print("student not able to sit in exam")
else: print("nil")

# #question2
presentage = int(input("enter your presentage "))
if presentage <25:
    print("your grade is D")
elif 25<= presentage <45:
    print("your grade is C")
elif 45<= presentage <50:
    print("your grade is B")
elif 50<= presentage <60:
    print("your grade is B+") 
elif 60<= presentage <80:
    print("your grade is A")
elif presentage >=80:
    print("your grade is A+")  
else: print("invaled")             


mohamed hafez













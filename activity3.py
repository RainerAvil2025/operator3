print("Enter the marks obtained in 5 subjects")
marks1=int(input("Enter the first subject marks"))
marks2=int(input("Enter the second subject marks"))
marks3=int(input("Enter the third subject marks"))
marks4=int(input("Enter the fourth subject marks"))
marks5=int(input("Enter the fifth subject marks"))

total = marks1+marks2+marks3+marks4+marks5
average=total/5
if average>=91 and average<=100:
    print("Your grade is A1")
if average>=81 and average<=91:
    print("Your grade is A2")
if average>=71 and average<=81:
    print("Your grade is B1")
if average>=61 and average<=71:
    print("Your grade is B2")
if average>=51 and average<=61:
    print("Your grade is C1")
if average>=41 and average<=51:
    print("Your grade is C2")
print("sum of 5 subjects is",sum)
print('average of 5 subjects is',average)

year = int(input("Enter a Your birth Year : "))
month = int(input("Enter a Your birth Month : "))
c_year = int(input("Enter a Current Year"))


f_age = c_year - year
f_month = f_age * 365
f_day = f_month * 30
f_hours = f_day * 24
f_min = f_hours * 60
if(year % 4 == 0):
    print("Your Year is a Leap Year : ",year)
else:
    print("Your Year is Not Leap year")
print("The Age is : ",f_age)
print("The Total Month is : ",f_month)
print("The Total Day's is : ",f_day)
print("The Total Hourse is : ",f_hours)
print("The Total Minute : ",f_min)

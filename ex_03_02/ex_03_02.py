hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
try:
    f_hours = float(hours)
    f_rate = float(rate)
except:
    print("Error, please enter numeric input")
    quit()
    
if f_hours > 40:
    #print("Overtime")
    r_pay = f_rate * f_hours
    otp = (f_hours - 40.0) * (f_rate * 0.5)
    pay = r_pay + otp
else:
    #print("regular")
    pay = f_hours * f_rate
print("Pay:",pay)

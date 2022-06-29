def computepay(hours, rate) :
    #print("In compute pay")
    if hours > 40:
        r_pay = rate * hours
        otp = (hours - 40.0) * (rate * 0.5)
        pay = r_pay + otp
    else:
        pay = hours * rate
    #print("Returning",pay)
    return pay


hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
    f_hours = float(hours)
    f_rate = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

pay = computepay(f_hours, f_rate)

print("Pay:",pay)

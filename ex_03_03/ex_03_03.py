
score = input("Enter Score: ")

try:
    f_score = float(score)

except:
    print("Error, please enter numeric input")
    quit()

if f_score > 1.0 or f_score < 0:
    #print("Overtime")
    print("ERROR, enter score between 0.0 and 1.0")
else:
    #print("regular")
    if f_score >= 0.9:
        print("A")
    elif f_score >= 0.8:
        print("B")
    elif f_score >= 0.7:
        print("C")
    elif f_score >= 0.6:
        print("D")
    else:
        print("F")

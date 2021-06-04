#Asks for an input from the user as a mark.
#If the mark is greater that 85 print "distinction"
#If the mark is between 65 and 85 "pass"
#Anything else print "Fail"
#Try to do it both with and without elif statements.

mark = int(input("Enter your mark:"))

if mark >= 85:
    print("Distinction")
elif 85 >= mark >=  65:
    print("pass")
else:
    print("fail")
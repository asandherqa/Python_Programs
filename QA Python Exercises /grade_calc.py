#Create an application which asks the user for an input for a maths mark, a chemistry mark and a physics mark.
#Add the marks together, then work out the overall percentage. And print it out to the screen.
#If the percentage is below 40%, print “You failed”
#If the percentage is 40% or higher, print “D”
#If the percentage is 50% or higher, print “C”
#If the percentage is 60% or higher, print “B”
#If the percentage is 70% or higher, print “A”

#Welcome to Grade Calculator
#Please enter your maths mark: 67
#Please enter your chemistry mark: 63
#Please enter your physics mark: 80
#Your percentage score is: 70.0%
#You scored a grade of: A
welcome = ("Welcome to Garde Calculator")
print (welcome)
maths = float(input("Please enter you maths mark:"))
print(maths)
chemistry = float(input("Please enter you chemistry mark:"))
print(chemistry)
physics = float(input("Please enter you physics mark:"))
print(physics)

mark = (maths + chemistry + physics) / 3
print("Your percenatge score is:", mark)

if mark >= 70:
    print("You scored a grade of: A")
elif 69 >= mark >=  60:
     print("You scored a grade of: B")
elif 59 >= mark >=  50:
     print("You scored a grade of: C")
elif 49 >= mark >=  40:
     print("You scored a grade of: D")
elif mark < 40:
     print("You scored a grade of: You failed")
else:
    print("incorrect input")
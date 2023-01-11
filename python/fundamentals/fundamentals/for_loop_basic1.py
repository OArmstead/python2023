



# Basic - Print all integers from 0 to 150.

# for x in range(0,151):
#     print(x)



# Multiples of Five - Print all the multiples of 5 from 5 to 1,000

# for x in range(5, 1001, 5):
#     print(x)


# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead.
# If divisible by 10, print "Coding Dojo".


for i in range(1, 101):
    if i % 10 == 0:
        print(str(i)+ ' Coding Dojo')
    elif i % 5 == 0:
        print(str(i)+ ' Coding')
    # needed to add an if statement to not make duplicates if the
    # number is divisible by 5 and 10.
    else:
        print(i)

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

# sum = 0

# for x in range(1, 500001,2):
#     if x % 2 != 1:
#         sum  += x
#     print(x)


# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

# for i in range(20, 1, -4):
#     print(i)

#Flexible Counter - Set three variables: lowNum, highNum, mult.
#Starting at lowNum and going through highNum,
#print only the integers that are a multiple of mult.
#For example, if lowNum=2, highNum=9, and mult=3,
#the loop should print 3, 6, 9 (on successive lines)

# lowNum = 2
# highNum = 9
# multi = 3

# for i in range(lowNum,highNum + 1):
#     if i % multi == 0:
#         print(i)


my_bool = True
print(my_bool)
my_bool = False
print(my_bool)

print(bool(0))
print(bool(1))

letter="A"
print(ord("A"))
print(ord("B"))
print(letter < "B")

x =10
y = 10
z = 20
print(x == 10 and y == 10)

x = 8
y = 9
print(x == y)
print(x != y)

# if BOOLEAN OR BOOLEAN EXP;
    #codeblock
    #for if true
# else:
    #for the if flase code block

height = 76

# Must be 5 feet tall to ride my ride
# Must be under 6 feet tall to ride

if height < 60:
    print("You are to short")
    print("I am sorry but get off of my ride!")
elif height > 72:
    print("You are to tall")
    print("get off my ride")
else:
    print("Enjoy the ride!")

print("Thanks for visiting")

number = 8
if True:
    print("Number is less than 8")
# def Name_of_Function(Parameters):
    #these line
    #belong
    #to the code block
    #for the fucntion

# def hello():
#     return "hello"

# print(hello())

# def hello(name, age):
#     print(f"hello {name} you are {age} years old")

# hello("Kevin",23)

# #keyword arguemnts
# hello( age = 23, name = "Kevin")

# def hello(age, name="John"):
#     print(f"hello {name} you are {age} years old")

# hello(23)




# def say_hello(name, age):
#     print(f"hello {name} you are {age} years old")
          
# def say_goodbye():
#     print("Goodbye")

# def greet_back(feeling):
#     if feeling == "good":
#         print("Awesome I feel good too")
#     elif feeling == "bad":
#         print("I am so sorry")
#     elif feeling == "stressed":
#         print("Coding can be hard to learn")
#     else:
#         print("Well, have a good day!")

# # Driver code
# while True:
#     response = input("What do you want to do? Say hello [H] Say goodbye [G] talk to me [T], quit [Q]")
#     if response.lower()== "q":
#         say_goodbye()
#         break
#     elif response.lower() == "h":
#         name = input("what is your name? ")
#         age = input("what is your age? ")
#         say_hello(name, age)
#     elif response.lower() == "g":
#         say_goodbye()
#     elif response.lower() == "t":
#         f = input("How are you today? ")
#         greet_back(f)
#     else:
#         print("invaid input")

def my_function(num):
    while num < 10:
        print(num)

        if num == 6:
            return
        num +=1

my_function(4)

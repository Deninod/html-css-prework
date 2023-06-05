#The while loop
#while Boolean or Boolean Exp:
    #code block
    #to run while
    #condition is true


# You must be over 5 feet to ride my ride
# I have a magic potion that will let you grow one inch everytime you use it!
#height = int(input("what is your height in inches? "))
#while height < 60:
 #   height += 1
  #  if height < 58:
   #     continue
    #print("You are {height} inches to short to ride!")
    #print("Did my magic potion")
   
    
#print("Thanks for coming")

while True:
    response = input("What do you want to do? Say hi [h], Say goodbyr [g], or Quit? [q]")
    if response.lower()== "h":
        print("hello")
    elif response.lower()== "g":
        print("goodbye")
    elif response.lower()== "q":
        break
    else:
        print("Invalid option")
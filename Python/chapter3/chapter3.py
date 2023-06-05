squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)

squares = [value**2 for value in range(1,11)]

print(squares)

squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)

odd_numbers = []
for number in range(1,100,3):
    odd_numbers.append(number)

print(odd_numbers)

cube_number = [value**3 for value in range (1,11)]

print(cube_number)

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team")
for player in players[:3]:
    print(player.title())
    
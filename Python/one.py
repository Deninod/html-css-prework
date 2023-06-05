#q1
def hello_name(user_name):
    return "hello_USERNAME"



print(hello_name("Bob"))

#q2
def first_odds():
    for num in range(1, 101,3):
        return None
    
print(first_odds())

#q3
a_list = [2, 30, 67, 56, 90, 87]

def max_num_in_list(a_list):
     result = []
     result = a_list
     max_number = result
     return max(result)
    

max_num_in_list(a_list)

#q4
def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 400 == 0:
        return True
    else:
        return False

print(is_leap_year(2001))


#q5

def is_consecutive(a_list):
    if sorted(a_list) == a_list:
        return True
    else:
        False

print(is_consecutive(a_list))
        



# block of codes running together as a unit
# initialize function then call the function

def print_name ():
    print("My name is Teresa Githinji")

# calling the function
    print_name() 

def print_details(name , age , id , gender):
    print("I am {0} , {1}years old . My id number is {2} and gender is {3}" . format(name, age , id , gender )) 
    
print_details ("Teresa Githinji" , "18" , "3456" , "female" ) 


def sum_nums(x,y):
    return x + y

z = sum_nums (10,20)
print(z)

def print_odds(first_no,last_number):
    for i in range (first_no , last_number):
        print(i % 2)
    


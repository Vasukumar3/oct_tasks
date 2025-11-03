#syntax
# def functionname():
    #block of code


# def details():
#     user = input("enter the user name: ")
#     num_1 = 10
#     num_2 = 20
#     print(num_1 + num_2)
#     print(user)
# details()

# def add():
#     num_1 = 10
#     num_2 = 20
#     print(num_1 + num_2)
# add()
# add()
# add()
# add()
# add()




# def details(user,id,dept):#function definition
#     print("welcome to pythonlife")#function body
#     print(user,id,dept)
# details("abc",1234,"frontend")#function calling,here abc 1234 frontend arguments(values)


# def add(num_1,num_2):#function definition
#     result = num_1 + num_2
#     print(f"addition of two numbers {result}")
# add(10,10)#arguments are passed during function calling
# add(20,40)
# add(40,20)
# add(2826,20)

#print(exp)--> it is used to display the information on the screen
#return -->

# def add(num_1,num_2):
#     return num_1 + num_2
# obj = add(20,20)
# print(obj*50)
# print(obj)
# print(obj+50)


# def add(num_1,num_2):
#     return num_1 + num_2
# obj = add(10,10)
# print(obj)


# def sample(a):
#     print(a)
# sample("achyuth")


# def sample(a):
#     for i in range(5):
#         print(i)
#     return a
# obj = sample("achyuth")
# print(obj)

#arbitary arguments--> function can accept a variable number of arguments by using *args(syntax)
# def details(*a):
#     print(a)
# details("raju","achyuth","pooja","veena","anudeeop","sai")

#*--> all
#*--> tuple


#keyword arguments :-->keyword arguments are passed to a function with a keyword and a value, allowing for more explicit parameter passing


# def sample(**a):
#     print(a)
# sample(a=5,b=5,c=10)


#*--> tuples
#**--> dict





# default parameters value
# def details(user=None,id=None,dept="frontend"):#function defintion
#     print(user,id,dept)
# details("anudeep",)
# details()
# details()
# details()



# def discount(price,discount=0):
#     discount_amount = (price*discount)/100
#     final_price = price - discount_amount
#     print(final_price)
# discount(10000,)
# discount(20000,)
# discount(20000,)
# discount(20000,)
# discount(20000,)
# discount(50000,10)



#variables ---> two types -->local variables ---> global variables
#1. local variables --> funtion (inside the function )
#2. global variables --> outside the function 

# def details():#function definition
#     user = "bharat" #local variables
#     id = 1234 #local variables
#     salary = 50000
#     print(user)
#     print(id)
#     hike = 5000
#     print(f"total salary {salary+hike}")
# details()



# balance = 1000 #global variables
# def credit(amount):
#     global balance
#     user = "rohan"#local variables
#     print(user)
#     balance+=amount
#     print(f"credited amount {amount}")
#     print(f"total balance{balance}")
# credit(500)


# print(balance)




#calculator
# def add(a,b):
#     print(a+b)
# def sub(a,b):
#     print(a-b)
# def mul(a,b):
#     print(a*b)
# def expo(a,b):
#     print(a**b)



# product_cost = 1000000000000000



# balance = 1000
# def credit():
#     pass
# def withdraw():
#     debit = int(input("enter amount to withdraw: "))
#     if debit<=balance:
#         balance-=debit
#         print("info")
#     else:
#         print()

# def balance_enquiry():
#     pass
# def exit():
#     pass
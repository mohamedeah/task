data = {
    "email" : "mohamed.hafez@hotmail.com",
     "email2" : "omar.mostafa@gmail.com" 
    }


email = []
login = input("enter email :")
for e in data.values():
     email.append(e)
     if login in email:
        print("User authenticated.")        



# email = []
# def login_required(fun):
#     def wrapper(email,password,username):
#         for e in data.values():
#             email.append(e)
#             if fun in email:
#                 print(True)
#     return wrapper

# print(email)
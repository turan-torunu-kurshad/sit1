def save_password(password1,password2):
    global password_1
    password_1=password1
    password_2=password2
    if not password_1 == password_2:
        print("error' try again!!! ")
        password_1,password_2 =None,None
    else:
        print("your password has been registered!")    
def enter_password(password):
    if not password == password_1:
        task=" error' try again!!! "
        print(task)
    else:
        task = "welcome"
        print(task)  
        
           
save_password("amkd","amkd")
enter_password("amkd")





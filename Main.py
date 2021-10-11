import time
import hashlib


def file_read(choise):
    
    f = open('passwords.txt','r')
    b = f.read().split("\n")
    f.close()
    login_list = list()
    pass_list = list()
    for i in b:
        if(len(i)== 0):
            continue
        login_list.append(i.split(" ")[0])
        pass_list.append(i.split(" ")[1])
    if(choise == "login"):
        return login_list
    elif(choise == "password"):
        return pass_list
    else:
        return 0

    
def file_write(data):
    
    f = open('passwords.txt','a')
    f.write("\n"+data)
    f.close()

    
def is_mail(mail):
    text = False
    dog = False
    dot = False
    if(mail.find("@")>mail.find(".")):
        return False
    for i in mail:
        if(i.isalnum() == True):
            text = True
        elif(i == "@" and dog == False):
            if(text == True):
                dog = True
                text = False
            else:
                return False
        elif(i =="."):
            dot = True
            if(text == False):
                return False
            else:
                text = False
    if(text == True and dot == True and dog == True):
        return True
    else:
        return False
        
    
def login_correct(data):
    
    if data.replace(".","").replace("@","").isalnum() == True and is_mail(data) == True:
        return 1
    else:
        if(data.count("@") == 1 and data.replace(".","").replace("@","").isalnum() == False):
            return 2
        elif(data.count("@") != 1  and data.replace(".","").replace("@","").isalnum() == True):
            return 3
        else:
            return 4

        
def login_unique(existed, new):
    
    for i in existed:
        if(new == i):
            return False
    return True


def password_correct(password):
    
    if(len(password)>=8 and password.isalnum() == True):
        return 1
    elif(len(password)<8 and password.isalnum() == True):
         return 2
    elif (password.isalnum() == False  and len(password)>=8):
        return 3
    else:
        return 4

    
def code(pass_str):
    
    return hashlib.sha224(pass_str.encode('utf-8')).hexdigest()


def entering(passlist, loginlist, login, password):
    
    for i in range(len(loginlist)):
        if(loginlist[i] == login and passlist[i] == password):
            return True
    return False


f = open('passwords.txt','a')
f.close()

correct_list = list("1234")
print("Приветствую!")
while 1:
    
    a = input("""Вы можете:
              1.Зарегистрироваться
              2.Войти в существующий аккаунт
              3.Посмотреть список пользователей
              4.Завершить сеанс
Для того, чтобы воспользоваться какой-либо функцией, введите её номер.
Например, 1 - для регистрации.\n""")
    
    if(a in correct_list):
        
        if(a == "1"):
            
            print("Чтобы зарегистрироваться, вам необходимо ввести e-mail и пароль.")
            print("Внимание! Длина пароля - не менее 8 цифр или латинских букв. Почта содержит @ и домен, состоит только из латинских символов или цифр.")
            print("Использовать уже существующие логины запрещено. Нечувствительно к регистру (только логин).")
            print("Например: ivan2020@mail.ru 12345678\n")
            
            log_list = file_read("login")
            pass_list = file_read("password")
            login = ""
            password = ""
            
            while(login_unique(log_list,login) != True or login_correct(login) != 1):
                
                time.sleep(0.75)
                login = input("Введите логин: ").lower()
                
                if(login_unique(log_list,login) == False):
                    
                    print("Аккаунт с таким логином уже существует. Попробуйте ещё раз.")
                    print("---------------")
                    
                elif(login_correct(login) != 1):
                    
                    if(login_correct(login)  == 2 ):
                        print("Логин содержит недопустимые символы")
                        
                    elif(login_correct(login)  == 3 ):
                        print("Логин не является почтой. Почта должна содержать @ и домен")

                    else:
                        print("Логин содержит недопустимые символы или не является почтой")
                    
                    print("Попробуйте ещё раз.")
                    print("---------------")
                    time.sleep(0.6)
                    
            while(password_correct(password) != 1):
                
                password = input("Введите пароль: ")
                
                if(password_correct(password) != 1):
                    
                    if(password_correct(password) == 2):
                        print("Пароль слишком короткий")
                        
                    elif(password_correct(password) == 3):
                        print("Пароль содержит недопустимые символы")
                        
                    else:
                        print("Пароль слишком короткий и содержит недопустимые символы")
                        
                    print("Попробуйте ещё раз.")
                    print("---------------")
                    time.sleep(0.75)
                    
            print("Вы успешно зарегистрировались! Теперь вы можете войти под своим логином и паролем.")
            
            final = login+" "+code(password)
            file_write(final)
            time.sleep(1)
            
            input("\nНажмите Enter, чтобы вернуться к главному меню."+"\t")
            
        elif(a == "2"):
            
            suc = False
            
            log_list = file_read("login")
            pass_list = file_read("password")
            login = ""
            password = ""
            
            while( suc == False):
                
                login = input("Введите логин: ").lower()
                password = input("Введите пароль: ")
                password = hashlib.sha224(password.encode('utf-8')).hexdigest()
                
                if(entering(pass_list, log_list, login, password) == True):
                    suc = True

                else:
                    print("Неверное имя пользователя или пароль")
                    
                    local = input("Введите что-угодно, чтобы попробовать ещё раз или 0, чтобы вернуться к главному меню: ")
                    
                    if(local == "0"):
                        break
                    
            if(suc == True):
                print("Успех! Добро пожаловать, "+login+"!")
                time.sleep(1)
                
                input("\nНажмите Enter, чтобы выйти из аккаунта вернуться к главному меню."+"\t")
                
        elif(a == "3"):
            
            log_list = file_read("login")
            
            if(len(log_list) == 0):
                
                print("Увы, но ещё никто не зарегистрировался :(")
                time.sleep(0.5)
                print("Но вы можете стать первым!")
                time.sleep(1)
                
                input("\nНажмите Enter, чтобы вернуться к главному меню."+"\t")
            else:
                
                print("Наши пользователи: ")
                
                for i in log_list:
                    print(i)
                    time.sleep(1)
                    
                time.sleep(1)
                input("\nНажмите Enter, чтобы вернуться к главному меню."+"\t")
        else:
            
            print("Спасибо за пользование этой программой!")
            print("Завершаю сеанс", end ="")
            
            for i in range(5):
                print(".", end ="")
                time.sleep(1)
            break
    else:
        
        print("Такой функции у нас ещё нет :(. Убедитесь, что номер функции записан без пробелов или других лишних символов.")
        time.sleep(1)
        
        input("\nНажмите Enter, чтобы вернуться к главному меню."+"\t")
    

def check1():
    password = input("введите пароль: ")
    c_password = input("Подтвердите пароль: ")
    if password == c_password:
        print("Пароль принят.")
    else:
        print("Пароль неверный. Повторите ввод.")


check1()
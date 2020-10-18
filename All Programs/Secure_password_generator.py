secu=(('s','$'),('1','i'),('a','@'),('o','0'),('and','&'),('0','o'))
def security(password):
     for a,b in secu:
          password = password.replace(a,b)
     return password

if __name__ == '__main__':
    a=input("Please Enter your Password : ")
    password=security(a)
    print(password)








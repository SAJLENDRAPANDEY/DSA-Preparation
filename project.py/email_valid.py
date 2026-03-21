email = input("Enter your email: ")


k = j = d = 0

if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") or (email[-3] == "."):
                for i in email:
                    if i.isspace(): 
                        k = 1
                    elif i.isalpha():
                        if i.isupper():  
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i in ["_", ".", "@"]:
                        continue
                    else:
                        d = 1
                if k == 1 or j == 1 or d == 1:
                    print("Wrong email 5")
                else:
                    print("Valid email")
            else:
                print("Wrong email 4")
        else:
            print("Wrong email 3")
    else:
        print("Wrong email 2")
else:
    print("Wrong email 1")

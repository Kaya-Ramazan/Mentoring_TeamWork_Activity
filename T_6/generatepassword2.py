import random
name = input("please enter your full name without any space: ")
password = []
for i in range(3):
    password.append(name[random.randint(0,len(name)-1)])
password += str(random.randint(1000,9999))
print(password)
print(''.join(password)) 
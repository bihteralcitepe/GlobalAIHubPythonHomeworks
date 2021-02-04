userInformation = list(range(4))
userInformation[0] = input("Enter your First Name: ")
userInformation[1] = input("Enter your Last Name: ")
userInformation[2] = input("Enter your Age: ")
userInformation[3] = input("Enter your Year of Birth: ")

for i in userInformation:
        print(i)
if int(userInformation[2]) >= 18:
        print("You can go out to the street.")
else:
        print("You can't go out because it's too dangerous!")
        
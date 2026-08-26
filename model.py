print(" I am a boy")
i = 1
for i in range(2):
    if i == 1:
        break
    else :
        print("done")
lucky_number = "3"        
while True:
     user = input("Guess a lucky number :")
     if user.isdigit() == True:
         break  
     else:
         print("Enter a valid number") 
while True:
    if user != lucky_number:
        print("try again :")
        user = input("Guess a lucky number :")
    else:
        print("number guessed correctly")  
        break
print("Who you really are?")


        
        

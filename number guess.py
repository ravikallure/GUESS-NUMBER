from random import randint

print('''
Select the level :
1. easy
2. medium
3. hard
''')

select = input("select here: ")

end = 0

if select == "1":
    print("You have selected easy level")
    end = 30
elif select == "2":
    print("You have selected medium level")
    end = 60
elif select == "3":
    print("You have selected hard level")
    end = 100
else:
    print("Invalid input, please try again.")
    exit()

avi = randint(1, end)
print(avi)  # for debugging, remove in final version

chances = 4
won = False

for i in range(chances):
    num = int(input(f"Guess the number between 1 to {end}: "))
    if num == avi:
        print("You won!")
        won = True
        break
    elif abs(num - avi) <= 5:
        print("It's nearest number!")
    else:
        print("the number is not near .")
if not won:
    print(f"You lost! The correct number was {avi}.")
    

    
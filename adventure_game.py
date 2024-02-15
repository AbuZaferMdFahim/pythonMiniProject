name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input(
        "You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ").lower()

    if answer == "swim":
        print("You swam acrross and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print('Not a valid option. You lose.')

elif answer == "right":
    answer = input(
        "You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ").lower()

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ").lower()

        if answer == "yes":
            answer = input("You talk to the stanger and he told you to go Thailand or Saudi (Thailand/Saudi)? ").lower()
            if answer == "thailand":
                answer = input("You go to take drug in thailand or go to laus (drug/laus)?").lower()
                if answer == "drug":
                    print("You take drag and got cancer. You Lose.")
                elif answer == "laus":
                    print("You go to laus and become slave to the USA people. You Lose.")
                else:
                    print('Not a valid option. You lose.')
            elif answer == "saudi":
                answer = input("You go to decide to do HAjj or Go to WWE. (hajj/wwe?)").lower()
                if answer =="hajj":
                    print("You decided to go Best Place in the World. You Won.")
                elif answer =="wwe":
                    print("You decided to go wwe and eat knockoutpunch by BIG SHOW. You Lose.")  
                else:
                    print('Not a valid option. You lose.')      
            else:
                    print('Not a valid option. You lose.')
        elif answer == "no":
            answer = input("You ignore the stranger and they are offended and but give you another chance.  go to USA or ready to punnishment. (usa/punnishment)").lower()
            if answer == "usa":
                answer = input("You come here and decided to go higher study or politics. (higher study/ politics)")
                if answer == "politics":
                    print("You do politics but trumph killed you. You Lose.")
                elif answer == "higher study":
                    answer = input("After Study what you wanna do. work criminal agency or work as a service holder. (criminal agency/ service holder)").lower()
                    if answer == "criminal agency":
                        print("You choose this and live a adventures life. You Won.")
                    elif answer == "service holder":
                        print("You choose boring life. But still You Won.")
                    else:
                        print('Not a valid option. You lose.')
                else:
                    print('Not a valid option. You lose.')
            elif answer =="punnishment":
                answer = input("After Punishment what you wanna choose one or two. (1/2)").lower()
                if answer == "1":
                    print("You decided punishment for no comitted crime. So you never be winner. You Lose.")
                elif answer == "2":
                    print("You decided punishment for no comitted crime. So you never be winner. You Lose.") 
                else:
                    print('Not a valid option. You lose.')   
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose.')

print("Thank you for trying", name)
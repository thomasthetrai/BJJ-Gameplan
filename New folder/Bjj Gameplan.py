Choice = input("Welcome to the best bjj gameplan, Write in which Stratergy you are going to use, Pick either Guard Or Attack: ")

print("You have chosen " + Choice)
if Choice == "Attack":
    Attack = input("Which type of Attack would you like to use 1- Kneecut, 2- Reverse kneecut 3- Toriando: ")
    if Attack == "1":
        print("Kneecut is when you are at the top and\n "
              "you control the opponent's legs with youre\n"
              "arms put youre knee on the opponent's thighs and then make a slice type of\n"
              "movement between the knees and the thighs then\n"
              "you get to the opponent's side, then you can get side control.\n")

    if Attack == "2":
        print("Reverse Kneecut is if you're gonna do a kneecut\n and then they have a leg between you and the opponent \n if that happens you have to take the opponents leg \n and throw both of you're legs over the opponent to jump over his guard \n and take side control")

    if Attack == "3":
        print("toriando is when you either grip the gi or hold the feet \n and whip it to the opposite side you wanna take side control \n the guard is just gonna go away and they easily give you the side control")


elif Choice == "Guard":
    Guard = input("Which Type of Guard would you like to use 1- Closed guard -2 Half Guard 3- Dela Riva: ")
    if Guard == "1":
        print("Closed guard is one of the best and safest Guards \n Closed guard is when you're legs are wrapped around \n you're opponent's stomach which also give's you \n a very good position since \n you have all the control and you can execute many diffirent \n types of finishes from here for example triangle \n or you can do a sweep such as the scissor sweeep")

    if Guard == "2":
        print("Half guard is not one of the best Guards in Bjj \n but it really helps if you are in a tight situation \n maybe if someone is gonna go and mount you can \n take you're legs and form a type of triangle for the opponet's foot \n it makes their feet stuck and they don't directly get the point \n for the mount and it's harder for them to execute certain finishes \n")

    if Guard == "3":
        print("Dela Riva is in my opinion one of the best guards \n it works by taking you're leg behind the thigh and one foot at the thigh \n there is very many sweeps you can execute from this position \n it is also a very safe position because \n if they want to attack you can push away with you're foot \n and if they wanna go you can drag them back. ")


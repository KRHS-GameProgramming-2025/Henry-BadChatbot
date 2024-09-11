name = input("Ello What is your name ")
if name  == "William Afton":
    print("YOU")
    want = input ("What do you want from me? ")
    print ("No I will not help you")
    leave = input ("Why wont you leave me alone? ")
    print ("LEAVE")
    if leave == "Delete": 
        print ("???")
        delete = input ("Are you sure you want do do this? ")
        if delete == "yes":
            print  ("Deleting Program... ")
            username = input ("Username ")
            password = input ("Password ")
        if username == "William Afton":
         print ("Hello William Afton Welcome to Afton Robotics")
        else:
            print ("Hello " + username + " And Welcome to Fazbear Entertainment And Faz Ent Program")
    else:
        print ("I am ending this conversation anything you would like to say before I end it")
        input (" ")
else:
    greeting = " Nice to meet you "
    print(greeting + " " + name)
    Color = input(" What is your favorite color? ")
    print( " Oh " + Color + " is mine too :3 ")
    day = input(" how is your day today, " + name + "?" + " ")
    if day == "Bad":
        print (" Oh Sorry... " + name + " ")

    else:
        print( "Well Thats good ")

    doing = input( "What have you been up too lately, " + name + "?" + " ")
    if doing == "Nothing":
        print("Sorry Goodbye")
    else:
        print(doing + " Is Interesting")
        print("Well thats all the questions, have a good day")

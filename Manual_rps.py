
import random


comput_scores = 0
user_scores = 0 
#rounds = 1
#winner = ''
#winning =''


CHOICE_CLASS_DISC = {
    0: "Rock",
    1: "Paper",
    2: "Scissors",
    3: "Nothing",
    4: "none"
}

def get_labels_dict():
    
    players_choices ={}
    labels_classes = "labels.txt"
    with open(labels_classes, 'r') as txt_file:
        
        for line in txt_file:            
            (key, value) = line.split()
            players_choices[int(key)] = value

    dict_class_value = players_choices
    return dict_class_value

def map_labels_classes(value):
    #class_value = get_labels_dict()
    #print(class_value[value])
    return CHOICE_CLASS_DISC[value]
    #return class_value[value]


def get_computer_choice():
    global computer_choice
    #computer_labels_dict = get_labels_dict()
    choice_list = ["Rock","Paper","Scissors","Nothing"]
    computer_choice = random.choice(choice_list)
    
    print("")
    print("\tPLEASE TYPE ONE OF THE OPTIONS BELLOW...")
    print("\t<----------------------------------------->")
    print(choice_list)
    #print(computer_choice)
    return computer_choice


    #for value in computer_labels_dict.values():
       # choice_list.append(value)

    #random_choice = choice_list
    


def get_user_choice():
    
    user_guess = input()
    
    return user_guess
    

def get_winner(computer_choice, user_select):

    global user_scores 
    global comput_scores
    #global rounds
    global winning
    
   
        
    if computer_choice == user_select:
        winning = "DRAW"
        print("The COMPUTER choice is {} and the USER choice is {}. This is a Draw".format(computer_choice,user_select))
        user_scores+=0
        comput_scores+=0
        print("Computer score is {} and User score is {}".format(str(comput_scores),str(user_scores)))
        #rounds+=1
        #print("\tROUND: {}".format(rounds))
        return winning
    if computer_choice == "Rock":
            
        if user_select == "Scissors":
            winning = "USER"
            print("The User choice is {} and the Computer choice is {}\n USER is winning".format(user_select,computer_choice))   
            user_scores +=1 
            print("User score is {} and Computer is {}".format(str(user_scores),str(comput_scores)))
            #rounds +=1
            #print("\tROUND: {}".format(str(rounds)))
            #total_user_count+=user_scores
            return winning

                           
        if user_select =="Paper":
            winning = "COMPUTER"
            print("The COMPUTER choice is {} and the USER choice is {}\n COMPUTER is  winning".format(computer_choice,user_select))
            comput_scores +=1
            print("Computer score is: {} and The User score is {}".format(str(comput_scores),str(user_scores)))
            #rounds +=1
            #print("\tROUND: {}".format(str(rounds)))           
            return winning
        if user_select =="Nothing":
            winning = "COMPUTER"
            print("The USER choice is {} and the Computer choice is {}\n COMPUTER is winning".format(user_select,computer_choice))
            comput_scores+=1
            print("Computer score is: {} AND The User score is {}".format(str(comput_scores),str(user_scores)))
            #rounds +=1
            #print("\tROUND: {}".format(str(rounds)))
            return winning
            
    if computer_choice == "Paper":

        if user_select == "Rock":  
            winning = "USER"
            print("The USER choice is {} and the Computer choice is {}\n USER is winning".format(user_select,computer_choice))
            user_scores+=1
            print("User score is: {} and the Computer score is {}".format(str(user_scores),str(comput_scores)))
            #rounds +=1
            #print("\tROUND: {}".format(str(rounds)))
            return winning
            #total_user_count+=user_scores
        if user_select =="Nothing":
            winning = "USER"
            print("The USER choice is {} and the Computer choice is {}\n USER is winning".format(user_select,computer_choice))
            user_scores+=1
            print("User score is: {} and the Computer score is {}".format(str(user_scores),str(comput_scores))) 
            #rounds +=1
            #print("\tROUND: {}".format(str(rounds)))
            return winning

        if user_select == "Scissors":
            winning = "USER"
            print("The COMPUTER choice is {} and the USER choice is {}\n COMPUTER is winning".format(computer_choice,user_select))           
            comput_scores+=1
            print("Computer score is: {} and the User score is {}".format(str(comput_scores),str(user_scores)))
            #rounds +=1
            #print("\tROUND: {}".format(str(rounds)))
            return winning

    if computer_choice == "Nothing":

        if user_select == "Paper":
            winning ="USER"
            print("The USER choice is {} and the Computer choice is {}\n USER is winning".format(user_select,computer_choice))
            user_scores+=1
            print("User score is: {} and the Computer score is {}".format(str(user_scores),str(comput_scores)))
            #rounds +=1
            #print("\tROUND: {}".format(str(rounds)))
            return winning

        if user_select == "Rock":
            winning = "COMPUTER"
            print("The USER choice is {} and the Computer choice is {}\n COMPUTER is winning".format(user_select,computer_choice))
            comput_scores+=1
            print("Computer score is: {} and the User score {}".format(str(comput_scores),str(user_scores)))
            #rounds +=1
            #print("\tROUND: {}".format(str(rounds)))
            return winning

        if user_select == "Scissors":
            winning = "USER"
            print("The USER choice is {} and the Computer choice is {}\n USER is winning".format(user_select,computer_choice))
            user_scores+=1
            print("User score is: {} and the Computer score is {}".format(str(user_scores),str(comput_scores)))
            #rounds +=1
            #print("\tROUND: {}".format(str(rounds)))
            return winning

             
    if computer_choice == "Scissors": 
        winning = "USER"           
        if user_select == "Paper":
            print("The USER choice is {} and the Computer choice is {}\n USER is winning".format(user_select,computer_choice))
            user_scores+=1
            print("User score is: {} and the User score is {}".format(str(user_scores),str(comput_scores)))
            #rounds +=1
            #print("\tROUND: {}".format(str(rounds)))
            return winning
            

        if user_select == "Rock":
            winning = "COMPUTER"
            print("The COMPUTER choice is {} and the USER choice is {}\n COMPUTER is winning".format(computer_choice,user_select))
            comput_scores+=1
            print("Computer score is: {} and the User score is {}".format(str(comput_scores),str(user_scores)))
            #rounds +=1
            #print("\tROUND: {}".format(str(rounds)))
            return winning

        if user_select =="Nothing":
            winning = "COMPUTER"
            print("The USER choice is {} and the Computer choice is {}\n COMPUTER is winning".format(user_select,computer_choice))
            comput_scores+=1
            print("Computer score is: {} and the User score is {}".format(str(comput_scores),str(user_scores)))
            #rounds +=1
            #print("\tROUND: {}".format(str(rounds)))
            return winning   
    else:
        print("Wrong entry. Please type the word as it showing on the screen")
            #print("")
   
           
def play_again():
       
    while True:

        user_choice = input("Do you want to play again...?(y/n)")
        if user_choice in ["Y","y","Yes","yes"]:
            play()
                   
        elif user_choice in ["No","no","N","n"]:
            print("GOOD BYE..!!")
            break
        else:
             break
  

 
def play():
    
    rounds =1
    print("")
    print("\t!!!...WELCOME TO THE MASTER MIND GAME...!!!")
    

    while (rounds < 5):
     
        print("")
        print("\t------------ROUND: {} -------------".format(str(rounds)))
        computer_user = get_computer_choice()
        User = get_user_choice()
        get_winner(computer_user, User) 
        
        rounds+=1
        

                                                     
    else:
        print("GAME OVER...")
        get_winner_score()


                   

def get_winner_score():
    global winner
    try:
        
        if comput_scores > user_scores:
            winner = "COMPUTER"
            print("{} wins the game with {} score(s).".format(winner,str(comput_scores)))
            return winner
                
        elif user_scores > comput_scores:
            winner = "USER"
            print("{} wins the game with {} score(s).".format(winner, str(user_scores)))
            return winner
        
        elif user_scores == comput_scores:
            winner = "DRAW"
            print(" THE USER Score is {}, and COMPUTER Score is {}.\n {} MATCH--".format(str(user_scores),str(comput_scores),winner))
            return winner
         
    finally:
        play_again()



        #play_again()
    

play()


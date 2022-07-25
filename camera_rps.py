#from asyncio import run_coroutine_threadsafe
#from winsound import PlaySound
import cv2
from cv2 import rectangle
from cv2 import putText

from keras.models import load_model 
import numpy as np 
import random
import time

comput_scores = 0
user_scores = 0
rounds = 1
#winning = ''
winner = ''
final_score = 5

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
    
    return CHOICE_CLASS_DISC[value]
    
"""
def get_user_choice():
    global user_choice
    max_value = np.argmax(prediction[0])
    user_input = map_labels_classes(max_value)
    if len(user_store) < 12:
        user_store.append(user_input)
    else:
        user_store.pop(0)
        user_store.append(user_input)

    if user_store.count("Rock") >=2:
        user_choice = "Rock"
    else:
        user_choice = max(user_store, key = user_store.count)

"""
def get_computer_choice():

    global computer_choice
    choice_list = ["Rock","Paper","Scissors","Nothing"]

    computer_choice = random.choice(choice_list)
    
    print("")
    print("\tPLEASE TYPE ONE OF THE OPTIONS BELLOW...")
    print("\t<----------------------------------------->")
    print(choice_list)
    #print(computer_choice)
    return computer_choice



def get_winner(computer_choice, user_select):
    global user_scores 
    global comput_scores
    global rounds
    global winning
    #global  final_score
    
   
        
    if computer_choice == user_select:
        winning = "DRAW"
        print("The COMPUTER choice is {} and the USER choice is {}. This is a Draw".format(computer_choice,user_select))
        user_scores+=0
        comput_scores+=0
        print("Computer score is {} and User score is {}".format(str(comput_scores),str(user_scores)))
        rounds+=1
        print("\tROUND: {}".format(rounds))
        #get_winner_score()
        return winning

    if computer_choice == "Rock":
            
        if user_select == "Scissors":
            winning = "USER"
            print("The User choice is {} and the Computer choice is {}\n USER is winning".format(user_select,computer_choice))   
            user_scores +=1 
            print("User score is {} and Computer is {}".format(str(user_scores),str(comput_scores)))
            rounds +=1
            print("\tROUND: {}".format(str(rounds)))
            #get_winner_score()
            #total_user_count+=user_scores
            return winning

                           
        if user_select =="Paper":
            winning = "COMPUTER"
            print("The COMPUTER choice is {} and the USER choice is {}\n COMPUTER is  winning".format(computer_choice,user_select))
            comput_scores +=1
            print("Computer score is: {} and The User score is {}".format(str(comput_scores),str(user_scores)))
            rounds +=1
            print("\tROUND: {}".format(str(rounds))) 
            #get_winner_score()       
            return winning
        if user_select =="Nothing":
            winning = "COMPUTER"
            print("The USER choice is {} and the Computer choice is {}\n COMPUTER is winning".format(user_select,computer_choice))
            comput_scores+=1
            print("Computer score is: {} AND The User score is {}".format(str(comput_scores),str(user_scores)))
            rounds +=1
            print("\tROUND: {}".format(str(rounds)))
            #get_winner_score()
            return winning
            
    if computer_choice == "Paper":

        if user_select == "Rock":  
            winning = "USER"
            print("The USER choice is {} and the Computer choice is {}\n USER is winning".format(user_select,computer_choice))
            user_scores+=1
            print("User score is: {} and the Computer score is {}".format(str(user_scores),str(comput_scores)))
            rounds +=1
            print("\tROUND: {}".format(str(rounds)))
            #get_winner_score()
            return winning
            #total_user_count+=user_scores
        if user_select =="Nothing":
            winning = "USER"
            print("The USER choice is {} and the Computer choice is {}\n USER is winning".format(user_select,computer_choice))
            user_scores+=1
            print("User score is: {} and the Computer score is {}".format(str(user_scores),str(comput_scores))) 
            rounds +=1
            print("\tROUND: {}".format(str(rounds)))
            #get_winner_score()
            return winning

        if user_select == "Scissors":
            winning = "USER"
            print("The COMPUTER choice is {} and the USER choice is {}\n COMPUTER is winning".format(computer_choice,user_select))           
            comput_scores+=1
            print("Computer score is: {} and the User score is {}".format(str(comput_scores),str(user_scores)))
            rounds +=1
            print("\tROUND: {}".format(str(rounds)))
            #get_winner_score()
            return winning

    if computer_choice == "Nothing":

        if user_select == "Paper":
            winning ="USER"
            print("The USER choice is {} and the Computer choice is {}\n USER is winning".format(user_select,computer_choice))
            user_scores+=1
            print("User score is: {} and the Computer score is {}".format(str(user_scores),str(comput_scores)))
            rounds +=1
            print("\tROUND: {}".format(str(rounds)))
            #get_winner_score()
            return winning

        if user_select == "Rock":
            winning = "COMPUTER"
            print("The USER choice is {} and the Computer choice is {}\n COMPUTER is winning".format(user_select,computer_choice))
            comput_scores+=1
            print("Computer score is: {} and the User score {}".format(str(comput_scores),str(user_scores)))
            rounds +=1
            print("\tROUND: {}".format(str(rounds)))
            #get_winner_score()
            return winning

        if user_select == "Scissors":
            winning = "USER"
            print("The USER choice is {} and the Computer choice is {}\n USER is winning".format(user_select,computer_choice))
            user_scores+=1
            print("User score is: {} and the Computer score is {}".format(str(user_scores),str(comput_scores)))
            rounds +=1
            print("\tROUND: {}".format(str(rounds)))
            #get_winner_score()
            return winning

             
    if computer_choice == "Scissors": 
        winning = "USER"           
        if user_select == "Paper":
            print("The USER choice is {} and the Computer choice is {}\n USER is winning".format(user_select,computer_choice))
            user_scores+=1
            print("User score is: {} and the User score is {}".format(str(user_scores),str(comput_scores)))
            rounds +=1
            print("\tROUND: {}".format(str(rounds)))
            #get_winner_score()
            return winning
            

        if user_select == "Rock":
            winning = "COMPUTER"
            print("The COMPUTER choice is {} and the USER choice is {}\n COMPUTER is winning".format(computer_choice,user_select))
            comput_scores+=1
            print("Computer score is: {} and the User score is {}".format(str(comput_scores),str(user_scores)))
            rounds +=1
            print("\tROUND: {}".format(str(rounds)))
            #get_winner_score()
            return winning

        if user_select =="Nothing":
            winning = "COMPUTER"
            print("The USER choice is {} and the Computer choice is {}\n COMPUTER is winning".format(user_select,computer_choice))
            comput_scores+=1
            print("Computer score is: {} and the User score is {}".format(str(comput_scores),str(user_scores)))
            rounds +=1
            print("\tROUND: {}".format(str(rounds)))
            #get_winner_score()
            return winning 
      
    else:
        print("Wrong entry. Please type the word as it showing on the screen")

    

    


def play_again():
       
    while True:

        user_choice = input("Do you want to play again...?(y/n)")
        if user_choice in ["Y","y","Yes","yes"]:
            get_winner(user_input, computer_move)
                   
        elif user_choice in ["No","no","N","n"]:
            print("GOOD BYE..!!")
            break
        else:
             break



#def play():
    #global rounds
    
    #rounds =1
    #print("")
    #print("\t!!!...WELCOME TO THE MASTER MIND GAME...!!!")
    

    #while (rounds < 5):
     
        #print("")
        #print("\t------------ROUND: {} -------------".format(str(rounds)))
        #computer_user = get_computer_choice()
        #User = get_user_choice()
        #get_winner(computer_user, user_input) 
        
        #rounds+=1
        

                                                     
    #else:
        #print("GAME OVER...")
        #get_winner_score()
 

def get_winner_score():
    global winner
    global final_score
    try:
        
        if comput_scores > user_scores:
            winner = "COMPUTER"
            print("{} wins the game with {} score(s).".format(winner,str(comput_scores)))
            return winner
                
        elif comput_scores < user_scores:
            winner = "USER"
            print("{} wins the game with {} score(s).".format(winner, str(user_scores)))
            return winner
        
        else:
            winner = "DRAW"
            print(" THE USER Score is {}, and COMPUTER Score is {}.\n {} MATCH--".format(str(user_scores),str(comput_scores),winner))
            return winner
    finally:
        print("Good Game")

        
        #play_again()

        
        """    #print("")
def gameDisplay():
    get_user_choice()
    cv2.rectangle(frame, (10,430), (440,350), (255,255,255), -1)
    cv2.putText(frame, "USER", (55,389), 1, 2, (0,0,0))
    cv2.putText(frame, "COMPUTER", (270,380), 1, 2, (0,0,0))
    cv2.putText(frame,  "/", (190,420), 2, 3, (0,0,0))
    cv2.putText(frame, user_choice, (20,420), 0, 1, (0,0,0))
    cv2.putText(frame, computer_choice, (320,420), 0, 1, (0,0,0))
    cv2.rectangle(frame, (175,80), (275,120), (20,120,20), -1)
    cv2.putText(frame, "click", (100,110), 3, 1, (0,0,0))
"""




model = load_model('keras_model.h5')
capture = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
pre_move = None
user_store = []

#winner =''
#user_choice =""
#countdown = 3
#computer_choice = "EMPTY"
#comput_scores = 0
#user_scores = 0

#rounds =1


while True: 
    ret, frame = capture.read()
    if frame is None:
        print("No output")
        continue
    else:
        frame = frame[32:, 118:]
    resized_frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalise the image 
    data[0] = normalized_image
    prediction = model.predict(data)
    max_value = np.argmax(prediction[0])
    user_input = map_labels_classes(max_value)

    if pre_move != user_input:
        if user_input !="none":
            computer_move = get_computer_choice()
            get_winner(user_input, computer_move)
            
            get_winner_score()
            
            #rounds+=1
            #if rounds == 4:
                #get_winner_score()
            
        else:
            computer_move = "none"
    pre_move = user_input
    

    #cv2.rectangle(frame, (10,10), (200, 50), (225,225,0), -1)
    #msg= "Round: " + str(rounds)
    #cv2.putText(frame, msg, (20,40), 1, 2, (0,0,0))

    cv2.rectangle(frame, (8,90), (240,40), (0,255,0), 2)
    msg = "CPU Score:"+ str(comput_scores)
    cv2,putText(frame,msg, (14,80),1,2, (0,0,0),2)


    cv2.rectangle(frame, (510, 90), (250, 40),(0, 255, 0), 2)
    msg2= "USER Score:"+ str(user_scores)
    cv2.putText(frame,msg2,(250,83),1,2,(0,0,0),2)

    cv2.rectangle(frame, (8, 200), (510, 150), (0, 255, 0), 2)
    msg3="CPU: "+computer_choice + " V "+"USER:"+user_input
    cv2.putText(frame,msg3,(8,185),1,2,(0,0,0),2)

    cv2.rectangle(frame, (8, 230), (510, 280),(0, 255, 0), 2)
    msg4 = "ROUND :"+str(rounds)+ "  "+ "WINNING:"+ winning
    cv2.putText(frame,msg4,(8,260),1,2, (0,0,0), 2)

    cv2.rectangle(frame, (45,325), (450,380), (255,0,255), 2)
    msg5 ="GAME WINNER: "+ winner
    cv2.putText(frame, msg5,(48,360),1,2, (0,0,0), 2)




    #cv2.putText(frame, "USER", (55,380),1,2, (0,0,0))
    #cv2.putText(frame,"COMPUTER", (270,380), 1,2, (0,0,0))
    #cv2.putText(frame, "V", (190,420), 2, 3, (0,0,0))
    #cv2.putText(frame, "Score: " + str(user_scores), (20,420), 4,1, (0,0,0))
    #cv2.putText(frame, "Score: " + str(comput_scores), (280,420),0,1, (0,0,0))
    #cv2.rectangle(frame, (50,80), (402,120), (20,170,20), -1)

    #cv2.rectangle(frame, (10,430), (440,350), (200,200,200), -1)
    #cv2.putText(frame, "Winning: " + winning, (55, 380),1, 2, (0,0,0))
    #cv2.putText(frame, "GAME WINNER: " + winner, (270, 380), 1, 2, (0,0,0))


    cv2.imshow('Rock Paper Scissor', frame)

    #print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#capture.release()

#cv2.destroyAllWindows()




    
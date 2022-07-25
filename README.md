# Rock_Paper_Sciss_Project

Rock_Paper_Scissors is a computer vision game in which the user shows actions using their hands,the commputer stored fews actions and the users will guesss the option.the user that shows the first action wins. The gane is played using a computer web camera.

- Milestone 1:


  In Milestone 1, an image project is created with four classes using a machine learning models 'Teachable Machine'. After creating the image project with Teachable-Machine,the zip file was downloaded and store to the computer file system,extracted and push to a github repository.
  
 - Milestone 2:


 in Milestone 2 a virtual environment is created using Conda an open source package management system and an environment system. After setting up the virtual environment, we run the model created in Milestone 1 into the local machine.
 
 - Milestone 3:
  In this milestone the game Rock-paper-scissors is created.in the first task a python file manual_rps.py is     created to play the game without the camera,and in the file we have two functions:
    -get_computer_choice:
      This function picks randomly the choice between'paper,rock,scissor'by using the random module.The choice      is store to a list variable.
     - get_user-_input:
     This function ask a user to type in a selection choice.
    In the next step of this Milestone,another function get_winner is created to check if one of the player wins;and the last part part of the task was the implementation of the function called play() to run the game.  
  
        -Milestone 4:
        In this milestone we create and implement get_winner function that include two arguments User_choice and comput_choice.Within the function we include a series of conditions (if's)statments  to meet the winner criteria.We also implemented a play() function.The function will call get_user_choice, get_computer_choice and pass them as parameter to get_winner() function to find the game winner.
        
         -Milestone 5:
         In this milestone we create another file cameras_rsp.py. Using the same steps with Manuals_rsp.py but this file will notuse the user input but the camera as input to play the game against the computer. We update this file with three variables 'user_scores' to count the number of scores the user has, and computer scores to count the number of scores the computer has. The last variable (rounds) define the number of rounds both have to complete the game. If the user or computer wins a function get_winner_score will be called to display the player that wins the game.CV2 graphical is used to display graphic information on the screen when the the game is load.
      

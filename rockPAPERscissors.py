from tkinter import *
import random

root = Tk()
root.geometry("400x200")




Label(root, text="Welcome to the rock, paper, scissors game").pack()

t_box = Entry(root)
t_box.pack()

player = False

def game():
    computer = random.choice(['Rock','Paper','Scissors'])
    player = t_box.get()
    if player == computer:
        Label(root, text="It's a tie").pack()
        
    elif player == "Paper":
        if computer == "Rock":
            Label(root, text="You win").pack()
        else:
            Label(root, text="You lose.").pack()        
    
    elif player == "Rock":
        if computer == "Scissors":
            Label(root, text="You win").pack()
        else:
            Label(root, text="You lose.").pack()  
            
    elif player == "Scissors":
        if computer == "Paper":
            Label(root, text="You win").pack()  
        else:
            Label(root, text="You lose.").pack()  
            
    else:
        Label(root, text="Errors")                      
     

def reset():
    computer = random.choice(['Rock','Paper','Scissors'])
    Label(root, text="The game has been reset").pack()
    
re = Button()
re ["text"] = "Reset"
re ["command"] = reset
re.pack()    

but = Button()
but ["text"] = "Submit"
but ["command"] = game
but.pack()



root.mainloop()
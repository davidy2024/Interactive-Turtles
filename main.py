from turtle import Screen,ontimer
from keyboardturtle import KeyboardTurtle
from clickableturtle import ClickableTurtle
from moveingturtle import MovingTurtle
from wall import Wall

def moveturtles():
  moveT.move_self()
  ontimer(moveturtles,1)


window = Screen()
window.bgpic("BG.png")


# set up instance of the screen
window = Screen()
screen_width = 600
screen_height = 400
window.setup(screen_width, screen_height)

#list up
wall_list = []

moving_thing_list = []


# set up clickable instance
button = ClickableTurtle()

#set up players
player_1 = KeyboardTurtle(window, walls = wall_list)
w1 = Wall(100, 0, 2, 2)
wall_list.append(w1)
wall_list.append(Wall(0, 100, 2, 2))
wall_list.append(Wall(0,-100,2,2))
wall_list.append(Wall(-100,0,2,2))

player_2 = KeyboardTurtle(window, "w", "s","d","a")
player_1.goto(0,200)
player_2.goto(200,0)

# set target of other player(our collison check) to the opposite player
player_1.other_player = player_2
player_2.other_player = player_1
#moving_thing_list.append(MovingTurtle(screen_width, screen_height, 0,0, player_1,player_2))

moveT = MovingTurtle(screen_width, screen_height, 100,100,player_1,player_2)
ontimer(moveturtles,1)



# This is needed to listen for inputs
window.listen()
window.mainloop()


# be CAREFUL. We aren't controlling the screen draws in this program, so NO while True loops

#TODO:  Check the classes and complete TODOs
#push to github repo.
#link repo to assignment
from turtle import Turtle, ontimer


class MovingTurtle(Turtle):
  def __init__(self, width, height, x, y, player_1,player_2):
    Turtle.__init__(self)
    self.width = width
    self.height = height
    self.x = x
    self.y = y
    self.player_1 = player_1
    self.player_2 = player_2

    # initial setup
    self.shape("circle") 
    self.shapesize(.5, .5, 1)
    self.penup()
    ontimer(self.move_self, 1)

    # variables
    self.x_spd = 4
    self.y_spd = 4
    self.collision_distance = 20

  def move_self(self):
    self.goto(self.xcor() + self.x_spd, self.ycor() + self.y_spd )
   
    if self.at_edge_x():
      self.x_spd = -self.x_spd

    if self.at_edge_y():
      self.y_spd = -self.y_spd

    if self.check_collision(self.player_1):
      quit()
    if self.check_collision(self.player_2):
      quit()


  

  def at_edge_x(self):
    if self.xcor() >= self.width/2 or self.xcor() <= -self.width/2:
      return True
    else:
      return False

  def at_edge_y(self):
    if self.ycor() >= self.height/2 or self.ycor() <= -self.height/2:
      return True
    else:
      return False

  def check_collision(self, obj_to_check):
    distance_x = obj_to_check.xcor() - self.xcor()
    distance_x = abs(distance_x)

    distance_y = obj_to_check.ycor() - self.ycor()
    distance_y = abs(distance_y)

    if distance_x < self.collision_distance and distance_y < self.collision_distance:
      return True
    else:
      return False

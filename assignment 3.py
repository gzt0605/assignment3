# Draw plus signs
# Ryan Ge
# September 20, 2016

import turtle
def get_side_length():
    side_length = input('Input the length of the sides for the plus signs:')
    return float(side_length)

def get_color():
    mycolor = input('Input the color of the plus signs:')
    return mycolor

def draw_rectangle(height, width, mycolor):

     # Move to the lower left corner
     turtle.goto(turtle.xcor() - width / 2, turtle.ycor() - height / 2)
     turtle.pendown()

     # Begin to fill in color
     turtle.color(mycolor, mycolor)
     #get_color('Green')
     #turtle.color('Green')
     turtle.begin_fill()
     for x in range(2):
         turtle.forward(width)
         turtle.left(90)
         turtle.forward(height)
         turtle.left(90)
     turtle.end_fill()
     turtle.penup()
     # Move back to original location after filling color
     turtle.goto(turtle.xcor() + width / 2, turtle.ycor() + height / 2)
# Make a def so that easier to draw plus signs
def draw_plus_sign(size, mycolor):

    # Draw the horizontal rectangle
      draw_rectangle(size, size * 3, mycolor)
    # Draw the vertical rectangle
      draw_rectangle(size * 3, size, mycolor)
def main():
    size = get_side_length()
    mycolor = get_color()
    # start to draw signs
    turtle.speed()
    # Make pen up avoid lines
    turtle.penup()
    # Draw first sign
    draw_plus_sign(size, mycolor)
    # Move to the right
    turtle.setx(turtle.xcor() + 3 * size)
    # Draw second sign
    draw_plus_sign(size, mycolor)
    # Move to the top
    turtle.goto(turtle.xcor() - 3 * size, turtle.ycor() + 3 * size)
    # Draw third sign
    draw_plus_sign(size, mycolor)
    # Move to the left
    turtle.goto(turtle.xcor() - 3 * size, turtle.ycor() - 3 * size)
    # Draw fourth sign
    draw_plus_sign(size, mycolor)
    # Move to the bottom
    turtle.goto(turtle.xcor() + 3 * size, turtle.ycor() - 3 * size)
    # Draw fifth sign
    draw_plus_sign(size, mycolor)
    turtle.down()

main()
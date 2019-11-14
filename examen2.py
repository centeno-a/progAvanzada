# LIBREIA TURTLE

import turtle
ventana=turtle.Screen ()
ventana.bgcolor('red')
ventana.title('mi ventana')

rafael=turtle.Turtle()
rafael.shape('turtle')
rafael.color('blue')
rafael.pensize(2)
rafael.speed(3)

i=10
e=5
rafael.left(90)
rafael.forward(e)
rafael.right(90)
rafael.forward(i)
rafael.right(90)
rafael.forward(i)
rafael.right(90)
rafael.forward(i+e)

i=10
e=5
while i<=120:
    rafael.right(90)
    rafael.forward(i+e)

    i=i+e

rafael.right(90)
rafael.forward(i+e)



ventana.mainloop()

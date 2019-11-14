# examen2

import turtle
ventana=turtle.Screen ()
ventana.bgcolor('white')
ventana.title('mi ventana')

rafael=turtle.Turtle()
rafael.shape('turtle')
rafael.color('black')
rafael.pensize(2)
rafael.speed(5)

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

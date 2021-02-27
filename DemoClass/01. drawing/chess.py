import turtle

'''
国际象棋：4*8 
1.车马象王后象马车
2.兵*8 
'''

size = 50
font_size = 32
black = '♜♞♝♛♚♟'
white = '♖♘♗♕♔♙'

black_1 = '♜♞♝♛♚♝♞♜'
black_2 = '♟♟♟♟♟♟♟♟'

white_1 = '♜♞♝♛♚♝♞♜'
white_2 = '♟♟♟♟♟♟♟♟'

turtle.speed(0)
turtle.hideturtle()
turtle.tracer(False)

colors = ['white', 'gray']
for r in range(8):
    turtle.penup()
    turtle.goto(-size * 8 / 2, size * 8 / 2 - r * 50)
    turtle.pendown()
    for c in range(8):
        turtle.fillcolor(colors[(r * 8 + c + r) % 2])
        turtle.begin_fill()
        for k in range(5):
            turtle.forward(size)
            turtle.left(90)
        turtle.right(90)
        turtle.end_fill()
turtle.penup()


def draw_pieces(pos, pieces):
    turtle.goto(pos)
    for c in pieces:
        turtle.write(c, font=('arial', font_size))
        turtle.forward(size)


draw_pieces((-size * 8 / 2, size * 8 / 2), black[:5] + black[-4::-1])
draw_pieces((-size * 8 / 2, size * 8 / 2 - size), black[-1] * 8)
draw_pieces((-size * 8 / 2, size * 8 / 2 - size * 6), white[-1] * 8)
draw_pieces((-size * 8 / 2, size * 8 / 2 - size * 7), white[:5] + white[-4::-1])

turtle.update()
turtle.done()

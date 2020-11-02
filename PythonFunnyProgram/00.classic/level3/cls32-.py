    # global question_index
    # for i in range(len(option_list)):
    #     if position_list[i][0] - 80 < x < position_list[i][0]+30 and position_list[i][1] < y < position_list[i][1] + 80:
    #         if option_list[question_index][i].split('.')[1] == answer_list[question_index]:
    #             question_index += 1
    #             result(result_pen, 'right')
    #             getQuestion(question_pen, question_index)
    #         else:
    #             result(result_pen, 'wrong')


#
# def init():
#     global question_list, answer_list, option_list, position_list, question_index, question_pen, result_pen
#     #turtle.bgpic('背景.png')
#     turtle.setup(720, 720)
#     question_list = ['[整数在Python中是用什么表示的?]', '[怎样在Python中输出?]', '[条件判断在Python中是怎么写的?]']
#     answer_list = ['int', 'print', 'if']
#     option_list = [['A.int', 'B.float', 'C.str'],
#                    ['A.while', 'B.print', 'C.input'],
#                    ['A.if', 'B.list', 'C.turtle']]
#     position_list = [[-180, -100], [0, -100], [200, -100]]
#     question_index = 0
#     question_pen = turtle.Pen()
#     question_pen.hideturtle()
#     result_pen = turtle.Pen()
#     result_pen.hideturtle()
#     result_pen.penup()
#     result_pen.goto(-100, -50)
#
# #绘制文字
# def drawText(p, color, text, size=20):
#     p.pencolor(color)
#     p.write(text, font=('Arial', size))
#
# #按序显示题目和选项
# def getQuestion(p, index):
#     p.clear()
#     p.penup()
#     p.goto(-300, 150)
#     if index >= len(question_list):
#         p.goto(-50, 0)
#         drawText(p, 'green', '已通关')
#         return
#     drawText(p, 'black', question_list[index])
#
#     for i in range(3):
#         p.penup()
#         p.goto(position_list[i][0] - 55 , position_list[i][1] + 25)
#         drawText(p, 'black', option_list[index][i])
#
# def checkPos(x, y):
#     global question_index
#     for i in range(len(option_list)):
#         if position_list[i][0] - 80 < x < position_list[i][0]+30 and position_list[i][1] < y < position_list[i][1] + 80:
#             if option_list[question_index][i].split('.')[1] == answer_list[question_index]:
#                 question_index += 1
#                 result(result_pen, 'right')
#                 getQuestion(question_pen, question_index)
#             else:
#                 result(result_pen, 'wrong')
#
# def result(p, r):
#     p.goto(-100, 100)
#     if r == 'right':
#         drawText(p, 'green', '恭喜你回答正确', 30)
#     else:
#         drawText(p, 'red', '    再想想哦', 30)
#     time.sleep(1)
#     p.clear()

# init()
# getQuestion(question_pen, question_index)
# turtle.tracer(0)
# turtle.onscreenclick(checkPos)
# turtle.done()

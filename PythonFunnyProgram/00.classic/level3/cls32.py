import time
import turtle

current_question = 0

question_list = [
    {'content': '整数在''Python中是用什么表示的?', 'options': ['int', 'float', 'str'], 'answer': 0},
    {'content': '怎样在Python中输出?', 'options': ['while', 'print', 'input'], 'answer': 1},
    {'content': '条件判断在Python中是怎么写的?', 'options': ['if', 'list', 'turtle'], 'answer': 0},
]

question_pane = {
    'size': (720, 600),
    'content_loc': (-300, 150),
    'option_loc': ((-180, -100), (0, -100), (200, -100)),
    'hint_loc': (-100, 100)
}


def selection_answer(x, y):
    """获取鼠标选中了哪个选项"""
    global question_pane
    for i, loc in enumerate(question_pane['option_loc']):
        if loc[0] - 80 < x < loc[0] + 80 and loc[1] - 80 < y < loc[1] + 80:
            return i
    return -1


# 绘制文字
def draw_text(text, pos=(0, 0), color='black', size=30):
    turtle.penup()
    turtle.goto(pos)
    turtle.pendown()
    turtle.color(color)
    turtle.write(text, font=('Arial', size))


def show_question():
    """显示题目"""
    global question_list, question_pane, current_question
    turtle.clear()
    if current_question >= len(question_list):
        draw_text('已通关', (-50, 0), 'green')
    else:
        draw_text(question_list[current_question]['content'], question_pane['content_loc'])
        for i, s, l in zip('ABC', question_list[current_question]['options'], question_pane['option_loc']):
            draw_text(i + '.' + s, l)


def show_hint(type):
    """显示提示"""
    global question_pane
    if type == 'pass':
        draw_text('恭喜你回答正确', question_pane['hint_loc'], 'green', 20)
    elif type == 'err':
        draw_text('    再想想哦', question_pane['hint_loc'], 'red', 20)
    time.sleep(1)
    turtle.undo()


def check_pos(x, y):
    """处理鼠标点击事件"""
    global question_list, question_pane, current_question
    if current_question >= len(question_list):
        return
    answer = selection_answer(x, y)
    if answer == question_list[current_question]['answer']:
        show_hint('pass')
        current_question += 1
        show_question()
    elif answer != -1:
        show_hint('err')


turtle.hideturtle()
turtle.bgcolor('skyblue')
turtle.setup(question_pane['size'][0], question_pane['size'][1])
show_question()
turtle.tracer(0)
turtle.onscreenclick(check_pos)
turtle.done()

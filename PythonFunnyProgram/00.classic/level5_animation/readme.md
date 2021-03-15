<h2> 概述 </h2>
这个level是利用turtle做动画，主要是理解函数在编程中的应用

##### The template code:
```
"""
create by ric
"""
"""
imports
"""
import turtle

"""
global status variables
"""

def init():
    pass


def update():
    pass


def draw():
    pass


def flush():
    update()
    draw()
    turtle.ontimer(flush, FPS)


init()
flush()

turtle.done()

```    


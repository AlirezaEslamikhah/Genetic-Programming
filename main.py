import numpy as np
import random_expression_tree as ret
import genetic_programing as gen
import matplotlib.pyplot as plt

def main_function(x,y):
    """
    این تابع در واقع تابع اصلی ما و همان چیزی است که ما باید به آن با 
    استفاده از الگوریتم ژنتیک برسیم سپس میتوانیم با استفاده از این تابع 
    مقادیر مختلف را بدست آوریم
    """
    result = x + y / 100 
    return result

input_x =[]
input_y = []
output = []
for i in range(0,1000):
    input_x.append(i)
    input_y.append(np.random.randint(0,10))

for i in range(1000):
    # print(main_function(input_x[i],input_y[i]))
    output.append(main_function(input_x[i],input_y[i]))

""" 
حالا نوبت اینست که یک جمعیت اولیه ایجاد کنیم پس با استفاده از کلاسی که در فایلی دیگر ایجاد کرده ایم
یک جمعیت اولیه ایجاد میکنیم و برای هر شخص ازین جمعیت یک درخت ایجاد میکنیم 
سپس چندین بار ایتریشن زده و در آخر بهترین را به عنوان جواب برمیگردانیم
"""
gene = gen.generation(6,input_x,input_y,output,itteration=1000)

final_tr = gene.gp()
output = ""
for i in range(len(final_tr.graph)):
    output += final_tr.graph[i] + "  "
print("The final expression is :",output)

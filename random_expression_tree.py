# from binarytree import Node
# from binarytree import build
import random
# from math import *
import math
import sys 
sys.float_info.max
exp = {1:['+', '-', '*', '/'],2:['sin','cos']}
val = ['x','y']
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.parent = None
        
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val), 
        printInorder(root.right)

class Tree:
    def __init__(self,depth): ## فراهم سازی کانستراکتور درخت و تعیین عمق درخت
        self.depth = depth
        self.graph = []
        self.fitness = None
        self.random_expression_tree()
    def random_expression_tree(self,height = 0): # تولید درخت تصادفی
        """
        در ابتدا چندین نظریه برای درخت مطرح شد که معروف ترین آنها اینگونه بود که یک روت در نظر گرفته 
        و بیاییم چپ و راست برای آن رندوم تولید کنیم ولی در این روش برای کراس اور به دردسر میخوریم زیرا 
        تولید نود تصادفی کمی دشوار میشد بعد از آن گفتیم از لیست استفاده کنیم ولی مشکلی که این روش داشت 
        این بود که ما چون از اول باید نودها را پر میکردیم و تعداد زیادی نود چپ و راست نداشتند پس درون لیست ما 
        ناچارا تعدادی زیادی نال قرار میگرفت برای حل این مشکل گراف را اینگونه تعریف کردیم 
        از چپ شروع میکنیم و تا هرجا که لازم بود همین چپ را در عمق ادامه میدهیم تا به یک متغیر برسیم 
        سپس آن را برمیگردانیم البته برای این روش بنده از اینترنت کمک گرفتم که این روش پویا را معرفی کرده بود
        """
        if height == self.depth:
            self.graph.append(random.choice(val))
        else:
            if random.random() > 0.3:
                vv = random.choice(exp[2] + exp[1])
                if vv in exp[1]:
                    self.graph.append(vv)
                    self.random_expression_tree(height + 1)
                    self.random_expression_tree(height + 1)
                else:
                    self.graph.append(vv)
                    self.random_expression_tree(height + 1)
            else:
                v = random.choice(val)
                self.graph.append(v)
    def calculate_tree(self,input1,input2,position):
        """
        بعد از ساختن درختها اینبار نوبت به محاسبه درخت میباشد به طوری که اگر یک یا چند ورودی 
        به آن بدهیم بتواند خروجی را به ما برگرداند به طوری که تمام ورودیها در آن دخیل بوده اند
        در این تابع ما به صورت بازگشتی حرکت میکنیم به طوری که اگر به عبارتی رسیدیم  که دو ورودی
        میگرفت عبارت چپ و راست برایش مشخص میکنیم و در آخر آنها را با هم جمع یا تفریق و غیره میکنیم
        یک حالت پایه هم میگذاریم که اگر به متغیر رسیدیم برگرداند
        """
        ## base case 
        if self.graph[position] == 'x':
            return input1 , position
        elif self.graph[position] == 'y':
            return input2 , position
        elif self.graph[position] == '+':
            poz = position
            left , position = self.calculate_tree(input1,input2,poz+1)
            right , position = self.calculate_tree(input1,input2,poz+1)
            return left + right , poz
        elif self.graph[position] == '-':
            poz = position
            left , position = self.calculate_tree(input1,input2,poz+1)
            right , position = self.calculate_tree(input1,input2,poz+1)
            return left - right , poz
        elif self.graph[position] == '*':
            poz = position
            left , position = self.calculate_tree(input1,input2,poz+1)
            right , position = self.calculate_tree(input1,input2,poz+1)
            return left * right , poz
        elif self.graph[position] == '/':
            poz = position
            left , position = self.calculate_tree(input1,input2,poz+1)
            right , position = self.calculate_tree(input1,input2,poz+1)
            if left == 0 or right == 0:
                return 0 , poz
            return left / right , poz
        elif self.graph[position] == 'sin':
            left , position = self.calculate_tree(input1,input2,position+1)
            return math.sin(left) , position
        elif self.graph[position] == 'cos':
            left , position = self.calculate_tree(input1,input2,position+1)
            return math.cos(left) , position
    def fitnessss (self,input1,input2,output):
        """
        این تابع برای محاسبه فیتنس درخت است که به طوری که اگر خروجی درخت با 
        خروجی داده شده مطابقت داشت
        فیتنس بیشتری داشته باشد
        """
        result = 0
        for i in range(len(input1)):
            result += (self.calculate_tree(input1[i], input2[i], 0)[0] - output[i]) ** 2
        # print(result)
        r = str(result)
        n = len(r)
        if n > 35:
            r = r[:35]
            result = float(r)
        self.fitness = result / (len(input1))
        return self.fitness
    
    








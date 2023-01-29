import numpy as np
import random
import random_expression_tree as ret

exp = {1:['+', '-', '*', '/'],2:['sin','cos']}
val = ['x','y']
class generation:
    """
    این کلاس برای ایجاد جمعیت اولیه است و برای هر شخص یک درخت ایجاد میکند
    سپس با استفاده از این کلاس میتوانیم ایتریشن های مختلفی را انجام دهیم 
    و جمعیت را بهتر کنیم سپس بهترین را به عنوان جواب برمیگردانیم
    """
    def __init__(self,depth,input_x,input_y,output,itteration=1000):
        self.depth = depth
        self.generation_list = []
        self.first_size = 4000
        self.select = 800
        self.generation_list = self.create_generation(self.depth,self.first_size,self.select)
        self.input_x = input_x
        self.input_y = input_y
        self.output = output
        self.itteration = itteration
    def create_generation(self,depth,first_size,select):
        result = []
        for i in range(first_size):
            result.append(ret.Tree(depth))
            # print(result[i].graph)
        return result
    
    def _fitness(self):
        """
        این تابع برای محاسبه فیتنس کل جامعه است
        """
        result = []
        for i in range(self.first_size):
            result.append(self.generation_list[i].fitnessss(self.input_x,self.input_y,self.output)) 
            print(result[i])
            if result[i] == 10000:
                print(self.generation_list[i].graph)
        return result
    
    def sort_population(self , generation , first_size , select):
        """
        این تابع برای کمک به پیدا کردن والد است
        """
        best = self.generation_list[0]
        for i in range(first_size):
            if generation[i].fitness < best.fitness:
                best = generation[i]
        return best
    
    def traverse(self,index,parent):
        """
        این تابع برای پیدا کردن متغیر در یک درخت است
        """
        if parent.graph[index] == "x" or parent.graph[index] == "y":
            return index + 1
        else:
            return self.traverse(index+1,parent)
    
    def generate_child(self,parent1,parent2):
        """
        این تابع که در واقع اصلی ترین تابع ما هست برای کراس اور کردن و به نوعی
        ساختن یک بچه از بین دو والد و اضافه کردن آن به جمعیت است
        بدین صورت کار میکند که ابتدا از والد اول یک ایندکس رندوم و سپس از والد دوم یک ایندکس
        رندوم دیگر انتخاب کرده و اینها را به هم متصل میکند 
        """
        result = ret.Tree(self.depth)
        index1 = np.random.randint(len(parent1.graph))
        index2 = np.random.randint(len(parent2.graph))
        ## ابتدا دو اینکدس تصادفی از والدین برداشته و سپس چک میکنیم 
        ## که در کدام ایندکس یک متغیر وجود دارد سپس از همان اول را برداشته 
        ## و تا زمانی که به متغیر میرسد را از هر والد برداشته و در نهایت آنها را به هم متصل میکنیم
        ## منبع : https://favtutor.com/blogs/invert-binary-tree
        end1 = self.traverse(index1,parent1)
        end2 = self.traverse(index2,parent2)
        result.graph = parent1.graph[:index1] + parent2.graph[index2 : end2] + parent1.graph[end1 :]
        return result
    def mutate(self,child):
        p = np.random.randint(len(child.graph)) ## تابعی برای میوتیت کردن یا به نوعی ضعیف کردن بچه ایجاد شده از کراس اور
        if child.graph[p] in exp[1] or child.graph[p] in exp[2]:
            if child.graph[p] in exp[1]:
                child.graph[p] = random.choice(exp[1])
            else:
                child.graph[p] = random.choice(exp[2])
        else:
            child.graph[p] = random.choice(val)
        return child
    
    def get_worst(self):
        worst = self.generation_list[0]
        for i in range(1, len(self.generation_list)):
            if self.generation_list[i].fitness > worst.fitness:
                worst = self.generation_list[i]
        return worst
    def replace(self,child):
        worst = self.get_worst()
        if child.fitness < worst.fitness:
            for i in range(len(self.generation_list)):
                if self.generation_list[i].fitness == worst.fitness:
                    # print("hello",worst.fitness,self.generation_list[i].fitness,len(self.generation_list))
                    self.generation_list[i] = child
                    break

    def gp(self):
        """
        در این تابع ابتدا بعد از بدست اوردن فیتنسها میتوانیم بهترینها را انتخاب کنیم
        سپس آنها را برای کراس اور انتخاب کنیم و در نهایت  بچه های جدید را ایجاد کنیم
        بعد از آن هم آنها را جایگزین درخت های ضعیف تر کنیم
        """
        self._fitness()
        for i in range(self.itteration):## در اینجا هر سری دو والد انتخاب کرده و آنها رو کراس اور میکنیم
            parent1 = self.sort_population(self.generation_list,self.first_size,self.select)
            # print("hello")
            parent2 = self.sort_population(self.generation_list,self.first_size,self.select)
            # print("ooooo",self.sort_population(self.generation_list, self.first_size, self.select).fitness)
            child = self.generate_child(parent1,parent2)
            child = self.mutate(child)
            child.fitness = child.fitnessss(self.input_x,self.input_y,self.output)
            self.replace(child)
        # return self.final_tree()
        best_tree = self.generation_list[0] ## در اینجا بهترین درخت را برمیگردانیم   
        for i in range(self.first_size):
            if self.generation_list[i].fitness > best_tree.fitness:
                best_tree = self.generation_list[i]
        minn = 1100000
        for i in self.generation_list:
            if i.fitness < minn:
                minn = i.fitness
        print("the best is",minn)
        return best_tree
'''
/* File Info 
 * Author:      Linbin Lai 
 * CreateTime:  2019/11/18 下午6:47:50 
 * LastEditor:  Linbin Lai 
 * ModifyTime:  2019/11/18 下午6:48:30 
 * Description:  可以统计同时掷多个不同的骰子的结果 
*/ 
'''
from random import randint
import pygal

class Dice():
    """表示一个骰子的类"""
    def __init__ (self,sides_num=6):#初始化骰子，设置骰子有六个面
        self.sides_num=sides_num

    def set_sides(self,sides_num):
        self.sides_num=sides_num

    def roll(self):#返回一个1-sides_num之间的随机值
        return randint(1,self.sides_num)

    def dice_rolling(self,rool_times):
        results=[]
        
        for a in range(0,rool_times):
            result=self.roll()
            results.append(result)
        return results

def add_list(list1,list2):
    addlists=[]
    for value1,value2 in zip(list1, list2):#用zip函数将两个列表打包保证value1和value2各自在两个列表中循环
        add_element=value1+value2
        addlists.append(add_element)

    return addlists

def result_frequency_static(results,sides):
    #对结果进行统计
    frequencies=[]
    for value in range(1,sides+1):
        frequency=results.count(value)
        frequencies.append(frequency)
    print(frequencies)
    return frequencies




if __name__ == "__main__":
    die=Dice()

    hist=pygal.Bar()
    frequencies=[]
   

    rool_times=int(input("please input the rooling times:\n"))
    dice_num=int(input("please input the number of dices:\n"))

    hist.title=f"Result of roolling {dice_num} dices {rool_times} times."
    hist.x_labels=list(range(1,dice_num*9))
    hist.x_title="Result"
    hist.y_title="Frequency of Result"

    result_add=[0]*rool_times
    print(result_add)
    
    for i in range(0,dice_num):
        dice_sides=int(input(f"please input the sides of dice_{i} 【<10】:\n"))
        die.set_sides(dice_sides)
        results=die.dice_rolling(rool_times)

        print(results)

        frequencies=result_frequency_static(results,dice_sides)

        hist.add(f'D{i}',frequencies)

        result_add=add_list(result_add,results)
        results=[]
    
    frequencies=result_frequency_static(result_add,dice_num*9)
    hist.add('summary',frequencies)
    hist.render_to_file('dice_enhance.svg')


    pass
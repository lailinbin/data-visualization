'''
/* File Info 
 * Author:      Linbin Lai 
 * CreateTime:  2019/11/18 下午4:39:32 
 * LastEditor:  Linbin Lai 
 * ModifyTime:  2019/11/18 下午4:39:42 
 * Description: 
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


if __name__ == "__main__":
    die=Dice()

    die.set_sides(9)
    rool_times=int(input("please input the rooling times:\n"))
    results=die.dice_rolling(rool_times)

    print(results)

    #对结果进行统计
    frequencies=[]
    for value in range(1,die.sides_num+1):
        frequency=results.count(value)
        frequencies.append(frequency)
    print(frequencies)

    #对结果进行可视化
    hist=pygal.Bar()

    hist.title=f"Result of roolling one D{die.sides_num} {rool_times} times."
    hist.x_labels=list(range(1,die.sides_num+1))
    hist.x_title="Result"
    hist.y_title="Frequency of Result"
    hist.add(f'D{die.sides_num}',frequencies)
    hist.render_to_file('test.svg')


    pass
        

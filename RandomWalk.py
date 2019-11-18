'''
/* File Info 
 * Author:      Linbin Lai 
 * CreateTime:  2019/11/12 上午11:05:45 
 * LastEditor:  Linbin Lai 
 * ModifyTime:  2019/11/12 上午11:08:42 
 * Description: 
*/ 
'''

from random import choice
import matplotlib.pyplot as plt

class RandomWalk():
    '''一个生成随机漫步的类'''
    def __init__(self,num_points=5000):#初始化随机漫步的属性
        self.num_points=num_points
        self.x_values=[0]#起点定为（0，0）
        self.y_values=[0]

    def fill_walk(self):
        while len(self.x_values)<self.num_points:
            x_direction=choice([-1,1])
            x_distance=choice(list(range(0,101)))
            x_step=x_direction*x_distance

            y_direction=choice([-1,1])
            y_distance=choice(list(range(0,101)))
            y_step=y_direction*y_distance

            #拒绝原地踏步
            if x_step==0 or y_step==0 :
                continue

            #计算下一个点的坐标位置
            next_x=self.x_values[-1]+x_step
            next_y=self.y_values[-1]+y_step

            #将计算好的坐标位置加入列表
            self.x_values.append(next_x)
            self.y_values.append(next_y)

if __name__ == "__main__":
    rw=RandomWalk(50000)
    rw.fill_walk()
    plt.scatter(rw.x_values,rw.y_values,c=rw.y_values,s=1,edgecolors='none')
    plt.show()
    pass
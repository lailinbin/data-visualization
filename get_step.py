'''
/* File Info 
 * Author:      Linbin Lai 
 * CreateTime:  2019/11/18 下午3:46:36 
 * LastEditor:  Linbin Lai 
 * ModifyTime:  2019/11/18 下午3:46:56 
 * Description:用于get_step函数计算随机漫步每次的方向和步长对随机漫步进行改进
*/ 
'''

from random import choice
import matplotlib.pyplot as plt

class RandomWalk():
    '''一个生成随机漫步的类'''
    def __init__(self,num_points=5000):#初始化随机漫步的属性
        self.num_points=num_points#漫步的步数
        self.x_values=[0]#起点定为（0，0）
        self.y_values=[0]

    def fill_walk(self):
        while len(self.x_values)<self.num_points:
            x_step=self.get_step()
            y_step=self.get_step()
            #拒绝原地踏步
            if x_step==0 or y_step==0 :
                continue

            #计算下一个点的坐标位置
            next_x=self.x_values[-1]+x_step
            next_y=self.y_values[-1]+y_step

            #将计算好的坐标位置加入列表
            self.x_values.append(next_x)
            self.y_values.append(next_y)
    
    def get_step(self):#计算漫步的方向和步长
            direction=choice([-1,1])
            distance=choice(list(range(0,101)))
            step=direction*distance
            return step


if __name__ == "__main__":
    rw=RandomWalk(50000)
    rw.fill_walk()
    plt.scatter(rw.x_values,rw.y_values,c=rw.y_values,s=1,edgecolors='none')
    plt.show()
    pass
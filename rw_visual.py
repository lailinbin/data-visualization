'''
/* File Info 
 * Author:      Linbin Lai 
 * CreateTime:  2019/11/12 上午11:34:02 
 * LastEditor:  Linbin Lai 
 * ModifyTime:  2019/11/12 上午11:35:12 
 * Description:模拟多次随机漫步 
*/ 

'''

import matplotlib.pyplot as plt
from RandomWalk import RandomWalk

if __name__ == "__main__":
   
    while True:
        rw=RandomWalk()
        rw.fill_walk()
        plt.figure(figsize=(10,6)) 
        point_num=list(range(rw.num_points))
        plt.scatter(rw.x_values,rw.y_values,c=point_num,cmap=plt.cm.Blues,edgecolors='none',s=10)
        
        #突出起点和终点
        plt.scatter(0,0,c='green',s=100)
        plt.scatter(rw.x_values[-1],rw.y_values[-1],c='yellow',s=100)

        #隐藏坐标轴
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)

        #调整窗口尺寸
   
        plt.show()

        keepruning=input("Make another RandomWalk?(Y/N):")
        if keepruning =='N':
            break
    pass

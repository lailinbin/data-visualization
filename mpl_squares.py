'''
 * File Info 
 * Author:      Linbin Lai 
 * CreateTime:  2019/11/9 下午9:18:16 
 * LastEditor:  Linbin Lai 
 * ModifyTime:  2019/11/11 下午5:07:15 
 * Description:  pratice of data visualization
'''

import matplotlib.pyplot as plt

#绘制直方图的练习

input_values=[1,2,3,4,5]
squareas=[1,4,9,16,25]
x_values=[x for x in range(1,101,10)]
y_values=[x*2 for x in x_values]
plt.plot(input_values,squareas,linewidth=6)
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Reds)#S是点的大小，50时大小正好合适。C是设置颜色,这边是让c值根据y_values改变颜色。在通过cmap使y值匹配相应的颜色
plt.title("Square Numbers",fontsize=24)
plt.xlabel("value",fontsize=24)
plt.ylabel("Square of Value",fontsize=24)

plt.tick_params(axis='both',labelsize=14)
plt.show()
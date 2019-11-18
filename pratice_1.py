'''
/* File Info 
 * Author:      Linbin Lai 
 * CreateTime:  2019/11/12 上午10:45:24 
 * LastEditor:  Linbin Lai 
 * ModifyTime:  2019/11/12 上午10:45:37 
 * Description: 立方的彩色图表
*/ 
'''
import matplotlib.pyplot as plt

x_values=[x for x in range(1,5001)]
y_values=[x**3 for x in x_values]

plt.title("x^3 Numbers",fontsize=24)
plt.xlabel("value",fontsize=24)
plt.ylabel("X^3 of Value",fontsize=24)

plt.plot(x_values,y_values,c='blue')
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Reds)
plt.show()
plt.savefig('pratice_1.png',bbox_inches='tight')
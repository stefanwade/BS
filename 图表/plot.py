#coding:utf-8
#gbk
import matplotlib.pyplot as plt 
import numpy as py 
import matplotlib

print matplotlib.matplotlib_fname()

y = [600, 150, 200, 300, 200, 100, 125, 180]
x = [60, 65, 73, 70, 65, 58, 66, 67]
plt.title(u'图片')
plt.xlabel(u'x轴')
plt.ylabel(u'y轴')
plt.scatter(x, y)
plt.plot(x, y, color = "blue", linewidth = 1.0, linestyle = "-")
plt.show()
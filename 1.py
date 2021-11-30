import matplotlib.pyplot as plt
import matplotlib

plt.style.use('seaborn')
matplotlib.rc("font",family='MicroSoft YaHei',weight="bold")
#mpl.rcParams['font.sans-serif'] = ['SimHei'] 

x_values = range(1,1001)
y_values = [x**2 for x in x_values]
fig, ax = plt.subplots()
#ax.plot(input_value,Squares,linewidth = 3)
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s=10)
ax.set_title("平方数",fontsize = 24)
ax.set_xlabel("value",fontsize = 14)
ax.set_ylabel("值的平方",fontsize = 14)
ax.axis([0,1100,0,1100000])
ax.tick_params(axis = 'both',which = 'major',labelsize = 14)
#plt.savefig('squares_plot.png',bbox_inches = 'tight')
plt.show()
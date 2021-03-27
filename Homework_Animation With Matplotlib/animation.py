import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
import sqlite3
import pylab as py
from scipy.stats import shapiro
from scipy import stats
import seaborn as sns

connection = sqlite3.connect('data_db.db')
c = connection.cursor()

plt.xkcd()
fig = plt.figure(figsize=(30, 12))
gs = plt.GridSpec(2, 3)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[0:, 2])
ax4 = fig.add_subplot(gs[1, 0])
ax5 = fig.add_subplot(gs[1, 1])
#plt.show()


p_values =[]
values = []

i = 0
def animate(i):
	query = ('SELECT * FROM sept_values')
	data = pd.read_sql_query(query, connection)
	
	ax1.cla()
	ax1.set_title("The histogram of the means")
	ax1.hist(data.avg, bins = 10, rwidth = 0.95)
	#ani = FuncAnimation(plt.gcf(), animate, interval = 500)
	#plt.show()
	
	ax2.cla()	
	ax2.set_title("QQ plot")
	stats.probplot(data.avg,dist="norm",plot=ax2)


	ax3.set_title("The original distribution")
	for i in range (1,data.shape[1]-1):
		values.append(data.iloc[-1,i])
	sns.countplot(values,ax = ax3)

	ax4.cla()
	ax4.set_title("Shapiro-Wilk Test P-Values")
	ax4.axis("off")
	print(data)
	results = stats.shapiro(data.avg)[1]
	p_values.append(results)
	anno_opts = dict(xy=(0.5, 0.5), xycoords='axes fraction', va='center', ha='center',size=12)
	ax4.annotate(text = 'P-value: {values}'.format(values=round(results,3)),**anno_opts)

	ax5.set_title("Chart of p-values")
	ax5.plot(p_values)	

	
ani = FuncAnimation(plt.gcf(), animate, interval = 500)

plt.show()
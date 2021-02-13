import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Part1
mpg_df=sns.load_dataset('mpg')

sns.heatmap(mpg_df.corr(),cmap='coolwarm')
plt.show()
sns.pairplot(mpg_df)
plt.tight_layout()
plt.show()

#Part2
diamonds_df=sns.load_dataset('diamonds')
diamonds_df = diamonds_df[(~diamonds_df.color.isin(["D","E"])) & (diamonds_df.cut!="Fair")]
diamonds_df["color"] = diamonds_df["color"].cat.remove_unused_categories()
diamonds_df["cut"] = diamonds_df["cut"].cat.remove_unused_categories()

sns.set()
sns.set_style('darkgrid')
fg=sns.FacetGrid(diamonds_df,col='color',row='cut')
fg=fg.map(plt.scatter,'carat','price')
plt.show(fg)

#Part3
cc_df=sns.load_dataset('car_crashes')
sns.regplot(x='total',y='speeding',data=cc_df,fit_reg=True)
plt.show()
sns.regplot(x='total',y='alcohol',data=cc_df,fit_reg=True)
plt.show()

#Part 4
iris_df=sns.load_dataset('iris')
fig,ax=plt.subplots(2,2)
sns.boxplot(ax=ax[0,0],x='sepal_length',y='species',hue='species',data=iris_df)
sns.boxplot(ax=ax[0,1],x='sepal_width',y='species',hue='species',data=iris_df)
sns.boxplot(ax=ax[1,0],x='petal_length',y='species',hue='species',data=iris_df)
sns.boxplot(ax=ax[1,1],x='petal_width',y='species',hue='species',data=iris_df)
plt.show()

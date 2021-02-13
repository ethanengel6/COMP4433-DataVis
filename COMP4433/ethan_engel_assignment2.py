import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

#Part 1
elements=['Hydrogen','Helium','Lithium','Beryllium','Boron','Carbon']
atomic_mass=[1,4,7,9,11,12]
fig,ax=plt.subplots(1,2,figsize=(16,9),num=55)

ax[0].pie(atomic_mass,labels=elements,explode=(0,0,0,0,0,.2),autopct='%1.1f%%')
ax[0].set_title('Atomic Masses')
ax[0].axis('equal')

ax[1].pie(atomic_mass,labels=elements,explode=(.2,0,0,0,0,0),autopct=lambda q:'{:.0f}'.format(q*sum(atomic_mass)/100.0))
ax[1].set_title('Atomic Masses')
ax[1].axis('equal')

plt.show()

#Part 2
ide_df=pd.read_csv('py_ide2.csv')
fig,ax2=plt.subplots(1,2,figsize=(13,8),num=55)

ax2[0].barh(ide_df['IDE'],ide_df['Adoption'])
ax2[0].set_xlabel('Adoption')
ax2[0].set_ylabel('IDE')

ax2[1].bar(ide_df['IDE'],ide_df['Adoption'])
ax2[1].set_xlabel('IDE')
ax2[1].set_ylabel('Adoption')
plt.xticks(range(len(ide_df)),ide_df['IDE'],rotation=40)
plt.tight_layout()

plt.show()

#Part 3
dlist=['1980-01-15','1981-02-15','1982-03-15','1983-04-15','1984-05-15','1985-06-15','1986-07-15','1987-08-15']
rand_array=np.random.rand(8)*100+100
d4={'dates':dlist,'values':rand_array}
df4=pd.DataFrame(d4)
df4['dates']=pd.to_datetime(df4['dates'])
df4=df4.set_index('dates')

fig3=plt.figure(figsize=(16,9))
ax3=fig3.add_axes([.1,.1,.85,.35])
ax4=fig3.add_axes([.1,.5,.85,.4])
ax3.plot(df4['values'])
ax4.bar(dlist,df4['values'])

plt.show()

#Part4
df5=yf.download('MMM','2020-12-02','2021-01-01')
df6=df5[['Close','Volume']]
fig4=plt.figure(figsize=(16,9))
ax5=fig4.add_axes([.1,.07,.85,.35])
ax6=fig4.add_axes([.1,.55,.85,.35])
ax5.plot(df6['Close'])
ax6.plot(df6['Volume'])
ax5.set_title('3M Closing Values - December 2020')
ax6.set_title('3M Trading Volume - December 2020 (Millions of Shares)')

plt.show()

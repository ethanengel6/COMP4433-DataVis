import numpy as np
import pandas as pd

#part1
df = pd.read_csv('elements.csv')
df.loc[8]=["Flourine","F",9]
df.loc[9]=["Neon","Ne",10]
weights=[1,4,7,9,11,12,14,16,19,20]
df["Atomic Weights"]=weights
print(df)

#Part 2
greek_list=["psi","chi","delta","nu","kappa","sigma","beta","omega","iota"]
mu=10
sigma=1.5
arr1=sigma*np.random.randn(9)+mu
arr2=sigma*np.random.randn(9)+mu
angle_array=np.arange(0,9)*np.math.pi/4
cosines=np.cos(angle_array)
d1={"Greek Letters":greek_list,"Random Values 1":arr1, "Random Values 2":arr2, "Angles":angle_array,"Cosines":cosines}
df2=pd.DataFrame(d1)
print(df2)
df2.sort_values(by="Greek Letters",inplace=True)
df2.drop("Random Values 1",axis=1, inplace=True)
df2.drop("Random Values 2",axis=1, inplace=True)
df2.drop([4],axis=0,inplace=True)
print(df2)

#Part 3
fib1=1
fib2=1
fiblist=[1,1]
for fibs in range (10):
    newfib=fib1+fib2
    fiblist.append(newfib)
    fib1=fib2
    fib2=newfib
print (fiblist)
ratio_list=[]
for ratios in range(5):
    ratio = (fiblist[ratios+7])/(fiblist[ratios+6])
    ratio_list.append(ratio)
print(ratio_list)
#The ratios are honing in on the Golden Ratio, approximately 1.618033989.

#Part 4
def kelvin_to_rankine(kelvin_list):
    rankine_list=[]
    for k in range(len(kelvin_list)):
        rankine=(kelvin_list[k])*9/5
        rankine_list.append(rankine)
    return(rankine_list)
print (kelvin_to_rankine([10,20,100, 111111]))

kelvin_list2=[10,20,100, 111111]
rankine2_list=[]
for k2 in range(len(kelvin_list2)):
    rankine2 = lambda kel2: kel2*9/5
    rankine2_list.append(rankine2(kelvin_list2[k2]))
print (rankine2_list)

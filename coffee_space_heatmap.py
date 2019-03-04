
# coding: utf-8

# In[74]:

import csv
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[75]:

data = pd.read_csv("혜우_커피공간.csv")
data.head()
data=data.rename(columns={data.columns[0]:"브랜드"})
data


# In[76]:

data1= data.drop('공간',axis=1)
data2= data.drop('커피',axis=1)

df_pivot1 = pd.pivot_table(data1,index=data.columns[0])
df_pivot2 = pd.pivot_table(data2,index=data.columns[0])


df_pivot2
df_pivot


# In[ ]:




# In[94]:

import platform
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family = 'AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname = path).get_name()
    rc('font', family=font_name)
else:
    print ("Unknown System OS")


# In[78]:

# df_pivot1=df_pivot1.sort_values(by=['커피'],ascending=False)
heat_m=sns.heatmap(data=df_pivot1,fmt='f',annot=True)

heat_m
plt.show()


# In[ ]:




# In[79]:

# df_pivot2=df_pivot2.sort_values(by=['공간'],ascending=False)
heat_m=sns.heatmap(data=df_pivot2,fmt='f',annot=True)

heat_m
plt.show()


# In[109]:

data3={"커피브랜드":["던킨",
"탐앤탐스",
"스타벅스",
"할리스",
"투썸",
"커피빈",
"엔제리너스",
"이디야",
"빽다방"
],
"커피 출현비율":[-1.231059492,
-1.296425664,
0.086127697,
-0.318149959,
-0.419383773,
1.116799513,
-0.136566134,
1.745979257,
0.452678554
],
"공간 출현비율":[-1.35458496,
0.093851234,
0.708269543,
1.37889399,
0.571012412,
0.000882836,
0.817880503,
-0.719175318,
-1.497030241,
]}


# In[112]:

data3=pd.DataFrame(data3)
data3


# In[113]:

df_pivot3 = pd.pivot_table(data3,index=data3.columns[2])
df_pivot3


# In[119]:


df_pivot3=df_pivot3.sort_values(by=['커피 출현비율'],ascending=False)
heat_m=sns.heatmap(data=df_pivot3,fmt='f',annot=True,linewidths=5)

heat_m
plt.show()


# In[ ]:




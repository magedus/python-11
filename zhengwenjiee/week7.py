
# coding: utf-8

# 1 请将‘1，2，3，4’  变成 ['1', '2', '3', '4']

# In[26]:


st = '1,2,3,4'

st = st.split(',')
st


# 2 使用python copy 一个文件到另一个目录

# In[108]:


import shutil

#shutil.copy2('./week6.ipynb', '../null')  



# 3 解释下面代码

# 似乎是建了看不见的映射表， 把index 0 3 放在了一起， 把 index 1， 4 放在了一起。  
#
# In[150]:

li = [[],[]，1]
lili = li * 2  

lili[1].append(3)
lili[0].append(2)
lili

#[[2], [3], 1, [2], [3], 1]

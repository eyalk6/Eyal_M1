#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns;sns.set_style()
from sklearn.impute import SimpleImputer


# In[3]:


data = pd.read_excel("C:/Users/keren/Desktop/PY/FirstNames.xlsx", sheet_name=[0,1,2,3,4,5,6,7,8,9])


# In[4]:


for i in data:
    data[i] = data[i].iloc[11:,]
    data[i] = data[i].reset_index(drop = 'TRUE')
    data[i] = data[i].replace(".", "0").replace("..","2")
    data[i].columns = data[i].iloc[0]
    data[i] = data[i][1:]
    data[i].rename(columns={data[i].columns[1]: 'Total'}, inplace = True)
    data[i].rename(columns={data[i].columns[0]: 'Name'}, inplace = True)


# In[5]:


Jew_m = data[0]
Jew_w = data[1]
Mus_m = data[2]
Mus_w = data[3]
Chri_m = data[4]
Chri_w = data[5]
Droz_m = data[6]
Droz_w = data[7]
Other_m = data[8]
Other_w = data[9]


# In[6]:


# Cheking if there are null values in any df (xls sheets)
Jew_m.isnull().values.any()
Jew_w.isnull().values.any()
Chri_m.isnull().values.any()
Chri_w.isnull().values.any()
Mus_m.isnull().values.any()
Mus_w.isnull().values.any()
Droz_m.isnull().values.any()
Droz_w.isnull().values.any()
Other_m.isnull().values.any()
Other_w.isnull().values.any()


# In[7]:


#1 Top 10 male jewish names over the years.
top_10_Jm_for_plot = Jew_m.sort_values(by='Total',ascending=False)
top_10_Jm_for_plot.set_index("Name",inplace=True)
top_10_Jm0 = top_10_Jm_for_plot.iloc[0:10,1:]
top_10_Jm0 = top_10_Jm0.apply(pd.to_numeric)
top_10_Jm0 = top_10_Jm0.T
top_10_Jm0.plot.line()
plt.xlabel('Year') 
plt.title("Top 10 men names over the years")


# In[8]:


#2 A comparison of how top common name changes among Muslims between the establishment of the State of Israel and today
Mus_females_1948 = Mus_w.groupby(['Name']).sum()[1948]
Mus_females_1948 = Mus_females_1948.apply(pd.to_numeric)
Mus_females_1948 = Mus_females_1948.sort_values(ascending=False).head(10).reset_index()
plt.figure(figsize=(7,3.5))
sns.scatterplot(x='Name',y=1948,data=Mus_females_1948,s=100).set(title='Top 10 Common Female First Names in 1948')

Mus_females_2021 = Mus_w.groupby(['Name']).sum()[2021]
Mus_females_2021 = Mus_females_2021.apply(pd.to_numeric)
Mus_females_2021 = Mus_females_2021.sort_values(ascending=False).head(10).reset_index()
plt.figure(figsize=(7,3.5))
sns.scatterplot(x='Name',y=2021,data=Mus_females_2021,s=100).set(title='Top 10 Common Female First Names in 2021')


# In[9]:


#3 Top 10 male Droz names in total.
top_10_Droz_m = Droz_m.sort_values(by='Total',ascending=False) 
top_10_Droz_m = top_10_Droz_m.iloc[0:10,0:2]
sns.barplot(data=top_10_Droz_m,x="Name", y = 'Total')


# In[129]:


#4 The percentage of Jewish women's names ending in the letter "ה"

plt.figure(1,figsize = (5,5))
Jew_w["Name"].str.endswith("ה").value_counts().plot.pie(autopct = "%1.1f%%")
plt.show()


# In[ ]:


#5 Unique male names in each sector
Jewish_males_unique = Jew_m['Name'].count()
Muslim_males_unique = Mus_m['Name'].count()
Druze_males_unique = Droz_m['Name'].count()
Christian_males_unique = Chri_m['Name'].count()
Other_males_unique = Other_m['Name'].count()
Unique_Names = pd.DataFrame({'Jewish_males': [Jewish_males_unique],
                             'Muslim_males':[Muslim_males_unique],
                             'Druze_males': [Druze_males_unique],
                             'Christian_males':[Christian_males_unique],
                             'Other_males':[Other_males_unique],
                            }).transpose().reset_index()
Unique_Names = Unique_Names.rename(columns={'index': 'Category',0:'Count'}).sort_values('Count',ascending=False)
Unique_Names

plt.figure(figsize=(8,6))
sns.barplot(x='Category',y='Count',data=Unique_Names).set(title='Unique Names On Each Male Sector')


# In[ ]:


#6 Unisex names in the jewish sector over the years.

Unisex_names = Jew_w.loc[Jew_w['Name'].isin(Jew_m['Name'])]
Unisex_names_top_w = Unisex_names.sort_values(by='Total',ascending=False) 
Unisex_names_top_w.set_index("Name",inplace=True)
Unisex_names_top_w = Unisex_names_top_w.iloc[0:10,10:]
Unisex_names_top_w = Unisex_names_top_w.apply(pd.to_numeric)
Unisex_names_top_wT = Unisex_names_top_w.T 
Unisex_names_top_wT.plot.line()
plt.xlabel('Year') 
plt.title("Names in each year")


# In[ ]:


#7 Names statrs with vowels letters

Alef = Jew_m[Jew_m['Name'].str.startswith('א')]
e = Alef.iloc[:,:2]
He = Jew_m[Jew_m['Name'].str.startswith('ה')]
h = He.iloc[:,:2]
Vav = Jew_m[Jew_m['Name'].str.startswith('ו')]
v = Vav.iloc[:,:2]
Yod = Jew_m[Jew_m['Name'].str.startswith('י')]
i = Yod.iloc[:,:2]
a = e.sum()['Total']
b = h.sum()['Total']
c = v.sum()['Total']
d = i.sum()['Total']
Letter_list = [a,b,c,d]


# In[ ]:


fig, ax = plt.subplots()

let = ['א', 'ה', 'ו', 'י']
counts = Letter_list
bar_labels = ['א', 'ה', 'ו', 'י']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

ax.bar(let, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('count')
ax.set_title('אותיות אהוי')
ax.legend(title='letters')

plt.show()


# In[ ]:


# 8 A comparison between unisex names in 1948 and 2019 (Jewish sector)

Jew_m_1948_both = Jew_m.loc[Jew_m[1948] != 0]
Jew_w_1948_both = Jew_w.loc[Jew_w[1948] != 0]
Jew_m_1948_both[1948] = Jew_m_1948_both[1948].apply(pd.to_numeric)
Jew_m_1948_both_len = Jew_m_1948_both[1948].sum()

Jew_m_1948 = Jew_m_1948_both.loc[Jew_m_1948_both['Name'].isin(Jew_w_1948_both['Name']),:]
Jew_m_2019[1948] = Jew_m_2019[1948].apply(pd.to_numeric)
Jew_m_1948_len = Jew_m_1948[1948].sum()
Jew_m_1948_len


# In[ ]:


pai_graph_1948 = np.array([Jew_m_1948_both_len-Jew_m_1948_len,Jew_m_1948_len])
mylabels = ["All names", "Both for man and woman"]
myexplode = [0.2, 0]

plt.pie(pai_graph_1948, labels = mylabels, explode = myexplode, shadow = True,autopct='%1.2f%%')
plt.show() 


# In[ ]:


Jew_m_2019_both = Jew_m.loc[Jew_m[2019] != 0]
Jew_w_2019_both = Jew_w.loc[Jew_w[2019] != 0]
Jew_m_2019_both[2019] = Jew_m_2019_both[2019].apply(pd.to_numeric)
Jew_m_2019_both_len = Jew_m_2019_both[2019].sum()

Jew_m_2019 = Jew_m_2019_both.loc[Jew_m_2019_both['Name'].isin(Jew_w_2019_both['Name']),:]
Jew_m_2019[2019] = Jew_m_2019[2019].apply(pd.to_numeric)
Jew_m_2019_len = Jew_m_2019[2019].sum()
Jew_m_2019_len


# In[ ]:


pai_graph_2019 = np.array([Jew_m_2019_both_len-Jew_m_2019_len,Jew_m_2019_len])
mylabels = ["All names", "Both for man and woman"]
myexplode = [0.2, 0]

plt.pie(pai_graph_2019, labels = mylabels, explode = myexplode, shadow = True,autopct='%1.2f%%')
plt.show() 


# In[12]:


#9 Names that were unique to a specific gender at the founding of the state and now belong to both sexes.

Jew_m_above = Jew_m[Jew_m['Total']>500]
Jw_s1 = Jew_w.iloc[:,:36]
Jw_s1.drop('Total', inplace=True, axis=1)
Jw_s1_name = Jw_s1['Name'] 
Jw_s1 = Jw_s1.iloc[:,2:36].apply(pd.to_numeric)
Jw_s1['totu80'] = Jw_s1.iloc[:,2:36].apply(np.sum, axis=1)
Jw_s1['Name'] = Jw_s1_name
Jw_s1 = Jw_s1[((Jw_s1['totu80'])<5)]
Jw_above = Jew_w[Jew_w['Total']>500]


# In[14]:


list1 = []
for i in Jw_s1['Name']:
    for j in Jw_above['Name']:
        if i == j:
            list1.append(i)            
list2 = []
for i in list1:
    for j in Jew_m_above['Name']:
        if i == j:
            list2.append(j)
unisex_u = Jew_w.loc[Jew_w['Name'].isin(list2)]
unisex_u.set_index('Name', inplace=True)
ab  = unisex_u.iloc[:,1:]
ab = ab.apply(pd.to_numeric)
ab = ab.T
ab.plot.line()
plt.xlabel('Year') 
plt.title("Names")  


# In[21]:


#10 Exploring my name accross the years.
Eyal=Jew_m[Jew_m["Name"] == "אייל"]
Eyal=Eyal.iloc[:,2:]
fig=plt.subplots(figsize=(33,17))
sns.barplot(data=Eyal,orient="v")


# In[39]:


#11 Comparison of the ratio of the 10 most common names in relation to the total amount of Muslim male names. (1948 and 2020)

top_10_mm_for_plot = Mus_m.sort_values(by='Total',ascending=False) 
top_10_mm_for_plot.set_index("Name",inplace=True)
top_10_mm0 = top_10_mm_for_plot.iloc[1:11,1:]
top_10_mm0 = top_10_mm0.apply(pd.to_numeric)
top_10_mm0 = top_10_mm0.T 
top_10_mm0.plot.line()
plt.xlabel('Year') 
plt.title("Names")


# In[40]:



sum_mm_2020 = Mus_m.sort_values(by='Total',ascending=False) 
sum_mm_2020.set_index("Name",inplace=True)
sum_mm_2020 = sum_mm_2020.iloc[:,1:]
sum_mm_2020 = sum_mm_2020.T
sum_mm_2020 = sum_mm_2020.iloc[73,:]
sum_mm_2020_q = 0
for i in sum_mm_2020:
    sum_mm_2020_q = sum_mm_2020_q + int(i)


# In[41]:


sum_top_10_mm_1948 = top_10_mm0.iloc[0,2:10].sum()


# In[42]:


sum_mm_1948 = Mus_m.sort_values(by='Total',ascending=False) 
sum_mm_1948.set_index("Name",inplace=True)
sum_mm_1948 = sum_mm_1948.iloc[:,1:]
sum_mm_1948 = sum_mm_1948.T
sum_mm_1948 = sum_mm_1948.iloc[0,:]
sum_mm_1948_q = 0
for i in sum_mm_1948:
    sum_mm_1948_q = sum_mm_1948_q + int(i)
sum_mm_1948_q


# In[44]:



sum_top_10_mm_2020 = Mus_m.sort_values(by='Total',ascending=False) 
sum_top_10_mm_2020.set_index("Name",inplace=True)
sum_top_10_mm_2020.apply(pd.to_numeric)
sum_top_10_mm_2020 = sum_top_10_mm_2020.T
sum_top_10_mm_2020 = sum_top_10_mm_2020.iloc[74,0:9].sum()


# In[45]:


number = [int(sum_top_10_mm_1948),int(sum_top_10_mm_2020),int(sum_mm_1948_q),int(sum_mm_2020_q)]
years = [1948,2020]
oriya_two = pd.DataFrame({'top10': number[0:2], 'total name': number[2:4]}, index = years)


oriya_two.plot.bar(rot=0)
plt.title("Muslim name top10 and total names")


# In[95]:


#12 Names over 4 letters in diffrent sectors.

Chri_woman_len = Chri_w.Name.reset_index()
Chri_woman_len = Chri_woman_len.drop("index",axis = 1)
Chri_woman_len["Name_Length"] = Chri_woman_len.Name.apply(len)
Chri_woman_len


# In[92]:


Chri_woman_len_over_4 = Chri_woman_len[Chri_woman_len["Name_Length"] > 4].count().reset_index()
Chri_woman_len_over_4 = Chri_woman_len_over_4.rename(columns={'index': 'column',0:'Count'})
Chri_woman_len_over_4


# In[96]:


Druz_woman_len = Droz_w.Name.reset_index()
Druz_woman_len = Druz_woman_len.drop("index",axis = 1)
Druz_woman_len["Name_Length"] = Droz_w.Name.apply(len)
Druz_woman_len


# In[98]:


Druz_woman_len_over_4 = Druz_woman_len[Druz_woman_len["Name_Length"] > 4].count().reset_index()
Druz_woman_len_over_4 = Druz_woman_len_over_4.rename(columns={'index': 'column',0:'Count'})
Druz_woman_len_over_4


# In[111]:


Chri_woman_len_over_4['Druz'] = Druz_woman_len_over_4.Count
Woman_len_over_4 = Chri_woman_len_over_4
Woman_len_over_4 = Woman_len_over_4.rename(columns={'column': 'column','Count':'Druz','Count':'Chri'})
Woman_len_over_4 = Woman_len_over_4.drop(0,axis = 0)
Woman_len_over_4 = Woman_len_over_4.transpose().reset_index().drop(0,axis = 0).rename(columns={'index': 'sector',1:'Count'})
Woman_len_over_4


# In[112]:


plt.figure(figsize=(8,6))
sns.barplot(x='sector',y='Count',data=Woman_len_over_4).set(title='Names Over 4 Letters')


# In[120]:


#13 Names found in both the Muslim and Jewish male sectors
e = []
total=0
for i in Jew_m['Name']:
    for j in Mus_m['Name']:
        if i == j:
            e.append(i)
            total=total+1   

print(e)
print(total)


# In[121]:


ju_names = Jew_m.loc[Jew_m['Name'].isin(e)]
mu_names = Mus_m.loc[Mus_m['Name'].isin(e)]
ju_names.set_index('Name', inplace=True)
mu_names.set_index('Name', inplace=True)
ju = ju_names.iloc[:,:1]
mu= mu_names.iloc[:,:1]
plt.figure(figsize=(20, 7))
plt.plot(ju,'g*', mu, 'ro')
plt.show()


# In[127]:


#14 The three most common names for jewish men are biblical names.

JEWֹֹֹ_M_top_3 = Jew_m.sort_values('Total', ascending=False)
JEWֹֹֹ_M_top_3=JEWֹֹֹ_M_top_3.head(3).iloc[:,:]
JEWֹֹֹ_M_top_3


# In[128]:


JEWֹֹֹ_M_top_3.set_index('Name',inplace=True)
JEWֹֹֹ_M_top_3 = JEWֹֹֹ_M_top_3.iloc[:,1:]

JEWֹֹֹ_M_top_3.T.plot.line()


# In[134]:


#15 Top 5 male names from the Other sectors over the years.
top_5_for_plot = Other_m.sort_values(by='Total',ascending=False)
top_5_for_plot.set_index("Name",inplace=True)
top_5 = top_5_for_plot.iloc[0:5,1:]
top_5 = top_5.apply(pd.to_numeric)
top_5 = top_5.T
top_5.plot.line()
plt.xlabel('Year') 
plt.title("Top 5 men names over the years")


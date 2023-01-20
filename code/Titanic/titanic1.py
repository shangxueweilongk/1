import warnings
warnings.filterwarnings('ignore')

#导入处理数据包
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#导入数据
#训练数据集
train = pd.read_excel(r"D:\pythonProject1\Titanic\data.xlsx")
#查看训练数据集
print(train)

#获取数据类型列的描述统计信息
print(train.describe())

#查看每一列的数据类型，和数据总数
print(train.info())

#泰坦尼克号乘客生还几率
n = train['Survived'].value_counts()

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#总体生还几率:
plt.figure(figsize=(6,6))
plt.pie(n,autopct='%.2f%%',labels=['死亡','存活'],pctdistance=0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1],textprops=dict(size=15))
plt.title('总体生还率')
plt.show()
"""
统计的数据中，将近62%的乘客都未能幸免，泰坦尼克号沉船事故可以说是和平时期死伤人数最惨重的海难之一。
"""


#不同性别乘客生还几率
sex_count = train.groupby(by='Sex')['Survived'].value_counts()
plt.figure(figsize=(2*5,5))

axes1=plt.subplot(1,2,1)
axes1.pie(sex_count.loc['female'][::-1],autopct='%.2f%%',labels=['死亡','存活'],pctdistance=0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1],textprops=dict(size=15),colors=['#9400D3','#FFB6C1'],startangle=90)
axes1.set_title('女性生还率')

axes2=plt.subplot(1,2,2)
axes2.pie(sex_count.loc['male'],autopct='%.2f%%',labels=['死亡','存活'],pctdistance=0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1],textprops=dict(size=15),colors=['#2E8B57','#AFEEEE'])
axes2.set_title('男性生还率')
plt.show()
"""
统计的数据中，女性将近3/4都存活了下来，而男性只有不到19%生还。可能确实如电影中所演的那样，绝大部分的救生筏都让给了女性。
"""


#不同年龄段乘客生还几率
age_range = train['Age']
age_num,_ = np.histogram(age_range,range=[0,80],bins=16 )

# 各年龄阶段生还人数
age_survived = []
for age in range(5,81,5):
    survived_num = train.loc[(age_range>=age-5) & (age_range<=age)]['Survived'].sum()
    age_survived.append(survived_num)

# 绘制条形图
plt.figure(figsize=(12,6))
plt.bar(np.arange(2,78,5)+0.5,age_num,width=5,label='总人数',alpha=0.8)
plt.bar(np.arange(2,78,5)+0.5,age_survived,width=5,label='生还人数')
plt.xticks(range(0,81,5))
plt.yticks(range(0,121,10))
plt.xlabel('年龄',position=(0.95,0),fontsize=15)
plt.ylabel('人数',position=(0,0.95),fontsize=15)
plt.title('各年龄阶段人数和生还人数条形图')
plt.grid(True,linestyle=':',alpha=0.6)
plt.show()
"""
从各年龄阶段生还人数条形图可以看出，在0-15岁年龄段的绝大部分孩子都得以生还，而在15-80岁的年龄段都有近一半或超过一半的人不幸身亡。
"""


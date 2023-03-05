#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df=pd.read_csv("C:\\Users\\Dr. Swetha Meruva\\Desktop\\Fall 2022\\HAP 780\\Proj_780\\diabet_780.csv")


# In[3]:


df.head()


# In[4]:



# Check dataset dimensions
print(df.shape)

# Check columns
print(df.columns)


# In[5]:


# Add columns to map IDs
#Load csv files from github 
ad_type = pd.read_csv("C:\\Users\\Dr. Swetha Meruva\\Desktop\\Fall 2022\\HAP 780\\Proj_780\\adm_type.csv")
ad_source = pd.read_csv("C:\\Users\\Dr. Swetha Meruva\\Desktop\\Fall 2022\\HAP 780\\Proj_780\\adm_source.csv")
discharge = pd.read_csv("C:\\Users\\Dr. Swetha Meruva\\Desktop\\Fall 2022\\HAP 780\\Proj_780\\adm_discharge.csv")


# In[6]:


df['admission_type'] = df['admission_type_id'].map(ad_type['description'])
df['admission_source'] = df['admission_source_id'].map(ad_source['description'])
df['discharge_disp'] = df['discharge_disposition_id'].map(discharge['description'])


# In[7]:


# Check data types of columns
df.info()


# In[8]:


# Drop duplicate patient_nbr
unique_patients = df.drop_duplicates(subset=['patient_nbr'], keep='first')
unique_patients.shape


# In[9]:


# Drop encounters that resulted in discharge due to hospice or patient death
hospice_death = [11, 19, 20, 13, 14]
df = unique_patients[~unique_patients['discharge_disposition_id'].isin(hospice_death)]
df.shape


# In[10]:


df.drop(columns=['admission_type_id', 'admission_source_id', 'discharge_disposition_id'], inplace=True)


# In[11]:


# Check for any null values
# Null values are represented by ? so replace ? with NaN
df = df.replace('?', np.nan)
df.isnull().sum()
# Here we can see some very problematic columns that have too much missing information


# In[12]:


# Drop columns that are missing too much data
df = df.drop(['weight', 'payer_code', 'medical_specialty'], axis=1)

# Remove null values
df = df.dropna()
df.isnull().sum()


# In[13]:


print(df.shape)
print('% data retained out of unique patients: ' + str(round(len(df.index)/71518 * 100,2)) + '%')
print('% data retained out of all encounters: ' + str(round(len(df.index)/101766 * 100,2)) + '%')
print(df.columns)


# In[14]:


# Drop other columns without relevant information
df = df.drop(['encounter_id', 'patient_nbr'], axis=1)
df.columns


# In[15]:


# Replace diagnoses with category names
#Circulatory: 390-459, 785
#Respiratory: 460-519, 786
#Digestive: 520-579, 787
#Diabetes: 250.xx
#Injury: 800-999
#Musculoskeletal: 710-739
#Genitourinary: 580-629, 788
#Neoplasms: 140-239, 
#Other: 
#780, 781, 784, 790-799, 240-279 except 250, 680-709, 782, 001-139, 290-319
#E-V (beginning with a letter), 280-289, 320-359, 630-679, 360-389, 740-759

def categorize_diagnosis(diag):
    if diag.isnumeric():
        diag = int(diag)
        if diag in range(390,460) or diag==785:
            return 'Circulatory'
        elif diag in range(460,520) or diag==786:
            return 'Respiratory'
        elif diag in range(520,580) or diag==787:
            return 'Digestive'
        elif diag in np.arange(250,260,0.01):
            return 'Diabetes'
        elif diag in range(800,1000):
            return 'Injury'
        elif diag in range(710,740):
            return  'Musculoskeletal'
        elif diag in range(580,630) or diag==788:
            return  'Genitourinary'
        elif diag in range(140,240):
            return  'Neoplasms'
        else:
            return 'Other'
    else:
        if "250" in diag:
            return 'Diabetes'
        else:
            return  'Other'
        


# In[16]:


df['diag_1_desc'] = df.apply(lambda row: categorize_diagnosis(row['diag_1']), axis=1)
df['diag_2_desc'] = df.apply(lambda row: categorize_diagnosis(row['diag_2']), axis=1)
df['diag_3_desc'] = df.apply(lambda row: categorize_diagnosis(row['diag_3']), axis=1)



# In[17]:


# Remove original diagnosis features
df.drop(columns=['diag_1', 'diag_2', 'diag_3'], inplace=True)
df.columns


# In[18]:


# corr matrix
corrMatrix = df.corr()
sns.heatmap(corrMatrix, annot=True)
plt.show()


# In[19]:


df.describe()


# In[20]:


df.to_csv(r'C:\Users\Dr. Swetha Meruva\Desktop\Fall 2022\HAP 780\finalfile.csv')


# In[23]:


main1=pd.read_csv(r"C:\Users\Dr. Swetha Meruva\Downloads\project_diabetes.csv")
main1 = main1.drop(['column1'], axis=1)
main1


# In[ ]:





# In[25]:


dia=pd.read_csv(r"C:\Users\Dr. Swetha Meruva\Desktop\Fall 2022\HAP 780\Proj_780\tablenew.csv")
dia = dia.drop(['column1'], axis=1)
dia


# In[26]:


# Diabetic patient count by age and gender
age_gender = dia.groupby(['age','gender']).count()
age_gender.iloc[:,0]


# In[27]:


# List categorical and numeric features
categorical_feat = []
numerical_feat = []

for col in dia.columns:
    if dia[col].dtype == 'object':
        categorical_feat.append(col)
    elif 'id' in col:
        categorical_feat.append(col)
    elif dia[col].dtype == 'int64':
        numerical_feat.append(col)


# In[28]:


for i in categorical_feat:
    plt.rcParams.update({'figure.max_open_warning': 0})
    plt.figure(i)
    plt.title(i)
    dia[i].value_counts().plot(kind='bar')


# In[30]:


plt.figure()
plt.title('Patients readmission')
dia['readmitted'].value_counts().plot(kind='bar',color=['#6EAE8B','#BDBDBD','#CD0000'])


# In[29]:


# % of categ features
for i in categorical_feat:
    a = dia.groupby([i]).size().reset_index(name='counts')
    a['pcts'] = round((a['counts']/a['counts'].sum() * 100),2)
    print(a)


# In[31]:



dia.groupby(['race','readmitted']).size().reset_index(name='counts')


# In[32]:


dia.groupby(['age','readmitted']).size().reset_index(name='counts')


# In[33]:


dia.groupby(['race','readmitted']).size().reset_index(name='counts')


# In[34]:


dia.groupby(['admission_type','readmitted']).size().reset_index(name='counts')


# In[35]:


dia.groupby(['time_in_hospital','readmitted']).size().reset_index(name='counts')


# In[36]:


# Reset index
dia.reset_index(inplace=True)
dia.drop(columns='index')


# In[37]:


#1. One-hot encode categorical features
dia_categ = dia[categorical_feat]
dia_categ = dia_categ.drop(columns='readmitted')
dia_categ.head()


# In[39]:


dia_numer = dia[numerical_feat]
dia_numer.head()


# In[40]:


from sklearn.preprocessing import RobustScaler

#Scale numerical features
dia_numer_scaled = pd.DataFrame(RobustScaler().fit_transform(dia_numer[numerical_feat]), columns=numerical_feat)
dia_numer_scaled


# In[50]:


pd.crosstab(main1['gender'],df['readmitted']).plot(kind="bar",stacked=True)


# In[52]:


pd.crosstab(df['race'],main1['readmitted']).plot(kind="bar",stacked=True)


# In[54]:


pd.crosstab(df['age'],main1['readmitted']).plot(kind="bar",stacked=True)


# In[56]:


pd.crosstab(df['insulin'],main1['readmitted']).plot(kind="bar",stacked=True)


# In[57]:


pd.crosstab(df['admission_type'],main1['readmitted']).plot(kind="bar",stacked=True)


# In[58]:


pd.crosstab(df['A1Cresult'],main1['readmitted']).plot(kind="bar",stacked=True)


# In[59]:


pd.crosstab(df['time_in_hospital'],main1['readmitted']).plot(kind="bar",stacked=True)


# In[ ]:





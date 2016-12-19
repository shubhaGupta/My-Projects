
# coding: utf-8

# In[34]:

import csv
f= open("guns.csv","r")
data = list(csv.reader(f))
print(data[0:5])


# In[35]:

headers= data[0]
data= data[1:len(data)]
print(headers)
print(data[0:5])


# In[36]:

year_count={}
year=[]
for i in data:
    year.append(i[1])
    #print(year)
for row in year:
    if row in year_count:
        year_count[row] = year_count[row]+1
    else:
        year_count[row] = 1
print(year_count)


# In[29]:

import datetime
date_counts={}
dates= [datetime.datetime(year=int(i[1]),month=int(i[2]),day=1) for i in data]
print(dates[0:5])
for row in dates:
    if row in date_counts:
        date_counts[row] = date_counts[row] +1
    else:
        date_counts[row]=1
print(date_counts)
    
    


# In[37]:

sex_counts={}
race_counts={}
for row in data:
    if row[5] in sex_counts:
        sex_counts[row[5]]=  sex_counts[row[5]] +1
    else:
         sex_counts[row[5]]=1
    if row[7] in race_counts:
        race_counts[row[7]] =  race_counts[row[7]] +1
    else:
         race_counts[row[7]]=1
print(sex_counts)
race_counts


# I have noticed that there are more number of males than females that died because of gun shooting and their ration is approx 6:1
# and the ratio of deaths of white people to that of black people is approx 3:1. Other races like Asian,Hispanic, native american reported to be killed less as compared to whites and black. Now we should further examine about the ages so that we can get to know in which age group people are dying most and we can examine area and education also.

# In[39]:

import csv
f= open("census.csv","r")
census= list(csv.reader(f))
census


# In[46]:

mapping={}
mapping["Asian/Pacific Islander"]= census[1][14]+census[1][15]
mapping["Black"]= census[1][12]
mapping["Hispanic"]= census[1][11]
mapping["Native American/Native Alaskan"]= census[1][13]
mapping["White"]= census[1][10]
race_per_hundredk ={}
for key in race_counts:
    race_per_hundredk[key]=race_counts[key] / int(mapping[key])
    race_per_hundredk[key]*=100000
print(race_per_hundredk)


# In[48]:

intents = [i[3] for i in data]
races = [i[7] for i in data]
homicide_race_per_hundredk = {}
for i, race in enumerate(races):
    if intents[i] == "Homicide":
        if race in homicide_race_per_hundredk:
            homicide_race_per_hundredk[race]+=1
        else:
            homicide_race_per_hundredk[race]=1
for key in homicide_race_per_hundredk:
    homicide_race_per_hundredk[key]= int(homicide_race_per_hundredk[key]) / int(mapping[key])
    homicide_race_per_hundredk[key]*=100000
print(homicide_race_per_hundredk)


# We can see that data per 100000 for all intent and homicide are different and in homicide maximum people are black and then hispanic. I want to analyze the age column also to get an idea about how many deaths are there in particular age group. 

# In[49]:

intents = [i[3] for i in data]
races = [i[7] for i in data]
accidental_race_per_hundredk = {}
for i, race in enumerate(races):
    if intents[i] == "Accidental":
        if race in accidental_race_per_hundredk:
            accidental_race_per_hundredk[race]+=1
        else:
            accidental_race_per_hundredk[race]=1
for key in homicide_race_per_hundredk:
    accidental_race_per_hundredk[key]= int(accidental_race_per_hundredk[key]) / int(mapping[key])
    accidental_race_per_hundredk[key]*=100000
print(accidental_race_per_hundredk)


# In[ ]:




# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 17:39:04 2018

@author: Andrew
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#from matplotlib.pyplot import hist

def num_stats(feature):
    stats = feature.describe()
    stats_table = pd.DataFrame(stats, columns = [feature.name])
    stats_table.index.name = 'Stats'
    print(display(stats_table))
    
def cat_feat(feature):
    print("")
    print(feature.count())
    print(feature.value_counts())
    
train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')
combine = pd.concat([train_df, test_df], sort=False)

num_stats(combine.Age)
num_stats(combine.Fare)
num_stats(combine.SibSp)
num_stats(combine.Parch)

cat_feat(combine.Sex)
cat_feat(combine.Survived)
cat_feat(combine.Pclass)
cat_feat(combine.Embarked)

print("")
#pclass_plot = sns.barplot(x='Pclass', y='Survived', data=combine)
#pclass_plot.figure.savefig("pclass_survived.png")
#sex_plot = sns.barplot(x='Sex', y='Survived', data=combine)
#sex_plot.figure.savefig("sex_survived.png")

print("")
survived_only = combine[(combine.Survived == 1)]
died_only = combine[(combine.Survived == 0)]
#died_histo = died_only.hist(column='Age', bins=25, grid=False)
#survived_histo = survived_only.hist(column='Age', bins=25, grid=False)
age1525died = died_only[(died_only.Age <= 25) & (died_only.Age >= 15)]
age1525surv = survived_only[(survived_only.Age <= 25) & (survived_only.Age >= 15)]

pclass1sur0 = died_only[(died_only.Pclass == 1)]
pclass2sur0 = died_only[(died_only.Pclass == 2)]
pclass3sur0 = died_only[(died_only.Pclass == 3)]
#died_class1 = pclass1sur0.hist(column='Age', bins=25, grid=False)
#died_class2 = pclass2sur0.hist(column='Age', bins=25, grid=False)
#died_class3 = pclass3sur0.hist(column='Age', bins=25, grid=False)

pclass1sur1 = survived_only[(survived_only.Pclass == 1)]
pclass2sur1 = survived_only[(survived_only.Pclass == 2)]
pclass3sur1 = survived_only[(survived_only.Pclass == 3)]
#surv_class1 = pclass1sur1.hist(column='Age', bins=25, grid=False)
#surv_class2 = pclass2sur1.hist(column='Age', bins=25, grid=False)
#surv_class3 = pclass3sur1.hist(column='Age', bins=25, grid=False)

#embarkedSsurvived0 = combine[(combine.Embarked == 'S')&(combine.Survived == 0)]
#test_plot1 = sns.barplot(x='Sex', y='Fare', data=embarkedSsurvived0, ci=None)
#test_plot1.set_title('Embarked = S | Survived = 0')
#test_plot1.set(ylim=(0, 80))

#embarkedCsurvived0 = combine[(combine.Embarked == 'C')&(combine.Survived == 0)]
#test_plot2 = sns.barplot(x='Sex', y='Fare', data=embarkedCsurvived0, ci=None)
#test_plot2.set_title('Embarked = C | Survived = 0')
#test_plot2.set(ylim=(0, 80))

#embarkedQsurvived0 = combine[(combine.Embarked == 'Q')&(combine.Survived == 0)]
#test_plot3 = sns.barplot(x='Sex', y='Fare', data=embarkedQsurvived0, ci=None)
#test_plot3.set_title('Embarked = Q | Survived = 0')
#test_plot3.set(ylim=(0, 80))

#embarkedSsurvived1 = combine[(combine.Embarked == 'S')&(combine.Survived == 1)]
#test_plot4 = sns.barplot(x='Sex', y='Fare', data=embarkedSsurvived1, ci=None)
#test_plot4.set_title('Embarked = S | Survived = 1')
#test_plot4.set(ylim=(0, 80))

#embarkedCsurvived1 = combine[(combine.Embarked == 'C')&(combine.Survived == 1)]
#test_plot5 = sns.barplot(x='Sex', y='Fare', data=embarkedCsurvived1, ci=None)
#test_plot5.set_title('Embarked = C | Survived = 1')
#test_plot5.set(ylim=(0, 80))

#embarkedQsurvived1 = combine[(combine.Embarked == 'Q')&(combine.Survived == 1)]
#test_plot6 = sns.barplot(x='Sex', y='Fare', data=embarkedQsurvived1, ci=None)
#test_plot6.set_title('Embarked = Q | Survived = 1')
#test_plot6.set(ylim=(0, 80))

ticketDup = combine.Ticket.duplicated()
trues = ticketDup[ticketDup == True]
dupRate = trues.count()/ticketDup.count()
print("Ticket duplicate rate: ")
print(dupRate)

#corrTic = combine['Ticket'].corr(combine['Survived'])

print("")
cabinNull = combine.Cabin.isnull().sum()
print("Cabin NULL Count:", cabinNull)
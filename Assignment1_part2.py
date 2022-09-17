import pandas as pd
import numpy as np

#question 1
directory = r'C:\Users\admin\Desktop\IMDB_movie_reviews_details.csv'

df = pd.read_csv(directory)
print(df)

#question 2
#dropping the Unnamed: 0 as the unnecessary column
df.drop(columns='Unnamed: 0',inplace=True)
print(df)

#question 3

#finding null values
df.isna().sum()

#dealing with the null values by droping them
new_data = df.dropna()

print(new_data)

#question 4

def mean():
    return np.mean(new_data['rating'])
print("the mean is",mean())

def standard_deviation():
    return np.std(new_data['rating'])
print("the standard deviation is", standard_deviation())

def minimum():
    return new_data['rating'].min()

print("the min is ",minimum())

def q1():
    return np.quantile(new_data['rating'],.50)
print("value of q1 is", q1())

def median():
    return np.median(new_data['rating'])
print("the median is",median())

def q3():
    return np.quantile(new_data['rating'],.75)
print("value of q3 is", q3())

def maximum():
    return (new_data['rating'].max())
print("the max is ",maximum())


#question 5
high_rating = (new_data['rating']) > 8.5 
high_metascore = (new_data['metascore']) > 85.0
print(new_data.loc[high_rating,['name']])
print(new_data.loc[high_metascore,'name'])


#the dark night

#question 6
#total number of years produced per year


production_count = df[['year','name']].groupby('year').count()
#printing the production number of movies from the 10th index to the 90th
print(production_count[10:90])


#mean ratings for each year


mean_production_count = df[['year','rating']].groupby('year').mean()

print(mean_production_count[10:90])


#question 7

#years where mean ratings are more than 7.5
higher_year_mean_ratings = mean_production_count['rating'] > 7.5
print(mean_production_count[higher_year_mean_ratings])

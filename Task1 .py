#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[2]:


df = pd.read_csv("E:/DATA ANALYSIS TASK LIST AND DATASET-20240120T092540Z-001/DATA ANALYSIS TASK LIST AND DATASET/Dataset .csv",encoding='utf8')
df


# In[3]:


print(df.isnull())   #to show that data is not null


# # LEVEL1_TASK1
# 

# Determine the top three most common cuisines in the dataset.

# In[4]:


cuisine_series = df['Cuisines'].str.split(',').explode()
# Count 
cuisine_counts = cuisine_series.value_counts()

#top three most common cuisines
top_three_cuisines = cuisine_counts.head(3)

print(top_three_cuisines)


# Calculate the percentage of restaurants that serve each of the top cuisines.

# In[5]:


#Calculate the total number of restaurants
total_restaurants = len(df)
print("total_restaurants=",total_restaurants)

# Calculate the percentage for each cuisine
top_cuisine_percentages = (top_three_cuisines / total_restaurants) * 100

print(top_cuisine_percentages)


# # LEVEL_1 ,Task_2

# In[10]:


# Count the occurrences of each unique city
city_counts = df['City'].value_counts()

# Get the city with the highest number of restaurants
city_with_most_restaurants = city_counts.idxmax()

print("City with the highest number of restaurants:", city_with_most_restaurants)


# In[12]:


# Group by city and calculate the mean rating for each city
average_ratings_by_city = df.groupby('City')['Aggregate rating'].mean()

print("Average ratings for restaurants in each city:")
print(average_ratings_by_city)


# In[14]:


# Group by city and calculate the mean rating for each city
average_ratings_by_city =df.groupby('City')['Aggregate rating'].mean()

# Find the city with the highest average rating
city_with_highest_avg_rating = average_ratings_by_city.idxmax()
highest_avg_rating = average_ratings_by_city.max()

print("City with the highest average rating:", city_with_highest_avg_rating)
print("Average rating for this city:", highest_avg_rating)


# # LEVEL_1 ,Task_3

# In[6]:


import matplotlib.pyplot as plt
price_ranges = df['Price range']
plt.hist(price_ranges, bins=[1, 2, 3, 4, 5], edgecolor='black', alpha=0.5)

#  plot
plt.title('Distribution of Price Ranges Among Restaurants')
plt.xlabel('Price Range')
plt.ylabel('Number of Restaurants')
# Show the plot
plt.show()


# In[7]:


price_range_counts = df['Price range'].value_counts()

# Calculate the total number of restaurants
total_restaurants = len(df)

# Calculate the percentage for each price range category
price_range_percentages = (price_range_counts / total_restaurants) * 100

print(price_range_percentages)


# In[ ]:





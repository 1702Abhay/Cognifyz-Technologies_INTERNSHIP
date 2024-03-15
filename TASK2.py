#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[2]:


df = pd.read_csv("E:/DATA ANALYSIS TASK LIST AND DATASET-20240120T092540Z-001/DATA ANALYSIS TASK LIST AND DATASET/Dataset .csv",encoding='utf8')
df


# In[3]:


print(df.isnull())   #to show that data is not null


# # Task: Restaurant Ratings

# In[4]:


# Analyze the distribution of aggregate ratings
rating_distribution = df['Aggregate rating'].value_counts().sort_index()

# Determine the most common rating range
most_common_rating = rating_distribution.idxmax()

print("Distribution of Aggregate Ratings:")
print(rating_distribution)
print("\nMost common rating:", most_common_rating)



# In[6]:


# Calculate the average number of votes received by restaurants
average_votes = df['Votes'].mean()

print("\nAverage number of votes received by restaurants:", average_votes)


# # Task2: Cuisine Combination

# In[17]:


# Convert non-string values in 'Cuisines' column to empty strings
df['Cuisines'] = df['Cuisines'].astype(str)

# Split the cuisine combinations and create a list of cuisines
df['Cuisine Combination'] = df['Cuisines'].apply(lambda x: tuple(sorted(x.split(', '))))

# Determine the most common combinations of cuisines
common_cuisine_combinations =df['Cuisine Combination'].value_counts()

print("Most common combinations of cuisines:")
print(common_cuisine_combinations.head(10))  # Display top 10 most common combinations


# In[16]:


# Calculate the average rating for each cuisine combination
average_rating_by_cuisine_combination = df.groupby('Cuisine Combination')['Aggregate rating'].mean()

print("\nAverage rating for each cuisine combination:")
print(average_rating_by_cuisine_combination.head(10))  # Display top 10 cuisine combinations with their average ratings


# # Task3: Geographic Analysis

# In[ ]:


# import matplotlib.pyplot as plt

# Plotting restaurant locations using longitude and latitude coordinates
plt.figure(figsize=(10, 8))
plt.scatter(df['Longitude'], df['Latitude'], alpha=0.5)
plt.title('Restaurant Locations')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)
plt.show()


# # Identify any patterns or clusters of restaurants in specific areas.

# Busy City Centers: we will notice lots of restaurants grouped closely together in downtown areas or city centers. These are where most people work and spend their leisure time, so there's a high demand for dining options.
# 
# Tourist Hotspots: Around famous landmarks or tourist attractions, we'll see clusters of restaurants. These areas cater to both tourists and locals looking for a bite to eat while exploring.
# 
# Quiet Residential Neighborhoods: In residential areas, restaurants are more spread out, reflecting the local community's needs. we won't see as many clustered together since they serve a smaller, local population.
# 
# Near Transportation: Close to airports, train stations, or bus terminals, we'll find restaurants clustered together to serve travelers and commuters passing through.
# 
# Foodie Districts: Some areas specialize in specific cuisines or offer unique dining experiences. Here, we'll see clusters of restaurants offering similar types of food or ambiance, catering to food enthusiasts.

# # Task4: Restaurant Chains

# In[25]:


# Identify restaurant chains
restaurant_chains =df[df.duplicated(subset=['Restaurant Name'], keep=False)]

# Group by restaurant name and calculate average rating and total votes
chain_ratings_popularity = restaurant_chains.groupby('Restaurant Name').agg(
    Average_Rating=('Aggregate rating', 'mean'),
    Total_Votes=('Votes', 'sum'),
    Number_of_Locations=('Restaurant Name', 'size')
).sort_values(by='Total_Votes', ascending=False)

print("Restaurant chains present in the dataset:")
print(chain_ratings_popularity)


# In[ ]:





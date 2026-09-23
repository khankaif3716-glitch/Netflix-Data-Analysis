# S-1 import thew libraries
import pandas as pd
import matplotlib.pyplot as plt


# load data
df = pd.read_csv("netflix_titles1.csv")

# clean data 
df = df.dropna(subset =['type','release_year','rating','country','duration'])

type_counts = df['type'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_counts.index, type_counts.values,color= ['skyblue','orange'])

# Head line of the bar chat
plt.title('Number of Movies Vs Tv Shows on Netflix')


# X and Y labels of plot
plt.xlabel('Type')
plt.ylabel('Count')

plt.tight_layout()

plt.savefig('moveis_vs_tvshows.png')
# display the data values in the figure
plt.show()

# Showing the rating content csv file in the form of Piechart
rating_counts = df['rating'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_counts, labels=rating_counts.index, autopct='%1.1f%%',startangle=86)

# Head line of the bar chat
plt.title('Percentage of Content Ratings')


# Automatically Arjeste the Subplot Between the Figurs
plt.tight_layout()

plt.savefig('content_ratings_pie.png')
# display the data values in the figure
plt.show()


# pilter the movies usig the histogram() method
movie_df = df[df['type'] == 'Movie'].copy()
# Movies duration of types
movie_df['duration_int'] = movie_df['duration'].str.replace('min','').astype(int)

plt.figure(figsize=(8,6))
plt.hist(movie_df['duration_int'], bins=30, color='purple', edgecolor='black')

# Head line of the bar chat
plt.title('Distribution of Movie Duration')


# X and Y labels of plot
plt.xlabel('Duration minutes')
plt.ylabel('Number of Movies')

plt.tight_layout()

plt.savefig('moveis_duration_histogram.png')
# display the data values in the figure
plt.show()

# Scatter() plot using mehtod
release_counts= df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(release_counts.index,release_counts.values,color='red')

# Head line of the bar chat
plt.title('Release Year VS Number of shows')


# X and Y labels of plot
plt.xlabel('Release year')
plt.ylabel('Number of shows')

# Add rectengular box and explain the markers values
plt.legend(loc = "upper left", fontsize = 12)

# Backgound of line and are show the Growth values to point them 
plt.grid(True,color = "gray", linestyle = ":", linewidth = 1)

plt.tight_layout()

plt.savefig('released_year_scatter.png')
# display the data values in the figure
plt.show()


country_counts = df['country'].value_counts().head(10)
plt.figure(figsize= (8,6))
plt.barh(country_counts.index,country_counts.values,color='teal')


# Head line of the bar chat
plt.title('Top 10 Countries by Number of shows')


# X and Y labels of plot
plt.xlabel('Number of Shows')
plt.ylabel('country')

plt.legend(loc = 'lower right', fontsize = 12)

# Backgound of line and are show the Growth values to point them 
plt.grid(True,color = "gray", linestyle = ":", linewidth = 1)

# Automatically Arjeste the Subplot Between the Figurs
plt.tight_layout()

plt.savefig('top10_countries.png')
# display the data values in the figure
plt.show()

content_by_year = df.groupby(['release_year','type']).size().unstack().fillna(0)
fig, ax = plt.subplots(1,2, figsize = (12,5))

# firat subplot:Movies
ax[0].plot(content_by_year,content_by_year['Movie'],color = 'blue')
ax[0].set_title('Movies Released Per Year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of Movies')

# Second subplot:movies
ax[0].plot(content_by_year.index,content_by_year['TV Show'],color = 'orange')
ax[0].set_title('TV Shows Released Per Year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of Movies')

fig.suptitle('Comperison of Movies and TV Shows Release over Years ')

plt.tight_layout()

plt.savefig('movies_tv_shows_comerison.png')

plt.show()

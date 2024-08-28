import requests
import json

# Get user input for the type of news and the number of articles
query = input("What type of news are you interested in? ")
num_articles = int(input("How many news articles would you like to see? "))

# Define the URL with the API key and query
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-07-05&sortBy=publishedAt&apiKey=7a6499ad0f07425ea64a7c43864d010f"

# Make the API request
r = requests.get(url)
news = json.loads(r.text)

# Print the specified number of news articles
for i, article in enumerate(news["articles"][:num_articles]):
    print(f"{i+1}. {article['title']}")
    print(article["description"])
    print("--------------------------------------")

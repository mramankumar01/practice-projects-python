import requests

query = input("What do you want to know today?: ")
api = "6266e11f0ad94e1b9b99228d51957bad"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-12-06&sortBy=publishedAt&apiKey={api}"

print(url)

content = requests.get(url).json()

for index, article in enumerate(content["articles"]):
    print(f"{index + 1}. {article["title"]} {article["url"]}")
    print("\n***************************************************\n")
import requests
import tkinter as tk

country = input("What Country are you interested in (Alpha-2 Format)? ")

def getNews():
    api_key = "85ced64dc13d4ac3b1084221bf8ffd47"
    url = "https://newsapi.org/v2/top-headlines?country=" + country + "&apiKey=" + api_key
    news = requests.get(url).json()

    articles = news["articles"]

    my_articles = []
    my_news = ""

    for article in articles:
        my_articles.append(article["title"])

    for i in range(10):
        my_news = my_news + str(i + 1) + ". " + my_articles[i] + "\n"

    label.config(text = my_news)



canvas = tk.Tk()
canvas.geometry("900x600")
canvas.title("News App")

button = tk.Button(canvas, font = 24, text = "Reload", command = getNews)
button.pack(pady = 20)

label = tk.Label(canvas, font = 18, justify = "left")
label.pack(pady = 20)

getNews()
canvas.mainloop()
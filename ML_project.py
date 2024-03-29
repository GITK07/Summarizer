import tkinter as tk
import nltk
from newspaper import Article
url=input("Enter the news URL: ")
article= Article(url)
nltk.download('punkt')
article.download()
article.parse()

article.nlp()

print(f'Title: {article.title}')
print(f'Author:  {article.authors}')
print(f'Publication Date: {article.publish_date}')
print(f'Summary: {article.summary}')

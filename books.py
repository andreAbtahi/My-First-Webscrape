import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('http://books.toscrape.com/')

#make webscraping easy
soup = BeautifulSoup(page.content,'html.parser')

#create a variable that has the div container we are working with
book_container = soup.find('ol',class_ = 'row')

#array of all books(access them like an array)
books = book_container.find_all('li', class_ = 'col-xs-6 col-sm-4 col-md-3 col-lg-3')

#This is the regular style of for looping
#for book in books:
    #Name of book
    #print(book.find('h3').text)

    #price of book
    #print(book.find('p',class_ = 'price_color').text)

    #Star rating
    #print("Star Rating: ",book.find('p',class_ = 'star-rating')['class'][1])
    #continue

#run a for loop to access all of them and store them in a variable
book_names = [book.find('h3').text for book in books]
price = [book.find('p',class_ = 'price_color').text for book in books]
rating = [book.find('p',class_ = 'star-rating')['class'][1] for book in books]

#using pandas: great organization tool
book_info = pd.DataFrame(
    {'Book Names': book_names,
     'Prices': price,
     'Ratings': rating,
     })

#testing the varibale that holds all information 
print(book_info)

#exporting book info to csv
book_info.to_csv('books.csv')



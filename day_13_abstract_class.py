'''
Given a Book class and a Solution class, write a MyBook class that does the following:

Inherits from Book
Has a parameterized constructor taking these  parameters:
string title
string author
int price
Implements the Book class' abstract display() method so it prints these  lines:
Title:, a space, and then the current instance's .
Author:, a space, and then the current instance's .
Price:, a space, and then the current instance's .
'''

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
    def display(self):
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')
        print(f'Price: {self.price}')


title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()

'''
Sample Input:
The Alchemist
Paulo Coelho
248

Sample Output:
Title: The Alchemist
Author: Paulo Coelho
Price: 248
'''

# Python OPP: Object Oriented Programming

Curso dictado por [Deepali Srivastava](https://www.udemy.com/user/deepalisrivastava/) en [Udemy](https://www.udemy.com/course/object-oriented-python-programming/learn/lecture/18242196#overview)


> Recursos para este curso está en Repositorio de Github : [Python OOP : Object Oriented Programming in Python](https://github.com/Deepali-Srivastava/object-oriented-programming-in-python)

|Ejercicio| Código |
|--|--|
| Ejercicio 1 | [Ver código](./#ejercicio-1) |
| Ejercicio 2 | [Ver código](./#ejercicio-2) |


## Ejercicio 1

Make a class that represents a bank account. Create four methods named set_details, display, withdraw and deposit.
In the set_details method, create two instance variables : name and balance. The default value for balance should be zero. In the display method, display the values of these two instance variables.
Both the methods withdraw and deposit have amount as parameter. Inside withdraw, subtract the amount from balance and inside deposit, add the amount to the balance.
Create two instances of this class and call the methods on those instances.

```python
class BankAccount:
  def set_details(self, name, balance=0):
      self.name = name
      self.balance = balance
  
  def display(self):
      print(f"""
      Name: {self.name}
      Balance: {self.balance}
      """)
      
  def deposit(self, amount):
      self.balance += amount
      self.display()

  def withdraw(self, amount):
      self.balance -= amount
      self.display()


customer1 = BankAccount()
customer1.set_details("Juan", 200)
customer1.deposit(200)
customer1.withdraw(300)

customer2 = BankAccount()
customer2.set_details('Mike')
customer2.deposit(300)
```
## Ejercicio 2
**1.** In the BankAccount class that you had created in the previous exercise, delete the set_details() method and create an __init__ method.

```python
class BankAccount:
  def __init__(self, name, balance=0):
      self.name = name
      self.balance = balance
  
  def display(self):
      print(f"""
      Name: {self.name}
      Balance: {self.balance}
      """)
      
  def deposit(self, amount):
      self.balance += amount
      self.display()

  def withdraw(self, amount):
      self.balance -= amount
      self.display()
      
customer1 = BankAccount("Juan", 200)
customer1.deposit(200)
customer1.withdraw(300)

customer2 = BankAccount('Mike')
customer2.deposit(300)
```

**2.**  Create a class named Book with an __init__ method. Inside the __init__ method, create the instance variables isbn, title, author, publisher, pages, price, copies.

Create these four instance objects from this class.

1.  book1 =  Book('957-4-36-547417-1',  'Learn Physics','Stephen',  'CBC',  350,  200,10)
2.  book2 =  Book('652-6-86-748413-3',  'Learn Chemistry','Jack',  'CBC',  400,  220,20)
3.  book3 =  Book('957-7-39-347216-2',  'Learn Maths','John',  'XYZ',  500,  300,5)
4.  book4 =  Book('957-7-39-347216-2',  'Learn Biology','Jack',  'XYZ',  400,  200,6)

Write a method display that prints the isbn, title, price and number of copies of the book.

```python
class Book:

  def __init__(self, isbn, title, author, publisher, pages, price, copies):
    self.isbn = isbn
    self.title = title
    self.author = author
    self.publisher = publisher
    self.pages = pages
    self.price = price
    self.copies = copies

  def display(self):
    print(f"""
    ISBN: {self.isbn}
    Title: {self.title}
    Price: {self.price}
    Number of copies: {self.copies}
    """)


book1 = Book('957-4-36-547417-1', 'Learn Physics', 'Stephen', 'CBC', 350, 200, 10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry', 'Jack', 'CBC', 400, 220, 20)
book3 = Book('957-7-39-347216-2', 'Learn Maths', 'John', 'XYZ', 500, 300, 0)
book4 = Book('957-7-39-347216-2', 'Learn Biology', 'Jack', 'XYZ', 400, 200, 6)

book1.display()
book2.display()
book3.display()
book4.display()
```

**3.**  For the Book class that you have created, write a method named in_stock that returns True if number of copies is more than zero, otherwise it returns False.

Create another method named sell that decreases the number of copies by 1 if the book is in stock, otherwise it prints the message that the book is out of stock.

```python
def in_stock(self):
    if self.copies > 0:
      return True
    else:
      return False

  def sell(self):
    if self.in_stock():
      self.copies -= 1
    else:
      print(f"We can't sell {self.title} by {self.author} because we're out of stock")
      
  def display(self):
    in_stock = self.in_stock()
    print(f"""
    ISBN: {self.isbn}
    Title: {self.title}
    Price: {self.price}
    Number of copies: {self.copies}
    In stock: {in_stock}
    """)
```

**4.**  Create a list named books that contains the 4 Book instance objects that you have created in question 2. Iterate over this list using a for loop and call display() for each object in the list.

```python
books = [book1, book2, book3, book4]
for book in books:
  book.display()

```

Write a list comprehension to create another list that contains title of books written by Jack.

```python
for book in books:
  if book.author == 'Jack':
    print(book.title)
```
  

**5.**  In the Book class, create a property named price such that the price of a book cannot be less than 50 or more than 1000.

```python
  @property
  def price(self):
      return self._price

  @price.setter
  def price(self, new_price):
      if 50 <= new_price <= 1000:
          self._price = new_price
      else:
          raise ValueError('Price cannot be less than 50 or more than 1000')
```
  

**6.**  Make a class Fraction that contains two instance variables, nr and dr (nr stands for numerator and dr for denominator). Define an __init__ method that provides values for these instance variables. Make the denominator optional by providing a default argument of 1.

In the __init__ method, make the denominator positive if it is negative. For example -2/-3 should be changed to 2/3 and 2/-3 to -2/3.


Write a method named show that prints numerator, then '/' and then the denominator.

```python
class fraction:
  def __init__(self, nr, dr=1):
    self.nr = nr
    self.dr = dr
    if self.dr < 0:
      self.nr = (self.nr * -1)
      self.dr = (self.dr * -1)


  def display(self):
    print(f"{self.nr}/{self.dr}")
```
  

**7.** Define a method named multiply that multiples two Fraction instance objects. For multiplying two fractions, you have to multiply the numerator with numerator and denominator with the denominator.

Inside the method, create a new instance object that is the product of the two fractions and return it. Write your method in such a way that it supports multiplication of a Fraction by an integer also.

Similarly define a method named add to add two Fraction instance objects. Sum of two fractions n1/d1 and n2/d2 is (n1*d2 + n2*d1) / (d1*d2). This method should also support addition of a Fraction by an integer.

Test your fraction class with this code.

1.  f1 =  Fraction(2,3)
2.  f1.show()
3.  f2 =  Fraction(3,4)
4.  f2.show()
5.  f3 = f1.multiply(f2)
6.  f3.show()
7.  f3 = f1.add(f2)
8.  f3.show()
9.  f3 = f1.add(5)  
10.  f3.show()
11.  f3 = f1.multiply(5)  
12.  f3.show()

The output that you should get is given below.

2/3
3/4
6/12
17/12
17/3
10/3

```python
def multiply(self,other):
    if isinstance(other,int):
        other = Fraction(other)
    return Fraction(self.nr * other.nr , self.dr * other.dr)

  def add(self, other):
    if isinstance(other, int):
      other = Fraction(other)
    return Fraction(((self.nr * other.dr)+(self.dr * other.nr)),self.dr * other.dr)
```

  

**8.** For the following class Product, create a read only property named selling_price that is calculated by deducting discount from the marked_price. The instance variable discount represents discount in percent.


```python
class  Product():
  def __init__(self, id, marked_price, discount):
    self.id = id
    self.marked_price = marked_price
    self.discount = discount

  def display(self):
    print(self.id,  self.marked_price,  self.discount)

p1 =  Product('X879',  400,  6)
p2 =  Product('A234',  100,  5)
p3 =  Product('B987',  990,  4)
p4 =  Product('H456',  800,  6)
```

```python
@property
  def selling_price(self):
    return self.marked_price - (0.01 * self.discount * self.marked_price)
```

**9.**  Suppose after some time, you want to give an additional 2% discount on a product, if its price is above 500. To incorporate this change, implement discount as a property in your Product class.

```python
@property
  def discount(self):
      if self.marked_price > 500:
        return self._discount+2
      else:
        return self._discount

  @discount.setter
  def discount(self, new_discount):
      self._discount = new_discount 
```
  

**10.**  Write a Circle class with an instance variable named radius and a method named area. Create two more attributes named diameter and circumference and make them behave as read only attributes.

Perform data validation on radius, user should not be allowed to assign a negative value to it.

For a circle

diameter = 2 * radius

circumference = 2 * 3.14 * radius

area = 3.14 * radius * radius






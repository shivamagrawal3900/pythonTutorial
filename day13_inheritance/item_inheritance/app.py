from day13_inheritance.item_inheritance.book import Book
from day13_inheritance.item_inheritance.dvd import Dvd

print("Enter 5 items you want to issue")

items = []
for i in range(5):
    item_type = input("book or dvd (b/d): ")
    item = Book() if 'b' == item_type else Dvd()
    item.read()
    items.append(item)

print("\nlist of issued items")

for item in items:
    item.show()

from day13_inheritance.item_inheritance.item import Item


class Book(Item):
    def read(self):
        self.title = input("Enter book's title: ")
        self.author = input("Enter book's author: ")
        self.publication = input("Enter book's publication: ")

    def show(self):
        print(f"book: {self.title}\tauthor: {self.author}\tpublication: {self.publication}")

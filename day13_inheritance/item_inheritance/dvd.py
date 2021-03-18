from day13_inheritance.item_inheritance.item import Item


class Dvd(Item):
    def read(self):
        self.title = input("Enter movie's title: ")
        self.director = input("Enter movie's director: ")
        self.category = input("Enter movie's category: ")

    def show(self):
        print(f"movie: {self.title}\tdirector: {self.director}\tcategory: {self.category}")

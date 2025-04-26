class FileSystemItem:
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def display_properties(self, indent=0):
        print(" " * indent + f"Ім'я: {self.name}, Дата: '{self.date}'")


class File(FileSystemItem):
    def __init__(self, name, date, size, file_type):
        super().__init__(name, date)
        self.size = size
        self.file_type = file_type

    def display_properties(self, indent=0):
        print(" " * indent + f"Ім'я: {self.name}, Дата: '{self.date}', Розмір: '{self.size}', Тип: '{self.file_type}'")


class Directory(FileSystemItem):
    def __init__(self, name, date):
        super().__init__(name, date)
        self.children = []

    def add_item(self, item):
        self.children.append(item)

    def remove_item(self, item_name):
        self.children = [item for item in self.children if item.name != item_name]

    def list_contents(self, indent=0):
        print(" " * indent + f"[Директорія] {self.name}")
        for child in self.children:
            child.display_properties(indent + 2)
            if isinstance(child, Directory):
                child.list_contents(indent + 2)

    def display_properties(self, indent=0):
        print(" " * indent + f"Ім'я: {self.name}, Дата: '{self.date}', Кількість елементів: {len(self.children)}")

file1 = File("text.txt", "2025-04-20", "1KB", "text/plain")
file2 = File("image.png", "2025-04-21", "3MB", "image/png")
subdir = Directory("Photos", "2025-04-22")
subdir.add_item(file2)

root = Directory("Root", "2025-04-19")
root.add_item(file1)
root.add_item(subdir)

root.list_contents()


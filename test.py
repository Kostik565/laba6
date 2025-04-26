import unittest
from lab6 import *
class TestFileSystem(unittest.TestCase):
    def test_file_properties(self):
        file = File("test.txt", "2025-04-20", "1KB", "text/plain")
        self.assertEqual(file.name, "test.txt")
        self.assertEqual(file.date, "2025-04-20")
        self.assertEqual(file.size, "1KB")
        self.assertEqual(file.file_type, "text/plain")

    def test_directory_add_and_remove_item(self):
        dir = Directory("MyDir", "2025-04-22")
        file = File("test.txt", "2025-04-20", "1KB", "text/plain")

        dir.add_item(file)
        self.assertEqual(len(dir.children), 1)
        self.assertEqual(dir.children[0], file)

        dir.remove_item("test.txt")
        self.assertEqual(len(dir.children), 0)

    def test_nested_directories(self):
        root = Directory("Root", "2025-04-19")
        subdir = Directory("SubDir", "2025-04-20")
        file = File("file.txt", "2025-04-21", "2KB", "text/plain")

        subdir.add_item(file)
        root.add_item(subdir)

        self.assertEqual(len(root.children), 1)
        self.assertEqual(root.children[0], subdir)
        self.assertEqual(root.children[0].children[0], file)

if __name__ == '__main__':
    unittest.main()

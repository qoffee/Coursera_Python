"""
Файл с магическими методами
"""
import os

class File:
    def __init__(self, path):
        self.path = path

    def write(self, string):
        with open(path, 'a') as f:
            f.write(string)

    def __add__(self, obj):
        return File(self.path + obj.path)

    def __str__(self):
        print(self.path)

    def get_file_content(self, file):
        f = open(file, 'r')
        return file.read()

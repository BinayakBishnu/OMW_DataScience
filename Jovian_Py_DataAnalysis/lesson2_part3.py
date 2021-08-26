import os

os.getcwd()

os.mkdir('abc')

url = "https://upload.wikimedia.org/wikipedia/commons/3/31/NumPy_logo_2020.svg"

from urllib.request import urlretrieve

urlretrieve(url,'./abc/pic.svg')
os.listdir('./abc')


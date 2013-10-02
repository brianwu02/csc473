import string
import random
from bs4 import BeautifulSoup

def lowerfy(func):
	def wrapper(string):
		return string.lower()
	return wrapper

@lowerfy
def ret_string(string):
	return string

def generate_string(size=10, chars=string.ascii_uppercase):
	return ''.join(random.choice(chars) for x in range(size))

temp = list()
for i in range(0, 100):
	temp.append(generate_string())
print temp[0]

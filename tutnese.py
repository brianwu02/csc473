import re

def lowerfy(func):
	def wrapper(string):
		return func(string.lower())
	return wrapper

def exception_check(func):
	def wrapper(string):
		for i in string:
			if i == "|":
				raise Exception("you have an \"|\"")
		return func(string)
	return wrapper

@lowerfy
@exception_check
def encode(string):
	temp=list()
	myDict = {"B":"bub", "C":"coch", "D": "dud", 
			"F":"fuf", "K":"kuck", "L":"lul","M":"mum",
			"N":"nun", "S":"sus", "T":"tut", "V":"vuv",
			"W":"wack", "G":"gug", "H":"hash", "J":"jug",
			"P":"pup", "Q":"quack", "R":"rur","X":"xux", 
			"Y":"yub", "Z":"zug" }
	for i in string:
		if i.upper() in myDict:
			## if the current character exists in the hash key
			## append the hash value to a temporary list
			temp.append(myDict[i.upper()])
			if len(temp) > 1:
				if temp[-1] == temp[-2]:
					del temp[-1]
					del temp[-1]
					temp.append("squa" + i)
		else:
			temp.append(i.lower())
	return ''.join(temp)

@lowerfy
@exception_check
def decode(string):
	reverseDict = { "bub":"b", "coch":"c", "dud":"d",
			"fuf":"f", "kuck":"k", "lul":"l","mum":"m", 
			"nun":"n", "sus":"s", "tut":"t", "vuv":"v",
			"wack":"w", "gug":"g", "hash":"h", "jug":"j", 
			"pup":"p", "quack":"q", "rur":"r", "xux":"x", 
			"yub":"y", "zug":"z"
			}
	reverseArray = [ "bub", "coch", "dud", "fuf", "kuck",
			"lul", "mum", "nun", "sus", "tut", "vuv", "wack",
			"gug", "hash", "jug", "pup", "quack", "rur", 
			"xux", "yub", "zug"
			]
	for i in reverseArray:
		string = re.sub(i, reverseDict[i], string, re.DOTALL)
	string = re.sub(r'''(squa)([a-z]+)''','\\2\\2', string)
	return string



"""
re.sub(r'pattern', replace_with, string, re.DOTALL)
"""

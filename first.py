	import csv

d = []
f = []
r = []
c = []
wb = []
iss = []
dis = []


def fetch(fetchIndex):
		



def decode(): 


def rename():

def commit(c):

def init(a, b):


	with open('file.csv', 'r') as csvfile:
			reader = csv.reader(csvfile, delimiter=',', skipinitialspace=True)    			for row in reader:
       			 # do something with the row


def writeback():

def Issue():

def Dispatch():

def main ():
	init(argc, argv)
	committedInsts = 0;	 

	while(committedInsts <icount):
		committedInsts = commit(committedInsts)	
		writeback()
		Issue()
		Dispatch()
		rename()
		decode()
		fetchIndex = fetch(fetchIndex)
		cyclecount++
		emitOutput()
		return 0

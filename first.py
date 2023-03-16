	
import csv
import pandas as pd	
d = []
f = []
r = []
c = []
wb = []
iss = []
dis = []


#def fetch(fetchIndex):
		



#def decode(): 


#def rename():

#def commit(c):

def init():
	instructions = pd.read_csv('ex1.txt')
	for i in len(range(instructions)):
		print(i)

#def writeback():

#def Issue():

#def Dispatch():

init()
committedInsts = 0;	 

while(committedInsts <icount):
	committedInsts = commit(committedInsts)	
	writeback()
	Issue()
	Dispatch()
	rename()
	decode()
	fetchIndex = fetch(fetchIndex)


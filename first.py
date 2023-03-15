

def fetch(fetchIndex)

def decode()

def rename()

def commit(c)

def init(a, b)

def writeback()

def Issue()

def Dispatch()

def main () 
	init(argc, argv);
	uint32 committedInsts=0;	 

	while(committedInsts <icount)
		committedInsts = commit(committedInsts)	
		writeback();
		Issue();
		Dispatch();
		rename();
		decode();
		fetchIndex = fetch(fetchIndex)
		cyclecount++;
	emitOutput();
	return 0;

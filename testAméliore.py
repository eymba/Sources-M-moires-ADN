##import time
##sequence = "TCCTGGAATTCGCGGAGGAATGTGATCATACAGAGAGCTTGCTGTTTGCCTGAAGTGCGA"
##dna=["AT","TA","CG","GC"]
##times = list()
##start=time.clock()
##for i in range(0,len(sequence) - 1,2):
##    if (sequence[i]+sequence[i+1])  not in dna:
##    
##        if i < len(sequence ) :
##            
##            if sequence[i]=="A" :
##                    sequence=sequence[:i+1]+"T"+sequence[i+2:]
##                    
##            elif sequence[i]=="T" :
##                sequence=sequence[:i+1]+"A"+sequence[i+2:]
##
##            elif sequence[i]=="C" :
##                    sequence=sequence[:i+1]+"G"+sequence[i+2:]
##                    
##            elif sequence[i]=="G" :
##                sequence=sequence[:i+1]+"C"+sequence[i+2:]
##end=time.clock()
##times.append(end-start)
##print(sequence)
###print(end)
##print("temps dexecution",times)
def  PresenceErreur(sequence):
    sequence=sequence.upper()
    dna=["AT","TA","CG","GC"]
    for i in range(0,len(sequence) - 1,2):
        if (sequence[i]+sequence[i+1])  not in dna:
        
            if i < len(sequence ) :
                
                if sequence[i]=="A" :
                        sequence=sequence[:i+1]+"T"+sequence[i+2:]
                        
                elif sequence[i]=="T" :
                    sequence=sequence[:i+1]+"A"+sequence[i+2:]

                elif sequence[i]=="C" :
                        sequence=sequence[:i+1]+"G"+sequence[i+2:]
                        
                elif sequence[i]=="G" :
                    sequence=sequence[:i+1]+"C"+sequence[i+2:]
    return sequence

def de_bruijn_ize(st, k):
    edges = []
    nodes = set()
    for i in range(len(st) - k + 1):
        edges.append((st[i:i + k - 1], st[i + 1:i + k]))
        nodes.add(st[i:i + k - 1])
        nodes.add(st[i + 1:i + k])
    return nodes, edges

def dist_hamming(m1,m2):
    d = 0
    for a,b in zip(m1,m2):
        if a != b :
            d += 1
    return d

#sequence = "TCCTGGAATTCGCGGAGGAATGT"
#PresenceErreur(sequence)
#nodes, edges = de_bruijn_ize(sequence, 3)
dist_hamming("TCCTGGAATTCGCGGAGGAATGT","ATCTGGAATTCGCGGAGGAATGT")         
        
    
    

#!/usr/bin/env python
# coding: utf-8

# In[11]:


def random_sequence(seqlen):
    "Generate a random DNA sequence of a given length "
    return "".join([random.choice("ACGT") for i in range(seqlen)])


# In[12]:


# set a random seed
import random
#random.seed(123)
# get a random genome sequence
genome1 = random_sequence(255)
print("génerer une sequence de longueur maximale 255", genome1)


# In[13]:


#import graphviz
#import os
#os.environ["PATH"]=os.environ["PATH"]+';'+ os.environ['CONDA_PREFIX']+r"\Library\bin\graphviz"
#import gvmagic
#from graphviz import Digraph 

def de_bruijn_ize(st, k):
    edges = []
    nodes = set()
    for i in range(len(st) - k + 1):
        edges.append((st[i:i + k - 1], st[i + 1:i + k]))
        nodes.add(st[i:i + k - 1])
        nodes.add(st[i + 1:i + k])
    return nodes, edges


nodes, edges = de_bruijn_ize(genome1, 3)


# In[14]:


#import random
#import toyplot
#def plot_debruijn_graph(edges, width=500, height=500):
   # "returns a toyplot graph from an input of edges"
 #   graph = toyplot.graph(
  #      [i[0] for i in edges],
    #    [i[1] for i in edges],
      #  width=width,
        #height=height,
        #tmarker=">", 
        #vsize=25,
        #vstyle={"stroke": "black", "stroke-width": 2, "fill": "none"},
        #vlstyle={"font-size": "11px"},
        #estyle={"stroke": "black", "stroke-width": 2},
        #layout=toyplot.layout.FruchtermanReingold(edges=toyplot.layout.CurvedEdges()))
    #return graph


# In[15]:


##def  PresenceErreur(sequence):
##     
##    while sequence.count('AA')!=0 or sequence.count('TT')!=0 or
##        sequence.count('CC')!=0 or sequence.count('GG')!=0:
##        #print("detection d'erreur dans la sequence")
##        #print(sequence.find('AA'))
##        #print("correction derreurs")
##        sequence=sequence.replace('AA','AT')
##        sequence=sequence.replace('TT','TA')
##        sequence=sequence.replace('CC','CG')
##        sequence=sequence.replace('GG','GC')
##        #sequence=sequence.replace('GG','GC')
##        #sequence=sequence.replace('GG','GC')
##    return sequence

def  PresenceErreur(sequence):
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
      
def dist_hamming(m1,m2):
    d = 0
    for a,b in zip(m1,m2):
        if a != b :
            d += 1
    return d

def DetectingErrorInSequence():
    #sequence=input("donner une sequence de taille maximale 255 ")
    sequence=genome1
    sequence=sequence.upper()
    bd=["ATCGATCGATCGATCGAATGATCGATCGAGCATGCATGCATGCATGCATGATCGATCGATCGATCGAATGATCGATCGAGCATGCATGCATGCATGCATGATCGATCGATCGATCGAATGATCGATCGAGCATGCATGCATGCATGCATGATCGATCGATCGATCGAATGATCGATCGAGCATGCATGCATGCATGCATGATGCAT"]
    
    for i in range(len(bd)):
        
        #if bd[i]==sequence[:len(bd[i])]:
        if bd[i]==sequence :
            print("sequence retrouvée dans la base")
            break
        #elif dist_hamming(bd[i],sequence[:len(bd[i])])  >=1:
        elif dist_hamming(bd[i],sequence )  >=1:
            
            print("le poids de haming du mot avec celui de la base est:", dist_hamming(bd[i],sequence))
            print("detection d'erreur dans la sequence")
            print("la sequence la plus proche de la sequence donnée est :",bd[i])
            print("la sequence corrigée est :",PresenceErreur(sequence))
            nodes, edges = de_bruijn_ize(PresenceErreur(sequence), 3)
            print("les noeuds obtenus a partir de la sequence sont :", nodes)
            print("les arrets obtenus a partir de la sequence sont :", edges)
            #print("la sequence de brujin construite est :", plot_debruijn_graph(edges))
     
            break
        #elif dist_hamming(bd[i],sequence[:len(bd[i])]) !=0 :
        else:
            print("sequence non trouvée dans la base")
            print("sequence ajoutée dans la base")
            bd=bd.append(sequence)
            
DetectingErrorInSequence()





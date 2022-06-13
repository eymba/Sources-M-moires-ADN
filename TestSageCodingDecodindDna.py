import random
print("Reconstruction de séquence de nucléotides")
print("Converting Nucleotides N={A,C,T,G} into Numbers Z= {0,1,2,3}")
ligne = input("entrez une séquence de longueur  n")
n=len(ligne)
ligne=ligne.upper()
print(ligne)
dna=' '
for i in range(len(ligne)):     
        if ligne[i] == 'A':
          dna += "0"
      
        elif ligne[i] == 'T':
          dna += "1"     
    
        elif ligne[i] == 'C':
          dna += "2"
        
        elif ligne[i] == 'G':
          dna += "3"
#dna=list(dna)
print("la sequence correspondante dans F4={0,1,2,3} est :",dna)
#dna=int(dna)
print("afficher la base de donnée" )
bd_seq=[random.randint(0, 3) for i in range(256)]
bd_seq=[''.join(str(elem) for elem in bd_seq) ]
#bd=str(bd_seq)
print(bd_seq[:n])
    
if dna in bd_seq:
    print("sequence retrouvée dans la base de donnéess l'individus est identifié")
    #elif dna not in bd_seq:
   
    
else:
    print("sequence non trouvée dans la base")
    bd_seq.append(dna)
    print(bd_seq)
    



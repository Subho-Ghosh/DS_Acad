''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
	# Note: the getMax function was found and modified from the following 
	# post : https://stackoverflow.com/questions/50254484/find-elements-from-an-array-such-that-no-two-are-adjacent-and-whose-sum-is-maxim

def main():

 # Write code here
 lines = []
 while True:
     try:
        line = input('')
     except EOFError:
        break
     lines.append(line)

 ntcases = 0
 numTickets = []
 houseTickets = []
 
 if not lines:
     print('{}'.format(-1), flush=True)
 else:
     ntcases = int(lines[0].lstrip(' ').rstrip(' '))
     numTickets = [int(lines[i].lstrip(' ').rstrip(' ')) for i in range(1,len(lines),2)]    
     houseTickets = [lines[i].lstrip(' ').rstrip(' ').split() for i in range(2,len(lines),2)]
     # pre checks for input data
     if not checkInp(ntcases,1) or len(numTickets)!=ntcases or len(houseTickets)!=ntcases or any(val[0]!=len(val[1]) or not checkInp(val[0],2) for val in zip(numTickets,houseTickets)):
         print('{}'.format(-1), flush=True)     
     else :
         for tklist in houseTickets:
             tklist = [val for val in list(map(int,tklist)) if checkInp(val)] # check only valid tickets
             if not tklist:
                 print('{}'.format(-1), flush=True)
             elif all(val<0 for val in tklist) or all(val==tklist[0] for val in tklist) or 1<=len(tklist)<=2:
                 print(str(max(tklist)),flush=True)
             else : 
                 tklist = [val for val in tklist if val!=0] # check only non zero tickets               
                 res = getMax(tklist)
                 if res: 
                     print(''.join(list(map(str,res))[::-1]), flush=True)
                 else :
                     print('{}'.format(-1), flush=True)    
         

def checkInp(inpval, inptype=3):
    if inptype == 1: return (1<= int(inpval) <=10)
    if inptype == 2: return (1<= int(inpval) <=10000)
    if inptype == 3: return (-1000<= int(inpval) <=1000)

def getMax(tickets):    
    seqi=[tickets[0]]    
    seqex,seqexn=[],[]     
    for i in range(1,len(tickets)):               
        
        # current max excluding i         
        seqexn = (seqi[:] if sum(seqi)>sum(seqex) else seqex[:])
        
        # current max including i         
        seqi = seqex[:]+[tickets[i]]        
        seqex = seqexn[:]        
   
    return (seqi[:] if sum(seqi)>sum(seqex) else seqex[:])      
            
    
main()
____________________________________________
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
	# Note: the getMax function was found and modified from the following 
	# post : https://stackoverflow.com/questions/50254484/find-elements-from-an-array-such-that-no-two-are-adjacent-and-whose-sum-is-maxim

def main():

 # Write code here
 lines = []
 while True:
     try:
        line = input('')
     except EOFError:
        break
     lines.append(line)

 ntcases = 0
 numTickets = []
 houseTickets = []
 
 ntcases = int(lines[0].lstrip(' ').rstrip(' '))
 numTickets = [int(lines[i].lstrip(' ').rstrip(' ')) for i in range(1,len(lines),2)]    
 houseTickets = [lines[i].lstrip(' ').rstrip(' ').split() for i in range(2,len(lines),2)]
 for tklist in houseTickets:
     tklist = [val for val in list(map(int,tklist)) if checkInp(val)]
     if all(val<0 for val in tklist):
         print(str(max(tklist)),flush=True)
     else:
         res = getMax(tklist)
         if res:         
             print(''.join(list(map(str,[val for val in res if val>0]))[::-1]), flush=True)          
         else :
             print('{}'.format(-1), flush=True)    
         

def checkInp(inpval, inptype=3):
    if inptype == 1: return (1<= int(inpval) <=10)
    if inptype == 2: return (1<= int(inpval) <=10000)
    if inptype == 3: return (-1000<= int(inpval) <=1000)

def getMax(tickets):    
    seqi=[tickets[0]]    
    seqex,seqexn=[],[]     
    for i in range(1,len(tickets)):               
        
        # current max excluding i         
        seqexn = (seqi[:] if sum(seqi)>sum(seqex) else seqex[:])
        
        # current max including i         
        seqi = seqex[:]+[tickets[i]]        
        seqex = seqexn[:]        
   
    return (seqi[:] if sum(seqi)>sum(seqex) else seqex[:])      
            
    
main()
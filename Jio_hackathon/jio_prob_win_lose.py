''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():

 # Write code here 
 lines = []
 while True:
     try:
        line = input('')
     except EOFError:
        break
     lines.append(line)

 villainslist,playerslist,ncases,msg = parseInput(lines)

 if not msg:
     for res in calcRes(villainslist,playerslist,ncases):
         print(res)
     
 else :
     print("\n",msg)

def checkInp(inpval, inptype=3):
    if inptype == 1: return (1<= int(inpval) <=10)
    if inptype == 2: return (1<= int(inpval) <=1000)
    if inptype == 3: return (1<= int(inpval) <=100000)

def parseInput(lines):
    msg = None
    if not lines:
        msg = "Empty Input"
    else :
        if not checkInp(int(lines[0]),inptype=1):
            msg = 'Incorrect number of test cases'        
        else :
            ncases = int(lines[0])
            numvp = [int(lines[i]) for i in range(1,len(lines),3)]
            villainslist = [lines[i].lstrip(' ').rstrip(' ').split(' ') for i in range(2,len(lines),3)]
            playerslist = [lines[i].lstrip(' ').rstrip(' ').split(' ') for i in range(3,len(lines),3)]
            if not len(villainslist) == ncases or not len(playerslist) == ncases:
                msg='Test cases don''t match'            
            else :
                for num,villains in enumerate(villainslist):
                    if not checkInp(len(villains),inptype = 2) or (int(numvp[num]) != len(villains)):
                        msg = 'Number of villains inside testcase# ' + str(num+1) + ' is wrong' 
                for num,players in enumerate(playerslist):
                    if not checkInp(len(players),inptype = 2) or (int(numvp[num]) != len(players)):
                        msg = 'Number of players inside testcase# ' + str(num+1) + ' is wrong'                    
    		 
    if msg:
        villainslist = 0
        playerslist = 0
		
    return villainslist,playerslist,ncases,msg

def checkEng(veng,plist):
    plist.sort()
    ret = None
    for peng in plist:
        if peng >= veng:
            ret = peng
            break
    
    return ret	
	
def setPlayer(vlist,plist):
    resmatrix = []
    for veng in vlist:
        peng = checkEng(veng,plist)
        if peng:
            resmatrix.append((veng,peng,'WIN'))
            plist.remove(peng)
        else :
            resmatrix.append((veng,'','LOSE'))
        
    if all(item[2] == 'WIN' for item in resmatrix):
        return 'WIN'
    else :
        return 'LOSE'    

def calcRes(villainslist,playerslist,ncases):
    outlist = []
    for i in range(ncases):
        outlist.append(setPlayer(list(map(int,villainslist[i])),list(map(int,playerslist[i]))))
    
    return outlist

main()


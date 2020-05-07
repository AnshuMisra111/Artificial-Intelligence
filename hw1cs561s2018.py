from sys import maxsize
import glob
import copy
import os


row=['A','B','C','D','E','F','G','H']

def func(a,b):
    d={'A':10,'B':20,'C':30,'D':40,'E':50,'F':60,'G':70,'H':80}
    a1=d[a[0]]+(9-int(a[1]))
    a2 = d[b[0]] +(9 - int(b[1]))
    return a2-a1

class Node(object):
   def __init__(self,Sstate,Cstate,Present,Prev,depth,Pass,star):
       self.sstate=Sstate
       self.cstate=Cstate
       self.present=Present
       self.prev=Prev
       self.children=[]
       self.Pass=Pass
       self.depth=depth
       self.value=0

       utilValue=0;
       if mainplayer=="Star":
        if len(Sstate)>0:
         for i in Sstate:
           utilValue=utilValue+int(star1[i[0]])
        if len(Cstate)>0:
         for i in Cstate:
           utilValue=utilValue-int(circle1[i[0]])
       else:
           if len(Sstate) > 0:
               for i in Sstate:
                   utilValue = utilValue - int(star1[i[0]])
           if len(Cstate) > 0:
               for i in Cstate:
                   utilValue = utilValue + int(circle1[i[0]])



       self.utilityValue=utilValue

       return

       #print(self.prev," ",self.present)





def childrens(Node1,star,depth):
       Sstate = Node1.sstate
       Cstate = Node1.cstate

       if depth==0 or Node1.present=="PASS" or len(Sstate)==0 or len(Cstate)==0:
           return



       if star is True:
           for i in Sstate:
                Node2=None
                Node3=None
                ind=row.index(i[0])
                if(ind<len(row)-1):
                    if int(i[1])>1:

                       pos1=row[ind+1]+str(int(i[1])-1)
                       if pos1 not in Cstate:
                         if pos1[0]=='H' or pos1 not in Sstate:

                           temp = list(copy.deepcopy(Sstate))
                           temp.remove(i)
                           temp.append(pos1)
                           temp=sorted(temp,cmp=func)
                           Node2=Node(temp,Node1.cstate,pos1,i,depth-1,False,False)
                           #Node1.children.append(Node2)
                       else:
                           if ind<len(row)-2:
                               if int(i[1])>2:

                                 pos2 = row[ind + 2] + str(int(i[1]) - 2)
                                 if pos2 not in Cstate:
                                  if pos2[0]=='H'or pos2 not in Sstate:

                                    temp = list(copy.deepcopy(Sstate))
                                    temp2=list(copy.deepcopy(Cstate))
                                    temp2.remove(pos1)
                                    temp.remove(i)
                                    temp.append(pos2)
                                    temp = sorted(temp, cmp=func)
                                    Node2=Node(temp, temp2, pos2, i, depth - 1, False, False)
                                    #Node1.children.append(Node2)

                    if int(i[1])<8:
                       pos1=row[ind+1]+str(int(i[1])+1)

                       if pos1 not in Cstate:
                         if pos1[0]=='H' or pos1 not in Sstate:

                           temp = list(copy.deepcopy(Sstate))
                           temp.remove(i)
                           temp.append(pos1)
                           temp=sorted(temp,cmp=func)
                           Node3=Node(temp,Node1.cstate,pos1,i,depth-1,False,False)
                           #Node1.children.append(Node2)
                       else:
                           if ind<len(row)-2:
                               if int(i[1])<7:

                                 pos2 = row[ind + 2] + str(int(i[1]) + 2)
                                 if pos2 not in Cstate:
                                  if pos2[0]=='H' or pos2 not in Sstate:
                                   temp = list(copy.deepcopy(Sstate))
                                   temp2 = list(copy.deepcopy(Cstate))
                                   temp2.remove(pos1)
                                   temp.remove(i)
                                   temp.append(pos2)
                                   temp = sorted(temp, cmp=func)
                                   Node3=Node(temp, temp2, pos2, i, depth - 1, False, False)
                                   #Node1.children.append(Node2)

                if (Node3 is not None) and (Node2 is not None):
                  '''  
                  t=func(Node3.prev,Node2.prev)
                  if t>0:
                    Node1.children.append(Node2)
                    Node1.children.append(Node3)
                  if t<0:
                    Node1.children.append(Node3)
                    Node1.children.append(Node2)
                  if t==0:
                  '''
                  t2=func(Node3.present,Node2.present)
                  if t2>0:
                        Node1.children.append(Node2)
                        Node1.children.append(Node3)
                  if t2<0:
                        Node1.children.append(Node3)
                        Node1.children.append(Node2)
                else:
                  if Node2 is not None:
                     Node1.children.append(Node2)
                  if Node3 is not None:
                     Node1.children.append(Node3)


           if len(Node1.children)==0:
               if Node1.Pass == True:
                   Node2=Node(Node1.sstate, Node1.cstate, "PASS", Node1.present, depth - 1, True, False)
                   Node1.children.append(Node2)
                   return Node1
               else:
                   Node2=Node(Node1.sstate,Node1.cstate,Node1.present,Node1.present,depth-1,True,False)
                   Node1.children.append(Node2)

       else:
           for i in Cstate:
               Node2=None
               Node3=None
               ind = row.index(i[0])
               if (ind>0):
                   if int(i[1]) > 1:
                       pos1 = row[ind - 1] + str(int(i[1]) - 1)
                       if pos1 not in Sstate:
                         if pos1[0]=='A' or pos1 not in Cstate:
                           temp = list(copy.deepcopy(Cstate))
                           temp.remove(i)
                           temp.append(pos1)
                           temp = sorted(temp, cmp=func)
                           Node2=Node(Node1.sstate,temp, pos1, i, depth - 1, False, True)
                           #Node1.children.append(Node2)

                       else:
                           if ind >1:
                               if int(i[1]) > 2:
                                 pos2 = row[ind - 2] + str(int(i[1]) - 2)
                                 if pos2 not in Sstate:
                                  if pos2[0]=='A' or pos2 not in Cstate:
                                   temp = list(copy.deepcopy(Cstate))
                                   temp.remove(i)
                                   temp.append(pos2)
                                   temp2 = list(copy.deepcopy(Sstate))
                                   temp2.remove(pos1)
                                   temp = sorted(temp, cmp=func)
                                   Node2=Node(temp2, temp, pos2, i, depth - 1, False, True)
                                   #Node1.children.append(Node2)

                   if int(i[1]) < 8:
                       pos1 = row[ind - 1] + str(int(i[1]) + 1)
                       if pos1 not in Sstate:
                         if pos1[0]=='A' or pos1 not in Cstate:
                           temp = list(copy.deepcopy(Cstate))
                           temp.remove(i)
                           temp.append(pos1)
                           temp = sorted(temp, cmp=func)
                           Node3=Node(Node1.sstate, temp, pos1, i, depth - 1, False, True)
                           #Node1.children.append(Node2)
                       else:
                           if ind > 1:
                               if int(i[1]) < 7:
                                 pos2 = row[ind - 2] + str(int(i[1]) + 2)
                                 if pos2 not in Sstate:
                                  if pos2[0]=='A' or pos2 not in Cstate:
                                   temp = list(copy.deepcopy(Cstate))
                                   temp.remove(i)
                                   temp.append(pos2)
                                   temp2 = list(copy.deepcopy(Sstate))
                                   temp2.remove(pos1)
                                   temp = sorted(temp, cmp=func)
                                   Node3=Node(temp2, temp, pos2, i, depth - 1, False, True)
                                   #Node1.children.append(Node2)

               if (Node3 is not None) and (Node2 is not None):
                 '''  
                 t = func(Node3.prev, Node2.prev)
                 if t > 0:
                   Node1.children.append(Node2)
                   Node1.children.append(Node3)
                 if t < 0:
                   Node1.children.append(Node3)
                   Node1.children.append(Node2)
                 if t == 0:
                 '''
                 t2 = func(Node3.present, Node2.present)
                 if t2 > 0:
                       Node1.children.append(Node2)
                       Node1.children.append(Node3)
                 if t2 < 0:
                       Node1.children.append(Node3)
                       Node1.children.append(Node2)
               else:
                 if Node2 is not None:
                   Node1.children.append(Node2)
                 if Node3 is not None:
                   Node1.children.append(Node3)

           if len(Node1.children)==0:
               if Node1.Pass == True:
                   Node2=Node(Node1.sstate, Node1.cstate, "PASS", Node1.present,depth-1,True,True)
                   Node1.children.append(Node2)
                   return Node1
               else:
                   Node2=Node(Node1.sstate,Node1.cstate,Node1.present,Node1.present,depth-1,True,True)
                   Node1.children.append(Node2)

       return Node1



def minmax(node1, depth,maxPlayer,index,star ):
    ind=""
    count=1
    if depth == 0 or node1.present == "PASS" or len(node1.sstate) == 0 or len(node1.cstate) == 0:
        leafnode.append(node1)
        return node1.utilityValue, index, count

    node1 = childrens(node1, star, depth)

    if maxPlayer is True:
        node1.value=(-1)*maxsize

        for i in range(0, len(node1.children)):
            child=node1.children[i]
            val,ind2,count2=minmax(child,depth-1,False,i,not star)
            count=count+count2
            if  val>node1.value:
                ind=i
            node1.value=max(node1.value,val)




        return node1.value, ind, count

    else:
        node1.value=maxsize
        for i in range(0,len(node1.children)):
            child=node1.children[i]
            val,ind2, count2=minmax(child, depth-1, True,i,not star)
            count=count+count2
            if val<node1.value:
                ind=i
            node1.value=min(node1.value,val)


        return node1.value,ind,count


def alphabeta(node1,depth,alpha,beta,maxPlayer,index,star):
    ind=""
    count=1
    if depth==0 or node1.present=="PASS" or len(node1.sstate)==0 or len(node1.cstate)==0:

        return node1.utilityValue, index,count

    node1 = childrens(node1, star, depth)



    if maxPlayer is True:
        for i in range(0, len(node1.children)):
            child=node1.children[i]
            val,ind2,count2=alphabeta(child,depth-1,alpha,beta,False,i,not star)
            count=count+count2
            if  val>alpha:
                ind=i
            alpha=max(alpha,val)

            if alpha>=beta:
                break




        return alpha, ind, count

    else:

        for i in range(0,len(node1.children)):
            child=node1.children[i]
            val,ind2, count2=alphabeta(child, depth-1,alpha,beta, True,i,not star)
            count=count+count2
            if val<beta:
                ind=i
            beta=min(beta,val)

            if alpha>=beta:
                break


        return beta,ind,count




counter=0

leafnode=[]
rows={7:'A',6:'B',5:'C',4:'D',3:'E',2:'F',1:'G',0:'H'}
path="/Users/anshuman786/Downloads/cases/"
h2=[]
h3=[]
algo=""
star=False
depth=0
star1={}
circle1={}
mainplayer=""
f=glob.glob(os.path.join(path, 'input*.txt'))
#print(len(f))
file=(open("input1.txt",'r')).readlines()

#print len(file),file[0],file[1],file[2]
weight=file[11].split(',')
algo=file[1].strip()

if file[0].strip()=="Star":
     star=True
else:
     star=False

if star is True:
    mainplayer="Star"
else:
    mainplayer="Circle"
depth=int(file[2])

matrix=file[3:-1]
for i in range(0,len(matrix)):
    line=matrix[i]
    line=line.split(",")
    #print(len(line))
    for j in range(0,len(line)):
        piece=line[j]
        if piece[0]=="S":
            num=int(piece[1])
            while num>0:
                row1=rows[i]
                row1=row1+str(j+1)
                h2.append(row1)
                num=num-1
        if piece[0]=="C":
            num=int(piece[1])
            while num>0:
                row1=rows[i]
                row1=row1+str(j+1)
                h3.append(row1)
                num=num-1


star1={'A':weight[0],
       'B':weight[1],
       'C':weight[2],
       'D':weight[3],
       'E':weight[4],
       'F':weight[5],
       'G':weight[6],
       'H':weight[7]}

circle1={'A':weight[7],
       'B':weight[6],
       'C':weight[5],
       'D':weight[4],
       'E':weight[3],
       'F':weight[2],
       'G':weight[1],
       'H':weight[0]}

h2=sorted(h2,cmp=func)
h3=sorted(h3,cmp=func)
 #print(h2,h3)
node = Node(h2, h3, "", "", depth, False, star)
 #print(star)
 #print type(algo),algo,len(algo)
if algo == "MINIMAX":
     val, ind, count = minmax(node, depth, True, 0, star)
 # print(node.children[0].present)

if algo == "ALPHABETA":
     val, ind, count = alphabeta(node, depth, -1 * maxsize, maxsize, True, 0, star)
 # print(node.children[0].present)
 #print ind

outputfile=open("output.txt","w")

if node.children[ind].Pass == True:
     #print "PASS"
     outputfile.write("pass"+'\n')
else:
     #print node.children[ind].prev, "-", node.children[ind].present
     outputfile.write(node.children[ind].prev+"-"+node.children[ind].present+'\n')


#print(node.children[ind].utilityValue, val, count)
outputfile.write(str(node.children[ind].utilityValue)+"\n")
outputfile.write(str(val)+'\n')
outputfile.write(str(count)+"\n")
child=node.children[0].children

#for i in child:
    #print i.prev+"-"+i.present
#child=node.children




'''

print(int(star1['A']))
h="G1"
print(int(h[1]))
h1=["H2","A1","C3","D5","D3","G7","G1","E3","E7","H1","H5"]
h1=sorted(h1,cmp=func)
i="G1"
h1.remove(i)
print(h1)
h1.insert(0,"G3")
h1=sorted(h1,cmp=func)
print(h1)
#h2=["C1","C3","C5","C7","B2","B4","B6","B8","A1","A3","A5","A7"]
#h3=["H2","H4","H6","H8","G1","G3","G5","G7","F2","F4","F6","F8"]
h2=["H1","H2","E8","D6"]
h3=["F8","E4","D3","A1","A2"]
#h2=["H2","H2","G1","E7","D6"]
#h3=["F8"]
depth=6
star=True
utilValue=0
node=Node(h2,h3,"","",depth,False,star)
#print len(node.children)
algo="ALPHABETA"
if algo=="MINMAX":
 val,ind,count=minmax(node,depth,True,0,star)
#print(node.children[0].present)

if algo=="ALPHABETA":
 val,ind,count=alphabeta(node,depth,-1*maxsize,maxsize,True,0,star)
#print(node.children[0].present)



if node.children[ind].Pass==True:
    print "PASS"
else:
    print node.children[ind].prev,"-",node.children[ind].present
print(node.children[ind].utilityValue,val,count)



#print(node.children[ind2].utilityValue,val2,count2)


#print(len(node.children[0].children))
'''
#for i in node.children:
 #print(i.value,i.utilityValue)
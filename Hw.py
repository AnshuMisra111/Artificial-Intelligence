from sys import maxsize

import copy


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
       if len(Sstate)>0:
        for i in Sstate:
           utilValue=utilValue+int(star1[i[0]])
       if len(Cstate)>0:
        for i in Cstate:
           utilValue=utilValue-int(circle1[i[0]])

       self.utilityValue=utilValue

       #print(self.prev," ",self.present)
       if self.depth==0 or self.present=="PASS" or len(Sstate)==0 or len(Cstate)==0:
           return


       if star is True:
           for i in Sstate:

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
                           self.children.append(Node(temp,self.cstate,pos1,i,self.depth-1,False,False))
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
                                   self.children.append(Node(temp, temp2, pos2, i, self.depth - 1, False, False))

                    if int(i[1])<8:
                       pos1=row[ind+1]+str(int(i[1])+1)

                       if pos1 not in Cstate:
                         if pos1[0]=='H' or pos1 not in Sstate:

                           temp = list(copy.deepcopy(Sstate))
                           temp.remove(i)
                           temp.append(pos1)
                           temp=sorted(temp,cmp=func)
                           self.children.append(Node(temp,self.cstate,pos1,i,self.depth-1,False,False))
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
                                   self.children.append(Node(temp, temp2, pos2, i, self.depth - 1, False, False))

           if len(self.children)==0:
               if self.Pass == True:
                   self.children.append(Node(self.sstate,self.cstate,"PASS",self.present,self.depth-1,True,False))
                   return
               else:
                   self.children.append(Node(self.sstate,self.cstate,self.present,self.present,self.depth-1,True,False))

       else:
           for i in Cstate:
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
                           self.children.append(Node(self.sstate,temp, pos1, i, self.depth - 1, False, True))

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
                                   self.children.append(Node(temp2, temp, pos2, i, self.depth - 1, False, True))

                   if int(i[1]) < 8:
                       pos1 = row[ind - 1] + str(int(i[1]) + 1)
                       if pos1 not in Sstate:
                         if pos1[0]=='A' or pos1 not in Cstate:
                           temp = list(copy.deepcopy(Cstate))
                           temp.remove(i)
                           temp.append(pos1)
                           temp = sorted(temp, cmp=func)
                           self.children.append(Node(self.sstate, temp, pos1, i, self.depth - 1, False, True))
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
                                   self.children.append(Node(temp2, temp, pos2, i, self.depth - 1, False, True))

           if len(self.children)==0:
               if self.Pass == True:
                   self.children.append(Node(self.sstate, self.cstate, "PASS", self.present,self.depth-1,True,True))
                   return
               else:
                   self.children.append(Node(self.sstate,self.cstate,self.present,self.present,self.depth-1,True,True))



def minmax(node1, depth,maxPlayer,index ):
    ind=""
    count=1
    if depth==0 or len(node1.children)==0:

        return node1.utilityValue, index,count

    if maxPlayer is True:
        node1.value=(-1)*maxsize

        for i in range(0, len(node1.children)):
            child=node1.children[i]
            val,ind2,count2=minmax(child,depth-1,False,i)
            count=count+count2
            if  val>node1.value:
                ind=ind2
            node1.value=max(node1.value,val)




        return node1.value, ind, count

    else:
        node1.value=maxsize
        for i in range(0,len(node1.children)):
            child=node1.children[i]
            val,ind2, count2=minmax(child, depth-1, True,i)
            count=count+count2
            if val<node1.value:
                ind=ind2
            node1.value=min(node1.value,val)


        return node1.value,ind,count


def alphabeta(node1,depth,alpha,beta,maxPlayer,index):
    ind=""
    count=1
    if depth==0 or len(node1.children)==0:

        return node1.utilityValue, index,count

    if maxPlayer is True:

        for i in range(0, len(node1.children)):
            child=node1.children[i]
            val,ind2,count2=alphabeta(child,depth-1,alpha,beta,False,i)
            count=count+count2
            if  val>alpha:
                ind=ind2
            alpha=max(alpha,val)

            if alpha>=beta:
                break




        return alpha, ind, count

    else:

        for i in range(0,len(node1.children)):
            child=node1.children[i]
            val,ind2, count2=alphabeta(child, depth-1,alpha,beta, True,i)
            count=count+count2
            if val<beta:
                ind=ind2
            beta=min(beta,val)

            if alpha>=beta:
                break


        return beta,ind,count





file=(open("/Users/anshuman786/Downloads/cases/input1.txt","r")).readlines()
print len(file)
weight=file[11].split(',')
print(weight[1])
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
utilValue=0
node=Node(h2,h3,"","",6,False,True)
val,ind,count=minmax(node,6,True,0)
#print(node.children[0].present)
val2,ind2,count2=alphabeta(node,6,-1*maxsize,maxsize,True,0)
#print(node.children[0].present)



if node.children[ind].Pass==True:
    print "PASS"
else:
    print node.children[ind].prev,"-",node.children[ind].present
print(node.children[ind].utilityValue,val,count)


print(node.children[ind2].utilityValue,val2,count2)

a=[1,2,3,4,5,6,7]
print(a[1:-1])
#print(len(node.children[0].children))



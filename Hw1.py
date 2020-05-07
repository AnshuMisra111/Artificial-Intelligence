class group:
    def __init__(self):
     self.teams=[]
     self.continents={"AFC":0,"CAF":0,"CONCACAF":0,"CONMEBOL":0,"OFC":0,"UEFA":0}
     self.potnumber=[]
     self.afc=0
     self.caf=0
     self.concacaf=0
     self.conmebol=0
     self.ofc=0
     self.uefa=0

def getlen(obj):
    return len(obj.teams)






def func(a,b):
 if len(a.teams)<len(b.teams):
  return a-b
 else:
  return b-a


def swap():
 t=0


file=(open("/Users/anshuman786/Downloads/input.txt",'r')).readlines()
gcount=int(file[0])
pcount=int(file[1])
#print gcount,pcount
dict={}
dict3={}
groupassigned={}
dict2={"AFC":0,"CAF":0,"OFC":0,"CONCACAF":0,"CONMEBOL":0,"UEFA":0}
pots=[]
groups=[]
flag=0
potcount=0
for i in range(2,2+pcount):
 potcount+=1
 pot=file[i].split("\n")[0]
 pot=pot.split("\r")[0]
 print pot
 pots.append(pot)
 pot=pot.split(",")
 #print(type(pot))
 if len(pot)>gcount:
  flag=1
  break
 for j in range(0,len(pot)):
  dict[str(pot[j])]=None
  dict3[str(pot[j])]=potcount


print len(dict),dict3
if flag==1:
 print "No"
else:
 for i in range(2+pcount,8+pcount):
  data=file[i].split("\r")[0]
  data=data.split("\n")[0]
  data=data.split(":")
  #print data[0]
  countries=data[1].split(",")
 #print(countries)
  for j in countries:
   if j!="None":
    dict2[str(data[0])]+=1
    dict[str(j)]=str(data[0])



 #print dict
 for i in dict2:
  if i is "UEFA":
   if dict2[i]>(2*gcount):
    flag=1
    break
  else:
   if dict2[i]>gcount:
    flag=1
    break



 if flag==1:
  print "No"
 else:
  #print dict
  for i in range(0,gcount):
     grp=group()
     groups.append(grp)
     #groups=sorted(groups,key=getlen)
  for pot in pots:
    pot=pot.split(",")
    for country in pot:
     #groups = sorted(groups, key=getlen)
     placed=0
     #print country
     for j in range(0, len(groups)):
      #if placed==1:
       #break
      #print country
      grp=groups[j]

      continent=dict[str(country)]
      number=dict3[str(country)]
      print(len(grp.teams), country,grp.continents,grp.potnumber,continent,number,grp.teams)
      #print continent, number
      #print(grp.potnumber, grp.teams)
      if number not in grp.potnumber:
       if continent=="UEFA":
        #print "came here1 ", country
        if grp.continents[continent]<2:
         #print "came here2 ", country
         placed=1
         grp.teams.append(country)
         grp.potnumber.append(number)
         grp.continents[continent]+=1
         groupassigned[country]=j
         #groups = sorted(groups, key=getlen)
         #print len(groups)
         break
       else:
        #print "came here ",country
        #print continent
        if grp.continents[continent] < 1:
         #print "came here ", country
         placed=1
         grp.teams.append(country)
         grp.potnumber.append(number)
         grp.continents[continent] += 1
         groupassigned[country]=j
         #if country=="Australia":
         #print j, groups[j].teams
         #groups = sorted(groups,key=getlen)
         #print len(groups)
         break


     if placed==0:
      #print country
      for j in range(0,len(groups)):
       grp=groups[j]
       continent = dict[str(country)]
       number = dict3[str(country)]
       if number not in grp.potnumber:
        for country2 in pot:
         #print country2
         if country2==country:
           break
         index=groupassigned[country2]
         continent2=dict[str(country2)]
         group3=groups[index]
         print group3.teams,index,country2
         if continent2 != continent:
          if continent=="UEFA":
           if group3.continents[continent]<2:
              if grp.continents[continent2]<1:
               group3.continents[continent2]-=1
               group3.continents[continent]+=1
               group3.teams.remove(country2)
               group3.teams.append(country)
               grp.continents[continent2]+=1
               grp.teams.append(country2)
               groupassigned[country2]=j
               groupassigned[country]=index
               grp.potnumber.append(number)
               placed=1
               break
          else:
            if group3.continents[continent]<1:
             if continent2=="UEFA":
              if grp.continents[continent2]<2:
               group3.continents[continent2] -= 1
               group3.continents[continent] += 1
               group3.teams.remove(country2)
               group3.teams.append(country)
               grp.continents[continent2] += 1
               grp.teams.append(country2)
               groupassigned[country2] = j
               groupassigned[country] = index
               grp.potnumber.append(number)
               placed = 1
               break
             else:
              if grp.continents[continent2]<1:
               group3.continents[continent2] -= 1
               group3.continents[continent] += 1
               #print groups[index].teams
               #print country2, group3.teams,continent,continent2,group3.continents
               group3.teams.remove(country2)
               group3.teams.append(country)
               grp.continents[continent2] += 1
               grp.teams.append(country2)
               groupassigned[country2] = j
               groupassigned[country] = index
               grp.potnumber.append(number)
               placed = 1
               break
       if placed==1:
          break


      if placed==0:
       print country
       flag=1
       break

    if flag==1:
     break

  if flag==1:
   print "Reached here " "No"
  else:
   for i in range(0,len(groups)):
    print groups[i].teams
    #for team in groups[i].teams:
     #print dict[team],dict3[team]


#print(dict)
#print(pots)
#print(dict3)
import copy








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


def swap(group1,group2,country1,country2):
  continent=dict[country1]
  continent2=dict[country2]
  newgroup1=group()
  newgroup1.teams=copy.deepcopy(group1.teams)
  #newgroup1.continents=copy.deepcopy(group1.continents)
  #newgroup1.potnumber=copy.deepcopy(group1.potnumber)
  newgroup2=group()
  newgroup2.teams=copy.deepcopy(group2.teams)
  #newgroup2.continents=copy.deepcopy(group2.continents)
  #newgroup2.potnumber=copy.deepcopy(group2.potnumber)
  g1continent={"AFC":[],"CAF":[],"OFC":[],"CONCACAF":[],"CONMEBOL":[],"UEFA":[]}
  g2continent={"AFC":[],"CAF":[],"OFC":[],"CONCACAF":[],"CONMEBOL":[],"UEFA":[]}
  g1pot={}
  g2pot={}
  for i in range(0,pcount):
   g1pot[i+1]=[]
   g2pot[i+1]=[]

  for country in group1.teams:
   g1continent[dict[country]].append(country)
   g1pot[dict3[country]].append(country)

  for country in group2.teams:
   g2continent[dict[country]].append(country)
   g2pot[dict3[country]].append(country)

  #print "g1pot= ",g1pot
  #print "g2pot= ", g2pot
  #print "g1continent= ",g1continent
  #print "g2continent= ", g2continent
  counter=0
  finalvalue=len(group1.teams)+len(group2.teams)+2
  #print newgroup1.continents[continent2]
  country3=None
  for team in group1.teams:
      if dict[team]==continent2:
        country3=team
        break

  #print "country3= ",country3,country2
  newgroup2.teams.append(country3)
  newgroup2.teams.remove(country2)
  #print "group2= ",group2.teams
  #print "new group= ",newgroup2.teams
  newgroup2.teams.append(country1)

  newgroup1.teams.remove(country3)
  newgroup1.teams.append(country2)
  #print "group1= ",group1.teams
  #print "new group1= ",newgroup1.teams
  #print "new group= ", newgroup2.teams
  #print "g2pot= ",g2pot
  #print "g2continent= ",g2continent
  #print country2 in g2continent[dict[country2]],country2
  #index=g2continent[dict[country2]].index(country2)

  g2continent[dict[country2]].remove(country2)
  g2continent[dict[country3]].append(country3)
  g2continent[dict[country1]].append(country1)
  #del g2continent[dict[country2]][index]

  #print len(g2continent[dict[country]].append(country))

  g2pot[dict3[country3]].append(country3)
  g2pot[dict3[country1]].append(country1)
  g2pot[dict3[country2]].remove(country2)

  #print "g1pot= ",g1pot
  #print "g1continent= ",g1continent

  g1continent[dict[country3]].remove(country3)
  g1continent[dict[country2]].append(country2)

  g1pot[dict3[country3]].remove(country3)
  g1pot[dict3[country2]].append(country2)

  #print "g1pot= ", g1pot
  #print "g1continent= ", g1continent
  #print "g2pot= ", g2pot
  #print "g2continent= ", g2continent

  flag1=1

  newgroup1, newgroup2, g1pot, g1continent, g2pot, g2continent, newplace=swap2(newgroup1,newgroup2,g1pot,g1continent,g2pot,g2continent,counter,finalvalue,flag1,country3)
  if newplace==1:

   for key in g1continent:
    if len(g1continent[key])>0:
     newgroup1.continents[key]=len(g1continent[key])
   pot_list=[]
   for key in g1pot:
     if len(g1pot[key])>0:
      pot_list.append(key)

   newgroup1.potnumber=pot_list

   for key in g2continent:
    if len(g2continent[key])>0:
     newgroup2.continents[key]=len(g2continent[key])
   pot_list=[]
   for key in g2pot:
     if len(g2pot[key])>0:
      pot_list.append(key)

   newgroup2.potnumber=pot_list
   #print "newgroup1= ",newgroup1.teams, newgroup1.continents,newgroup1.potnumber
   #print "newgroup2= ", newgroup2.teams, newgroup2.continents, newgroup2.potnumber

   return newgroup1,newgroup2,newplace

  else:
   return newgroup1,newgroup2,newplace

#flag=1 is for removal from g2 and flag=0 is for removal from g1
def swap2(newgroup1,newgroup2,g1pot,g1continent,g2pot,g2continent,counter,finalvalue,flag1,countryadded):
  counter+=1
  newplace=1
  if counter>=finalvalue:
   return newgroup1,newgroup2,g1pot,g1continent,g2pot,g2continent,0

  if flag1==1:
   if(len(g2pot[dict3[countryadded]])>1):
    #print "came here 1", countryadded
    newcountry=g2pot[dict3[countryadded]][0]
    #print newcountry
    newgroup2.teams.remove(newcountry)
    newgroup1.teams.append(newcountry)
    g2pot[dict3[newcountry]].remove(newcountry)
    g2continent[dict[newcountry]].remove(newcountry)
    g1pot[dict3[newcountry]].append(newcountry)
    g1continent[dict[newcountry]].append(newcountry)
    #print "g1pot= ",g1pot
    #print "g1continent= ",g1continent
    #print "g2pot= ",g2pot
    #print "g2continent= ",g2continent
    newgroup1, newgroup2, g1pot, g1continent, g2pot, g2continent, newplace=swap2(newgroup1, newgroup2, g1pot, g1continent, g2pot, g2continent, counter, finalvalue, 0, newcountry)
   if dict[countryadded] == "UEFA":
    if len(g2continent[dict[countryadded]]) > 2:
     #print "came here 2"
     newcountry = g2continent[dict[countryadded]][0]
     newgroup2.teams.remove(newcountry)
     newgroup1.teams.append(newcountry)
     g2pot[dict3[newcountry]].remove(newcountry)
     g1pot[dict3[newcountry]].append(newcountry)
     g2continent[dict[newcountry]].remove(newcountry)
     g1continent[dict[newcountry]].append(newcountry)
     newgroup1, newgroup2, g1pot, g1continent, g2pot, g2continent, newplace=swap2(newgroup1, newgroup2, g1pot, g1continent, g2pot, g2continent, counter, finalvalue, 0, newcountry)
   else:
    if len(g2continent[dict[countryadded]]) > 1:
     #print "came here 3"
     newcountry = g2continent[dict[countryadded]][0]
     newgroup2.teams.remove(newcountry)
     newgroup1.teams.append(newcountry)
     g2pot[dict3[newcountry]].remove(newcountry)
     g1pot[dict3[newcountry]].append(newcountry)
     g2continent[dict[newcountry]].remove(newcountry)
     g1continent[dict[newcountry]].append(newcountry)
     newgroup1, newgroup2, g1pot, g1continent, g2pot, g2continent, newplace=swap2(newgroup1, newgroup2, g1pot, g1continent, g2pot, g2continent, counter, finalvalue, 0, newcountry)

  if flag1==0:
    if (len(g1pot[dict3[countryadded]]) > 1):
      #print "came here 4"
      newcountry = g1pot[dict3[countryadded]][0]
      newgroup1.teams.remove(newcountry)
      newgroup2.teams.append(newcountry)
      g1pot[dict3[newcountry]].remove(newcountry)
      g2pot[dict3[newcountry]].append(newcountry)
      g1continent[dict[newcountry]].remove(newcountry)
      g2continent[dict[newcountry]].append(newcountry)
      newgroup1, newgroup2, g1pot, g1continent, g2pot, g2continent, newplace=swap2(newgroup1, newgroup2, g1pot, g1continent, g2pot, g2continent, counter, finalvalue, 1, newcountry)

    if dict[countryadded]=="UEFA":
     if len(g1continent[dict[countryadded]])>2:
      #print "came here 5"
      newcountry=g1continent[dict[countryadded]][0]
      newgroup1.teams.remove(newcountry)
      newgroup2.teams.append(newcountry)
      g1pot[dict3[newcountry]].remove(newcountry)
      g2pot[dict3[newcountry]].append(newcountry)
      g1continent[dict[newcountry]].remove(newcountry)
      g2continent[dict[newcountry]].append(newcountry)
      newgroup1, newgroup2, g1pot, g1continent, g2pot, g2continent, newplace=swap2(newgroup1, newgroup2, g1pot, g1continent, g2pot, g2continent, counter, finalvalue, 1, newcountry)
    else:
     if len(g1continent[dict[countryadded]]) > 1:
      #print "came here 6", countryadded
      newcountry = g1continent[dict[countryadded]][0]
      #print newcountry
      newgroup1.teams.remove(newcountry)
      newgroup2.teams.append(newcountry)
      g1pot[dict3[newcountry]].remove(newcountry)
      g2pot[dict3[newcountry]].append(newcountry)
      g1continent[dict[newcountry]].remove(newcountry)
      g2continent[dict[newcountry]].append(newcountry)
      #print "g1pot= ", g1pot
      #print "g1continent= ", g1continent
      #print "g2pot= ", g2pot
      #print "g2continent= ", g2continent
      newgroup1, newgroup2, g1pot, g1continent, g2pot, g2continent, newplace=swap2(newgroup1, newgroup2, g1pot, g1continent, g2pot, g2continent, counter, finalvalue, 1, newcountry)


  if newplace==1:
   return newgroup1,newgroup2,g1pot,g1continent,g2pot,g2continent,1
  else:
   return newgroup1,newgroup2,g1pot,g1continent,g2pot,g2continent,0

#file=(open("/Users/anshuman786/Downloads/Sample_test_cases/input.txt",'r')).readlines()
#file=(open("input.txt",'r')).readlines()
file=(open("/Users/anshuman786/Downloads/CS561_HW2_grading_test_cases/5.txt",'r')).readlines()
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
 #print pot
 pots.append(pot)
 pot=pot.split(",")
 #print(type(pot))
 if len(pot)>gcount:
  flag=1
  break
 for j in range(0,len(pot)):
  dict[str(pot[j])]=None
  dict3[str(pot[j])]=potcount

outputfile=open("output.txt","w")

if flag==1:
 #print "No"
 outputfile.write("No"+'\n')
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
  #print "No"
  outputfile.write("No" + '\n')
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
      #print(len(grp.teams), country,grp.continents,grp.potnumber,continent,number,grp.teams)
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
         #print group3.teams,index,country2
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

       for j in range(0,len(groups)):
        #print j

        grp=groups[j]
        continent = dict[str(country)]
        number = dict3[str(country)]
        if number not in grp.potnumber:
         for country2 in pot:
          # print country2
          if country2 == country:
             break
          index = groupassigned[country2]
          continent2 = dict[str(country2)]
          #print "Came here", country,country2,number,index,j
          group3 = groups[index]
          if continent2 != continent:
            if grp.continents[continent2]>0:
             if continent=="UEFA":
              #print "Came here", country, country2, number, index, j
              if group3.continents[continent]<2:
               newgroup1,newgroup2,placed=swap(grp,group3,country,country2)
             else:
              #print "Came here 1", country, country2, number, index, j
              if group3.continents[continent]==0:
               newgroup1, newgroup2,placed=swap(grp,group3,country,country2)
               #print newgroup1.teams,newgroup2.teams
          if placed==1:
           groups[j]=newgroup1
           groups[index]=newgroup2
           for team in newgroup1.teams:
            groupassigned[team]=j
           for team in newgroup2.teams:
            groupassigned[team]=index
           break
         if placed==1:
             break

       if placed==0:

        #print country
        flag=1
        break

    if flag==1:
     break

  if flag==1:
   #for i in range(0,len(groups)):
    #print groups[i].teams,groups[i].potnumber,groups[i].continents
   #print "Reached here " "No"
   outputfile.write("No" + '\n')
  else:
   outputfile.write("Yes" + "\n")
   #print("came here")
   for i in range(0,len(groups)):

    print groups[i].teams,groups[i].continents,groups[i].potnumber
    #outputfile.write(groups[i].teams)
    '''
    for k in range(0,len(groups[i].teams)):
        if k==len(groups[i].teams)-1:
            outputfile.write(groups[i].teams[k]+"\n")
        else:
            outputfile.write(groups[i].teams[k]+",")
    '''
    #outputfile.write("\n")
    #for team in groups[i].teams:
     #print dict[team],dict3[team]


#print(dict)
#print(pots)
#print(dict3)
import xml.etree.ElementTree as ET
import numpy as np

allin=list()
subin=list()

#country_node=list()
company_node=list()
artist_node=list()
year_node=list()
title_node=list()
price_node=list()

word_cnt=dict()
findcompany=list()
findartist=list()
findyear=list()
x=list()
y=list()

def wordPositions(findword,lst,biglst):
 res_list=[k for k, value in enumerate(lst) if value==findword]
 for i in range(len(res_list)):
  print(biglst[res_list[i]])

def childPositions(findword,lst,onlst,biglst):
 if len(lst)==len(onlst):
  for j in range(len(lst)):
   print(biglst[lst[j]])
 else:
  x=list(set(onlst)-set(lst))
  y=list(set(onlst)-set(x))
  for i in range(len(y)):
   print(biglst[y[i]])
   


class CATALOG:
 def __init__(self,word_cnt,findcompany,findartist,findyear):
  self.word_cnt=word_cnt.clear()
  self.findcompany=findcompany
  self.findartist=findartist
  self.findyear=findyear
  self.x=x
  self.y=y
  
 def ShowInfo():
  for word in xmlcountry: 
   if word not in word_cnt.keys(): 
    word_cnt[word] = 1 
   else: 
    word_cnt[word] += 1
  print("COUNTRY : ")
  print(word_cnt)
  print("\n")
  word_cnt.clear()
  
  for word in xmlcompany: 
   if word not in word_cnt.keys(): 
    word_cnt[word] = 1 
   else: 
    word_cnt[word] += 1
  print("COMPANY : ")
  print(word_cnt)
  print("\n")
  word_cnt.clear()
  
  for word in xmlartist: 
   if word not in word_cnt.keys(): 
    word_cnt[word] = 1 
   else: 
    word_cnt[word] += 1
  print("ARTIST : ")
  print(word_cnt)
  print("\n")
  word_cnt.clear()
  
  for word in xmlyear: 
   if word not in word_cnt.keys(): 
    word_cnt[word] = 1 
   else: 
    word_cnt[word] += 1
  print("YEAR : ")
  print(word_cnt)
  print("\n")
  word_cnt.clear()
  
  for word in xmltitle: 
   if word not in word_cnt.keys(): 
    word_cnt[word] = 1 
   else: 
    word_cnt[word] += 1
  print("TITLE : ")
  print(word_cnt)
  print("\n")
  word_cnt.clear()
  
  for word in xmlprice: 
   if word not in word_cnt.keys(): 
    word_cnt[word] = 1 
   else: 
    word_cnt[word] += 1
  print("PRICE : ")
  print(word_cnt)
  print("\n")
  word_cnt.clear()
   
  
 def Classify():
  for word in xmlcountry: 
   if word not in word_cnt.keys(): 
    word_cnt[word] = 1 
   else: 
    word_cnt[word] += 1
  print(word_cnt)
  word_cnt.clear()
  
  clsf_country=input("나라 태그 : ")
  for i in range(len(country)):
   if clsf_country==country[i]:
    choose_country=country[i]
    wordPositions(country[i],xmlcountry,xmllist)
    con_list=[i for i, value in enumerate(xmlcountry) if value==choose_country]
    #print(con_list)
    for j in range(len(con_list)):
     findcompany.append(xmlcompany[con_list[j]])
    for word in findcompany: 
     if word not in word_cnt.keys(): 
      word_cnt[word] = 1 
     else: 
      word_cnt[word] += 1
    if j < len(con_list)-1:
     word_cnt.clear()
    print(word_cnt)
    word_cnt.clear()

    

    clsf_company=input("회사 태그 : ")
    for i in range(len(company)):
     if clsf_company==company[i]:
      choose_company=company[i]
      com_list=[i for i, value in enumerate(xmlcompany) if value==choose_company]
      if len(con_list)==len(com_list):
       com_list=com_list
       #print(com_list)
      else:
       x=list(set(con_list)-set(com_list))
       y=list(set(con_list)-set(x))
       com_list=y
       #print(com_list)
      childPositions(company[i],com_list,con_list,xmllist)

      for j in range(len(com_list)):
       findartist.append(xmlartist[com_list[j]])
      for word in findartist: 
       if word not in word_cnt.keys(): 
        word_cnt[word] = 1 
       else: 
        word_cnt[word] += 1
      if j < len(com_list)-1:
       word_cnt.clear()
      print(word_cnt)
      word_cnt.clear()
      
      clsf_artist=input("가수 태그 : ")
      for i in range(len(artist)):
       if clsf_artist==artist[i]:
        choose_artist=artist[i]
        art_list=[i for i, value in enumerate(xmlartist) if value==choose_artist]
        if len(com_list)==len(art_list):
         art_list=art_list
         #print(art_list)
        else:
         x=list(set(com_list)-set(art_list))
         y=list(set(com_list)-set(x))
         art_list=y
         #print(art_list)
        childPositions(artist[i],art_list,com_list,xmllist)
        for j in range(len(art_list)):
         findyear.append(xmlyear[art_list[j]])
        for word in findyear: 
         if word not in word_cnt.keys(): 
          word_cnt[word] = 1
         else:
          word_cnt[word] += 1
        if j < len(art_list)-1:
         word_cnt.clear()
        print(word_cnt)
        word_cnt.clear()
        
        clsf_year=input("연도 태그 : ")
        for j in range(len(year)):
         if clsf_year==year[j]:
          choose_year=year[j]
          yea_list=[i for i, value in enumerate(xmlyear) if value==choose_year]
          if len(art_list)==len(yea_list):
           yea_list=yea_list
           #print(yea_list)
          else:
           x=list(set(art_list)-set(yea_list))
           y=list(set(art_list)-set(x))
           yea_list=y
           #print(yea_list)
          childPositions(year[j],yea_list,art_list,xmllist)




findsome="<CD>"
count=0
findproblem=0

xmlcountry=list()
xmlcompany=list()
xmlartist=list()
xmlyear=list()
xmltitle=list()
xmlprice=list()
xmllist=list()

tree = ET.parse("./example.xml")
root=tree.getroot()
file_read=open("./example.xml","r")

while True:
 f_line = file_read.readline()
 if not f_line:
  break
 raw=f_line.split()
 
 if count>=findproblem:
  if findsome in f_line:
   count=count+1

for element in root.findall("CD"):
 xmlcountry.append(element.find("COUNTRY").text)
 xmlcompany.append(element.find("COMPANY").text)
 xmlartist.append(element.find("ARTIST").text)
 xmlyear.append(element.find("YEAR").text)
 xmltitle.append(element.find("TITLE").text)
 xmlprice.append(element.find("PRICE").text)

country=set(xmlcountry)
country=list(country)
company=set(xmlcompany)
company=list(company)
artist=set(xmlartist)
artist=list(artist)
year=set(xmlyear)
year=list(year)
title=set(xmltitle)
title=list(title)
price=set(xmlprice)
price=list(price)


for i in range(0,count):
 xmllist.append("COUNTRY : "+xmlcountry[i]+"\n"+"COMPANY : "+xmlcompany[i]+"\n"+"ARTIST : "+xmlartist[i]+"\n"+"YEAR : "+xmlyear[i]+"\n"+"TITLE : "+xmltitle[i]+"\n"+"PRICE : "+xmlprice[i])


print(country)
CATALOG.ShowInfo()
CATALOG.Classify()



import xml.etree.ElementTree as ET
import numpy as np
import os
import sys

mode_num=0
readcount=0
findsome="<CD>"
findproblem=0
title_list=list()
artist_list=list()
country_list=list()
company_list=list()
price_list=list()
year_list=list()

xmlcountry=list()
xmlcompany=list()
xmlartist=list()
xmlyear=list()
xmltitle=list()
xmlprice=list()
xmllist=list()

outflag=0
printflag=1

def wordPositions(findword,lst,biglst):
 res_list=[k for k, value in enumerate(lst) if value==findword]
 for u in range(len(res_list)):
  print("\n"+biglst[res_list[u]])

def indent(elem, level=0):
 i = "\n" + level*" "
 if len(elem):
  if not elem.text or not elem.text.strip():
   elem.text = i + " "
  if not elem.tail or not elem.tail.strip():
   elem.tail = i
  for elem in elem:
   indent(elem, level+1)
  if not elem.tail or not elem.tail.strip():
   elem.tail = i
 else:
  if level and (not elem.tail or not elem.tail.strip()):
   elem.tail = i

Lfilename="./example.xml"
tree=ET.parse(Lfilename)
root=tree.getroot()
file_read=open(Lfilename,"r")

while True:
 f_line = file_read.readline()
 if not f_line:
  break
 raw=f_line.split()
 
 if readcount>=findproblem:
  if findsome in f_line:
   readcount=readcount+1

for element in root.findall("CD"):
 xmlcountry.append(element.find("COUNTRY").text)
 xmlcompany.append(element.find("COMPANY").text)
 xmlartist.append(element.find("ARTIST").text)
 xmlyear.append(element.find("YEAR").text)
 xmltitle.append(element.find("TITLE").text)
 xmlprice.append(element.find("PRICE").text)

Scountry=set(xmlcountry)
Scountry=list(Scountry)
Scompany=set(xmlcompany)
Scompany=list(Scompany)
Sartist=set(xmlartist)
Sartist=list(Sartist)
Syear=set(xmlyear)
Syear=list(Syear)
Stitle=set(xmltitle)
Stitle=list(Stitle)
Sprice=set(xmlprice)
Sprice=list(Sprice)

for i in range(0,readcount):
 xmllist.append("COUNTRY : "+xmlcountry[i]+"\n"+"COMPANY : "+xmlcompany[i]+"\n"+"ARTIST : "+xmlartist[i]+"\n"+"YEAR : "+xmlyear[i]+"\n"+"TITLE : "+xmltitle[i]+"\n"+"PRICE : "+xmlprice[i])

while True:
 if mode_num==0:
  mode_num=int(input("사용할 모드 설정(1:xml 정보 추가  2:xml 정보 수정  3:xml 정보 삭제  4:종료)\n"))

 elif mode_num==1:
  #추가부분
  while True:
   title=input("TITLE : ")
   artist=input("ARTIST : ")
   country=input("COUNTRY : ")
   company=input("COMPANY : ")
   price=float(input("PRICE (float): "))
   year=int(input("YEAR (int): "))
 
   title_list.append(title)
   artist_list.append(artist)
   country_list.append(country)
   company_list.append(company)
   price_list.append(price)
   year_list.append(year)

   cd=ET.SubElement(root,"CD")
   ET.SubElement(cd,"TITLE").text=title
   ET.SubElement(cd,"ARTIST").text=artist
   ET.SubElement(cd,"COUNTRY").text=country
   ET.SubElement(cd,"COMPANY").text=company
   ET.SubElement(cd,"PRICE").text=str(price)
   ET.SubElement(cd,"YEAR").text=str(year)
 
   again=input("추가 정보 입력? y/n\n")
   if again=="Y" or again=="y":
    pass
   elif again=="N" or again=="n":
    print("정보 입력 종료")
    mode_num=4
    indent(root)
    ET.dump(root)
    tree=ET.ElementTree(root)
    tree.write(Lfilename+"_Add"+".xml")
    break
   else:
    break

 elif mode_num==2:
  #수정부분
  #값이 있는 태그 찾고 값을 찾은 후 그 값 새로운 값으로 대체
  tagword=["country","COUNTRY","company","COMPANY","artist","ARTIST","year","YEAR","title","TITLE","price","PRICE"]
  listword=[xmlcountry,xmlcountry,xmlcompany,xmlcompany,xmlartist,xmlartist,xmlyear,xmlyear,xmltitle,xmltitle,xmlprice,xmlprice]
  Sword=[Scountry,Scountry,Scompany,Scompany,Sartist,Sartist,Syear,Syear,Stitle,Stitle,Sprice,Sprice]
  print("\n[COUNTRY, COMPANY, ARTIST, YEAR, TITLE, PRICE]")
  while True:
   paint=input("\n검색할 태그 : ")
   if paint in tagword:
    break
   else:
    print("입력 오류 : 태그를 찾을 수 없습니다")
  for word in range(0,len(tagword),2):
   if paint==tagword[word] or paint==tagword[word+1]:
    print(Sword[word])
    while True:
     Position=input("\n검색 값 : ")
     if Position in Sword[word]:
      break
     else:
      print("입력 오류 : 태그를 찾을 수 없습니다 (대소문자, 띄어쓰기 구분)")
    for j in range(len(Sword[word])):
     if Position==Sword[word][j]:
      wordPositions(Sword[word][j],listword[word],xmllist)
      tag_list=[z for z, value in enumerate(listword[word]) if value==Sword[word][j]]
    while True:
     Findtag=int(input("\n수정할 정보(Number) : "))
     if (str(type(Findtag))=="<class 'int'>"):
      if Findtag <= len(tag_list):
       break
      else:
       print("입력 오류 : 입력 범위 오류 1 ~",len(tag_list))
     else:
      print("입력 오류 : 정수로 입력해 주시기 바랍니다")
    print(xmllist[tag_list[Findtag-1]])
  
    while True:
     Fixtag=input("\n수정할 태그(영어) : ")
     if Fixtag not in tagword:
      print("입력 오류 : 태그를 찾을 수 없습니다")
     else:
      break
    if Fixtag=="COUNTRY" or Fixtag=="country":
     print(xmlcountry[tag_list[Findtag-1]])
     FixVal=input("\n수정할 값 : ")
     xmlcountry[tag_list[Findtag-1]]=FixVal
     xmllist=list()
     for i in range(0,readcount):
      xmllist.append("COUNTRY : "+xmlcountry[i]+"\n"+"COMPANY : "+xmlcompany[i]+"\n"+"ARTIST : "+xmlartist[i]+"\n"+"YEAR : "+xmlyear[i]+"\n"+"TITLE : "+xmltitle[i]+"\n"+"PRICE : "+xmlprice[i])
     print(xmllist[tag_list[Findtag-1]])
     print(root[tag_list[Findtag-1]][2].text)
     root[tag_list[Findtag-1]][2].text=xmlcountry[tag_list[Findtag-1]]
     indent(root)
     ET.dump(root)
     tree=ET.ElementTree(root)
     tree.write(Lfilename+"_Fix"+".xml")
     mode_num=4
   
    elif Fixtag=="COMPANY" or Fixtag=="company":
     print(xmlcompany[tag_list[Findtag-1]])
     FixVal=input("\n수정할 값 : ")
     xmlcompany[tag_list[Findtag-1]]=FixVal
     xmllist=list()
     for i in range(0,readcount):
      xmllist.append("COUNTRY : "+xmlcountry[i]+"\n"+"COMPANY : "+xmlcompany[i]+"\n"+"ARTIST : "+xmlartist[i]+"\n"+"YEAR : "+xmlyear[i]+"\n"+"TITLE : "+xmltitle[i]+"\n"+"PRICE : "+xmlprice[i])
     print(xmllist[tag_list[Findtag-1]])
     root[tag_list[Findtag-1]][3].text=xmlcompany[tag_list[Findtag-1]]
     indent(root)
     ET.dump(root)
     tree=ET.ElementTree(root)
     tree.write(Lfilename+"_Fix"+".xml")
     mode_num=4
     
    elif Fixtag=="ARTIST" or Fixtag=="artist":
     print(xmlartist[tag_list[Findtag-1]])
     FixVal=input("\n수정할 값 : ")
     xmlartist[tag_list[Findtag-1]]=FixVal
     xmllist=list()
     for i in range(0,readcount):
      xmllist.append("COUNTRY : "+xmlcountry[i]+"\n"+"COMPANY : "+xmlcompany[i]+"\n"+"ARTIST : "+xmlartist[i]+"\n"+"YEAR : "+xmlyear[i]+"\n"+"TITLE : "+xmltitle[i]+"\n"+"PRICE : "+xmlprice[i])
     print(xmllist[tag_list[Findtag-1]])
     root[tag_list[Findtag-1]][1].text=xmlartist[tag_list[Findtag-1]]
     indent(root)
     ET.dump(root)
     tree=ET.ElementTree(root)
     tree.write(Lfilename+"_Fix"+".xml")
     mode_num=4
    
    elif Fixtag=="YEAR" or Fixtag=="year":
     print(xmlyear[tag_list[Findtag-1]])
     #오류 출현 필요
     while True:
      FixVal=int(input("\n수정할 값 : "))
      if (str(type(FixVal))=="<class 'int'>"):
       break
      else:
       print("입력 오류 : 정수로 입력해 주시기 바랍니다")
     xmlyear[tag_list[Findtag-1]]=str(FixVal)
     xmllist=list()
     for i in range(0,readcount):
      xmllist.append("COUNTRY : "+xmlcountry[i]+"\n"+"COMPANY : "+xmlcompany[i]+"\n"+"ARTIST : "+xmlartist[i]+"\n"+"YEAR : "+xmlyear[i]+"\n"+"TITLE : "+xmltitle[i]+"\n"+"PRICE : "+xmlprice[i])
     print(xmllist[tag_list[Findtag-1]])
     root[tag_list[Findtag-1]][5].text=xmlyear[tag_list[Findtag-1]]
     indent(root)
     ET.dump(root)
     tree=ET.ElementTree(root)
     tree.write(Lfilename+"_Fix"+".xml")
     mode_num=4
   
    elif Fixtag=="TITLE" or Fixtag=="title":
     print(xmltitle[tag_list[Findtag-1]])
     FixVal=input("\n수정할 값 : ")
     xmltitle[tag_list[Findtag-1]]=FixVal
     xmllist=list()
     for i in range(0,readcount):
      xmllist.append("COUNTRY : "+xmlcountry[i]+"\n"+"COMPANY : "+xmlcompany[i]+"\n"+"ARTIST : "+xmlartist[i]+"\n"+"YEAR : "+xmlyear[i]+"\n"+"TITLE : "+xmltitle[i]+"\n"+"PRICE : "+xmlprice[i])
     print(xmllist[tag_list[Findtag-1]])
     root[tag_list[Findtag-1]][0].text=xmltitle[tag_list[Findtag-1]]
     indent(root)
     ET.dump(root)
     tree=ET.ElementTree(root)
     tree.write(Lfilename+"_Fix"+".xml")
     mode_num=4
   
    elif Fixtag=="PRICE" or Fixtag=="price":
     print(xmlprice[tag_list[Findtag-1]])
     while True:
      FixVal=float(input("\n수정할 값 : "))
      if (str(type(FixVal))=="<class 'int'>") or (str(type(FixVal))=="<class 'float'>"):
       break
      else:
       print("입력 오류 : 실수로 입력해 주시기 바랍니다")
     xmlprice[tag_list[Findtag-1]]=str(FixVal)
     xmllist=list()
     for i in range(0,readcount):
      xmllist.append("COUNTRY : "+xmlcountry[i]+"\n"+"COMPANY : "+xmlcompany[i]+"\n"+"ARTIST : "+xmlartist[i]+"\n"+"YEAR : "+xmlyear[i]+"\n"+"TITLE : "+xmltitle[i]+"\n"+"PRICE : "+xmlprice[i])
     print(xmllist[tag_list[Findtag-1]])
     root[tag_list[Findtag-1]][4].text=xmlprice[tag_list[Findtag-1]]
     indent(root)
     ET.dump(root)
     tree=ET.ElementTree(root)
     tree.write(Lfilename+"_Fix"+".xml")
     mode_num=4
  
 elif mode_num==3:
  #삭제부분
  #삭제할 값이 포함된 부분 찾아서 덩어리째로 삭제/제외(?)
  tagword=["country","COUNTRY","company","COMPANY","artist","ARTIST","year","YEAR","title","TITLE","price","PRICE"]
  listword=[xmlcountry,xmlcountry,xmlcompany,xmlcompany,xmlartist,xmlartist,xmlyear,xmlyear,xmltitle,xmltitle,xmlprice,xmlprice]
  Sword=[Scountry,Scountry,Scompany,Scompany,Sartist,Sartist,Syear,Syear,Stitle,Stitle,Sprice,Sprice]
  print("\n[COUNTRY, COMPANY, ARTIST, YEAR, TITLE, PRICE]")
  while True:
   paint=input("\n검색할 태그 : ")
   if paint in tagword:
    break
   else:
    print("입력 오류 : 태그를 찾을 수 없습니다")
  for word in range(0,len(tagword),2):
   if paint==tagword[word] or paint==tagword[word+1]:
    print(Sword[word])
    while True:
     Position=input("\n검색 값 : ")
     if Position in Sword[word]:
      break
     else:
      print("입력 오류 : 태그를 찾을 수 없습니다 (대소문자, 띄어쓰기 구분)")
    for j in range(len(Sword[word])):
     if Position==Sword[word][j]:
      wordPositions(Sword[word][j],listword[word],xmllist)
      tag_list=[z for z, value in enumerate(listword[word]) if value==Sword[word][j]]
    while True:
     Findtag=int(input("\n삭제할 정보(Number) : "))
     if (str(type(Findtag))=="<class 'int'>"):
      if Findtag <= len(tag_list):
       break
      else:
       print("입력 오류 : 입력 범위 오류 1 ~",len(tag_list))
     else:
      print("입력 오류 : 정수로 입력해 주시기 바랍니다")
    print(xmllist[tag_list[Findtag-1]])
    del xmllist[tag_list[Findtag-1]]
    root.remove(root[tag_list[Findtag-1]])
    indent(root)
    ET.dump(root)
    tree=ET.ElementTree(root)
    tree.write(Lfilename+"_Delete"+".xml")
    mode_num=4
  

 elif mode_num==4:
  print("프로그램 종료")
  sys.exit()

 else:
  print("입력 오류 : 1~4의 숫자를 입력해 주세요")
  mode_num=0

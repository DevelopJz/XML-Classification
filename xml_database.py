import xml.etree.ElementTree as ET
import os
import subprocess
import sys
import time, datetime
from lxml import etree, objectify
from lxml.etree import XMLSyntaxError
import shutil

def xml_validator(some_xml_string, xsd_file="xmlfiles/valid.xsd"):
 try:
  schema=etree.XMLSchema(file=xsd_file)
  parser=objectify.makeparser(schema=schema)
  objectify.fromstring(some_xml_string,parser)
  print("xml schema 파일 검증 완료")
 except XMLSyntaxError:
  #handle exception here
  print("xml schema 파일 검증 에러")
  pass

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

def classify():
 #country 분류
 for a in range(len(country)):
  con_list=[k for k, value in enumerate(xmlcountry) if value==country[a]]
  
  #company 분류
  for d in range(len(company)):
   com_list=[k for k, value in enumerate(xmlcompany) if value==company[d]]
   if len(con_list)>len(com_list):
    x=list(set(con_list)-set(com_list))
    y=list(set(con_list)-set(x))
    com_list=y
   elif len(con_list)<=len(com_list):
    com_list=con_list
   
   #artist 분류
   for h in range(len(artist)):
    art_list=[k for k, value in enumerate(xmlartist) if value==artist[h]]
    if len(com_list)>len(art_list):
     x=list(set(com_list)-set(art_list))
     y=list(set(com_list)-set(x))
     art_list=y
    elif len(com_list)<=len(art_list):
     art_list=com_list
     
    #year 분류
    for l in range(len(year)):
     yea_list=[k for k, value in enumerate(xmlyear) if value==year[l]]
    if len(art_list)>len(yea_list):
     x=list(set(art_list)-set(yea_list))
     y=list(set(art_list)-set(x))
     yea_list=y
    elif len(art_list)<=len(yea_list):
     yea_list=art_list
    
     #title 분류
     for v in range(len(title)):
      tit_list=[k for k, value in enumerate(xmltitle) if value==title[v]]
     if len(yea_list)>len(tit_list):
      x=list(set(yea_list)-set(tit_list))
      y=list(set(yea_list)-set(x))
      tit_list=y
     elif len(yea_list)<=len(tit_list):
      tit_list=yea_list
  
     #country
     if not os.path.isdir("./xmlfiles/country/"+country[a]):                                                           
      os.mkdir("./xmlfiles/country/"+country[a])
    
     for xml1 in range(len(con_list)):
      firstroot=ET.Element("CATALOG")
      cd_1=ET.SubElement(firstroot,"CD")
      ET.SubElement(cd_1,"TITLE").text=xmltitle[con_list[xml1]]
      ET.SubElement(cd_1,"ARTIST").text=xmlartist[con_list[xml1]]
      ET.SubElement(cd_1,"COUNTRY").text=xmlcountry[con_list[xml1]]
      ET.SubElement(cd_1,"COMPANY").text=xmlcompany[con_list[xml1]]
      ET.SubElement(cd_1,"PRICE").text=xmlprice[con_list[xml1]]
      ET.SubElement(cd_1,"YEAR").text=xmlyear[con_list[xml1]]
      indent(firstroot)
      firsttree=ET.ElementTree(firstroot)
      firsttree.write("./xmlfiles/country/"+country[a]+"/xml_"+country[a]+".xml")
  
      with open("./xmlfiles/country/"+country[a]+"/xml_"+country[a]+".txt",'w') as Maketxt:
       for txt1 in range(len(con_list)):
        Maketxt.write("".join(xmllist[con_list[txt1]])+"\n\n")
    
      #company
      for xml2 in range(len(com_list)):
       if not os.path.isdir("./xmlfiles/country/"+country[a]+"/"+xmlcompany[com_list[xml2]]):                                                           
        os.mkdir("./xmlfiles/country/"+country[a]+"/"+xmlcompany[com_list[xml2]])
  
       secondroot=ET.Element("CATALOG")
       cd_2=ET.SubElement(secondroot,"CD")
       ET.SubElement(cd_2,"TITLE").text=xmltitle[com_list[xml2]]
       ET.SubElement(cd_2,"ARTIST").text=xmlartist[com_list[xml2]]
       ET.SubElement(cd_2,"COUNTRY").text=xmlcountry[com_list[xml2]]
       ET.SubElement(cd_2,"COMPANY").text=xmlcompany[com_list[xml2]]
       ET.SubElement(cd_2,"PRICE").text=xmlprice[com_list[xml2]]
       ET.SubElement(cd_2,"YEAR").text=xmlyear[com_list[xml2]]
       indent(secondroot)
       secondtree=ET.ElementTree(secondroot)
       secondtree.write("./xmlfiles/country/"+country[a]+"/"+xmlcompany[com_list[xml2]]+"/xml_"+country[a]+"_"+xmlcompany[com_list[xml2]]+".xml")

       with open("./xmlfiles/country/"+country[a]+"/"+xmlcompany[com_list[xml2]]+"/xml_"+country[a]+"_"+xmlcompany[com_list[xml2]]+".txt",'w') as Maketxt:
        for txt2 in range(len(com_list)):
         Maketxt.write("".join(xmllist[com_list[txt2]])+"\n\n")


       #artist 
       for xml3 in range(len(art_list)):  
        if not os.path.isdir("./xmlfiles/country/"+country[a]+"/"+xmlcompany[com_list[xml2]]+"/"+xmlartist[art_list[xml3]]):                                                           
         os.mkdir("./xmlfiles/country/"+country[a]+"/"+xmlcompany[com_list[xml2]]+"/"+xmlartist[art_list[xml3]])
   
        thirdroot=ET.Element("CATALOG")
        cd_3=ET.SubElement(thirdroot,"CD")
        ET.SubElement(cd_3,"TITLE").text=xmltitle[art_list[xml3]]
        ET.SubElement(cd_3,"ARTIST").text=xmlartist[art_list[xml3]]
        ET.SubElement(cd_3,"COUNTRY").text=xmlcountry[art_list[xml3]]
        ET.SubElement(cd_3,"COMPANY").text=xmlcompany[art_list[xml3]]
        ET.SubElement(cd_3,"PRICE").text=xmlprice[art_list[xml3]]
        ET.SubElement(cd_3,"YEAR").text=xmlyear[art_list[xml3]]
        indent(thirdroot)
        thirdtree=ET.ElementTree(thirdroot)
        thirdtree.write("./xmlfiles/country/"+country[a]+"/"+xmlcompany[com_list[xml2]]+"/"+xmlartist[art_list[xml3]]+"/xml_"+country[a]+"_"+xmlcompany[com_list[xml2]]+"_"+xmlartist[art_list[xml3]]+".xml")
   
        with open("./xmlfiles/country/"+country[a]+"/"+xmlcompany[com_list[xml2]]+"/"+xmlartist[art_list[xml3]]+"/xml_"+country[a]+"_"+xmlcompany[com_list[xml2]]+"_"+xmlartist[art_list[xml3]]+".txt",'w') as Maketxt:
         for txt3 in range(len(art_list)):
          Maketxt.write("".join(xmllist[art_list[txt3]])+"\n\n")



        #year
        for xml4 in range(len(yea_list)):
         if not os.path.isdir("./xmlfiles/country/"+country[a]+"/"+xmlcompany[com_list[xml2]]+"/"+xmlartist[art_list[xml3]]+"/"+xmlyear[yea_list[xml4]]):                                                           
          os.mkdir("./xmlfiles/country/"+country[a]+"/"+xmlcompany[com_list[xml2]]+"/"+xmlartist[art_list[xml3]]+"/"+xmlyear[yea_list[xml4]])
    
         fourthroot=ET.Element("CATALOG")
         cd_4=ET.SubElement(fourthroot,"CD")
         ET.SubElement(cd_4,"TITLE").text=xmltitle[yea_list[xml4]]
         ET.SubElement(cd_4,"ARTIST").text=xmlartist[yea_list[xml4]]
         ET.SubElement(cd_4,"COUNTRY").text=xmlcountry[yea_list[xml4]]
         ET.SubElement(cd_4,"COMPANY").text=xmlcompany[yea_list[xml4]]
         ET.SubElement(cd_4,"PRICE").text=xmlprice[yea_list[xml4]]
         ET.SubElement(cd_4,"YEAR").text=xmlyear[yea_list[xml4]]
         indent(fourthroot)
         fourthtree=ET.ElementTree(fourthroot)
         fourthtree.write("./xmlfiles/country/"+country[a]+"/"+xmlcompany[com_list[xml2]]+"/"+xmlartist[art_list[xml3]]+"/"+xmlyear[yea_list[xml4]]+"/xml_"+country[a]+"_"+xmlcompany[com_list[xml2]]+"_"+xmlartist[art_list[xml3]]+"_"+xmlyear[yea_list[xml4]]+".xml") 
     
         with open("./xmlfiles/country/"+country[a]+"/"+xmlcompany[com_list[xml2]]+"/"+xmlartist[art_list[xml3]]+"/"+xmlyear[yea_list[xml4]]+"/xml_"+country[a]+"_"+xmlcompany[com_list[xml2]]+"_"+xmlartist[art_list[xml3]]+"_"+xmlyear[yea_list[xml4]]+".txt",'w') as Maketxt:
          for txt4 in range(len(yea_list)):
           Maketxt.write("".join(xmllist[yea_list[txt4]])+"\n\n")

 
      

         #title
         for xml5 in range(len(tit_list)):
          if not os.path.isdir("./xmlfiles/country/"+country[a]+"/"+xmlcompany[com_list[xml2]]+"/"+xmlartist[art_list[xml3]]+"/"+xmlyear[yea_list[xml4]]+"/"+xmltitle[tit_list[xml5]]):                                                           
           os.mkdir("./xmlfiles/country/"+country[a]+"/"+xmlcompany[com_list[xml2]]+"/"+xmlartist[art_list[xml3]]+"/"+xmlyear[yea_list[xml4]]+"/"+xmltitle[tit_list[xml5]])
       
          fiveroot=ET.Element("CATALOG")
          cd_5=ET.SubElement(fiveroot,"CD")
          ET.SubElement(cd_5,"TITLE").text=xmltitle[tit_list[xml5]]
          ET.SubElement(cd_5,"ARTIST").text=xmlartist[tit_list[xml5]]
          ET.SubElement(cd_5,"COUNTRY").text=xmlcountry[tit_list[xml5]]
          ET.SubElement(cd_5,"COMPANY").text=xmlcompany[tit_list[xml5]]
          ET.SubElement(cd_5,"PRICE").text=xmlprice[tit_list[xml5]]
          ET.SubElement(cd_5,"YEAR").text=xmlyear[tit_list[xml5]]
          indent(fiveroot)
          fivetree=ET.ElementTree(fiveroot)
          fivetree.write("./xmlfiles/country/"+country[a]+"/"+xmlcompany[com_list[xml2]]+"/"+xmlartist[art_list[xml3]]+"/"+xmlyear[yea_list[xml4]]+"/"+xmltitle[tit_list[xml5]]+"/xml_"+country[a]+"_"+xmlcompany[com_list[xml2]]+"_"+xmlartist[art_list[xml3]]+"_"+xmlyear[yea_list[xml4]]+"_"+xmltitle[tit_list[xml5]]+".xml")
   
          with open("./xmlfiles/country/"+country[a]+"/"+xmlcompany[com_list[xml2]]+"/"+xmlartist[art_list[xml3]]+"/"+xmlyear[yea_list[xml4]]+"/"+xmltitle[tit_list[xml5]]+"/xml_"+country[a]+"_"+xmlcompany[com_list[xml2]]+"_"+xmlartist[art_list[xml3]]+"_"+xmlyear[yea_list[xml4]]+"_"+xmltitle[tit_list[xml5]]+".txt",'w') as Maketxt:
           for txt5 in range(len(tit_list)):
            Maketxt.write("".join(xmllist[tit_list[txt5]])+"\n\n")
          


findsome="<CD>"
count=0
findproblem=0

printflag=0
endflag=0
 
xmlcountry=list()
xmlcompany=list()
xmlartist=list()
xmlyear=list()
xmltitle=list()
xmlprice=list()
xmllist=list()
 
recountry=list()
recompany=list()
reartist=list()
reyear=list()
retitle=list()
reprice=list()

filename="example"
    
xml_file=open("./xmlfiles/"+filename+".xml",'r')
xml_string=xml_file.read()
xml_file.close()
xml_validator(xml_string,"xmlfiles/valid.xsd")

tree = ET.parse("./xmlfiles/"+filename+".xml")
root=tree.getroot()

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

file_read=open("./xmlfiles/"+filename+".xml","r")

while True:
 f_line = file_read.readline()
 if not f_line:
  break
 raw=f_line.split()
  
 if count>=findproblem:
  if findsome in f_line:
   count=count+1
   
for i in range(0,count):
 xmllist.append("COUNTRY : "+xmlcountry[i]+"\n"+"COMPANY : "+xmlcompany[i]+"\n"+"ARTIST : "+xmlartist[i]+"\n"+"YEAR : "+xmlyear[i]+"\n"+"TITLE : "+xmltitle[i]+"\n"+"PRICE : "+xmlprice[i]+"\n")
 
while True:
 startTime=time.time()
 if not os.path.isdir("./xmlfiles/country/"):   
  print("폴더가 존재하지 않아 생성합니다 (country)")                                                        
  os.mkdir("./xmlfiles/country/")
 else:
  print("폴더가 이미 존재합니다 (country)")
 
 print("xml 분석 및 분류 시작")

 classify()
 
 print("xml 파일 분석 및 분류 완료")

 sec=time.time()-startTime
 times=str(datetime.timedelta(seconds=sec)).split(".")
 times=times[0]
 print(times)

 print("파일 검색 및 수정")
 while True:
  findmode=input("방식 : 1.태그별 검색 / 2.순서별 검색 및 수정 / 3. 프로그램 종료 (1/2/3)\n")
  if findmode=="1":
   while True:
    findtag=input("태그별 검색 : TITLE / ARTIST / COUNTRY / COMPANY / PRICE / YEAR\n")
    if findtag=="TITLE" or findtag=="title":
     print(title)
     while True:
      findtitle=input("TITLE : ")
      if findtitle in title:
       findtit=[k for k, value in enumerate(xmltitle) if value==findtitle]
       for p in range(len(findtit)):
        if printflag==0:
         result=subprocess.run(["notepad","./xmlfiles/country/"+xmlcountry[findtit[p]]+"/"+xmlcompany[findtit[p]]+"/"+xmlartist[findtit[p]]+"/"+xmlyear[findtit[p]]+"/"+"xml_"+xmlcountry[findtit[p]]+"_"+xmlcompany[findtit[p]]+"_"+xmlartist[findtit[p]]+"_"+xmlyear[findtit[p]]+".xml"])
         printflag=1
        if result.returncode==0:
         if endflag==0:
          print("파일 확인 완료.")
          endflag=1
       break
      else:
       print("입력 오류 : 대소문자 / 띄어쓰기 구분")
     break
    elif findtag=="ARTIST" or findtag=="artist":
     print(artist)
     while True:
      findartist=input("ARTIST : ")
      if findartist in artist:
       findart=[k for k, value in enumerate(xmlartist) if value==findartist]
       for q in range(len(findart)):
        if printflag==0:
         result=subprocess.run(["notepad","./xmlfiles/country/"+xmlcountry[findart[q]]+"/"+xmlcompany[findart[q]]+"/"+xmlartist[findart[q]]+"/"+"xml_"+xmlcountry[findart[q]]+"_"+xmlcompany[findart[q]]+"_"+xmlartist[findart[q]]+".xml"])
         printflag=1
        if result.returncode==0:
         if endflag==0:
          print("파일 확인 완료.")
          endflag=1
       break
      else:
       print("입력 오류 : 대소문자 / 띄어쓰기 구분")
     break
    elif findtag=="COUNTRY" or findtag=="country":
     print(country)
     while True:
      findcountry=input("COUNTRY : ")
      if findcountry in country:
       findcon=[k for k, value in enumerate(xmlcountry) if value==findcountry]
       for r in range(len(findcon)):
        if printflag==0:
         result=subprocess.run(["notepad","./xmlfiles/country/"+xmlcountry[findcon[r]]+"/"+"xml_"+xmlcountry[findcon[r]]+".xml"])
         printflag=1
        if result.returncode==0:
         if endflag==0:
          print("파일 확인 완료.")
          endflag=1
       break
      else:
       print("입력 오류 : 대소문자 / 띄어쓰기 구분")
     break
    elif findtag=="COMPANY" or findtag=="company":
     print(company)
     while True:
      findcompany=input("COMPANY : ")
      if findcompany in company:
       findcom=[k for k, value in enumerate(xmlcompany) if value==findcompany]
       for s in range(len(findcom)):
        if printflag==0:
         result=subprocess.run(["notepad","./xmlfiles/country/"+xmlcountry[findcom[s]]+"/"+xmlcompany[findcom[s]]+"/"+"xml_"+xmlcountry[findcom[s]]+"_"+xmlcompany[findcom[s]]+".xml"])
         printflag=1
        if result.returncode==0:
         if endflag==0:
          print("파일 확인 완료.")
          endflag=1
       break
      else:
       print("입력 오류 : 대소문자 / 띄어쓰기 구분")
     break
    elif findtag=="PRICE" or findtag=="price":
     print(price)
     while True:
      findprice=input("PRICE : ")
      if findprice in price:
       findpri=[k for k, value in enumerate(xmlprice) if value==findprice]
       for t in range(len(findpri)):
        if printflag==0:
         result=subprocess.run(["notepad","./xmlfiles/country/"+xmlcountry[findpri[t]]+"/"+xmlcompany[findpri[t]]+"/"+xmlartist[findpri[t]]+"/"+xmlyear[findpri[t]]+"/"+"xml_"+xmlcountry[findpri[t]]+"_"+xmlcompany[findpri[t]]+"_"+xmlartist[findpri[t]]+"_"+xmlyear[findpri[t]]+".xml"])
         printflag=1
        if result.returncode==0:
         if endflag==0:
          print("파일 확인 완료.")
          endflag=1
       break
      else:
       print("입력 오류 : 대소문자 / 띄어쓰기 구분")
     break
    elif findtag=="YEAR" or findtag=="year":
     print(year)
     while True:
      findyear=input("YEAR : ")
      if findyear in year:
       findyea=[k for k, value in enumerate(xmlyear) if value==findyear]
       for u in range(len(findyea)):
        if printflag==0:
         result=subprocess.run(["notepad","./xmlfiles/country/"+xmlcountry[findyea[u]]+"/"+xmlcompany[findyea[u]]+"/"+xmlartist[findyea[u]]+"/"+xmlyear[findyea[u]]+"/"+"xml_"+xmlcountry[findyea[u]]+"_"+xmlcompany[findyea[u]]+"_"+xmlartist[findyea[u]]+"_"+xmlyear[findyea[u]]+".xml"])
         printflag=1
        if result.returncode==0:
         if endflag==0:
          print("파일 확인 완료.")
          endflag=1
       break
      else:
       print("입력 오류 : 대소문자 / 띄어쓰기 구분")
     break
    else:
     print("태그를 찾을 수 없습니다")
   printflag=0
   endflag=0
   break
 
  elif findmode=="2":
   print("순서별 검색 및 수정 : COUNTRY->COMPANY->ARTIST->YEAR->TITLE")
   print(country)
   while True:
    flowcon=input("\n나라 : ")
    if flowcon in country:
     flowcon_list=[k for k, value in enumerate(xmlcountry) if value==flowcon]
     for ff in range(len(flowcon_list)):
      print(xmllist[flowcon_list[ff]])
     while True:
      flowcom=input("\n회사 : ")
      if flowcom in company:
       flowcom_list=[k for k, value in enumerate(xmlcompany) if value==flowcom]
       if len(flowcon_list)>len(flowcom_list):
        x=list(set(flowcon_list)-set(flowcom_list))
        y=list(set(flowcon_list)-set(x))
        flowcom_list=y
       elif len(flowcon_list)<=len(flowcom_list):
        flowcom_list=flowcon_list
       for w in range(len(flowcom_list)):
        print(xmllist[flowcom_list[w]])
       while True:
        flowart=input("\n가수 : ")
        if flowart in artist:
         flowart_list=[k for k, value in enumerate(xmlartist) if value==flowart]
         if len(flowcom_list)>len(flowart_list):
          x=list(set(flowcom_list)-set(flowart_list))
          y=list(set(flowcom_list)-set(x))
          flowart_list=y
         elif len(flowcom_list)<=len(flowart_list):
          flowart_list=flowcom_list
         for aa in range(len(flowart_list)):
          print(xmllist[flowart_list[aa]])
         while True:
          flowyea=input("\n연도 : ")
          if flowyea in year:
           flowyea_list=[k for k, value in enumerate(xmlyear) if value==flowyea]
           if len(flowart_list)>len(flowyea_list):
            x=list(set(flowart_list)-set(flowyea_list))
            y=list(set(flowart_list)-set(x))
            flowyea_list=y
           elif len(flowart_list)<=len(flowyea_list):
            flowyea_list=flowart_list
           for bb in range(len(flowyea_list)):
            print(xmllist[flowyea_list[bb]])
           while True:
            flowtit=input("\n제목 : ")
            if flowtit in title:
             flowtit_list=[k for k, value in enumerate(xmltitle) if value==flowtit]
             if len(flowyea_list)>len(flowtit_list):
              x=list(set(flowyea_list)-set(flowtit_list))
              y=list(set(flowyea_list)-set(x))
              flowtit_list=y
             elif len(flowyea_list)<=len(flowtit_list):
              flowtit_list=flowyea_list
             for cc in range(len(flowtit_list)):
              print(xmllist[flowtit_list[cc]])
              result=subprocess.run(["notepad","./xmlfiles/country/"+xmlcountry[flowyea_list[bb]]+"/"+xmlcompany[flowyea_list[bb]]+"/"+xmlartist[flowyea_list[bb]]+"/"+xmlyear[flowyea_list[bb]]+"/"+xmltitle[flowyea_list[bb]]+"/"+"xml_"+xmlcountry[flowyea_list[bb]]+"_"+xmlcompany[flowyea_list[bb]]+"_"+xmlartist[flowyea_list[bb]]+"_"+xmlyear[flowyea_list[bb]]+"_"+xmltitle[flowyea_list[bb]]+".xml"])
              if result.returncode==0:
               refile=ET.parse("./xmlfiles/country/"+xmlcountry[flowyea_list[bb]]+"/"+xmlcompany[flowyea_list[bb]]+"/"+xmlartist[flowyea_list[bb]]+"/"+xmlyear[flowyea_list[bb]]+"/"+xmltitle[flowyea_list[bb]]+"/"+"xml_"+xmlcountry[flowyea_list[bb]]+"_"+xmlcompany[flowyea_list[bb]]+"_"+xmlartist[flowyea_list[bb]]+"_"+xmlyear[flowyea_list[bb]]+"_"+xmltitle[flowyea_list[bb]]+".xml")
               Reroot=refile.getroot()
               for element in Reroot.findall("CD"):
                recountry.append(element.find("COUNTRY").text)
                recompany.append(element.find("COMPANY").text)
                reartist.append(element.find("ARTIST").text)
                reyear.append(element.find("YEAR").text)
                retitle.append(element.find("TITLE").text)
                reprice.append(element.find("PRICE").text)
            
               xmlcountry[flowyea_list[cc-1]]=recountry[cc-1]
               xmlcompany[flowyea_list[cc-1]]=recompany[cc-1]
               xmlartist[flowyea_list[cc-1]]=reartist[cc-1]
               xmlyear[flowyea_list[cc-1]]=reyear[cc-1]
               xmltitle[flowyea_list[cc-1]]=retitle[cc-1]
               xmlprice[flowyea_list[cc-1]]=reprice[cc-1]
               xmllist=list()
               rexmllist=[xmltitle[flowyea_list[cc-1]],xmlartist[flowyea_list[cc-1]],xmlcountry[flowyea_list[cc-1]],xmlcompany[flowyea_list[cc-1]],xmlprice[flowyea_list[cc-1]],xmlyear[flowyea_list[cc-1]]]
               for i in range(0,count):
                xmllist.append("COUNTRY : "+xmlcountry[i]+"\n"+"COMPANY : "+xmlcompany[i]+"\n"+"ARTIST : "+xmlartist[i]+"\n"+"YEAR : "+xmlyear[i]+"\n"+"TITLE : "+xmltitle[i]+"\n"+"PRICE : "+xmlprice[i]+"\n")
               print("\n수정된 값\n"+xmllist[flowyea_list[cc]])
               for dd in range(0,6):
                root[flowyea_list[cc-1]][dd].text=str(rexmllist[dd])
               refiles=ET.ElementTree(root)
               refiles.write("./xmlfiles/"+filename+".xml")
               print("수정 완료")
               shutil.rmtree("./xmlfiles/country/")
               break
             break
            else:
             print("입력 오류 : 대소문자 / 띄어쓰기 구분")
           break
          else:
           print("입력 오류 : 값을 찾을 수 없습니다")
         break
        else:
         print("입력 오류 : 대소문자 / 띄어쓰기 구분")
       break
      else:
       print("입력 오류 : 대소문자 / 띄어쓰기 구분")
     break
    else:
     print("입력 오류 : 대소문자 구분")
   break
  elif findmode=="3":
   print("프로그램 종료.")
   sys.exit()
   break
    
  else:
   print("1 / 2 / 3 을 입력해 주세요")
import random
import time
from tabulate import tabulate
############FUNCTIONS##################
def asktraits():
           print("\n\n")
           print("Enter the trait(s) to be used (both capital and small letters are acceptable)")
           print("Be sure not to repeat traits or mistype, or else a wrong punnet square will be successfully made !\n")
           print("type\nt for height (tall and dwarf)")
           print("v for colour of flower (violet and white)")
           print("a for position of flower (axial and terminal)")
           print("y for color of seed (yellow and green)")
           print("r for shape of seed (round and wrinkled)")
           print("g for color of pod (green and yellow)")
           print("i for shape of pod (inflated and constricted)\n")
def deftrait():
           height=["T","t"]
           colorf=["V","v"]
           positionf=["A","a"]
           colors=["Y","y"]
           shapes=["R","r"]
           colorp=["G","g"]
           shapep=["I","i"]
           global trait
           if trait == "T" or trait=="t":
                      trait = height
           elif trait == "V" or trait== "v":
                      trait = colorf
           elif trait == "A" or trait== "a":
                      trait = positionf
           elif trait == "Y" or trait== "y":
                      trait = colors
           elif trait == "R" or trait== "r":
                      trait = shapes
           elif trait == "G" or trait== "g":
                      trait = colorp
           elif trait == "I" or trait== "i":
                      trait = shapep
def smallbig():
           global punnet
           if ("tT" in punnet) == True:
                      tT = punnet.index("tT")
                      punnet[tT] = "Tt"
           if ("vV" in punnet) == True:
                      vV = punnet.index("vV")
                      punnet[vV] = "Vv"
           if ("aA" in punnet) == True:
                      aA = punnet.index("aA")
                      punnet[aA] = "Aa"
           if ("yY" in punnet) == True:
                      yY = punnet.index("yY")
                      punnet[yY] = "Yy"
           if ("rR" in punnet) == True:
                      rR = punnet.index("rR")
                      punnet[rR] = "Rr"
           if ("gG" in punnet) == True:
                      gG = punnet.index("gG")
                      punnet[gG] = "Gg"
           if ("iI" in punnet) == True:
                      iI = punnet.index("iI")
                      punnet[iI] = "Ii"
def tablemake():
           global square,punnetsquare,punnet,x,trait,gamete
           length = len(punnet)
           square = length**0.5
           square = int(square)
           for i in range(0,square):
                      x = punnet[0:square]
                      punnet = punnet[square:]
                      punnetsquare.append(x)
           blank = ["♂/♀"]
           blank = blank+gamete
           head = blank
           for i in range(0,square):
                      punnetsquare[i].insert(0,gamete[i])
           print("\n\n",tabulate(punnetsquare, headers=head))
def genotype():
           global punnetreserve,gratio
           for i in punnetreserve:
                      if i not in gratio:
                                 count = punnetreserve.count(i)
                                 gratio[i] = count
           _gratio = list(gratio.values())
           print(*_gratio,sep=":")
##########BODY########################
while True:
           global punnet,punnetreserve,punnetsquare,gamete,gratio
           punnet =[]
           punnetreserve = []
           gratio = {}
           _punnet = []
           punnetsquare =[]
           gamete = []
           x = []
           print("\n\nEnter the cross to be made -")
           print("1-monohybrid\n2-dihybrid\n3-trihybrid\n4-tetrahybrid\n5-pentahybrid\n6-hexahybrid\n7-septahybrid")
           while True:
                      try:
                                 cross=int(input())
                                 break
                      except ValueError:
                                 print("Please enter the numbers specified only.")
                                 continue
           global trait
           ##############MONOHYBRID
           if cross == 1:
                      asktraits()
                      trait = input("Trait ->")
                      deftrait()
                      print("Loading, please wait...")
                      time.sleep(1)
                      for p1 in trait:
                                 for p2 in trait:
                                            _punnet.append(p1+p2)
                      gamete = trait
                      allele = []
                      j=[]
                      k=[]
                      for i in _punnet:
                                 allele = ([*i])
                                 while True:
                                            if trait[0] in allele:
                                                       j.append(trait[0])
                                                       allele.remove(trait[0])
                                            else:
                                                       break
                                 while True:
                                            if trait[1] in allele:
                                                       j.append(trait[1])
                                                       allele.remove(trait[1])
                                            else:
                                                       break
                                 k=j[0]+j[1]
                                 j=[]
                                 punnet.append(k)
                                 punnetreserve.append(k)
                      tablemake()
           ##############DIHYBRID
           elif cross == 2:
                      asktraits()
                      trait1 = input("Trait 1->")
                      trait2 = input("Trait 2->")
                      trait = trait1
                      deftrait()
                      trait1= trait
                      trait = trait2
                      deftrait()
                      trait2= trait
                      print("Loading, please wait...")
                      time.sleep(1)
                      for p1 in trait1:
                                 for p2 in trait2:
                                            gamete.append(p1+p2)
                      for p1 in gamete:
                                 for p2 in gamete:
                                            _punnet.append(p1+p2)
                      allele = []
                      j=[]
                      k=[]
                      for i in _punnet:
                                 allele = ([*i])
                                 while True:
                                            if trait1[0] in allele:
                                                       j.append(trait1[0])
                                                       allele.remove(trait1[0])
                                            else:
                                                       break
                                 while True:
                                            if trait1[1] in allele:
                                                       j.append(trait1[1])
                                                       allele.remove(trait1[1])
                                            else:
                                                       break
                                 while True:
                                            if trait2[0] in allele:
                                                       j.append(trait2[0])
                                                       allele.remove(trait2[0])
                                            else:
                                                       break
                                 while True:
                                            if trait2[1] in allele:
                                                       j.append(trait2[1])
                                                       allele.remove(trait2[1])
                                            else:
                                                       break
                                 k=j[0]+j[1]+j[2]+j[3]
                                 j=[]
                                 punnet.append(k)
                                 punnetreserve.append(k)
                      tablemake()
           ##############TRIHYBRID
           elif cross == 3:
                      asktraits()
                      trait1 = input("Trait 1->")
                      trait2 = input("Trait 2->")
                      trait3 = input("Trait 3->")
                      trait = trait1
                      deftrait()
                      trait1= trait
                      trait = trait2
                      deftrait()
                      trait2= trait
                      trait = trait3
                      deftrait()
                      trait3= trait
                      print("Loading, please wait...")
                      time.sleep(1)
                      for p1 in trait1:
                                 for p2 in trait2:
                                            for p3 in trait3:
                                                       gamete.append(p1+p2+p3)
                      for p1 in gamete:
                                 for p2 in gamete:
                                            _punnet.append(p1+p2)
                      allele = []
                      j=[]
                      k=[]
                      for i in _punnet:
                                 allele = ([*i])
                                 while True:
                                            if trait1[0] in allele:
                                                       j.append(trait1[0])
                                                       allele.remove(trait1[0])
                                            else:
                                                       break
                                 while True:
                                            if trait1[1] in allele:
                                                       j.append(trait1[1])
                                                       allele.remove(trait1[1])
                                            else:
                                                       break
                                 while True:
                                            if trait2[0] in allele:
                                                       j.append(trait2[0])
                                                       allele.remove(trait2[0])
                                            else:
                                                       break
                                 while True:
                                            if trait2[1] in allele:
                                                       j.append(trait2[1])
                                                       allele.remove(trait2[1])
                                            else:
                                                       break
                                 while True:
                                            if trait3[0] in allele:
                                                       j.append(trait3[0])
                                                       allele.remove(trait3[0])
                                            else:
                                                       break
                                 while True:
                                            if trait3[1] in allele:
                                                       j.append(trait3[1])
                                                       allele.remove(trait3[1])
                                            else:
                                                       break
                                 k=j[0]+j[1]+j[2]+j[3]+j[4]+j[5]
                                 j=[]
                                 punnet.append(k)
                                 punnetreserve.append(k)
                      tablemake()
           ##############TETRAHYBRID
           elif cross == 4:
                      asktraits()
                      trait1 = input("Trait 1->")
                      trait2 = input("Trait 2->")
                      trait3 = input("Trait 3->")
                      trait4 = input("Trait 4->")
                      trait = trait1
                      deftrait()
                      trait1= trait
                      trait = trait2
                      deftrait()
                      trait2= trait
                      trait = trait3
                      deftrait()
                      trait3= trait
                      trait = trait4
                      deftrait()
                      trait4= trait
                      print("Loading, please wait...")
                      time.sleep(1)
                      for p1 in trait1:
                                 for p2 in trait2:
                                            for p3 in trait3:
                                                       for p4 in trait4:
                                                                  gamete.append(p1+p2+p3+p4)
                      for p1 in gamete:
                                 for p2 in gamete:
                                            _punnet.append(p1+p2)
                      allele = []
                      j=[]
                      k=[]
                      for i in _punnet:
                                 allele = ([*i])
                                 while True:
                                            if trait1[0] in allele:
                                                       j.append(trait1[0])
                                                       allele.remove(trait1[0])
                                            else:
                                                       break
                                 while True:
                                            if trait1[1] in allele:
                                                       j.append(trait1[1])
                                                       allele.remove(trait1[1])
                                            else:
                                                       break
                                 while True:
                                            if trait2[0] in allele:
                                                       j.append(trait2[0])
                                                       allele.remove(trait2[0])
                                            else:
                                                       break
                                 while True:
                                            if trait2[1] in allele:
                                                       j.append(trait2[1])
                                                       allele.remove(trait2[1])
                                            else:
                                                       break
                                 while True:
                                            if trait3[0] in allele:
                                                       j.append(trait3[0])
                                                       allele.remove(trait3[0])
                                            else:
                                                       break
                                 while True:
                                            if trait3[1] in allele:
                                                       j.append(trait3[1])
                                                       allele.remove(trait3[1])
                                            else:
                                                       break
                                 while True:
                                            if trait4[0] in allele:
                                                       j.append(trait4[0])
                                                       allele.remove(trait4[0])
                                            else:
                                                       break
                                 while True:
                                            if trait4[1] in allele:
                                                       j.append(trait4[1])
                                                       allele.remove(trait4[1])
                                            else:
                                                       break
                                 k=j[0]+j[1]+j[2]+j[3]+j[4]+j[5]+j[6]+j[7]
                                 j=[]
                                 punnet.append(k)
                                 punnetreserve.append(k)
                      tablemake()
           ##############PENTAHYBRID
           elif cross == 5:
                      asktraits()
                      trait1 = input("Trait 1->")
                      trait2 = input("Trait 2->")
                      trait3 = input("Trait 3->")
                      trait4 = input("Trait 4->")
                      trait5 = input("Trait 5->")
                      trait = trait1
                      deftrait()
                      trait1= trait
                      trait = trait2
                      deftrait()
                      trait2= trait
                      trait = trait3
                      deftrait()
                      trait3= trait
                      trait = trait4
                      deftrait()
                      trait4= trait
                      trait = trait5
                      deftrait()
                      trait5= trait
                      print("Loading, please wait...")
                      time.sleep(1)
                      for p1 in trait1:
                                 for p2 in trait2:
                                            for p3 in trait3:
                                                       for p4 in trait4:
                                                                  for p5 in trait5:
                                                                             gamete.append(p1+p2+p3+p4+p5)
                      for p1 in gamete:
                                 for p2 in gamete:
                                            _punnet.append(p1+p2)
                      allele = []
                      j=[]
                      k=[]
                      for i in _punnet:
                                 allele = ([*i])
                                 while True:
                                            if trait1[0] in allele:
                                                       j.append(trait1[0])
                                                       allele.remove(trait1[0])
                                            else:
                                                       break
                                 while True:
                                            if trait1[1] in allele:
                                                       j.append(trait1[1])
                                                       allele.remove(trait1[1])
                                            else:
                                                       break
                                 while True:
                                            if trait2[0] in allele:
                                                       j.append(trait2[0])
                                                       allele.remove(trait2[0])
                                            else:
                                                       break
                                 while True:
                                            if trait2[1] in allele:
                                                       j.append(trait2[1])
                                                       allele.remove(trait2[1])
                                            else:
                                                       break
                                 while True:
                                            if trait3[0] in allele:
                                                       j.append(trait3[0])
                                                       allele.remove(trait3[0])
                                            else:
                                                       break
                                 while True:
                                            if trait3[1] in allele:
                                                       j.append(trait3[1])
                                                       allele.remove(trait3[1])
                                            else:
                                                       break
                                 while True:
                                            if trait4[0] in allele:
                                                       j.append(trait4[0])
                                                       allele.remove(trait4[0])
                                            else:
                                                       break
                                 while True:
                                            if trait4[1] in allele:
                                                       j.append(trait4[1])
                                                       allele.remove(trait4[1])
                                            else:
                                                       break
                                 while True:
                                            if trait5[0] in allele:
                                                       j.append(trait5[0])
                                                       allele.remove(trait5[0])
                                            else:
                                                       break
                                 while True:
                                            if trait5[1] in allele:
                                                       j.append(trait5[1])
                                                       allele.remove(trait5[1])
                                            else:
                                                       break
                                 k=j[0]+j[1]+j[2]+j[3]+j[4]+j[5]+j[6]+j[7]+j[8]+j[9]
                                 j=[]
                                 punnet.append(k)
                                 punnetreserve.append(k)
                      tablemake()
           ##############HEXAHYBRID
           elif cross == 6:
                      asktraits()
                      trait1 = input("Trait 1->")
                      trait2 = input("Trait 2->")
                      trait3 = input("Trait 3->")
                      trait4 = input("Trait 4->")
                      trait5 = input("Trait 5->")
                      trait6 = input("Trait 6->")
                      trait = trait1
                      deftrait()
                      trait1= trait
                      trait = trait2
                      deftrait()
                      trait2= trait
                      trait = trait3
                      deftrait()
                      trait3= trait
                      trait = trait4
                      deftrait()
                      trait4= trait
                      trait = trait5
                      deftrait()
                      trait5= trait
                      trait = trait6
                      deftrait()
                      trait6= trait
                      print("Loading, please wait...")
                      time.sleep(1)
                      for p1 in trait1:
                                 for p2 in trait2:
                                            for p3 in trait3:
                                                       for p4 in trait4:
                                                                  for p5 in trait5:
                                                                             for p6 in trait6:
                                                                                        gamete.append(p1+p2+p3+p4+p5+p6)
                      for p1 in gamete:
                                 for p2 in gamete:
                                            _punnet.append(p1+p2)
                      allele = []
                      j=[]
                      k=[]
                      for i in _punnet:
                                 allele = ([*i])
                                 while True:
                                            if trait1[0] in allele:
                                                       j.append(trait1[0])
                                                       allele.remove(trait1[0])
                                            else:
                                                       break
                                 while True:
                                            if trait1[1] in allele:
                                                       j.append(trait1[1])
                                                       allele.remove(trait1[1])
                                            else:
                                                       break
                                 while True:
                                            if trait2[0] in allele:
                                                       j.append(trait2[0])
                                                       allele.remove(trait2[0])
                                            else:
                                                       break
                                 while True:
                                            if trait2[1] in allele:
                                                       j.append(trait2[1])
                                                       allele.remove(trait2[1])
                                            else:
                                                       break
                                 while True:
                                            if trait3[0] in allele:
                                                       j.append(trait3[0])
                                                       allele.remove(trait3[0])
                                            else:
                                                       break
                                 while True:
                                            if trait3[1] in allele:
                                                       j.append(trait3[1])
                                                       allele.remove(trait3[1])
                                            else:
                                                       break
                                 while True:
                                            if trait4[0] in allele:
                                                       j.append(trait4[0])
                                                       allele.remove(trait4[0])
                                            else:
                                                       break
                                 while True:
                                            if trait4[1] in allele:
                                                       j.append(trait4[1])
                                                       allele.remove(trait4[1])
                                            else:
                                                       break
                                 while True:
                                            if trait5[0] in allele:
                                                       j.append(trait5[0])
                                                       allele.remove(trait5[0])
                                            else:
                                                       break
                                 while True:
                                            if trait5[1] in allele:
                                                       j.append(trait5[1])
                                                       allele.remove(trait5[1])
                                            else:
                                                       break
                                 while True:
                                            if trait6[0] in allele:
                                                       j.append(trait6[0])
                                                       allele.remove(trait6[0])
                                            else:
                                                       break
                                 while True:
                                            if trait6[1] in allele:
                                                       j.append(trait6[1])
                                                       allele.remove(trait6[1])
                                            else:
                                                       break
                                 k=j[0]+j[1]+j[2]+j[3]+j[4]+j[5]+j[6]+j[7]+j[8]+j[9]+j[10]+j[11]
                                 j=[]
                                 punnet.append(k)
                                 punnetreserve.append(k)
                      tablemake()
           ##############SEPTAHYBRID
           elif cross == 7:
                      asktraits()
                      print("Though all the traits are used, you need to specify the order of traits.\n")
                      trait1 = input("Trait 1->")
                      trait2 = input("Trait 2->")
                      trait3 = input("Trait 3->")
                      trait4 = input("Trait 4->")
                      trait5 = input("Trait 5->")
                      trait6 = input("Trait 6->")
                      trait7 = input("Trait 7->")
                      trait = trait1
                      deftrait()
                      trait1= trait
                      trait = trait2
                      deftrait()
                      trait2= trait
                      trait = trait3
                      deftrait()
                      trait3= trait
                      trait = trait4
                      deftrait()
                      trait4= trait
                      trait = trait5
                      deftrait()
                      trait5= trait
                      trait = trait6
                      deftrait()
                      trait6= trait
                      trait = trait7
                      deftrait()
                      trait7= trait
                      print("Loading, please wait...")
                      time.sleep(1)
                      for p1 in trait1:
                                 for p2 in trait2:
                                            for p3 in trait3:
                                                       for p4 in trait4:
                                                                  for p5 in trait5:
                                                                             for p6 in trait6:
                                                                                        for p7 in trait7:
                                                                                                   gamete.append(p1+p2+p3+p4+p5+p6+p7)
                      for p1 in gamete:
                                 for p2 in gamete:
                                            _punnet.append(p1+p2)
                      allele = []
                      j=[]
                      k=[]
                      for i in _punnet:
                                 allele = ([*i])
                                 while True:
                                            if trait1[0] in allele:
                                                       j.append(trait1[0])
                                                       allele.remove(trait1[0])
                                            else:
                                                       break
                                 while True:
                                            if trait1[1] in allele:
                                                       j.append(trait1[1])
                                                       allele.remove(trait1[1])
                                            else:
                                                       break
                                 while True:
                                            if trait2[0] in allele:
                                                       j.append(trait2[0])
                                                       allele.remove(trait2[0])
                                            else:
                                                       break
                                 while True:
                                            if trait2[1] in allele:
                                                       j.append(trait2[1])
                                                       allele.remove(trait2[1])
                                            else:
                                                       break
                                 while True:
                                            if trait3[0] in allele:
                                                       j.append(trait3[0])
                                                       allele.remove(trait3[0])
                                            else:
                                                       break
                                 while True:
                                            if trait3[1] in allele:
                                                       j.append(trait3[1])
                                                       allele.remove(trait3[1])
                                            else:
                                                       break
                                 while True:
                                            if trait4[0] in allele:
                                                       j.append(trait4[0])
                                                       allele.remove(trait4[0])
                                            else:
                                                       break
                                 while True:
                                            if trait4[1] in allele:
                                                       j.append(trait4[1])
                                                       allele.remove(trait4[1])
                                            else:
                                                       break
                                 while True:
                                            if trait5[0] in allele:
                                                       j.append(trait5[0])
                                                       allele.remove(trait5[0])
                                            else:
                                                       break
                                 while True:
                                            if trait5[1] in allele:
                                                       j.append(trait5[1])
                                                       allele.remove(trait5[1])
                                            else:
                                                       break
                                 while True:
                                            if trait6[0] in allele:
                                                       j.append(trait6[0])
                                                       allele.remove(trait6[0])
                                            else:
                                                       break
                                 while True:
                                            if trait6[1] in allele:
                                                       j.append(trait6[1])
                                                       allele.remove(trait6[1])
                                            else:
                                                       break
                                 while True:
                                            if trait7[0] in allele:
                                                       j.append(trait7[0])
                                                       allele.remove(trait7[0])
                                            else:
                                                       break
                                 while True:
                                            if trait7[1] in allele:
                                                       j.append(trait7[1])
                                                       allele.remove(trait7[1])
                                            else:
                                                       break
                                 k=j[0]+j[1]+j[2]+j[3]+j[4]+j[5]+j[6]+j[7]+j[8]+j[9]+j[10]+j[11]+j[12]+j[13]
                                 j=[]
                                 punnet.append(k)
                                 punnetreserve.append(k)
                      tablemake()
           ##############ELSE:
           else:
                      print("Please check and select a cross again..")
                      time.sleep(1)
                      continue
           select = input("\n\nPress\ng to check genotype ratio,\np to check phenotype ratio\nany other button to make a new cross.\n")
           if select == 'p' or select == 'P':
                      pass###
           elif select == 'g' or select == 'G':
                      genotype()
                      
           
           
           

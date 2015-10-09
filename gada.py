#!/usr/bin/python
#
#  [Program]
#
#  GADA 0.01
#  Generator Automatic Dictionaries Advanced
#
#
#
#  [Author]
#
#  Roberto Espinosa (Rochesto)
#
#
#  [License]
#
#GGNU GENERAL PUBLIC LICENSE  Version 2
###

import sys
import os
import ConfigParser

# Config options
charsBool = False
datesBool = False
capitalBool = False
randomBool = False
mixBool = False

# Reading configuration file...
config = ConfigParser.ConfigParser()
config.read('gada.cfg')

years = config.get('years', 'years').split(',')
chars = config.get('specialchars', 'chars').split(',')

numfrom = config.getint('nums','from')
numto = config.getint('nums','to')

wcfrom = config.getint('nums','wcfrom')
wcto = config.getint('nums','wcto')

limit = config.getint('nums','limit')

def modifyDic():
    print(mixBool)
    fajl = open(sys.argv[-1], "r")
    
    listic = fajl.readlines()

    linije = 0
    for line in listic:
        linije += 1
        
    listica = []
    for x in listic:
        listica += x.split() #Delete \n

    if linije > limit:
        print "\r\n      *************************************************"	
        print "      *                    \033[1;31mWARNING!!!\033[1;m                 *"
        print "      *         Using large wordlists in some         *"
        print "      *       options bellow is NOT recommended!      *"
        print "      *************************************************\r\n"
    else:
        print "\r\n      *************************************************"	
        print "      *                                               *"
        print "      *      Your dictionary have "+str(linije)+" words           *"
        print "      *                                               *"
        print "      *************************************************\r\n"
        
###    Combine words
    
    if mixBool == True and linije > limit:
        print "\r\n[-] The Maximum number of words configured for concatenation is "+str(limit)
        sure = raw_input("> Do you want to concatenate all words from wordlist? Y/[N]: ").lower()
        if sure != "y":
            exit()

    cont = ['']
    if mixBool == True:
        for cont1 in listica:
            for cont2 in listica:
                if listica.index(cont1) != listica.index(cont2):
                    cont.append(cont1+cont2)
    
###     Especial Chars
    spechars = ['']
    if charsBool == True:
        for spec1 in chars:
            spechars.append(spec1)
            for spec2 in chars:
                spechars.append(spec1+spec2)
                for spec3 in chars:
                    spechars.append(spec1+spec2+spec3)
        
###	Dates and chars
    
    startDate = ['19',  '20']
    kombdate = []
    if datesBool == True:
        if charsBool == True:
            for w in listica:
                for c in chars:
                    for i in startDate:
                        for j in range(100):
                            kombdate.append(i+w+str(j)+c)
            for w in listica:
                for c in chars:
                    for i in startDate:
                        for j in range(100):
                            kombdate.append(c+i+w+str(j))
        for w in listica:
            for i in startDate:
                for j in range(100):
                    kombdate.append(i+w+str(j))
    
    kombinacija1 = list(comb(listica, years))
    kombinacija1 += kombdate ### Add dates
    kombinacija2 = ['']
    if charsBool == True:
        kombinacija2 = list(comb(cont, years))
    kombinacija3 = ['']
    kombinacija4 = ['']
    if charsBool == True:
        kombinacija3 = list(comb(listica, spechars))
        if charsBool == True:
            kombinacija4 = list(comb(cont, spechars))
    kombinacija5 = ['']
    kombinacija6 = ['']
    if randomBool == True:
        kombinacija5 = list(concats(listica, numfrom, numto))
        if charsBool == True:
            kombinacija6 = list(concats(cont, numfrom, numto))
    print("ERROR")
    print "\r\n[+] Now making a dictionary..."

    print "[+] Sorting list and removing duplicates..."

    komb_unique1 = dict.fromkeys(kombinacija1).keys()	
    komb_unique2 = dict.fromkeys(kombinacija2).keys()
    komb_unique3 = dict.fromkeys(kombinacija3).keys()
    komb_unique4 = dict.fromkeys(kombinacija4).keys()
    komb_unique5 = dict.fromkeys(kombinacija5).keys()
    komb_unique6 = dict.fromkeys(kombinacija6).keys()
    komb_unique7 = dict.fromkeys(listica).keys()
    komb_unique8 = dict.fromkeys(cont).keys()

    uniqlist = komb_unique1+komb_unique2+komb_unique3+komb_unique4+komb_unique5+komb_unique6+komb_unique7+komb_unique8

    unique_lista = dict.fromkeys(uniqlist).keys()
    unique_leet = []

    unique_list = unique_lista + unique_leet

    unique_list_finished = []
    for x in unique_list:
        if len(x) > wcfrom and len(x) < wcto:
            unique_list_finished.append(x)

    f = open ( sys.argv[-1]+'.txt', 'w' )
    unique_list_finished.sort()
    f.write (os.linesep.join(unique_list_finished))
    f = open ( sys.argv[-1]+'.txt', 'r' )
    lines = 0
    for line in f:
        lines += 1
    f.close()


    print "[+] Saving dictionary to \033[1;31m"+sys.argv[2]+".txt\033[1;m, counting \033[1;31m"+str(lines)+" words.\033[1;m"
    print "[+] Now load your pistolero with \033[1;31m"+sys.argv[2]+".cupp.txt\033[1;m and shoot! Good luck!"
    fajl.close()
    exit()

# for concatenations...

def concats(seq, start, stop):
    for mystr in seq:
        for num in xrange(start, stop):
            yield mystr + str(num)


# for sorting and making combinations...

def comb(seq, start):
    for mystr in seq:
        for mystr1 in start:
            yield mystr + mystr1
            
def helpMenu():
    print "\n\t\t\033[1;31mUsage:\033[1;m gada.py [Options] -w dictionary\r\n"
    print "	[ Options ]\n"
    print "	-h	--help"
    print "		 Default configuration file in gada.cfg\n"	

    print "	-w	 Use this option to improve existing dictionary,"
    print "		  and modify this.\n"

    print "	-d	 Add dates modifier\n"
    
    print "\t-c   Add especial characters modifier\n"
    
    print "\t-r   Add random numbers\n"
    
    print "\t-C   Capital letters\n"
    
    print "	-v	Version of the program\n"
    exit()
    
### MAIN
if __name__ == "__main__":
    
    if len(sys.argv) < 2 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
       helpMenu()

    elif sys.argv[1] == '-v':
        print "\r\n	\033[1;31m 'gada.py'  v0.01\033[1;m\r\n"
        print "	\033[1;31m >> \033[1;mCreated by Rochesto"
        print "	\033[1;31m >> \033[1;mTake a look docs/README file for more info about the program\r\n"
        exit()


    elif sys.argv[1] > 1:
        
        if len(sys.argv) < 3:
            helpMenu()
        if len(sys.argv) > 8:
            print ("\t\t\033[1;31mToo many arguments\033[1;m")
            helpMenu()
        for i in sys.argv:
            print (i)
            if (i == "-c"):
                charsBool = True
            elif (i == "-d"):
                datesBool = True
            elif(i == "-C"):
                capitalBool = True
            elif (i == "-r"):
                randomBool = True
            elif(i == "-m"):
                print ("oooooo0")
                mixBool = True
                
        modifyDic()

    else:
        helpMenu()

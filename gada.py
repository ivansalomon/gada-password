#!/usr/bin/python

###################################
#                                                                                       #
#  GADA 0.1                                                                      #
#          Generator Automatic Dictionaries Advanced       #
#                                                                                       #
#                                                                                       #
#  Author                                                                          #
#           Roberto Espinosa (Rochesto)                              #
#                                                                                       #
#                                                                                       #
#  License                                                                         #
#            GGNU GENERAL PUBLIC LICENSE  Version 2   #
#                                                                                       #
###################################

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

def main():
    newDict = []
    try:
        file = open(sys.argv[-1], "r")
    except:
        print ("Error: Can't read file.\n")
        print ("File don't exist\n")
        print ("Use -h to help")
        exit()

    lines = file.readlines()

    linije = 0
    for line in lines:
        linije += 1
        
    for x in lines:
        newDict += x.split() #Delete \n
    
    print "\r\n      *************************************************"	
    print "      *                                               *"
    if linije > limit:
        print "      *                                               *"
        print "      *                    \033[1;31mWARNING!!!\033[1;m                 *"
        print "      *         Using large wordlists in some         *"
        print "      *       options bellow is NOT recommended!      *"
        print "      *                                               *"
    print "               Your dictionary have "+str(linije)+" words           "
    print "      *                                               *"
    print "      *************************************************\r\n"
        
###    Combine words
    
    if linije > limit:
        print "\r\n[-] The Maximum number of words configured for concatenation is "+str(limit)
        sure = raw_input("> Do you want to concatenate all words from wordlist? Y/[N]: ").lower()
        if sure != "y":
            exit()
### Concat words
    conc = []
    if mixBool == True:
        for conc1 in newDict:
            for conc2 in newDict:
                if newDict.index(conc1) != newDict.index(conc2):
                    conc.append(conc1+conc2)

###     Especial Chars
    spechars = []
    if charsBool == True:
        for char1 in chars:
            spechars.append(char1)
            for char2 in chars:
                spechars.append(char1+char2)
                for char3 in chars:
                    spechars.append(char1+char2+char3)

###	Dates
    
    startDate = ['19',  '20']
    endDate = []
    if datesBool == True:
        for i in range(100):
            endDate.append(str(i).zfill(2))
            
###    CApital Letters
    
    capitals = []
    if capitalBool == True:
        for i in newDict:
            capitals.append(i.title())
        if mixBool == True:
            tmp = []
            for conc1 in capitals:
                for conc2 in capitals:
                    if capitals.index(conc1) != capitals.index(conc2):
                        tmp.append(conc1+conc2)
            capitals += tmp
    
###    combinations 
    list0, list1, list2, list3, list4, list5 = [],  [],  [],  [], [],  []
    list0 = list(comb(newDict,  years,  True))
    list0 += list(comb(newDict,  years,  False))
    
    if mixBool == True:
        list1 = list(comb(newDict, conc,  True))

    if charsBool == True:
        list2 = list(comb(newDict,  spechars,  True))
        list2 += list(comb(list2, chars, False))
        list2 += list(comb(newDict,  spechars,  False))

    if datesBool == True:
        list3 = list(comb(newDict,  startDate,  True))
        list3 = list(comb(list3,  endDate,  False) )
        
    if capitalBool == True:
        list4 = capitals
        
    if randomBool == True:
        for i in range(numfrom,  numto):
            for j in newDict:
                list5.append(j+str(i))
                list5.append(str(i)+j)

    print "\n[+] Making a dictionary..."

    print "[+] Sorting out list and removing duplicates..."
    
    komb_unique1 = dict.fromkeys(list1).keys()    
    komb_unique2 = dict.fromkeys(list2).keys()
    komb_unique3 = dict.fromkeys(list3).keys()
    komb_unique4 = dict.fromkeys(list4).keys()
    komb_unique5 = dict.fromkeys(list5).keys()
    komb_unique6 = dict.fromkeys(capitals).keys()
    komb_unique7 = dict.fromkeys(newDict).keys()
    komb_unique8 = dict.fromkeys(conc).keys()

    uniqlist = komb_unique1+komb_unique2+komb_unique3+komb_unique4+komb_unique5+komb_unique6+komb_unique7+komb_unique8

    unique_list = dict.fromkeys(uniqlist).keys()

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

    print "[+] Saving dictionary to \033[1;31m"+sys.argv[-1]+".txt\033[1;m.\n[+] Words: \033[1;31m"+str(lines)+".\033[1;m"
    file.close()
    exit()

# for concatenations...

def concats(seq, start, stop):
    for mystr in seq:
        for num in xrange(start, stop):
            yield mystr + str(num)


# for sorting and making combinations...

def comb(seq, start,  inv):
    for mystr in seq:
        if inv == False:
            for mystr1 in start:
                yield mystr + mystr1
        else:
            for mystr1 in start:
                yield mystr1 + mystr
            
def helpMenu():
    print "\n\t\t\033[1;31mUsage:\033[1;m gada.py [Options] dictionary\r\n"
    print "\tDefault configuration file in \033[1;31m gada.cfg \033[1;m\n"	
    print "	[ Options ]\n"
    print "	-h	--help"

    print "	-d	 Add dates modifier\n"
    
    print "\t-c   Add especial characters modifier\n"
    
    print "\t-n   Add numbers\n"
    
    print "\t-C   Capital letters\n"
    
    print "\t-all  Add all modifiers\n"
    
    print "	-v	Version of the program\n"
    exit()
    
### MAIN
if __name__ == "__main__":
    
    if len(sys.argv) < 2 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
       helpMenu()

    elif sys.argv[1] == '-v':
        print "\r\n	\033[1;31m 'gada.py'  v0.1\033[1;m\r\n"
        print "	\033[1;31m >> \033[1;mCreated by Rochesto"
        print "	\033[1;31m >> \033[1;mTake a look docs/README file for more info about the program\r\n"
        exit()


    elif sys.argv[1] > 1:
        
        if len(sys.argv) < 2:
            helpMenu()
        if len(sys.argv) > 8:
            print ("\t\t\033[1;31mToo many arguments\033[1;m")
            helpMenu()
        for i in sys.argv:
            if (i == "-c"):
                charsBool = True
            elif (i == "-d"):
                datesBool = True
            elif(i == "-C"):
                capitalBool = True
            elif (i == "-n"):
                randomBool = True
            elif(i == "-m"):
                mixBool = True
            elif (i == "-all") or (i == "all"):
                charsBool = True
                datesBool = True
                capitalBool = True
                randomBool = True
                mixBool = True
        main()

    else:
        helpMenu()

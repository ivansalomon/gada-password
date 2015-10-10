#! /usr/bin/python

str = ""

tamano = len(str)

f = open("dictionary.dic",  "w")


for i in range(tamano):
    if str[i] == " ":
        f.write("\n")
    else:
        if str[i] != " " and str[i] != "\t":
            f.write(str[i])
 


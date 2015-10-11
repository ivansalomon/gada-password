#! /usr/bin/python

###     Variables
content = ""
text = ""

###     Functions

# Transform text in string
def parseText(file):
    text = ""
    tamano = len(file)
    for i in range(tamano):
        if file[i] == "," or file[i] == "." or file[i] == "\n":
            text += " "
        else:
            text += file[i]
    return text

def parseStr(text):
    tamano = len(text)
    for i in range(tamano):
        if text[i] == " ":
            f.write("\n")
        else:
            if text[i] != " " and text[i] != "\t" and text[i] != "\n":
                f.write(text[i])

print (">>    Menu    <<")
print ("1. Read File")
print ("2. Manually entered words")
op = ""
while op != "1" and  op != "2":
    op = raw_input(">> ")

if op == "1":
    readOk = False
    while readOk == False:
        fileRead = raw_input("Intruduce path to file >> ")
        try:
            with open(fileRead,  "r") as f:
                content = f.readlines()
            readOk = True
        except:
            print ("Can't read file. Try againt")
    text = parseText(content)
    
elif op == "2":
    text = raw_input("Introduce words (Separated by space) >> ")

###     Create file
fileName = raw_input("Introduce name for new Dictionary >> ")
try:
    f = open("dictionaries/"+fileName+".dic",  "w")
except:
    print ("Can't create file.\n Check system permissions")
    exit()

parseStr(text)
    

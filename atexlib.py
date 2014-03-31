def parseSeq(infile, outfile, charOpen, charClose, parenOpen, parenClosed, control):
    oldPos=0
    passVar=False
    math=False
    paren=False
    thmline=infile.readline()
    while(thmline[0]== " "):
        thmline=remLeadWhite(thmline)
        for i in range(0, len(thmline)):
            if passVar:
                passVar=False
                if thmline[i]==control:
                    outfile.write("\\")
                else: 
                    outfile.write(thmline[i])
            elif(not thmline[i]== charOpen) and (not thmline[i]==charClose) and (not thmline[i]==control) and (not thmline[i]==parenOpen) and (not thmline[i]==parenClosed):
                outfile.write(thmline[i])
            elif thmline[i]==control:
                outfile.write("\\")
                passVar=True
            elif thmline[i]==charOpen or thmline[i]==charClose or thmline[i]==parenOpen or thmline[i]==parenClosed:
                if math and paren:
                    outfile.write("}")
                    paren=False
                elif math and (not paren) and (thmline[i]==parenOpen):
                    outfile.write("{")
                    paren=True
                elif math and (not paren):
                    outfile.write("$")
                    math=False
                elif (not math):
                    outfile.write("$")
                    math=True
        oldPos=infile.tell()
        thmline=infile.readline()
    infile.seek(oldPos)
def parseTex(infile, outfile):
    oldPos=0
    thmline=infile.readline()
    while(thmline[0]==" "):
        thmline=remLeadWhite(thmline)
        outfile.write(thmline)
        oldPos=infile.tell()
        thmline=infile.readline()
    infile.seek(oldPos)
def parseCmd(outfile, fields):
    if(len(fields)==3):
        outfile.write("\\newcommand{\\"+fields[1]+"}{\\"+fields[2]+"}\n")
    else:
        outfile.write("\\newcommand{\\"+fields[1]+"}["+fields[2]+"]{\\"+fields[3]+"}\n")
def remLeadWhite(word):
    count=0
    for i in range(0,len(word)):
        if(word[i]==" "):
            count+=1
        else:
            break;
    return word[count:]

def fileExt(f):
    return f[:-4]+".tex"

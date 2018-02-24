#!/usr/bin/env python3

def prepareln(line):
    from string import ascii_uppercase as charset
    line = line.upper() # make uppercase
    nline = ''
    for chr in line:#( line and charset): 
        if chr not in charset: continue
        nline += chr + ' ' # remove chars that are not in charset and add a space between letters
    #nline=nline[:-1] # remove trailing space
    return nline

def squareln(line):
    #N=len(line)
    line=prepareln(line)
    square=""
    N=len(line)//2
    for i in range(N): square+=(line+line)[2*i:2*(N+i)] + '\n'
    return square

def reverselines(lines):
    lst = lines.splitlines()
    lst.reverse()
    block = ""
    for line in lst: block += line + "\n"
    return block

def shiftlines(lines, n=1):
    lst = lines.splitlines()
    block=''
    for line in lst: block += ( n * ' ' ) + line + '\n'
    return block

def diamondln(line):
    line=prepareln(line)
    tmp=line[:-2]
    block=triangln(tmp)
    block=shiftlines(block)
    return block + line + '\n' + reverselines(block)

def triangln(line):
    line=prepareln(line)
    shape=''
    N=len(line)//2
    for i in range(N):
        ln = line[0:1+2*i]
        pad = (2*N+len(ln))//2 #(len(ln)+N-1)//2
        #print ("[{0}],{1}".format(ln,pad))
        shape+=ln.rjust(pad,' ') + '\n'
    return shape

# interactive script
if __name__ == "__main__":
    try:
        while True:
            sqr=squareln(input("line> "))
            print("\n{0}\n".format(sqr))
    except KeyboardInterrupt or EOFError: 
        print("\n\nExiting for KeyboardInterrupt")
        exit(0)
    ### Uncomment only one of the following
    pass                                  ## DEBUG
    #except: print("Exception occurred")   ## PRE RELEASE
    #except: pass                          ## PRODUCTION ONLY

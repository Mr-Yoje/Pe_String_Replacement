# !/usr/bin/env python
# -*- coding:utf-8 -*- 
import sys,os
#print(sys.argv)
if sys.argv[1]=="-help":
    print("[filepath] [start] [end] [strings]")
else:
    FilePath='/'.join(sys.argv[1].split('\\'))
    Start=int(sys.argv[2],16)
    End=int(sys.argv[3],16)
    OriStrLen=End-Start+1
    Strings=sys.argv[4].encode('gbk')
    StrLen=len(Strings)
    #print(FilePath,Start,End,Strings)
    NewFilePath=os.path.abspath('.')+"\\new."+FilePath.split(".")[1]
    #print(NewFilePath)
    #print(StrLen,OriStrLen)
    if StrLen < OriStrLen:
        f1=open(FilePath,"rb+")
        f2=open(NewFilePath,"wb+")
        s=f1.read()
        f2.write(s)
        f1.close()
        f2.close()
        f=open(NewFilePath,"rb+")
        f.seek(Start,0)
        FillStrings=sys.argv[4]+" "*(OriStrLen-StrLen)
        bytes_FillStrings=FillStrings.encode('gbk')
        f.write(bytes_FillStrings) 
        f.close()
        print("OK")
    else:
        print("eroor") 








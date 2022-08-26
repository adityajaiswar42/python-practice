try:
    fbj=open("venkiii.txt","r")
    #fbj.write("Hello file handling")
    adi=fbj.readlines()
except IOError:
    print("File is not found in folder")
else:
    #adi=fbj.readlines()
    print("new file name is:",adi)
    fbj.close()
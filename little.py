while 1:
    filename=input('Please input the filename: ')
    try :
        if filename=='break' or int(filename)<0:
            break

        filedata=open(filename,'rb')
    except:
        continue
    li=[]
    res=''
    for i in filedata:
        s=str(i).split('<h1>')
        if len(s)>1:
            res=s[1][0:6]
    print(res)


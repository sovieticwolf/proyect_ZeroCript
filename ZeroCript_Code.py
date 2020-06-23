import os,sys,time
print("MMMMMMMMMMMMMMMMNOl;..       .;oONMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMXx,  .,coddddoc,.  ,xNMMMMMMMMMMMMMM\nMMMMMMMMMMMMM0;  .o0WMMMMMMMMN0o'  ;0WMMMMMMMMMMMM\nMMMMMMMMMMMM0,  cKMMMMMMMMMMMMMMKc  ,0MMMMMMMMMMMM\nMMMMMMMMMMMNc  :XMMMMMMMMMMMMMMMMX:  cNMMMMMMMMMMM\nMMMMMMMMMMM0' .xMMMMMMMMMMMMMMMMMMx. '0MMMMMMMMMMM\nMMMMMMMMMMMO' .kMMMMMMMMMMMMMMMMMMk. '0MMMMMMMMMMM\nMMMMMMMMMMMO. .kMMMMMMMMMMMMMMMMMMk. 'OMMMMMMMMMMM\nMMMMMMMMMMMO' .kMMMMMMMMMMMMMMMMMMk. 'OMMMMMMMMMMM\nMMMMMMMMMMM0' .kMMMMMMMMMMMMMMMMMMk. 'OMMMMMMMMMMM\nMMMMMMMMWXOl. .cxxxxxxxxxxxxxxxxxx:. .lOXWMMMMMMMM\nMMMMMMMXo.                              .oXMMMMMMM\nMMMMMMWl  'dkkkkkkkkkkkkkkkkkkkkkkkkkko'  lWMMMMMM\nMMMMMMX:  oWMMMMMMMMMMMMMMMMMMMMMMMMMMWo  :XMMMMMM\nMMMMMMX:  oWMMMMMMMMMMWOddOWMMMMMMMMMMWo  :XMMMMMM\nMMMMMMX:  oWMMMMMMMMMM0'  '0MMMMMMMMMMWo  :XMMMMMM\nMMMMMMX:  oWMMMMMMMMMMO.  .OMMMMMMMMMMWo  :XMMMMMM\nMMMMMMX:  oWMMMMMMMMM0;    ;0MMMMMMMMMWo  :XMMMMMM\nMMMMMMX:  oWMMMMMMMMWl      lWMMMMMMMMWo  :XMMMMMM\nMMMMMMX:  oWMMMMMMMMW0:....:0MMMMMMMMMWo  :XMMMMMM\nMMMMMMX:  oWMMMMMMMMMMWXKKXWMMMMMMMMMMWo  :XMMMMMM\nMMMMMMX:  oWMMMMMMMMMMMMMMMMMMMMMMMMMMWo  :XMMMMMM\nMMMMMMNc  :KWNWWNNWNNWWWWWWWNNWWNNNNWNK:  cNMMMMMM\nMMMMMMWO'  .''''''''''''''''''''''''''.  'OWMMMMMM\nMMMMMMMWO:.                            .:OWMMMMMMM")
print("▀█ █▀▀ █▀█ █▀█ █▀▀ █▀█ █ █▀█ ▀█▀   █░█ █▀█ ░ █░█\n█▄ ██▄ █▀▄ █▄█ █▄▄ █▀▄ █ █▀▀ ░█░   ▀▄▀ █▄█ ▄ ▀▀█")
print("bienvenido al sistema de encriptacion seguro , mientras mas largo\n el archivo mas seguro sera el esconder adecuadamente la infomación")
def main():
    inputfilename='libro.txt'
    outputfilename='libro.encriptado.txt'
    desencriptado='libro.desencriptado.txt'
    mykey=int(input('introduce la llave a usar >>>>'))
    mymode=input('introduce (E)ncriptar o (D)esencriptar >>>>')
    if mymode.upper()=="E":
        mymode="Encript"
    elif mymode.upper()=="D":
        mymode="Desencript"
    elif mymode.upper()!= "E" or "D":
        print("opcion incorrecta , re-iniciando el programa")
        main()
    if not os.path.exists(inputfilename):
        print('el archivo %s no existe ,terminando el programa....'%(inputfilename))
        sys.exit()
    if os.path.exists(outputfilename):
        print('esto sobreescribira en el archivo %s \n(C)ontinuar (Q)quitar'%(outputfilename))
        response=input('>>>')
        if not response.lower().startswith('c'):
            sys.exit()
    fileobj=open(inputfilename)
    content=fileobj.read()
    fileobj.close()
    
    print("%ando...."%(mymode.title()))
    starttime=time.time()
    if mymode=='Encript':
        translated=encriptMessage(mykey,content)
        outputfileobj=open(outputfilename,'w')
        outputfileobj.write(translated)
        outputfileobj.close()
    elif mymode=="Desencript":
        file=open(outputfilename)
        content=file.read()
        file.close()
        translated=decriptmessage(mykey,content)
        outputfileobj=open(desencriptado,'w')
        outputfileobj.write(translated)
        outputfileobj.close()
    totaltime=round(time.time()-starttime,2)
    print('%so tiempo:%s segundos'%(mymode.title(),totaltime))

    print('terminado %sado %s(%s caracteres usados).'%(mymode,inputfilename,len(content)))
    print("%sado archivo como %s"%(mymode.title(),outputfilename))
    
    print("¿¿quieres intentarlo de nuevo??")
    seleccion=input('>>S o N>>>')
    if seleccion.upper()=='S':
        main()
    else:
        sys.exit()

def encriptMessage(key,message):
    ciphertext=['']*key
    for column in range(key):
        currentIndex=column
        while currentIndex<len(message):
            ciphertext[column]+=message[currentIndex]
            currentIndex+=key
    return''.join(ciphertext)

def decriptmessage(key,message):
    numofcolumns=int(math.ceil(len(message)/float(key)))
    numofrows=key
    numofshadedboxes=(numofcolumns*numofrows)-len(message)
    plaintext=['']*numofcolumns
    column=0
    row=0
    for symbol in message:
        plaintext[column]+=symbol
        column+=1
        if(column==numofcolumns)or(column==numofcolumns-1 and row>=numofrows-numofshadedboxes):
            column=0
            row+=1
    return''.join(plaintext)

main()


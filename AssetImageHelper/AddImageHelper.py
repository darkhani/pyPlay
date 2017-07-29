#Image to Asset Helper
#Creat : HIT
#For Swift3 Asset

import os,sys
os.system('rm .DS_Store') 
onlyfiles = [f for f in os.listdir('./') if os.path.isfile('./'+f)]
for fileName in onlyfiles:
    removeExt = fileName.split('.')
    cLog = 'removeExt : '+removeExt[0]
    print(cLog)
    removeAt = fileName.split('@')
    cFolderName = './'+removeAt[0]+ '.imageset'
    cLog = 'cFolderName : ' + cFolderName
    print(cLog)
    if not os.path.exists(cFolderName):
        os.makedirs(cFolderName)
        copyString2 = 'cp '+removeAt[0]+'@2x.png '+ cFolderName+'/'
        os.system(copyString2)
        copyString3 = 'cp '+removeAt[0]+'@3x.png '+ cFolderName+'/'
        os.system(copyString3)
        cLog = 'try create file : ' + removeAt[0] + '/Contents.json'
        print(cLog)
        os.system('touch '+cFolderName+'/Contents.json')
        file = open(cFolderName+'/Contents.json',"w")
        file.write("{\n")
        file.write("\"images\" : [\n")
        file.write("{\n")
        file.write("\"idiom\" : \"universal\",\n")
        file.write("\"scale\" : \"1x\"\n")
        file.write("},\n")
        file.write("{\n")
        file.write("\"idiom\" : \"universal\",\n")
        file.write("\"filename\" : \""+removeAt[0] + "@2x.png\",\n")
        file.write("\"scale\" : \"2x\"\n")
        file.write("},\n")
        file.write("{\n")
        file.write("\"idiom\" : \"universal\",\n")
        file.write("\"filename\" : \""+removeAt[0] + "@3x.png\",\n")
        file.write("\"scale\" : \"3x\"\n")
        file.write("}\n")
        file.write("],\n")
        file.write("\"info\" : {\n")
        file.write("\"version\" : 1,\n")
        file.write("\"author\" : \"xcode\"\n")
        file.write("}\n")
        file.write("}\n")
        file.close()
    # else:
    #     copyString3 = 'cp '+removeAt[0]+'@3x.png '+ cFolderName+'/'
    #     os.system(copyString3)
    #     print("... : " +copyString )       
print(onlyfiles)
os.system('rm -rf imageHelper.py.imageset')
os.system('mkdir temp')
os.system('mv *.imageset ./temp/')
import os
path=input("Enter location:")
music=['.mp3']
video=['.mp4','.mkv','.3gp']
document=['.doc','.docx','.pdf']
compress=['.zip','.rar','.gz']
image=['.jpg','.png','.gif']
for i in os.listdir(path):
    print(i)
    if os.path.isfile(path+"/"+i):
        for j in music:
            if i.endswith(j):
                if os.path.exists(path+'/'+'Music'):
                    pass
                else:
                    os.mkdir(path+'/'+'Music')
                os.rename(path+'/'+i,path+'/'+'Music/'+i)
        for j in video:
            if i.endswith(j):
                if os.path.exists(path+'/'+'Video'):
                    pass
                else:
                    os.mkdir(path+'/'+'Video')
                os.rename(path+'/'+i,path+'/'+'Video/'+i)
        for j in document:
            if i.endswith(j):
                if os.path.exists(path+'/'+'Document'):
                    pass
                else:
                    os.mkdir(path+'/'+'Document')
                os.rename(path+'/'+i,path+'/'+'Document/'+i)
        for j in compress:
            if i.endswith(j):
                if os.path.exists(path+'/'+'Compress'):
                    pass
                else:
                    os.mkdir(path+'/'+'Compress')
                os.rename(path+'/'+i,path+'/'+'Compress/'+i)
        for j in image:
            if i.endswith(j):
                if os.path.exists(path+'/'+'Image'):
                    pass
                else:
                    os.mkdir(path+'/'+'Image')
                os.rename(path+'/'+i,path+'/'+'Image/'+i)
    else:
print("MOVING SUCCESSFUL")
                    
        
        
        
        


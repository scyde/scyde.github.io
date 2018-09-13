import os
import glob
path = './'
files = glob.glob('*[jJ]*')
print(files)
i = 1
for file in files:
    os.rename(file,str(i)+'.jpg')
    i = i+1

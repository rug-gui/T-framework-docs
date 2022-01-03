
import os

# specify your path of directory
path = r"md/"

# call listdir() method
# path is a directory of which you want to list
directories = os.listdir( path )
mdlist=[]
# This would print all the files and directories
for file in directories:
   print("Recd. "+file)
   mdlist.append(file)
  
print(mdlist)
    

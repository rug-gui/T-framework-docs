
import os

# specify your path of directory
path = r"md/"

# call listdir() method
# path is a directory of which you want to list
directories = os.listdir( path )
mdlist=[]
# This installs all the dependencies on build machine
def install_dependencies():
   os.system('pip install markdown')
   print('Requirements Complete')
   
def perform_cleanup():
   #remove build.py andother md files
   print('Deployment Complete')
   
install_dependencies()
'''# For Hosting on Personal Server
perform_cleanup()'''
# This would print all the files and directories
for file in directories:
   print("Recd. "+file)
   mdlist.append(file)
   
print(mdlist)
import markdown
html = markdown.markdown('This is a *test* string')
print(html)
with open("md/readme.md", "r", encoding="utf-8") as input_file:
    text = input_file.read()
html = markdown.markdown(text)
with open("docs/index.html", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
    output_file.write(html)

    

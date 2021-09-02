import shutil
import os

#set where the source of the files are
source = 'C:/Users/whalt/Desktop/Folder A/'

#set the destination path to folder B
destination = 'C:/Users/whalt/Desktop/Folder B/'
files = os.listdir(source)

for i in files:
    #we are saying move the files represented by 'i' to their new destination
    shutil.move(source+i, destination)

    #Importing shutil and time package
import shutil
try:
    print("Copying File")
    #Provide the path to the file which you want to copy
    src = "Path-to-file"
    #Provide path to the destination folder
    dst = "destination-path-where-we-want-to-save-the-file"
    #Using shutil's .copy() function which 
    #include source and destination path
    shutil.copy(src,dst)
    print("Successfully Completed")
except:
    print("Unsuccessful!! Error Generated")

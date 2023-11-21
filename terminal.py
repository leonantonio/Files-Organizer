import shutil
import os
'''
Antonio Leon
10/14/2023
Folder Organizer Terminal Version
'''
#Defining source and destination paths variables.
userInput = input("Please enter the folder SOURCE path: ")
userInput = userInput.replace('"', '').replace("'", '')
src = userInput

userInput = input("Please enter the folder DESTINATION path: ")
userInput = userInput.replace('"', '').replace("'", '')
dst = userInput

def move_jpg():  
        
    try: 
        for filename in os.listdir(src):
            if filename.endswith('.jpg') or filename.endswith('jpeg') or filename.endswith('JPG'):
                src_file = os.path.join(src, filename)
                dst_file = os.path.join(dst, filename)
                    
                #Move file src to folder destination to dst.
                shutil.move(src_file, dst_file)
                    
    except FileNotFoundError:
        print("File jpg not found")
    
def move_mp4():
    
    try:
        for filename in os.listdir(src):
            if filename.endswith('.mp4'):
                src_file = os.path.join(src, filename)
                dst_file = os.path.join(dst, filename)
                
                #Move file src to folder destination to dst.
                shutil.move(src_file, dst_file)
                
    except FileNotFoundError:
        print("File mp4 not found")

while True:
    user = input("What would you like to do?: ")
    if user == "1":
        move_jpg()
    elif user == "2":
        move_mp4()
    elif user == "9":
        break
    else:
        print("Wrong input!")
        
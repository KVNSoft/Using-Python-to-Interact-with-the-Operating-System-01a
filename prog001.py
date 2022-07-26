import os

def create_python_script(filename):
    #PATH01 = "D:\\Prog001\\Google02_Using_Python_to_Interact_OS\\01"
    PATH01 = os. getcwd()
    PATH02 = os.path.join(PATH01, filename)
    #PATH02 = PATH01 +  + filename
    comments = "# Start of a new Python program"
    
    
    with open(PATH02, "w") as file01:
        file01.write(comments)

    
    filesize = os.path.getsize(PATH02)
    
    return(filesize)

print(create_python_script("program.py"))
import os
import string

#task 1

path = r"c:\Users\bekza\OneDrive\Документы\project"
all = list(os.listdir(path))
print(all)

#task 2

def check(path):
    if not os.path.exists(path):
        print(f"{path} exists")

        if os.access(path,os.R_OK):
            print(f"{path} is readable.")
        else:
            print(f"{path} is not readable.")
        if os.access(path,os.W_OK):
            print(f"{path} is writable.")
        else:
            print(f"{path} is not writable.")
        if os.access(path,os.X_OK):
            print(f"{path} is executable.")
        else:
            print(f"{path} is not executable.")
    else:
        print(f"{path} does not exist.")

path=r"c:\Users\bekza\OneDrive\Документы\project"
check(path)

#task 3

def analyze_path(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
        
        filename = os.path.basename(path)
        directory = os.path.dirname(path)

        print(f"Filename: {filename}")
        print(f"Directory: {directory}")
    else:
        print(f"The path '{path}' does not exists.")

path=r"c:\Users\bekza\OneDrive\Документы\project"
analyze_path(path)


#task 4

with open("text.txt") as f:
    data = f.read()  

print(len(list(data.split("\n"))))
f.close()

#task 5

def write_list_to_file(file_path,data):
    try:
        with open (file_path,'w') as file:
            for item in data:
                file.write(str(item)+ '\n')
        print(f"List has been written to '{file_path}' successfully.")

    except Exception as e:
        print(f"Error: {e}")
        
file_path="text.txt"
data= ["apple",'ananas',"orange","Grapes"]
write_list_to_file(file_path,data)


#task 6

def generate_text_files():
    filenames = [f"{letter}.txt" for letter in string.ascii_uppercase]

    for filename in filenames:
        try:

            with open(filename,'w') as file:
                print(f"File '{filename}' created successfully.")

        except Exception as e:
            print(f"Error creating file '{filename}': {e}")
generate_text_files()

#task 7 

def copy_file(file1,file2):

    try:
        with open(file1,'r') as copy: 
            cop=copy.read()
        with open (file2,'w') as copy:
            copy.write(cop)

    except FileNotFoundError:
        print(f"Error: File '{cop}' not found.")

    except Exception as e:
        print(f"Error: {e}")

file1="text.txt"
file2="text2.txt"
copy_file(file1,file2)

#task 8

def delete(file):
    try:
        if not os.path.exists(file):
            print(f"Error: File '{file}' does not exist.")
            return 
        
        if not os.access(file,os.F_OK):
            print(f"Error: No access to '{file}'.")
            return

        os.remove(file)
        print(f"File '{file}' has been deleted successfully.")
    
    except Exception as e:
        print(f"Error: {e}")
path="text3.txt"
delete(path)
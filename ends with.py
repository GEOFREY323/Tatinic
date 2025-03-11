filename=input("Enter a file name: ")
if filename.endswith(".txt"):
    print(filename)
else:
    print("File must end with txt") 
try:      
    names=open("Traitz.txt","r")  
    file=names.read()
    print(file)
except FileNotFoundError:   
    print("file does not exist")   


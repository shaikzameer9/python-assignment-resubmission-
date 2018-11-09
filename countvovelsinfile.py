
fileName = input("enter the file name: ").strip()

infile = open(fileName, "r")

vowels = set("AEIOUaeiou")


countV = 0

for c in infile.read():
    if c in vowels:
        countV += 1
   
print("Total no of vovels in file is: ",countV)

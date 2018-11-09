fileName = input("Enter the file to check: ").strip()
infile = open(fileName, "r")
vowels = set("A E I O U a e i o u")
countV = 0
for c in infile.read():
    if c in vowels:
        countV += 1

print("The number of Vowels is: ",countV)
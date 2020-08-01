#Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case.


fname = input("Enter file name: ")
fh = open(fname)

for fx in fh:
    fy = fx.rstrip()
    print(fy.upper())

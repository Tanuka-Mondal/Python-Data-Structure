"""
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below. 
"""

#-----------------------------------------------------------------------------------------------------------------


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

d=dict()
for line in handle:
    if not line.startswith("From "): 
        continue
    else:    
        line=line.split()
        line=line[5]
        line=line[0:2]
        d[line]=d.get(line,0)+1

lst=list()        
for value,count in d.items():
    lst.append((value,count))

lst.sort()
for value,count in lst:
    print (value,count)

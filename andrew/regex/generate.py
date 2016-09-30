import random
import string
domains = ['@stcloudstate.edu', '@gmail.com', '@hotmail.com', '@aol.com', '@netzero.com', '@fbi.gov']
file = open('testfile.html', 'w')

numRecords = 1000

for i in range(numRecords):
    rand = random.random()
    email = ""
    if rand < 0.5:
        #OldSchool
        for j in range(0,4):
            email += string.ascii_lowercase[random.randrange(0,26)]
        for k in range(0,4):
            email += str(random.randrange(0,10))
    else:
        #newSchool
        for j in range(random.randrange(8,12)):
            email += string.ascii_lowercase[random.randrange(0,26)]
    
    
    email += domains[random.randrange(0,len(domains))]

    file.write((email + ' '))

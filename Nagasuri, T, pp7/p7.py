#Name:Tanmayi Nagasuri
#Email: nagasurit@slu.edu
#1 May 2016
# CSCI 1300 Section 01
#Instructor: Judy Etchison
#Sources consulted: textbook, stackoverflow.com
#Honor Code Statement: In keeping with the honor code policies of Saint Louis University
#the Department of Mathematics and Computer Science, I affirm that I have neither 
#give not received assistance on this programming assignment. This assignment
#represents my individual, original effort. 



from pp7 import *
#imports from file containing functions

filename = raw_input('Enter a file name to be checked: ')
fi = file(filename)
#asks user for file name to be checked and casts as file

f = filename.split('.')
fn = f[0] + 'Chk' + '.txt'
#renames file to add 'Chk' to the end

newFile =  file(fn,'w')
#makes new file with new name and opens for writing to it

line = fi.readline()
#reads first line of file entered by user
while line: #while there is a line present, then go through loop
	line = line.strip()#trims leadings and trailing whitespace
	stripped = line.split()#splits on spaces and puts words from line into a list
	for i in stripped: #for each word in each line
		print i #print word that is being corrected so user knows which word they are looking at
		g = validateWords(i,words) #call validateWords function
		d = findReplacement(g,i) #call findReplacement function
		#print d
		if d != None: #if function does not return None, then write to new file
			newFile.write(d+' ')
	newFile.write('\n')	#if word is spelled correctly, then it is written to the new file
	#after going through line, breaks to new line
	line = fi.readline() #read next line in user inputted file
	
fi.close() 
newFile.close()
#close both files
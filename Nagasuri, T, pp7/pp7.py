
def readFile(s,w):
	
	source = file(s)
	line = source.readline()
	while line:
		line = line.strip()
		w.add(line)
		line = source.readline()
	return w
words = set()
setOfCorrectWords = readFile('words.txt', words)
#print setOfCorrectWords

#read text file of correctly spelled words, strip leading and trailing whitespaces
#add to set



def validateWords(g,correct):
	x = 1
	y = 0
	cts = {}
	for j in correct:
		y = 0
		if len(g) < 4:
			return cts
			#if length of first word being checked is less than 4, then return empty dictionary
		if len(j) == len(g) and len(g) >= 4 and g not in correct:
			for a,b in zip(j,g):
				if a == b:
					y+=1
					if y > 3:
						#print x,j
						cts[x] = j
						x+=1
						#if length of checked word is the same as a word in set of correctly spelled words
						#and checked word is not in set of correct words, then if there are 4 letter which are in the same place
						#add the word from correct set to the dictionary
		if len(j) != len(g) and len(g) > 3 and g not in correct:
			m = 0
			counter = 0
			for a,b in zip(j,g):
				counter +=1
				if counter < 4:
					if a == b:
						m+=1
						if m > 2:
							cts[x] = j
							x+=1
							#if length of checked word is not the same as length of correct word and is longer than 3 characters
							#if the letters of the first three indices of the words are the same
							#then add entry to the dictionary
					
	return cts
	#return the dictionary for each word that goes through function
						
						
						
					
def findReplacement(c,l):
	for key in c:
		print key, c[key]
	if len(c) == 0:
		return l
	elif len(c) > 0:
		choice = 0
		while not 1 <= choice <= len(c) and choice != -1:
			try:
				choice = int(raw_input('Enter the number corresponding to the spelling correction you wish to make. Enter -1 if you wish to leave the word as is. '))
				if choice != -1 and 1 <= choice <= len(c):
					return c[choice]
				if not 1 <= choice <= len(c) and choice != -1:
					print 'Your number must be from 1 to',len(c),'or enter -1'
				if choice == -1:
					return l
			except ValueError:
				print 'That is not a valid integer'

#print number and corresponding word so user can see options for spell checking
#if the dictionary is empty, then returns the word user originally had
#if dictionary has something in it, then prompts user for which numbered suggestion it would want to use
#if integer is not within range or is not valid, then prompts again
#user enters -1, then returns original word

		
		
		
		





		
		

		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		

		







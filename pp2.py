from decimal import Decimal 

def carRental(clc):
	
	mi = Decimal(odoend-odostart)
	mil = round(mi,1)

	if clc == 'b':
		miles = .25*mil
		tot = Decimal(40 + miles)
		total = round(tot,2)
		return total 
	elif clc == 'd':
		base = 60
		miles = (mil)/e
		if miles < 100:
			return base
		else: 
			m = Decimal((miles - 100)*.25)
			n = round(m,2)
			return (base + n)
	elif clc == 'w' or 'W':
		week = e/7
		base = 190*week
		miles = (mil)/week
		if miles <= 900 and miles > 0:
			b = Decimal(base)
			ba = round(b,2)
			return ba
		elif miles > 900 and miles <=1500:
			tot = Decimal(base + 100*week)
			total = round(tot,2)
			return total
		else:
			tot = Decimal(200*week + 0.25*(miles-1500))
			total = round(tot,2)
			return total
d = raw_input('What is your classification code? ')
d = d.lower()
#e = int(raw_input('How many days have you rented the vehicle? '))
#f = float(raw_input("What was the vehicle odometer's reading at the start of the rental period? "))
#g = float(raw_input("What was the vehicle's odometer at the end of the rental period? "))

while d != 'q':
	print 'Classification code: ',carRental(d)
	print 'Number of days the vehicle was rented: ',e
	print 'The odometer reading at the start of the rental period: ',f
	print 'The odometer reading at the end of the rental period: ',g
	print 'The total number of miles driven during this rental period: ',mi
	d = raw_input('What is your classification code? ')
	e = int(raw_input('How may days have you rented the vehicle? '))
	odostart = float(raw_input("What was the vehicle odometer's reading at the start of the rental period? "))
	odoend = float(raw_input("What was the vehicle's odometer at the end of the rental period? "))

raw_input('Press enter to terminate the program')

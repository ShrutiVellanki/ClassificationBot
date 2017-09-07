from sklearn import tree

#initializes category and data lists, initializes classifier to be decision tree
X = []
Y = []
treeSort = tree.DecisionTreeClassifier()
		
#greeting section
print(" ")
print("Howdy stranger!")
print(" ")
print("My name is Classification Bot. The more data points you feed me, the more my powers of classification grow!")
print(" ")
proceed = input("If you want to continue, enter 'y'. Press any other key to quit: ")

#begin the game 
if proceed is 'y':
	print(" ")
	print("Phase 1: Pick two categories and a sample data point for each.")

	while True:

		#sample data point for category one 
		catOneLabel = input("First category label: ")
		Y.append(catOneLabel)
		catOnePoint = input("Sample data point: ")
		X.append([catOnePoint])

		#sample data point for category two
		catTwoLabel = input("Second category label: ")
		Y.append(catTwoLabel)
		catTwoPoint = input("Sample data point: ")
		X.append([catTwoPoint])

		#train the classifier on dataset, if this works, move on to Phase 2
		try:
			treeSort = treeSort.fit(X,Y)
			break
		#if data points not numerical, clear X and Y values and display error emssage 
		except ValueError:
			print (" ")
			print("ERROR! Data points should be numerical. Try again.")
			print (" ")
			Y = []
			X = []

	while True:

		#phase 2 keeps repeating as long as user wants it to
		proceed = input("If you want to continue, enter 'y'. Press any other key to quit: ")
		if proceed is not 'y':
			break
		print(" ")
		print("Phase 2: Watch my prediction accuracy grow as I am fed more data points!")

		while True:
			testPoint = input("Feed me a test point and I will predict it's category: ")

			#Try to predict but display error message if test point is not numerical
			try:
				prediction = treeSort.predict([[testPoint]])
				print(prediction)
				break
			except: 
				print (" ")
				print("ERROR! Data points should be numerical. Try again.")
				print (" ")

		testCat = input("If category for test point is "+catOneLabel+" enter 'y'. Press any other key if category is "+catTwoLabel+": ")

		#trains the classifier on new data 
		if testCat is 'y':	
			Y.append(catOneLabel)
		else:
			Y.append(catTwoLabel)

		X.append([testPoint])
		treeSort = treeSort.fit(X,Y)			

#default good bye			
print(" ")
print("Thanks for playing with me!")
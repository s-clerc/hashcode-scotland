def parseFile(path):
	file = open(path, "r")

	lines = file.readlines()
	# Get number of each from line 0
	line = lines[0].split()
	data = {
		"time": int(line[0]),
		"intersections": int(line[1]),
		"numStreets": int(line[2]),
		"numCars": int(line[3]),
		"points": int(line[4])

	}
	# Extract book scores
	data["streetInfo"] = [int(number) for number in lines[1].split()]
	libraries = []
	for libraryNumber in range(0, data["numStreets"]):
		index = (libraryNumber + 1)*2
		infoLine = lines[index].split()
		bookLine = lines[index+1].split()
		library = {
			"numberOfBooks": int(infoLine[0]),
			"signup": int(infoLine[1]),
			"rate": int(infoLine[2]),
			"books": [int(book) for book in bookLine]
		}
		libraries.append(library)
	file.close()
	data["libraries"] = libraries
	return data

def outputData (path, data):
	file = open(path, "w")
	#Line 0
	file.write(f"{len(data)}\n")
	for library in data:
		file.write(f"{library['id']} {len(library['books'])}\n")
		for bookId in library["books"]:
			file.write(f"{bookId} ")
		file.write("\n")
	file.close()
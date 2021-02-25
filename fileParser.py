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
	streets = []

	for streetNum in range(1, data["numStreets"]):
		
		streetLine = lines[streetNum].split()
		street = {
			"interStart": int(streetLine[0]),
			"interEnd": int(streetLine[1]),
			"name": int(streetLine[2]),
			"timeTaken": int(streetLine[3]),
		}

		streets.append(street)
		file.close()
		data["streets"] = streets
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
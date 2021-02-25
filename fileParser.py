from dataclasses import dataclass
from graph import Graph
import sys
from typing import *

@dataclass
class Data:
	time: int
	number_of_intersections: int
	number_of_streets: int
	number_of_cars: int
	points: int
	graph: Graph
	cars: List[List[str]]
	# Name to start, end, length
	streets: Dict[str, Tuple[int, int, int]]
	# Start, end to name.
	costreets: Dict[Tuple[int, int], str]

def parseFile(path):
	file = open(path, "r")

	lines = file.readlines()
	# Get number of each from line 0
	line = lines[0].split()
	data = Data(*[int(value) for value in line], Graph(), [], {}, {})

	next_id = 0
	for n in range(data.number_of_streets):
		start, end, name, length = lines[1+n].split()
		start, end, length = (int(v) for v in (start, end, length))
		data.graph.add_edge(start, end, length)
		data.streets[name] = (start, end, length)
		data.costreets[(start, end)] = name

	for n in range(data.number_of_cars):
		[number, *streets] = lines[data.number_of_streets + 1+ n].split()
		data.cars.append(streets)
	file.close()
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
	file.close


if __name__ == "__main__":
	data = (parseFile(sys.argv[1]))
	print(data)
import fileParser, sys
from typing import *

data = fileParser.parseFile(sys.argv[1])
graph = data.graph

street_frequencies = {}

for path in data.cars:
	for street in path:
		street_frequencies.setdefault(street, 0)
		street_frequencies[street] += 1

output = {}
for intersection in graph.nodes():
	enterant_names = [data.costreets[street[:2]] 
					  for street in graph.edges(to_node=intersection)]
	
	denominator = 0
	for name in enterant_names:
		denominator += street_frequencies.get(name, 0)
	if denominator == 0:
		continue
	output[intersection] = [(name, round(denominator/street_frequencies[name])) 
							for name in enterant_names
							if street_frequencies.get(name, 0) > 0]

print(output)
fileParser.outputData(sys.argv[1] + "out", output)
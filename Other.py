import collections
population_change = collections.defaultdict(int)

with open('Population_data/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header = next(inputFile)

    for line in inputFile:
        line = line.rstrip().split(',')
        line[5] = int(line[5])
        if line[1] == 'Total National Population':
            population_change[line[0]] += (float(line[6]) - (line[5]))
			
with open('national_population_2.csv', 'w') as outputFile:
    outputFile.write('continent,2100_population-change\n')

    for k, v in population_change.iteritems():
        outputFile.write(k + ',' + str(v) + '\n')
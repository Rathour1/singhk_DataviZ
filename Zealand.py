import csv 

categories = []
zealand = []
world = []

with open('Olympics-Winter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			categories.append(row)
			line_count += 1
		elif row[4] == "NZL":
			zealand.append([int(row[0]), row[5], row[6], row[7]]) # multidimensional array
		else:
			world.append([int(row[0]), row[5], row[6], row[7]])
		line_count += 1

print('total medals for Zealand:', len(zealand))
print('total medals for everyone else:', len(world))

print('processed', line_count, 'rows of data')
			

silver_1992 = []

for medal in zealand:
	if medal[0] == 1992 and medal[3] == "Gold":
					gold_1992.append(medal)


print('zealand won', len(gold_1924), 'gold medals in 1924')
print('zealand won', len(gold_2014), 'gold medals in 2014')

print('processed', line_count, 'rows of data')

# filter 2014 based on gender
#
# plot on a pie chart men vs women =>
# how many medals for each as a percentage og the total
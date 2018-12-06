import csv 

categories = []
America = []
world = []

with open("Olympics-Winter.csv") as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader: 
		if line_count is 0:
			categories.append(row)
			line_count += 1
		elif row[4] == "USA":
			America.append([int(row[0]), row[5], row[6], row[7]]) # multidimensional array
		else:
			world.append([int(row[0]), row[5], row[6], row[7]])
		line_count += 1

print('total medals for America:', len(America))
print('total medals for everyone else:', len(world))

print('processed', line_count, 'rows of data')
			

gold_1924 = []
gold_1928 =[]
gold_1932 = []
gold_1936 = []
gold_1948 = []
gold_1952 = []
gold_1956 = []
gold_1960 = []
gold_1964 = []
gold_1972 = []
gold_1976 = []
gold_1980 = []
gold_1984 = []
gold_1988 = []
gold_1992 = []
gold_1994 = []
gold_1998 = []
gold_2002 = []
gold_2006 = []
gold_2010 = []
gold_2014 = []

for medal in America:
	if medal[0] == 1924 and medal[3] == "Gold":
					gold_1924.append(medal)

	if medal[0] == 1928 and medal[3] == "Gold":
					gold_1928.append(medal)	

	if medal[0] == 1932 and medal[3] == "Gold":
					gold_1932.append(medal)
	if medal[0] == 1936 and medal[3] == "Gold":
					gold_1936.append(medal)

	if medal[0] == 1948 and medal[3] == "Gold":
					gold_1948.append(medal)
	if medal[0] == 1952 and medal[3] == "Gold":
					gold_1952.append(medal)

	if medal[0] == 1956 and medal[3] == "Gold":
					gold_1956.append(medal)	

	if medal[0] == 1960 and medal[3] == "Gold":
					gold_1960.append(medal)
	if medal[0] == 1964 and medal[3] == "Gold":
					gold_1964.append(medal)

	if medal[0] == 1972 and medal[3] == "Gold":
					gold_1972.append(medal)
	if medal[0] == 1976 and medal[3] == "Gold":
					gold_1976.append(medal)

	if medal[0] == 1980 and medal[3] == "Gold":
					gold_1980.append(medal)	

	if medal[0] == 1984 and medal[3] == "Gold":
					gold_1984.append(medal)
	if medal[0] == 1988 and medal[3] == "Gold":
					gold_1988.append(medal)

	if medal[0] == 1992 and medal[3] == "Gold":
					gold_1992.append(medal)
	if medal[0] == 1994 and medal[3] == "Gold":
					gold_1994.append(medal)

	if medal[0] == 1998 and medal[3] == "Gold":
					gold_1998.append(medal)	

	if medal[0] == 2002 and medal[3] == "Gold":
					gold_2002.append(medal)
	if medal[0] == 2006 and medal[3] == "Gold":
					gold_2006.append(medal)

	if medal[0] == 2010 and medal[3] == "Gold":
					gold_2010.append(medal)
	if medal[0] == 2014 and medal[3] == "Gold":
					gold_2014.append(medal)													

print('America won', len(gold_1924), 'gold medals in 1924')
print('America won', len(gold_2014), 'gold medals in 2014')

print('processed', line_count, 'rows of data')

# filter 2014 based on gender
#
# plot on a pie chart men vs women =>
# how many medals for each as a percentage og the total
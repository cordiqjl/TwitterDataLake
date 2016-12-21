file = open("twitter_output.txt")

columns = []
for line in file:
    columns.append(line.split(' ', 7))
print(columns[0])
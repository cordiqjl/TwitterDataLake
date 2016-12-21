file = open("/Users/JanLukes/Documents/GitHub/TwitterDataLake/TwitterDataLake/twitter_output.txt")

columns = []
for line in file:
    pom = line.split(' ', 6)
    for i, each in enumerate(pom):
        pom[i] = each.strip()

    pom2 = pom[-1].split('Wind', 1)
    for i, each in enumerate(pom2):
        pom2[i] = each.strip()

    pom3 = pom2[-1].split('..', 1)
    for i, each in enumerate(pom3):
        pom3[i] = each.strip()

    columns.append(pom[:-1] + pom2[:-1] + pom3[:-1])    
    
print(columns[0])
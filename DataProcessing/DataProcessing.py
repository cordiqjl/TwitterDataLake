file = open("/Users/JanLukes/Documents/GitHub/TwitterDataLake/TwitterDataLake/twitter_output.txt")

columns = [['Date', 'Temperature', 'Weather', 'Wind direction', 'Wind speed', 'Humidity']]
for line in file:
    pom = line.split(' ')
    for i, each in enumerate(pom):
        pom[i] = each.strip()
    
    pom2 = [' '.join(pom[1:4]).strip()]
    for i, each in enumerate(pom):
        if each == 'Error':
            pom2 = []
            break
        if each == 'Temperature':
            pom2.append(pom[i+1])
            j = 2
            pom3 = ''
            while not (pom[i+j] == 'Wind' or pom[i+j] == 'Humidity'):
                pom3 += pom[i+j] + ' '
                j += 1
            if pom3:
                pom3 = ' '.join(pom3.split(', ')).lower()
                pom2.append(pom3.strip())
        if each == 'Wind':
            pom2.append(pom[i+1])
            pom2.append(pom[i+2])
        if each == 'Humidity':
            pom2.append(pom[i+1])
    columns.append(pom2)

columns = [x for x in columns if x]

filename = 'parsed_tweets.txt'

with open(filename, 'w') as f:
    for each in columns:
        pom = ';'.join(each)
        f.write(pom + '\n')
with open('example3Input.csv', 'r', encoding='utf-8') as dataFile:
    for line in dataFile.readLines():
        print(line)
        break

    print(dataFile.read())
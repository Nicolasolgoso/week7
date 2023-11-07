import json
counter = 0
with open("files/inventory.csv" , "r") as file:
    for line in file:
        if counter == 0:
            headers = line
        
        
print(line,headers)
jsonOutput = {}
for column in line.split(","):
    print(column)
    jsonOutput[column] = column
print(jsonOutput)


with open("output/product.json", "w") as outputFile:
    json.dump(jsonOutput,outputFile,indent=4)



import json

counter = 0

with open("files/movie_ratings.csv", "r") as inputFile:
    for line in inputFile:
        if(counter == 0):
            headers = line
            headers = headers.split(",")
        else:
            dictLine = {}
            counterHeader =  0
            for column in line.split(","):
                dictLine[headers[counterHeader]] = column
                counterHeader += 1
            with open(f"peliculas/{counter}.json", "w") as outputFile:
                json.dump(dictLine, outputFile, indent=4)

        counter += 1

print(headers)
print(line)
        

solarSystemFile = open("solar_system.json")
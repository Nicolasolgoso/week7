import json

counter = 0

# Leer el archivo inventory.csv
with open("files/inventory.csv", "r") as file:
    for line in file:
        if counter == 0:
            headers = line
        counter += 1

print(line, headers)

jsonOutput = {}
for column in headers.strip().split(","):
    print(column)
    jsonOutput[column] = column

print(jsonOutput)

# Leer y mostrar el contenido del archivo book_catalog.json
with open("files/book_catalog.json", "r") as jsonFile:
    book_catalog_data = json.load(jsonFile)
    print(book_catalog_data)





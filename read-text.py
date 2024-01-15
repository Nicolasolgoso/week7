with open("files/fun_facts.txt", "r") as file:
    print(file.read())

content = ""
with open("files/inventory.csv", "r") as file2:
    for line in file2:
        content += line  

print(content)


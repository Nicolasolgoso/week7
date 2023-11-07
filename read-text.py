with open("files/fun_facts.txt","r") as file:
    print(file.read())

context = ""
with open("files/inventory.csv","r") as file2:
    for line in file2:
        content += file2.read()

print(content)
print(file.read(20))

file.close()
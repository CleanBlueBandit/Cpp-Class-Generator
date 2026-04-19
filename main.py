import os

className = input("Enter Class name: ")
varNum = int(input("Enter the amount of variables: "))
code = f"class {className}{{\nprivate:"

names = []
types = []

for i in range(varNum):
    varType = input(f"Enter type for variable {i+1}: ")
    varName = input(f"Enter name for variable {i+1}: ")
    names.append(varName)
    types.append(varType)
    code += f"\n    {varType} {varName};"

code += f"\n\npublic:\n    {className}("
params = [f"{types[i]} {names[i]}" for i in range(varNum)]
code += ", ".join(params) + ") {"
for name in names:
    code += f"\n        this->{name} = {name};"
code += "\n    }\n"


for i in range(varNum):
    cap_name = names[i].capitalize()
    code += f"\n    {types[i]} get{cap_name}() const {{ return {names[i]}; }}"


for i in range(varNum):
    cap_name = names[i].capitalize()
    code += f"\n    void set{cap_name}({types[i]} {names[i][0]}) {{ {names[i]} = {names[i][0]}; }}"

code += f"\n\n    ~{className}() {{}}\n}};"

if os.name == 'nt':
    os.system("cls")
else:
    os.system("clear")

print(code)

with open("text.txt", "w") as f:
    f.write(code)

os.system("pause")
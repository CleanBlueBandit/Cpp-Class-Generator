import os

class_name = input("Enter Class name: ")
var_num = int(input("Enter the amount of variables: "))

names = []
types = []

# Logic Flags
createFiles = False
withHeader = False
cohesiveFile = True

for i in range(var_num):
    v_type = input(f"Enter type for variable {i+1}: ")
    v_name = input(f"Enter name for variable {i+1}: ")
    names.append(v_name)
    types.append(v_type)

# Pre-calculate parameters to avoid NameErrors
params = [f"{types[i]} {names[i]}" for i in range(var_num)]

# --- Header file string generation ---
header = ""
if withHeader:
    header += f"#ifndef {class_name.upper()}_H\n#define {class_name.upper()}_H\n\n"
    header += f"class {class_name} {{\nprivate:"

    for i in range(var_num):
        header += f"\n    {types[i]} {names[i]};"

    header += f"\n\npublic:\n    {class_name}("
    header += ", ".join(params) + ");"

    for i in range(var_num):
        cap_name = names[i].capitalize()
        header += f"\n    {types[i]} get{cap_name}() const;"
        header += f"\n    void set{cap_name}({types[i]} {names[i]});"

    header += f"\n\n    ~{class_name}();\n}};\n\n#endif"

# --- Source file string generation ---
cpp = ""

if not withHeader:
    # Single cohesive file mode
    cpp += f"#include <iostream>\n\nusing namespace std;\n\nclass {class_name} {{\nprivate:\n"
    for i in range(var_num):
        cpp += f"    {types[i]} {names[i]};\n"
    cpp += f"\npublic:\n    {class_name}("
else:
    # Separate Header/Source mode
    cpp += f'#include "{class_name}.h"\n\n'
    cpp += f"{class_name}::{class_name}("

# Constructor implementation
cpp += ", ".join(params) + ") {"
for name in names:
    cpp += f"\n    this->{name} = {name};"
cpp += "\n}\n"

# Getters and Setters implementation
for i in range(var_num):
    cap_name = names[i].capitalize()
    
    # Getter
    cpp += f"\n{types[i]} "
    if withHeader: cpp += f"{class_name}::"
    cpp += f"get{cap_name}() const {{\n    return {names[i]};\n}}\n"
    
    # Setter
    cpp += f"void "
    if withHeader: cpp += f"{class_name}::"
    cpp += f"set{cap_name}({types[i]} {names[i]}) {{\n    this->{names[i]} = {names[i]};\n}}\n"

# Destructor implementation
cpp += "\n"
if withHeader:
    cpp += f"{class_name}::~{class_name}() {{}}\n"
else:
    cpp += f"    ~{class_name}() {{}}\n}};" # Close class with semicolon

# --- File Writing Logic ---
if createFiles and withHeader: 
    with open(f"{class_name}.h", "w") as f:
        f.write(header)
    with open(f"{class_name}.cpp", "w") as f:
        f.write(cpp)

if cohesiveFile:
    with open("text.txt", "w") as f:
        if withHeader:
            f.write(f"{header}\n\n// -----------------------------\n\n{cpp}")
        else:
            f.write(cpp)

# Final Feedback
finalMsg = "\nDone! "
if createFiles and withHeader:
    finalMsg += f"Generated {class_name}.h and {class_name}.cpp."
elif cohesiveFile:
    finalMsg += "Generated text.txt."
else:
    print("\n--- Generated Code ---\n")
    print(header if withHeader else "")
    print("-" * 30)
    print(cpp)

print(finalMsg)
os.system("pause")

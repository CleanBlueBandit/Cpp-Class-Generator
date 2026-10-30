# Cpp-Class-Generator

A simple Python script that automates C++ class code generation by automatically creating constructors, getters, setters, and destructors for user-defined variables.

## Why I Created It

Because I was too lazy to write header and class files myself.

Instead of manually writing the same boilerplate code every time I create a C++ class, I decided to automate the process with a small Python script.

## Features

- Automatically generates private class variables.
- Creates a constructor with parameters for all provided variables.
- Generates getters and setters for each variable.
- Automatically creates a destructor.
- Supports both single-file and separate header/source file generation.
- Option to generate `.h` and `.cpp` files automatically.
- Option to combine everything into a single output file.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR_USERNAME/Cpp-Class-Generator.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Cpp-Class-Generator
   ```

3. Run the script:

   ```bash
   python main.py
   ```

4. Enter the class name, number of variables, and their respective types and names when prompted.

5. The generated C++ code will be saved to `text.txt` (depending on the configuration).

## Configuration

The script includes three configuration flags that can be changed directly in the source code:

| Variable | Description | Default |
|---|---|---|
| `createFiles` | Automatically creates separate `.h` and `.cpp` files. | `False` |
| `withHeader` | Enables separate header and source code generation. | `False` |
| `cohesiveFile` | Combines generated code into a single `text.txt` file. | `True` |

## Requirements

- Python 3.x
- No external libraries required.

## License

Feel free to use, modify, or improve it.

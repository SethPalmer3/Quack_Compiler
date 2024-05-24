Firstly ensure tiny_vm is compiled correctly for your OS by already established instructions.

Next run:
`source venv/bin/activate`
`pip install -r requirements.txt`

Usage:
`./quack.sh /path/to/quack/program.qk`

This will compile, assemble, and run the program in the vm.

Working Features:
Most of the basic features of Quack do seem to be mostly working:
    - General arithmetic and logical operations
    - Short circuit evaluation
    - Assignments
    - Defining classes including:
        - Extends
        - Constructor method
        - Attributes
        - Any other defined methods (including recursive definitions)
        - And the `this` keyword
    - Calling the constructor of a class
    - Calling/getting methods and attributes from variables defined as user defined classes
    - If else statements
    - While loops
    - String literals, integer literals, false, true, and nothing
    - Automatic type assignment

Non-working Features:
Most of what isn't working is towards the typing and type checking
    - `typecase`
    - Reassigning type with the type hierarchy
    - Most likely class hierarchical 
    - General optimizations

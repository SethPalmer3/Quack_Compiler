# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/seth/Desktop/quack_compiler/lark_parser/tiny_vm

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/test_roll.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/test_roll.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/test_roll.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/test_roll.dir/flags.make

../vm_code_table.c: ../build_bytecode_table.py
../vm_code_table.c: ../vm_code_table.h
../vm_code_table.c: ../opdefs.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating ../vm_code_table.c"
	python3 /home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/build_bytecode_table.py /home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/opdefs.txt /home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/vm_code_table.c

CMakeFiles/test_roll.dir/cjson/cJSON.c.o: CMakeFiles/test_roll.dir/flags.make
CMakeFiles/test_roll.dir/cjson/cJSON.c.o: ../cjson/cJSON.c
CMakeFiles/test_roll.dir/cjson/cJSON.c.o: CMakeFiles/test_roll.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object CMakeFiles/test_roll.dir/cjson/cJSON.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/test_roll.dir/cjson/cJSON.c.o -MF CMakeFiles/test_roll.dir/cjson/cJSON.c.o.d -o CMakeFiles/test_roll.dir/cjson/cJSON.c.o -c /home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/cjson/cJSON.c

CMakeFiles/test_roll.dir/cjson/cJSON.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/test_roll.dir/cjson/cJSON.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/cjson/cJSON.c > CMakeFiles/test_roll.dir/cjson/cJSON.c.i

CMakeFiles/test_roll.dir/cjson/cJSON.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/test_roll.dir/cjson/cJSON.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/cjson/cJSON.c -o CMakeFiles/test_roll.dir/cjson/cJSON.c.s

CMakeFiles/test_roll.dir/unit_tests/test_roll.c.o: CMakeFiles/test_roll.dir/flags.make
CMakeFiles/test_roll.dir/unit_tests/test_roll.c.o: ../unit_tests/test_roll.c
CMakeFiles/test_roll.dir/unit_tests/test_roll.c.o: CMakeFiles/test_roll.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building C object CMakeFiles/test_roll.dir/unit_tests/test_roll.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/test_roll.dir/unit_tests/test_roll.c.o -MF CMakeFiles/test_roll.dir/unit_tests/test_roll.c.o.d -o CMakeFiles/test_roll.dir/unit_tests/test_roll.c.o -c /home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/unit_tests/test_roll.c

CMakeFiles/test_roll.dir/unit_tests/test_roll.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/test_roll.dir/unit_tests/test_roll.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/unit_tests/test_roll.c > CMakeFiles/test_roll.dir/unit_tests/test_roll.c.i

CMakeFiles/test_roll.dir/unit_tests/test_roll.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/test_roll.dir/unit_tests/test_roll.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/unit_tests/test_roll.c -o CMakeFiles/test_roll.dir/unit_tests/test_roll.c.s

CMakeFiles/test_roll.dir/vm_core.c.o: CMakeFiles/test_roll.dir/flags.make
CMakeFiles/test_roll.dir/vm_core.c.o: ../vm_core.c
CMakeFiles/test_roll.dir/vm_core.c.o: CMakeFiles/test_roll.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building C object CMakeFiles/test_roll.dir/vm_core.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/test_roll.dir/vm_core.c.o -MF CMakeFiles/test_roll.dir/vm_core.c.o.d -o CMakeFiles/test_roll.dir/vm_core.c.o -c /home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/vm_core.c

CMakeFiles/test_roll.dir/vm_core.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/test_roll.dir/vm_core.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/vm_core.c > CMakeFiles/test_roll.dir/vm_core.c.i

CMakeFiles/test_roll.dir/vm_core.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/test_roll.dir/vm_core.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/vm_core.c -o CMakeFiles/test_roll.dir/vm_core.c.s

CMakeFiles/test_roll.dir/vm_state.c.o: CMakeFiles/test_roll.dir/flags.make
CMakeFiles/test_roll.dir/vm_state.c.o: ../vm_state.c
CMakeFiles/test_roll.dir/vm_state.c.o: CMakeFiles/test_roll.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building C object CMakeFiles/test_roll.dir/vm_state.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/test_roll.dir/vm_state.c.o -MF CMakeFiles/test_roll.dir/vm_state.c.o.d -o CMakeFiles/test_roll.dir/vm_state.c.o -c /home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/vm_state.c

CMakeFiles/test_roll.dir/vm_state.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/test_roll.dir/vm_state.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/vm_state.c > CMakeFiles/test_roll.dir/vm_state.c.i

CMakeFiles/test_roll.dir/vm_state.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/test_roll.dir/vm_state.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/vm_state.c -o CMakeFiles/test_roll.dir/vm_state.c.s

CMakeFiles/test_roll.dir/builtins.c.o: CMakeFiles/test_roll.dir/flags.make
CMakeFiles/test_roll.dir/builtins.c.o: ../builtins.c
CMakeFiles/test_roll.dir/builtins.c.o: CMakeFiles/test_roll.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Building C object CMakeFiles/test_roll.dir/builtins.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/test_roll.dir/builtins.c.o -MF CMakeFiles/test_roll.dir/builtins.c.o.d -o CMakeFiles/test_roll.dir/builtins.c.o -c /home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/builtins.c

CMakeFiles/test_roll.dir/builtins.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/test_roll.dir/builtins.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/builtins.c > CMakeFiles/test_roll.dir/builtins.c.i

CMakeFiles/test_roll.dir/builtins.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/test_roll.dir/builtins.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/builtins.c -o CMakeFiles/test_roll.dir/builtins.c.s

CMakeFiles/test_roll.dir/vm_ops.c.o: CMakeFiles/test_roll.dir/flags.make
CMakeFiles/test_roll.dir/vm_ops.c.o: ../vm_ops.c
CMakeFiles/test_roll.dir/vm_ops.c.o: CMakeFiles/test_roll.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_7) "Building C object CMakeFiles/test_roll.dir/vm_ops.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/test_roll.dir/vm_ops.c.o -MF CMakeFiles/test_roll.dir/vm_ops.c.o.d -o CMakeFiles/test_roll.dir/vm_ops.c.o -c /home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/vm_ops.c

CMakeFiles/test_roll.dir/vm_ops.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/test_roll.dir/vm_ops.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/vm_ops.c > CMakeFiles/test_roll.dir/vm_ops.c.i

CMakeFiles/test_roll.dir/vm_ops.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/test_roll.dir/vm_ops.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/vm_ops.c -o CMakeFiles/test_roll.dir/vm_ops.c.s

CMakeFiles/test_roll.dir/logger.c.o: CMakeFiles/test_roll.dir/flags.make
CMakeFiles/test_roll.dir/logger.c.o: ../logger.c
CMakeFiles/test_roll.dir/logger.c.o: CMakeFiles/test_roll.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_8) "Building C object CMakeFiles/test_roll.dir/logger.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/test_roll.dir/logger.c.o -MF CMakeFiles/test_roll.dir/logger.c.o.d -o CMakeFiles/test_roll.dir/logger.c.o -c /home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/logger.c

CMakeFiles/test_roll.dir/logger.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/test_roll.dir/logger.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/logger.c > CMakeFiles/test_roll.dir/logger.c.i

CMakeFiles/test_roll.dir/logger.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/test_roll.dir/logger.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/logger.c -o CMakeFiles/test_roll.dir/logger.c.s

CMakeFiles/test_roll.dir/vm_code_table.c.o: CMakeFiles/test_roll.dir/flags.make
CMakeFiles/test_roll.dir/vm_code_table.c.o: ../vm_code_table.c
CMakeFiles/test_roll.dir/vm_code_table.c.o: CMakeFiles/test_roll.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_9) "Building C object CMakeFiles/test_roll.dir/vm_code_table.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/test_roll.dir/vm_code_table.c.o -MF CMakeFiles/test_roll.dir/vm_code_table.c.o.d -o CMakeFiles/test_roll.dir/vm_code_table.c.o -c /home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/vm_code_table.c

CMakeFiles/test_roll.dir/vm_code_table.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/test_roll.dir/vm_code_table.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/vm_code_table.c > CMakeFiles/test_roll.dir/vm_code_table.c.i

CMakeFiles/test_roll.dir/vm_code_table.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/test_roll.dir/vm_code_table.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/vm_code_table.c -o CMakeFiles/test_roll.dir/vm_code_table.c.s

# Object files for target test_roll
test_roll_OBJECTS = \
"CMakeFiles/test_roll.dir/cjson/cJSON.c.o" \
"CMakeFiles/test_roll.dir/unit_tests/test_roll.c.o" \
"CMakeFiles/test_roll.dir/vm_core.c.o" \
"CMakeFiles/test_roll.dir/vm_state.c.o" \
"CMakeFiles/test_roll.dir/builtins.c.o" \
"CMakeFiles/test_roll.dir/vm_ops.c.o" \
"CMakeFiles/test_roll.dir/logger.c.o" \
"CMakeFiles/test_roll.dir/vm_code_table.c.o"

# External object files for target test_roll
test_roll_EXTERNAL_OBJECTS =

../bin/test_roll: CMakeFiles/test_roll.dir/cjson/cJSON.c.o
../bin/test_roll: CMakeFiles/test_roll.dir/unit_tests/test_roll.c.o
../bin/test_roll: CMakeFiles/test_roll.dir/vm_core.c.o
../bin/test_roll: CMakeFiles/test_roll.dir/vm_state.c.o
../bin/test_roll: CMakeFiles/test_roll.dir/builtins.c.o
../bin/test_roll: CMakeFiles/test_roll.dir/vm_ops.c.o
../bin/test_roll: CMakeFiles/test_roll.dir/logger.c.o
../bin/test_roll: CMakeFiles/test_roll.dir/vm_code_table.c.o
../bin/test_roll: CMakeFiles/test_roll.dir/build.make
../bin/test_roll: CMakeFiles/test_roll.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_10) "Linking C executable ../bin/test_roll"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/test_roll.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/test_roll.dir/build: ../bin/test_roll
.PHONY : CMakeFiles/test_roll.dir/build

CMakeFiles/test_roll.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/test_roll.dir/cmake_clean.cmake
.PHONY : CMakeFiles/test_roll.dir/clean

CMakeFiles/test_roll.dir/depend: ../vm_code_table.c
	cd /home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/seth/Desktop/quack_compiler/lark_parser/tiny_vm /home/seth/Desktop/quack_compiler/lark_parser/tiny_vm /home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/cmake-build-debug /home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/cmake-build-debug /home/seth/Desktop/quack_compiler/lark_parser/tiny_vm/cmake-build-debug/CMakeFiles/test_roll.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/test_roll.dir/depend


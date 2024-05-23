.class binary_ops:Obj
.method $constructor
.local a,b
enter
const true
store a
const false
store b
const true
load a
jump_if short_or5
pop
load b
short_or5:
call Bool:print
pop
const "\n"
call String:print
pop
const false
load a
jump_ifnot short_and6
pop
load b
short_and6:
call Bool:print
pop
const "\n"
call String:print
pop
const false
store a
call Bool:equal
call Bool:print
pop
load $
return 0
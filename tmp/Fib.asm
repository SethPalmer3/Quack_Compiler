.class Fib:Obj
.method $constructor
.args i
.local c,a,b,z,y
enter
const 0
store c
const 0
store a
const 1
store b
const 0
store z
const "\n"
const "a"
call String:plus
store y
jump cond_2
while_1:
load y
call String:print
pop
const "\n"
load z
call Int:string
call String:plus
call String:print
pop
load b
store a
load z
store b
load b
load a
call Int:plus
store z
const 1
load c
call Int:plus
store c
cond_2:
load i
load c
call Int:less
jump_if while_1
load $
return 12
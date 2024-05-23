.class classes:Obj
.method $constructor
.local t,x
enter
const 10
new Test
call Test:$constructor
store t
load t
load_field Test:a
call Int:print
pop
const "\n"
call String:print
pop
const 6
load t
call Test:test_method
store x
load x
call Int:print
pop
load $
return 0
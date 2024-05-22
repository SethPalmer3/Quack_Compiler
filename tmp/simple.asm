.class simple:Obj
.method $constructor
.local t
enter
new Test
call Test:$constructor
store t
const 6
load t
call Test:set_a
load t
load_field Test:a
call Int:print
pop
load $
return 0
.class simple:Obj
.method $constructor
.local t,x
enter
new Test
call Test:$constructor
store t
const 21
load t
call Test:fib
store x
load x
call Int:print
pop
load $
return 0
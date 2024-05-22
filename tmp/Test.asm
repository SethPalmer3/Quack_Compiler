.class Test:Obj
.field a
.method set_a
.args s
enter
const 2
load s
call Int:times
load $
store_field $:a
load s
return 1
.method $constructor
enter
const 5
load $
store_field $:a
load $
return 0
.class Test:Obj
.field a
.method test_method
.args param
enter
const 2
load param
call Int:times
load $
store_field $:a
const 2
load param
call Int:times
return 1
.method $constructor
.args a
enter
load a
load $
store_field $:a
load $
return 1
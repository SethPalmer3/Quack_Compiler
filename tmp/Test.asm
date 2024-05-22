.class Test:Obj
.field a
.method set_a
.args s
enter
load s
load $
store_field $:a
const nothing
return 0
.method $constructor
enter
const 5
load $
store_field $:a
load $
return 0
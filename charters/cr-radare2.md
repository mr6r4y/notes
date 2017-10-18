# Code Reading - radare2 project

## 1

Read `libr/util` sources

### Note

Gone through:
* `r_vector`  - needs deeper understanding
* `r_binheap` - go back here after fully understanding `r_vector`
* `r_types` - needs another look

## 1.1

Go through `r_types`

### Note

Deeper look at:
* compile-time introspection helpers
* `R_FREE` - do not understand why we need `{`, `}` in the macro
* purpose of `run_call*` functions

## 1.1.1

Go through `r_sys.h` and `libr/util/sys.c`
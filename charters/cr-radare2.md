# Code Reading - radare2 project

## Legend

Symbol/Abbr. | Description
-------------|------------
✔ | Finished
❌ | Rejected / Not done


# Info

# Charters

## 1

Read `libr/util` sources

### Note

Gone through:
* `r_vector`  - needs deeper understanding
* `r_binheap` - go back here after fully understanding `r_vector`
* `r_types` - needs another look

## 1.2

2nd look at `r_binheap`

## 1.3

2nd look at `r_vector`

## 1.1

Go through `r_types`

### Note

Deeper look at:
* compile-time introspection helpers:
    * understand these:
        * CTO - Offset of a field in struct - y(struct), z(field)
        * CTA - Address of a field in struct at x(address),y(struct),z(field)
        * CTI - Dereference of a field in struct
        * CTS - Dereference of a field(z) in struct(y) at address(x) of type(t) and assign to v

```c
#define CTO(y,z) ((size_t) &((y*)0)->z)
#define CTA(x,y,z) (x+CTO(y,z))
#define CTI(x,y,z) (*((size_t*)(CTA(x,y,z))))
#define CTS(x,y,z,t,v) {t* _=(t*)CTA(x,y,z);*_=v;}
```

* `R_FREE` - do not understand why we need `{`, `}` in the macro
* purpose of `run_call*` functions:
    * used by `rarun2` in the `switch case` of `r_run_start()` (used for calling library function with different number of arguments)

## 1.1.1 ✔

Go through `r_sys.h` and `libr/util/sys.c`

### Note

* ifdefs for `__WINDOWS__` and `__CYGWIN__` scattered in every function
* signal handlers implemented
* use of structs implemented in `sftypes.h` - http://www.secdev.org/projects/shellforge/
* `r_sys_run` is not using `fork`

## 1.1.1.3 ✔

Go through `r_sandbox.h` and `util/sandbox.c`

### Note

Sandboxes file access to be under paths that are below RADARE data/www/etc. directories.

* `!strncmp(..)` returns 1 (true) if strings are equal cause `strncmp` returns 0 on string equality

## 1.1.1.3.1

Go through `libr/util/str.c`

### Note

* `r_str_home(..)` can result in `NULL` and must trace callers if they check for `NULL`

## 1.1.1.3.2

Go through `lbir/util/file.c`

## 1.1.1.2

Go through `libr/include/sflib/common/sftypes.h`

## 1.1.1.1

Go through `r_list.h` and `util/list.c`

## 1.1.2 ✔

Read `r_endian.h`

### Note

* various functions for read/write 1,2,4,8 byte little/big endian integers
* functions for "secure" add,mul,div,sub
* basic block used by `libr/reg`, `libr/asm/arch`, etc.

## 1.1.3 ✔

Read `r_str_util.h`

### Note

* basic checks like `ISWHITESPACE`, `ISDIGIT`, etc.
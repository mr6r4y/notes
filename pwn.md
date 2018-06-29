# Pwning

## GDB Commands

Cmmand | Description
--------|------------
`vmmap` | Memory map
`catch syscall` | Breaks on every `syscall` instruction
`start` | Stops at the beginning of the executable (entry point)
`set disassembly-flavor intel` | Intel syntax display

## GDB - Interacting with programs using `read()` in complex cmd menus

First set up a FIFO for process' STDIN:

    $> mkfifo p.in

Then in the debugger run the process as:

    (gdb) run < p.in

The FIFO is ready to take input from a python script. The script
should interact with FIFO by `open()`:

```python
f = open("p.in", "w")
f.write("1")
f.flush()
f.write("a" * 20)
f.flush()
```

## GDB - set local libc to be load instead default one

```
(gdb) set environment LD_PRELOAD=./libc.so.6
```

## Stack randomization

    echo 0 | sudo tee /proc/sys/kernel/randomize_va_space

## When I had problem with not getting core dumps

    sudo sysctl -w kernel.core_pattern=core

## Permanent ASLR configuration

    ..$> cat /etc/sysctl.d/01-disable-aslr.conf
    kernel.randomize_va_space = 2
# GDB + Pwndbg + pwning ..

# GDB Commands

Command | Description
--------|------------
vmmap | Memory map
catch syscall | Breaks on every `syscall` instruction
start | Stops at the beginning of the executable (entry point)
set disassembly-flavor intel | Intel syntax display

# Commands

Stack randomization:

    echo 0 | sudo tee /proc/sys/kernel/randomize_va_space

When I had problem with not getting core dumps:

    sudo sysctl -w kernel.core_pattern=core

Permanent ASLR configuration:

    ..$> cat /etc/sysctl.d/01-disable-aslr.conf
    kernel.randomize_va_space = 2
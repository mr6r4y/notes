# User and Kernel Space

## Charters

### 1

Explore:

* [Linux Inside: Booting](https://0xax.gitbooks.io/linux-insides/content/Booting/)
* [Minimal Boot Loader](https://www.cs.cmu.edu/~410/doc/minimal_boot.pdf)
* [Intel Manual vol 3A](https://www.intel.com/content/dam/www/public/us/en/documents/manuals/64-ia-32-architectures-software-developer-vol-3a-part-1-manual.pdf)

to discover:

* how the OS / processor switch from Real Mode to Protected Mode / Long Mode
* how the OS / processor starts to manage privileges via processor rings


### 1.2 !

Read [Linux Inside: Booting: First steps in the kernel setup](https://0xax.gitbooks.io/linux-insides/content/Booting/linux-bootstrap-2.html)


### 1.1 ✔

Read [Linux Inside: Booting: From Bootloader To Kernel](https://0xax.gitbooks.io/linux-insides/content/Booting/linux-bootstrap-1.html)

#### Note

Sequence of Booting:

```
.------------------------.
|    CPU - Real-mode     |
'------------------------'
             |
             |
             |
             v
.------------------------.
|       BIOS/UEFI        |
'------------------------'
             |
             |
             |
             v
.------------------------.
|       Bootloader       |
'------------------------'
             |
             |
             |
             v
.------------------------.
|         Kernel         |
'------------------------'
             |
             |
             |
             |
             v
.------------------------.
|      Init process      |
'------------------------'
```

[Reset Vector](http://en.wikipedia.org/wiki/Reset_vector):

    IP = 0xfff0
    CS Selector = 0xf000
    CS Base = 0xffff0000

CS Register points to CS Selector and CS Base, but CS Base is preset before CS Register is changed.

[A20 Bus Line](https://en.wikipedia.org/wiki/A20_line) is off so we have 1 MB access to memory.

    # .. << 4 .. is 1 nibble

    ph_addr = (CS << 4) + IP

    # >>> hex((0xffff << 4) + 0xffff)
    # '0x10ffef'

* `0xfffffff0` is in ROM.
* CS = `MZ` Offset + 0x200
* gs = fs = es = ds = ss = 0x10000
* cs = 0x10200
* ds = es  !
* check SS Register for Stack Setup
* CX Register for BSS Setup


### 1.1.2

Explore:

* understanding of [A20 Line](https://en.wikipedia.org/wiki/A20_line)

to understand:

* clear historical and backward compatibility issues that Intel has to comply with

### 1.1.3

Explore:

* [Linux Boot Protocol](https://github.com/torvalds/linux/blob/16f73eb02d7e1765ccab3d2018e0bd98eb93d973/Documentation/x86/boot.txt)
* [arch/x86/boot/header.S](https://github.com/torvalds/linux/blob/16f73eb02d7e1765ccab3d2018e0bd98eb93d973/arch/x86/boot/header.S)

to discover:

* kernel memory layout at boot time
* grasp of the whole document
* why after the bootloader transfers control to the kernel, we jump at `X + sizeof(KernelBootSector) + 1`
* what is this PE magic in the Linux kernel image: `00010000: 4d5a ...   MZ....`
* what are *loadflags*

### 1.1.4

Explore:

* semantics of `ret` instruction when processor is in Real Mode

with:

* Intel Manuals

to discover:

* differences from how it works in protected mode
* how segment registers are used

### 1.1.5

Check what `testb` instruction does in Intel Manuals


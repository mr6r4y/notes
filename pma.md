# From Practical Malware Analysis book

## Run exported DLL function

Basic and exported by ordinal:

```
C:\>rundll32.exe DLLname, Export arguments
C:\>rundll32.exe xyzzy.dll, #5
```

When dealing with service:

```
C:\>rundll32 ipr32x.dll,InstallService ServiceName
C:\>net start ServiceName
```

## References

* [Practical Malware Analysis](https://www.nostarch.com/malware)
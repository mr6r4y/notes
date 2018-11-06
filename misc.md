# Misc

## Mount .vmdk partition to folder in linux

1. list partitions in this virtual disk

    ```
    vmware-mount -p /path/to/vmdk/disk.vmdk
    ```

1. Make mount folder

    ```
    sudo mkdir /mnt/<folder>
    ```

1. mount

    ```
    sudo vmware-mount /path/to/vmdk/disk.vmdk 2 /mnt/<folder>/
    ```

1. umount

    ```
    sudo vmware-mount -d /mnt/<folder>/
    ```

## Add user to wireshark group for non-root usage of Wireshark

```
usermod -a -G wireshark user
```

## Fix DNS in VirtualBox VM

```
VBoxManage modifyvm "VM name" --natdnshostresolver1 on
```

## Extract .tar.gz file

Taken from https://www.cyberciti.biz/faq/linux-unix-bsd-extract-targz-file/

```
tar -zxvf {file.tar.gz}
```

## Try to extract with no -z if error with the first command

The -z is for gzip format

```
tar -xvf {file.tar.gz}
```

## Install Packer

1. Extract /home/user/archs/packer_0.12.2_linux_amd64.zip
1. Move 'packer' to /usr/local/bin/

    ```
    sudo mv /home/user/archs/packer /usr/local/bin
    ```

## Make the sudo group act with NO password

Add the following line in /etc/sudoers

```
%sudo ALL=NOPASSWD:ALL
```

## Make SSH keys

```
ssh-keygen -t rsa -C ansadm
```

## Enable traffic forwarding and NAT

```
sudo bash -c 'echo 1 > /proc/sys/net/ipv4/ip_forward'
sudo bash -c 'echo 1 > /proc/sys/net/ipv4/ip_dynaddr'
```

## Iptables NAT

```
iptables -t nat -A POSTROUTING -d 0/0 -s <NET-TO-BE-FORWARDED>/24 -j MASQUERADE
iptables -A FORWARD -s <NET-TO-BE-FORWARDED>/24 -d 0/0 -j ACCEPT
iptables -A FORWARD -s 0/0 -d <NET-TO-BE-FORWARDED>/24 -j ACCEPT

```

## Tools for Markdown format

```
apt-get install epubcheck pandoc
pip install mdv markdown2 Markdown2PDF md2ebook
```

## Disable password login to ssh server

In **/etc/ssh/sshd_config** change the following lines:

```
ChallengeResponseAuthentication no
PasswordAuthentication no
UsePAM no
```

## How to tell Git to use specific private key

The chosen solution is from http://superuser.com/questions/232373/how-to-tell-git-which-private-key-to-use :

```
vim ~/.ssh/config
```

In config:

```
host github.com
 HostName github.com
 IdentityFile ~/workspace/my-github/keys/id_rsa
 User git
```

## Making a partition with high number of inodes

```
mkfs.ext4 -T news /dev/<part>
```

# RE Misc

## Compilation date and environment info for ELF

```
objdump -s --section .comment /path/binary
```

## YARA scan without warning output

```
yara -w /opt/repo/yara-rules/index.yar /bin/true
```



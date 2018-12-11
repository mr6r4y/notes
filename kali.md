# Kali Set Up

## Set Up from fresh `kali-linux-xfce-2018.4-amd64`

### Initial

1. `sudo apt-get update`
1. `sudo apt-get dist-upgrade`
1. If in Vbox VM:
    - `sudo apt-get install virtualbox-guest-x11`
1. `sudo apt-get remove postgresql-10`
1. `sudo apt-get autoremove && sudo apt-get clean`
1. Restart

### Secondary

1. From `set-ups`:
    - clone `set-ups`
    - `install-base-dev.sh`
    - `install-tmux.sh`:
        - configs for users: `user` and `root`
    - `install-netsec.sh`
    - `install-subliime.sh`
1. Enable db for metasploit:
    - change port from `5433` to `5432` in `/etc/postgresql/11/main/postgresql.conf`
    - `sudo systemctl postgresql enable`
    - `sudo systemctl start postgresql`
    - `sudo msfdb init`
1. Additional packages for smb enumeration:
    - `sudo apt-get install snmp-mibs-downloader`
    - snmpv3enum:
    	- `git clone https://github.com/raesene/TestingScripts/` in `/opt/repo`
1. Hashcat:
	- needs `install-opencl.sh`
1. 
1. Bring back system ruby because installed metasploit breaks - `rvm set system`
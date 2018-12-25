import requests

url = "https://ukrainskamova.com/publ/slovnik_sinonimiv/"
baseUrl = "https://ukrainskamova.com/publ/"

#How many pages per each letter
numberOfPages = [
    (22, 8), (23, 11,), (24, 22),
    (25, 9), (26, 2), (27, 13),
    (28, 3), (29, 1), (30, 4),
    (31, 22), (32, 4), (59, 1),
    (33, 20), (34, 8), (35, 14),
    (36, 24), (37, 13), (38, 46),
    (39, 13), (40, 25), (41, 10),
    (42, 11), (43, 5), (44, 6),
    (45, 4), (46, 5), (47, 7),
    (48, 2), (49, 1), (50, 2)
]

urls = []



def getUrls():
    i = 22
    toWrite = False
    while i <= 50:
        r = requests.get(url + repr(i))
        currentUrl = ""
        for symbol in range(len(r.text)):
            if (toWrite == True and r.text[symbol] != '"'):
                currentUrl += r.text[symbol]
            if (toWrite == True and r.text[symbol] == '"'):
                toWrite = False
                urls.append(baseUrl + currentUrl)
            if (toWrite == False and len(r.text) > symbol + 5):
                if (r.text[symbol] == 's' and r.text[symbol + 1] == 'l' and r.text[symbol + 2] == 'o' and r.text[symbol + 3] == 'v' and r.text[symbol + 4] == 'n' and r.text[symbol + 5] == 'i'  and r.text[symbol + 6] == 'k' and r.text[symbol + 7] == '_' and r.text[symbol + 8] == 's' and r.text[symbol + 9] == 'i'):
                    currentUrl = r.text[symbol]
                    toWrite = True
                else:
                    toWrite = False

        i += 1
    f = open("urls.txt", "a")
    result = ""
    for s in range(len(urls)):
        result += urls[s] + '\n'
    f.write(result)

getUrls()




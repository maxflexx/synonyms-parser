import requests

url = "https://ukrainskamova.com/publ/slovnik_sinonimiv/"
baseUrl = "https://ukrainskamova.com/publ/"

urls = []
def getUrls():
    i = 22
    toWrite = False
    while i <= 50:
        r = requests.get(url + repr(i))
        currentUrl = "s"
        #print(r.text)
        for symbol in range(len(r.text)):
            if (toWrite == True and r.text[symbol] != '"'):
                currentUrl += r.text[symbol]
            if (toWrite == True and r.text[symbol] == '"'):
                toWrite = False
                urls.append(baseUrl + currentUrl)
            if (toWrite == False and len(r.text) > symbol + 5):
                if (r.text[symbol] == 's' and r.text[symbol + 1] == 'l' and r.text[symbol + 2] == 'o' and r.text[symbol + 3] == 'v' and r.text[symbol + 4] == 'n' and r.text[symbol + 5] == 'i'  and r.text[symbol + 6] == 'k' and r.text[symbol + 7] == '_' and r.text[symbol + 8] == 's' and r.text[symbol + 9] == 'i'):
                    currentUrl = "s"
                    toWrite = True
                else:
                    toWrite = False

        i += 1
    f = open("urls.txt", "a")
    result = ""
    for s in range(len(urls)):
        result += urls[s] + '\n'
    f.write(result)
    print(urls)

getUrls()




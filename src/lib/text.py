def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    text = " ".join(text.split())
    if casefold:
        text = text.casefold()
    else:
        text = text.lower()
    if yo2e:
        text = text.replace("ё","е")
    return text
x1 = "ПрИвЕт\nМИр\t", True, True
x2 = "ёжик, Ёлка", False, True
x3 = "Hello\r\nWorld",True,True
x4 = "  двойные   пробелы  "
#print(normalize("ПрИвЕт\nМИр\t"))
# text.isalnum()
def tokenize(text: str)-> list[str]:
    non_alnum = []
    cnt = 0
    for i in text:
        if not i.isalnum() and i != "-":
            non_alnum.append(i)
        if i == '-':
            if cnt > 0 and cnt != len(text) - 1: # Защита если - в начале или конце
                if text[cnt-1].isalnum() == False or text[cnt+1].isalnum() == False:
                    non_alnum.append("-")
        cnt += 1
    for i in non_alnum:
        text = " ".join(text.split(i))
    text = text.split()
    return text
x1 = "привет мир"
x2 = "hello,world!!!"
x3 = "по-настоящему круто"
x4 = "2025 год"
x5 = "emoji 😀 не слово"
#print(tokenize("emoji- 😀 не слово-"))
def count_freq(tokens: list[str]) -> dict[str, int]:
    result = {}
    x = sorted(set(tokens))
    for i in x:
        result[i] = 0
    for i in tokens:
        cnt = result[i]
        result[i] = result[i] + 1
    return result

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    items = list(freq.items())
    result = []
    while len(result) < n and len(items) > 0:
        best = items[0]
        for item in items:
            if item[1] > best[1]:
                best = item
            elif item[1] == best[1] and item[0] < best[0]:
                best = item
        result.append(best)
        items.remove(best)
    return result

    
x1 = ["a","b","a","c","b","a"]
x2 = ["bb","aa","bb","aa","cc"]
#print(count_freq(x2))
x1 = {"a":7,"b":6,"c":1},2
x2 = {"aa":2,"bb":2, "dd": 2,"cc":1}, 1
#print(top_n({"a":7,"b":6,"c":1},2))
'''
dic = {"aa":2,"bb":2,"cc":1}
n = 1
cnt = 0
mx = max(dic.values())
for i in dic.values():
        print(i,mx)
        if i == mx:
            cnt += 1
if cnt > 1:
    n = cnt
print(n)
'''
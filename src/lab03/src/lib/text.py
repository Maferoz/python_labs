def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    text1 = " ".join(text1.split())
    if casefold:
        text1 = text1.casefold()
    else:
        text1 = text1.lower()
    if yo2e:
        text1 = text1.replace("ё","е")
    return text1
x1 = "ПрИвЕт\nМИр\t", True, True
x2 = "ёжик, Ёлка", False, True
x3 = "Hello\r\nWorld",True,True
x4 = "  двойные   пробелы  ",True,True
# text.isalnum()
def tokenize(text: str)-> list[str]:
    non_alnum = []
    cnt = 0
    for i in text:
        if not i.isalnum() and i != "-":
            non_alnum.append(i)
        if i == '-':
            if cnt > 0:
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
#print(tokenize(x5))
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
    dic = freq
    new_a = {}
    cnt = 0
    mx = max(dic.values())
    for key in dic:
        value = dic[key]
        if value == mx:
            cnt += 1
    if cnt > 1:
        n = cnt
    second_dic = dic.copy()
    for key in second_dic:
        if n == 0:
            return new_a
        value = dic[key]
        if value == mx:
            new_a[key] = value
            del dic[key]
            mx = max(dic.values())
            n -= 1

    
x1 = ["a","b","a","c","b","a"]
x2 = ["bb","aa","bb","aa","cc"]
#print(count_freq(x2))
x1 = {"a":7,"b":6,"c":1},2
x2 = {"aa":2,"bb":2, "dd": 2,"cc":1}, 1
print(top_n({"a":7,"b":6,"c":1},2))
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
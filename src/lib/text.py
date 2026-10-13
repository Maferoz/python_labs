
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    text = " ".join(text.split())
    if casefold:
        text = text.casefold()
    else:
        text = text.lower()
    if yo2e:
        text = text.replace("ё","е")
    return text


def tokenize(text: str)-> list[str]:
    changed_text = "" # В нем все плохие символы меняем на пробел кроме - и _
    result_text = "" # В нем заменяем неподходящие - на пробел, потом обработка сплитом и конец
    for symbol in text:
        if symbol.isalnum() == False and symbol != "-" and symbol != "_": #Заменяем все плохие символы на пробел для последующего сплита
            changed_text += " "
        else:
            changed_text += symbol
    for index in range(len(changed_text)):
        symbol = changed_text[index]
        if symbol == "-":
            if index > 0 and index < len(changed_text) - 1:
                if changed_text[index-1] not in (" ", "-") and changed_text[index+1] not in (" ", "-"):
                    result_text += symbol
                else:
                    result_text += " "
            else:
                result_text += " "
        else:
            result_text += symbol
    result_text = result_text.split()
    return result_text

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
    maximum = max(freq.values())
    cnt = 0
    for i in freq.values():
        if i == maximum:
            cnt += 1
    if cnt > 1:
        n = cnt
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


    

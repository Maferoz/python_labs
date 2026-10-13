from src.lib.text import normalize, tokenize, count_freq, top_n

def starts(text):
    token = tokenize(normalize(text))
    freq = count_freq(token)
    topn = top_n(freq)
    print("Топ-5:")
    for x, i in tp:
        print(f"{x}: {i}")
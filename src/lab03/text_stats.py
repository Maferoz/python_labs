import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..")) #Изначально python ищет lib.text в lab03, а там нема. 
from lib.text import normalize, tokenize, count_freq, top_n


# 1. Читаем весь ввод до конца (EOF)
text = sys.stdin.read()

# 2. Приводим текст к нормальному виду (маленькие буквы, ё -> е, лишние пробелы)
text = normalize(text)

# 3. Разбиваем текст на слова
tokens = tokenize(text)

# 4. Считаем, сколько раз встречается каждое слово
freq = count_freq(tokens)

# 5. Берём 5 самых частых слов
top = top_n(freq, 5)

# 6. Печатаем результат
print("Всего слов:", len(tokens))       # len(tokens) = сколько всего слов
print("Уникальных слов:", len(freq))    # в словаре по одному ключу на каждое слово
print("Топ-5:")
for item in top:
    # item[0] — слово, item[1] — сколько раз оно встретилось
    print(item[0] + ":" + str(item[1]))
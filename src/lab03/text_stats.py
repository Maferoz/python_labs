import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.lib.text import normalize, tokenize, count_freq, top_n
def main() -> None:
    text = sys.stdin.read()
    tokens = tokenize(normalize(text))
    freq = count_freq(tokens)
    topn = top_n(freq)
    print("Топ-5:")
    for word, cnt in topn:
        print(f"{word}: {cnt}")

if __name__ == "__main__":
    main()
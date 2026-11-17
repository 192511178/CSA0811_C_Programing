"""Task A5: lexicon sentiment, extractive summary and rule-based chatbot."""
import re, sqlite3
from pathlib import Path

POSITIVE = {"good","clean","fast","helpful","improved"}
NEGATIVE = {"bad","dirty","slow","rude","smoke","broken"}
NEGATORS = {"not","never","no"}

def score(text):
    words = re.findall(r"[a-zA-Z']+", text.lower())
    total = 0
    for i, word in enumerate(words):
        value = 1 if word in POSITIVE else -1 if word in NEGATIVE else 0
        if i > 0 and words[i-1] in NEGATORS: value = -value
        total += value
    return total

def label(text):
    value = score(text)
    return "positive" if value > 0 else "negative" if value < 0 else "neutral"

def summarise(text, k=2):
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\\s+", text) if s.strip()]
    stop = {"the","is","are","and","a","to","of","in","our","was"}
    words = re.findall(r"[a-zA-Z]+", text.lower())
    freq = {}
    for w in words:
        if w not in stop: freq[w] = freq.get(w,0)+1
    def sentence_score(s):
        return sum(freq.get(w,0) for w in re.findall(r"[a-zA-Z]+",s.lower()))
    return " ".join(sorted(sentences, key=sentence_score, reverse=True)[:k])

def chatbot(question, db_path):
    q = question.lower()
    station = next((s for s in ("adyar","guindy") if s in q), None)
    if not station or "pm2.5" not in q:
        return "Please ask for PM2.5 and specify a supported station (Adyar or Guindy)."
    con = sqlite3.connect(db_path)
    row = con.execute("""SELECT pm25 FROM aq WHERE lower(station)=?
                         ORDER BY day DESC LIMIT 1""",(station,)).fetchone()
    con.close()
    return f"Latest available PM2.5 for {station.title()} is {row[0]}." if row else "No reading found."

if __name__ == "__main__":
    samples = ["Roads are clean and the bus was fast.",
               "Smoke from the factory, air is bad.",
               "The staff were not helpful.", "Not bad, service improved."]
    for item in samples: print(label(item), "|", item)
    print(summarise("Smoke is rising near the factory. The air is bad. Residents want clean roads."))

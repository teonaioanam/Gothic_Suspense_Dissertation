import pandas as pd
from collections import Counter, defaultdict
import nltk
from nltk.corpus import stopwords
from nltk import pos_tag
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\b[a-zA-Z]{3,}\b')  # Only alphabetic words with 3+ letters
stop_words = set(stopwords.words("english"))

# Load data
df = pd.read_csv("C:/Users/Admin/PycharmProjects/GothicSuspenseDissertation/analysis/tag_context_sentences.csv")

# Store results
tagged_words = defaultdict(list)

for tag in df["Tag"].unique():
    subset = df[df["Tag"] == tag]
    all_sentences = " ".join(subset["Clean_Sentence"].dropna()).lower()
    tokens = tokenizer.tokenize(all_sentences)
    filtered = [word for word in tokens if word not in stop_words]

    # POS tag & keep only adjectives/adverbs/verbs
    tagged = pos_tag(filtered)
    rich_words = [word for word, pos in tagged if pos.startswith("J") or pos.startswith("R") or pos.startswith("V")]

    # Count and store top 50
    top = Counter(rich_words).most_common(50)
    tagged_words[tag] = top

# Save to txt file
with open("C:/Users/Admin/PycharmProjects/GothicSuspenseDissertation/analysis/tag_cue_lexicon.txt", "w", encoding="utf-8") as f:
    for tag, top_words in tagged_words.items():
        f.write(f"\n=== Top cues for tag: {tag} ===\n")
        for word, count in top_words:
            f.write(f"{word}: {count}\n")

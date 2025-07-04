import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Input
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import re
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import nltk
from nltk import pos_tag, word_tokenize
nltk.download('averaged_perceptron_tagger')

file_path = "C:/Users/Admin/PycharmProjects/GothicSuspenseDissertation/analysis/tag_context_sentences.csv"
df = pd.read_csv(file_path)

le = LabelEncoder()
df["Author_encoded"] = le.fit_transform(df["Author"])

cue_lexicon = {
    "amb": [
        "perhaps", "seemed", "appeared", "apparently", "might", "may", "could have",
        "I know not", "I cannot tell", "I was unsure", "thought", "supposed",
        "as if", "as though", "it was as if", "imagined", "I speculated", "I believed",
        "dream", "unreal", "phantom", "illusion", "uncertain cause", "natural or supernatural",
        "strange influence", "peculiar feeling", "impression", "instinct", "curious effect",
        "inexplicable", "half-believed", "delusion", "hallucination", "disoriented",
        "coincidence", "mystified", "a mystery", "mistaken", "I could not explain",
        "unclear", "uncertain", "strange", "odd", "mysterious", "unexplained",
        "beyond understanding", "cannot explain", "not known", "indistinct",
        "blurred", "doubt", "confused", "enigmatic", "an impression", "felt wrong",
        "no reason", "what it meant", "unknown origin", "hard to say", "unnatural",
        "unusual", "somehow", "confused", "sense", "no explanation"
    ],
    "delay_withheld_info": [
        "never told", "unspoken", "he would not say", "refused to answer", "he remained silent",
        "he said nothing", "left unspoken", "not revealed", "didn't explain", "withheld",
        "I could not know", "no one knew", "a secret", "refused to speak", "I cannot speak of it",
        "it passed without mention", "left unsaid", "concealed", "not clear why",
        "missing piece", "avoided the subject", "incomplete", "obscured", "half-said",
        "left vague", "he faltered", "broke off", "when you come back", "nothing more was said",
        "I had to wait", "it was never spoken aloud", "nothing could be discovered",
        "no answer", "didn't say", "remained quiet", "silent", "no explanation",
        "something unsaid", "he would not", "it was left", "avoided", "evaded",
        "kept from me", "held back", "I never learned", "delayed", "he paused",
        "not at liberty", "uncertain motive", "refused to explain", "was not clear",
        "the reason unknown", "not disclosed", "expected", "abruptly", "certain", "strangely",
        "unanswered", "truth", "not told"
    ],
    "delay_foreshadowing": [
        "he had a feeling", "premonition", "foreboding", "he warned", "ominous", "if you must",
        "don't blame me", "you will see", "this is only the beginning", "he predicted",
        "bad sign", "dark omen", "dark look", "strange expression", "strange gesture",
        "mirror", "blood", "storm", "shadow", "red light", "broken glass", "clock stopped",
        "closed door", "sealed room", "buried object", "scratched floor", "open grave",
        "as if something was about to happen", "he insisted", "it was not over", "not the end",
        "he seemed afraid of something", "don't speak of it", "don't open it", "don't call out",
        "he sensed", "a feeling", "a shadow", "the sense that", "unease",
        "a strange sign", "not quite right", "more to come", "dark shape",
        "he warned me", "portent", "it meant something", "it would happen",
        "marked change", "symbol", "a signal", "harbinger", "ill omen",
        "sign of", "strange event", "nothing happened yet", "he stared ahead",
        "perhaps", "dread", "sense", "doom", "warning", "uneasy"
    ],
    "delay_cliffhanger": [
        "suddenly", "in an instant", "before he could", "at that moment", "interrupted",
        "abruptly", "just then", "a noise cut through", "he turned and", "as he reached",
        "without warning", "he opened the door and", "cut short", "he gasped", "he froze",
        "he stopped speaking", "sentence was broken", "as he was about to", "a knock came",
        "at that very instant", "all at once", "as if struck", "on the verge of", "climax interrupted",
        "all of a sudden", "just then", "something moved", "at once",
        "unexpectedly", "he opened the", "mid-sentence", "something behind",
        "the door opened", "and then", "just as", "on the edge", "break in thought", "as it began",
        "just before", "right then", "sudden"
    ],
    "delay_pacing": [
        "long enough to", "stood still", "lingered", "paused", "no one moved", "took his time",
        "a long silence", "step by step", "walked slowly", "deliberately", "repeatedly", "digression",
        "in the meantime", "delayed action", "interrupted by waiting", "slowly", "without reply",
        "he hesitated", "gradual", "drew it out", "breathless pause", "sentence winding on",
        "before anything happened", "held back", "built up", "with great care", "calm before the storm",
        "with care", "drawn out", "repeated", "for a long time", "he considered",
        "while nothing happened", "long description", "recounted", "little by little",
        "lingered on", "stopped to think", "did not act", "held moment", "built anticipation",
        "before the moment", "waiting", "rapidly", "rapid", "soon", "sound", "time passed",
        "delayed"
    ],
    "atmosphere": [
        "gloom", "stillness", "silence", "cold", "wind", "fog", "dim", "musty", "oppressive",
        "clammy", "damp", "dripping", "dark", "shadows", "twilight", "night", "black",
        "chill", "echo", "muffled", "deadly quiet", "low light", "decay", "desolate",
        "unearthly", "uncanny", "confined", "crumbling", "solitary", "rotting", "foul air",
        "bleak", "dusty", "no sound", "deafening silence", "morbid", "rottenness",
        "red glow", "tomb-like", "unnatural calm", "shadowy", "gloomy", "tight", "trapped",
        "dull", "empty", "red light", "thick air", "uneasy", "abandoned", "sealed",
        "claustrophobic", "low ceiling", "old", "weathered", "dead air", "airless", "quiet",
        "desolation", "heavy", "decayed", "narrow", "echo", "echoing", "stale"
    ]
}

def count_cues(text, cue_list):
    return sum(text.lower().count(cue.lower()) for cue in cue_list)

df["negated_cue"] = df["Clean_Sentence"].str.contains(
    r"\b(not|never|no)\b.*\b(seem|appear|know|say|explain|speak|understand)\b",
    case=False, regex=True
).astype(int)

for tag, cue_list in cue_lexicon.items():
    df[f"{tag}_count"] = df["Clean_Sentence"].apply(lambda x: count_cues(str(x), cue_list))

for tag in ["amb", "delay_withheld_info", "delay_foreshadowing", "delay_cliffhanger", "delay_pacing", "atmosphere"]:
    count_col = f"{tag}_count"
    adj_col = f"{tag}_adjusted"
    df[adj_col] = df[count_col] - df["negated_cue"]



df["negated_cue"] = df["Clean_Sentence"].str.contains(
        r"\b(not|never|no)\b.*\b(seem|appear|know|say|explain|speak|understand)\b",
        case=False, regex=True
    ).astype(int)

df["length"] = df["Clean_Sentence"].apply(lambda x: len(str(x).split()))
df["punctuation_density"] = df["Clean_Sentence"].apply(
    lambda x: sum([1 for c in str(x) if c in '.,;!?']) / (len(str(x)) + 1)
)

df["avg_word_length"] = df["Clean_Sentence"].apply(
    lambda x: np.mean([len(word) for word in str(x).split()]) if len(str(x).split()) > 0 else 0
)


df["ends_ellipsis"] = df["Clean_Sentence"].str.strip().str.endswith("...").astype(int)
df["ends_dash"] = df["Clean_Sentence"].str.strip().str.endswith("-").astype(int)


df["has_semicolon"] = df["Clean_Sentence"].str.contains(";").astype(int)

def pos_density(text, tag_prefix):
    words = word_tokenize(str(text))
    if not words:
        return 0
    pos_tags = pos_tag(words)
    count = sum(1 for word, tag in pos_tags if tag.startswith(tag_prefix))
    return count / len(words)

df["adj_density"] = df["Clean_Sentence"].apply(lambda x: pos_density(x, "JJ"))
df["adv_density"] = df["Clean_Sentence"].apply(lambda x: pos_density(x, "RB"))
df["modal_density"] = df["Clean_Sentence"].apply(lambda x: pos_density(x, "MD"))

def pos_density(text, prefix):
    words = word_tokenize(str(text))
    tagged = pos_tag(words)
    count = sum(1 for word, tag in tagged if tag.startswith(prefix))
    return count / len(words) if len(words) > 0 else 0

df["adj_density"] = df["Clean_Sentence"].apply(lambda x: pos_density(x, "JJ"))
df["adv_density"] = df["Clean_Sentence"].apply(lambda x: pos_density(x, "RB"))
df["verb_density"] = df["Clean_Sentence"].apply(lambda x: pos_density(x, "VB"))

df = pd.get_dummies(df, columns=["Tag"])

drop_cols = ["Author", "Sentence", "Clean_Sentence", "Author_encoded"] + [col for col in df.columns if col.startswith("Tag_")]
adjusted_tags = [
    "amb_adjusted", "delay_withheld_info_adjusted", "delay_foreshadowing_adjusted",
    "delay_cliffhanger_adjusted", "delay_pacing_adjusted", "atmosphere_adjusted"
]

linguistic_features = [
    "length", "punctuation_density", "avg_word_length",
    "ends_ellipsis", "ends_dash", "has_semicolon",
    "adj_density", "adv_density", "modal_density", "verb_density"
]

interaction_features = ["amb_and_atmosphere"] if "amb_and_atmosphere" in df.columns else []

feature_cols = adjusted_tags + linguistic_features + interaction_features
X = df[feature_cols].select_dtypes(include=[np.number]).values
y = df["Author_encoded"].values
y_cat = to_categorical(y)

scaler = StandardScaler()
X = scaler.fit_transform(X)

sss = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in sss.split(X, df["Author_encoded"]):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

y_train_cat = to_categorical(y_train)
y_test_cat = to_categorical(y_test)




model = Sequential()
model.add(Input(shape=(X.shape[1],)))
model.add(Dense(64, activation="relu"))
model.add(Dense(32, activation="relu"))
model.add(Dense(y_cat.shape[1], activation="softmax"))

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
model.fit(X_train, y_train_cat, epochs=20, batch_size=16, validation_split=0.2)
loss, accuracy = model.evaluate(X_test, y_test_cat)



print(f"Test Accuracy: {accuracy * 100:.2f}%")

lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)

y_pred = lr.predict(X_test)
print("Logistic Regression Test Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=le.classes_))

cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, cmap="Blues", xticklabels=le.classes_, yticklabels=le.classes_)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Logistic Regression Confusion Matrix")
plt.show()


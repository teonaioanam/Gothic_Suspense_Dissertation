import os
import re
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from itertools import combinations


annotation_dir = r"C:\Users\Admin\PycharmProjects\GothicSuspenseDissertation\annotations"
output_dir = r"C:\Users\Admin\PycharmProjects\GothicSuspenseDissertation\analysis"
os.makedirs(output_dir, exist_ok=True)

#patterns
tag_patterns_list = [
    r"<amb>",
    r"<atmosphere>",
    r"<delay type=\"withheld-info\">",
    r"<delay type=\"foreshadowing\">",
    r"<delay type=\"cliffhanger\">"
]
tag_patterns_dict = {
    "<amb>": "amb",
    "<atmosphere>": "atmosphere",
    "<delay type=\"withheld-info\">": "delay:withheld-info",
    "<delay type=\"foreshadowing\">": "delay:foreshadowing",
    "<delay type=\"cliffhanger\">": "delay:cliffhanger"
}


story_info = {
    "usher": ("Poe", "The Fall of the House of Usher"),
    "signal": ("Dickens", "The Signal-Man"),
    "monkey": ("Jacobs", "The Monkey’s Paw"),
    "judge": ("Stoker", "The Judge’s House")
}

#tag density per story + counts
records = []

for filename in os.listdir(annotation_dir):
    if filename.endswith(".txt"):
        basename = filename.replace("_annotated.txt", "")
        path = os.path.join(annotation_dir, filename)
        with open(path, "r", encoding="utf-8") as file:
            text = file.read()

        word_count = len(re.findall(r"\b\w+\b", text))
        tag_counts = Counter()

        for pattern in tag_patterns_list:
            tag_label = re.findall(r"<(\w+)", pattern)[0] if "delay" not in pattern else pattern[7:-2]
            tag_counts[tag_label] = len(re.findall(pattern, text))

        author, full_title = story_info.get(basename, ("Unknown", basename.title()))

        row = {
            "Author": author,
            "Story": full_title,
            "Word Count": word_count,
        }
        row.update(tag_counts)
        records.append(row)

df = pd.DataFrame(records).fillna(0).sort_values(by="Author")
df.to_csv(os.path.join(output_dir, "author_tag_summary.csv"), index=False)


tag_columns = [col for col in df.columns if col not in ["Author", "Story", "Word Count"]]
df_plot = df.set_index("Story")[tag_columns]

plt.figure(figsize=(10, 6))
df_plot.plot(kind="bar", stacked=True)
plt.title("Tag Counts by Story")
plt.ylabel("Count")
plt.xlabel("Story")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.grid(True)
plt.savefig(os.path.join(output_dir, "tag_counts_by_story_table.png"))
plt.show()

#sentence-level co-occurence
cooccurrence_counter = Counter()

def detect_tags_in_sentence(sentence, tag_patterns):
    present_tags = set()
    for pattern, label in tag_patterns.items():
        if re.search(re.escape(pattern), sentence):
            present_tags.add(label)
    return present_tags

for filename in os.listdir(annotation_dir):
    if filename.endswith(".txt"):
        with open(os.path.join(annotation_dir, filename), "r", encoding="utf-8") as file:
            text = file.read()


        sentences = re.split(r'(?<=[.!?])\s+', text)

        for sentence in sentences:
            tags_in_sentence = detect_tags_in_sentence(sentence, tag_patterns_dict)
            for tag_pair in combinations(sorted(tags_in_sentence), 2):
                cooccurrence_counter[tag_pair] += 1


cooc_rows = []
for (tag1, tag2), count in cooccurrence_counter.items():
    cooc_rows.append({
        "Tag 1": tag1,
        "Tag 2": tag2,
        "Co-occurrence Count": count
    })

cooc_df = pd.DataFrame(cooc_rows)
cooc_df.to_csv(os.path.join(output_dir, "sentence_level_tag_cooccurrences.csv"), index=False)

#author-averages
density_records = []

for _, group in df.groupby("Author"):
    author = group["Author"].iloc[0]
    total_words = group["Word Count"].sum()
    summed_tags = group[tag_columns].sum()
    densities = (summed_tags / total_words) * 1000
    density_row = {"Author": author}
    density_row.update(densities.round(2))
    density_records.append(density_row)

author_df = pd.DataFrame(density_records).set_index("Author")
author_df.to_csv(os.path.join(output_dir, "tag_density_by_author.csv"))

plt.figure(figsize=(10, 6))
author_df.plot(kind="bar")
plt.title("Average Tag Density by Author (per 1000 words)")
plt.ylabel("Tag Density")
plt.xlabel("Author")
plt.xticks(rotation=0)
plt.tight_layout()
plt.grid(True)
plt.savefig(os.path.join(output_dir, "tag_density_by_author.png"))
plt.show()

#local styles
tag_patterns_dict = {
    "<amb>": "amb",
    "<atmosphere>": "atmosphere",
    "<delay type=\"withheld-info\">": "delay:withheld-info",
    "<delay type=\"foreshadowing\">": "delay:foreshadowing",
    "<delay type=\"cliffhanger\">": "delay:cliffhanger"
}

tag_contexts = []

for filename in os.listdir(annotation_dir):
    if filename.endswith(".txt"):
        basename = filename.replace("_annotated.txt", "")
        author, _ = story_info.get(basename, ("Unknown", basename.title()))
        with open(os.path.join(annotation_dir, filename), "r", encoding="utf-8") as file:
            text = file.read()


        sentences = re.split(r'(?<=[.!?])\s+', text)

        for sentence in sentences:
            sentence_clean = sentence.strip()
            for pattern, label in tag_patterns_dict.items():
                matches = re.findall(re.escape(pattern), sentence)
                if matches:
                    for _ in matches:
                        tag_contexts.append({
                            "Author": author,
                            "Tag": label,
                            "Sentence": sentence_clean,
                            "Length": len(re.findall(r'\b\w+\b', sentence_clean))
                        })

context_df = pd.DataFrame(tag_contexts)
context_df["Clean_Sentence"] = context_df["Sentence"].str.replace(r"<[^>]+>", "", regex=True).str.strip()
context_df.to_csv(os.path.join(output_dir, "tag_context_sentences.csv"), index=False)

#timeline of tags
timeline_rows = []

for filename in os.listdir(annotation_dir):
    if filename.endswith(".txt"):
        basename = filename.replace("_annotated.txt", "")
        author, title = story_info.get(basename, ("Unknown", basename.title()))
        with open(os.path.join(annotation_dir, filename), "r", encoding="utf-8") as file:
            text = file.read()

        words = re.findall(r'\b\w+\b', text)
        total_words = len(words)


        for pattern, label in tag_patterns_dict.items():
            for match in re.finditer(re.escape(pattern), text):
                start_pos = match.start()

                preceding_text = text[:start_pos]
                word_index = len(re.findall(r'\b\w+\b', preceding_text))
                relative_position = round((word_index / total_words) * 100, 2)
                timeline_rows.append({
                    "Author": author,
                    "Story": title,
                    "Tag": label,
                    "Position (%)": relative_position
                })


timeline_df = pd.DataFrame(timeline_rows)
timeline_df.to_csv(os.path.join(output_dir, "tag_timeline.csv"), index=False)


import seaborn as sns

plt.figure(figsize=(10, 6))
for story in timeline_df["Story"].unique():
    subset = timeline_df[timeline_df["Story"] == story]
    sns.histplot(data=subset, x="Position (%)", hue="Tag", bins=20, multiple="stack", element="step", label=story)

plt.title("Suspense Tag Distribution Across Story Progression")
plt.xlabel("Story Progress (%)")
plt.ylabel("Tag Count")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "tag_timeline_plot.png"))
plt.show()

print(f"{filename} -> basename: {basename} → author: {author}")
print("All annotation files:", os.listdir(annotation_dir))


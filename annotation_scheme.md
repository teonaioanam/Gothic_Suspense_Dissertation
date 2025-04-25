# Annotation Scheme for Gothic Suspense

## 1. Introduction

The purpose of this scheme is to support a linguistic and stylistic analysis of suspense in  
Gothic fiction in order to identify and categorize instances of suspenseful language and narrative  
techniques across a corpus of 19th-century Gothic short stories. Through this annotation:

- The frequency and distribution of suspense markers is quantitatively analysed  
- The relationship between narrative structure and emotional tension is explored  
- Stylistic patterns between texts and authors are compared

This scheme is used to manually annotate the corpus,the tagged texts then forming the basis of a
literary interpretation through analysed aspects such as frequency counts, temporal distribution
and cross-textual comparison. The final objective is to provide insight into how suspense is 
linguistically encoded, and how stylistic choices contribute to the unsettling atmosphere
 characteristic of the Gothic genre.

## 2. Tag Overview


| Tag                             | Description                                 | Example (Text)                                                                                                                                         |
|----------------------------------|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<amb>`                          | Marks instances of ambiguity                | *"I know not how it was—but, with the first glimpse of the building, a sense of insufferable gloom pervaded my spirit."* (*The Fall of the House of Usher*) |
| `<delay type="foreshadowing">`   | Hints at future events                      | *"It had a spell put on it by an old fakir, a very holy man. He wanted to show that fate ruled people’s lives, and that those who interfered with it did so to their sorrow."* (*The Monkey’s Paw*) |
| `<delay type="cliffhanger">`     | Sudden interruption at a tense moment       | *"There at the end of the rope of the great alarm bell hung the body of the student, and on the face of the Judge in the picture was a malignant smile."* (*The Judge’s House*) |
| `<delay type="withheld-info">`   | Information is deliberately withheld        | *"Some of us think he’s not quite right in the head, and between ourselves, he has been trying to get on board the train for weeks."* (*The Signal-Man*) |
| `<delay type="pacing">`          | Stylistic slowing of narrative tension      | *"I looked upon the scene before me—upon the mere house, and the simple landscape features of the domain—upon the bleak walls—upon the vacant eye-like windows..."* (*The Fall of the House of Usher*) |


## 3. Definitions

This annotation scheme identifies two key strategies used to create suspense in Gothic fiction:  
**ambiguity** and **narrative delay**. The tags below are applied to specific linguistic or  
narrative patterns that evoke uncertainty, anticipation, or emotional tension in the reader.

### `<amb>` — Ambiguity

This tag is used when the meaning of a sentence or event is **unclear or open to multiple  
interpretations**:  
- Vague perceptions or unclear causes  
- Epistemic verbs (*seemed*, *perhaps*, *might*)  
- Unreliable narration or unclear motives  

---

### `<delay type="foreshadowing">` — Foreshadowing

This tag is used when  the text **hints at a future event** without explicitly revealing it:
- Statements suggesting coming danger or consequences  
- Symbolic or ominous remarks  
- Premonitory dialogue  
---

### `<delay type="cliffhanger">` — Cliffhanger

This tag is used when **sudden breaks in narrative flow** appear at a moment of high tension:
- Sentences that end abruptly  
- Unfinished thoughts or withheld outcomes  
- Shocking final lines of chapters or scenes  
---

### `<delay type="withheld-info">` — Withheld Information

This tag is used when key details are **deliberately left out**:
- Characters speaking vaguely or avoiding the truth  
- The narrator omitting critical background  
- Hints at secrets the reader isn't yet allowed to know  
---

### `<delay type="pacing">` — Pacing

This tag is used when the author **slows down the delivery of important information**:
- Long, digressive sentences  
- Repetition or excessive description  
- Embedded or nested clauses before a key moment   

## 5. Annotation Format

- All annotations are inserted **inline** using XML-style tags directly within the `.txt` files.

- Each tag wraps a suspenseful sentence or clause:
```xml
<amb>I know not how it was—but, with the first glimpse of the building, a sense of insufferable gloom pervaded my spirit.</amb>

<delay type="withheld-info">Some of us think he’s not quite right in the head...</delay>
```









## Annotation Notes

### The Fall of the House of Usher

---
#### Annotation Note 1 — Pacing vs. Exposition

**Text (Source):**  
> During the whole of a dull, dark, and soundless day in the  
autumn of the year, when the clouds hung oppressively low in the  
heavens, I had been passing alone, on horseback, through a  
singularly dreary tract of country; and at length found myself,  
as the shades of the evening drew on, within view of the  
melancholy House of Usher.

**Tagging Consideration:**  
Possible candidate for `<delay type="pacing">` due to stylistic slowing of narrative  
movement before reaching the House.

**Tagging Decision:**  
Not tagged.

**Rationale:**  
- While the sentence slows temporal progression, it serves as scene-setting rather than strategic delay.  
- The narrator’s arrival does not trigger a suspenseful event or key revelation.  
- The passage functions as **atmospheric exposition**, not narrative suspense modulation.

**Category Boundaries Clarified:**  
- `<delay type="pacing">` requires narrative deceleration that contributes directly to suspense buildup.  
- This passage introduces setting and tone, but does not delay or distort imminent narrative content.


---

#### Annotation Note 2 — Hint vs. Withholding

**Text (Source):**  
> I learned, moreover, at intervals, and through broken and equivocal hints, another singular  
feature of his mental condition.

**Tagging Consideration:**  
Initially considered for `<amb>` and `<delay type="withheld-info">` due to the vague phrasing  
("broken and equivocal hints") and the mention of a "singular feature" left unexplained.

**Tagging Decision:**  
Not tagged.

**Rationale:**  
- While the narrator reports having received partial information, he clearly states he has **learned** something 
specific.  
- The sentence functions as a **narrative transition**, not an instance of withheld content.  
- No interpretive instability or uncertainty is introduced; suspense is generated in the following sentence, not here.

**Category Boundaries Clarified:**  
- `<delay type="withheld-info">` requires the narrator or text to **withhold** known content from the reader.  
- `<amb>` requires semantic uncertainty or interpretive hesitation.  
- This sentence does **neither**; it frames what was learned, not what is withheld or unclear.



---

#### Annotation Note 3 — Conceptual Ambiguity vs. Withholding

**Text:**  
> He was enchained by certain superstitious impressions in regard to the dwelling which he  
tenanted, and whence, for many years, he had never ventured forth--in regard to an influence  
whose supposititious force was conveyed in terms too shadowy here to be re-stated--an influence  
which some peculiarities in the mere form and substance of his family mansion, had, by dint of  
long sufferance, he said, obtained over his spirit--an effect which the physique of the grey  
walls and turrets, and of the dim tarn into which they all looked down, had, at length, brought  
about upon the morale of his existence.

**Tagging Consideration:**  
Candidate for `<amb>`, `<delay type="withheld-info">`, and `<delay type="foreshadowing">` due to suggestive phrasing, 
conceptual vagueness, and suspenseful tone.

**Tagging Decision:**  
Tagged only as `<amb>`.

**Rationale:**  
- The suspense stems from **semantic opacity**, not from withheld narrative content.  
- Expressions like “superstitious impressions,” “supposititious force,” and “terms too shadowy to be re-stated” evoke 
**interpretive instability**.  
- There is **no direct postponement** of content (excluding withheld-info), and **no anticipatory cue** for a future 
event (excluding foreshadowing).

**Category Boundaries Clarified:**  
- `<amb>` captures unresolved or unclear meaning without temporal delay.  
- `<delay type="withheld-info">` would require known content deliberately withheld.  
- `<delay type="foreshadowing">` requires forward-pointing cues, which are not present here.


---

#### Annotation Note 4 — Affective Dread vs. Taggable Suspense

**Text:**  
> There was  
an iciness, a sinking, a sickening of the heart--an unredeemed  
dreariness of thought which no goading of the imagination could  
torture into aught of the sublime.

**Tagging Consideration:**  
Initially considered for `<atmosphere>` due to the language of sensory unease and emotional heaviness. Evaluated as 
potential environmental dread expressed through affective perception.

**Tagging Decision:**  
Not tagged.

**Rationale:**  
- The line describes **internal emotional and physiological sensations** (e.g., “sickening of the heart,” 
“dreariness of thought”).  
- It contains **no environmental or spatial reference**, but the dread is **affective, not descriptive**.  
- The sensory terms (“iciness,” “sinking”) are metaphorical and anchored in mood, not place.  
- While the emotion results from prior atmospheric buildup, this line itself does not instantiate a suspense mechanism.

**Category Boundaries Clarified:**  
- `<atmosphere>` requires explicit **environmental cues** (e.g., architecture, weather, decay) that generate dread 
through **setting**, not internal affect.  
- Affective dread is a **response to suspense**, not always a taggable device in itself.  
- No ambiguity, delay, or environmental tension is constructed in this line independently.

---

#### Annotation Note 5 — Ambiguity and Atmospheric Overlap

**Text:**  
> There grew in my mind a strange fancy... I had so worked upon my imagination as really to believe that about the whole
mansion and domain there hung an atmosphere peculiar to themselves and their immediate vicinity—an atmosphere which had 
no affinity with the air of heaven, but which had reeked up from the decayed trees, and the grey wall, and the silent 
tarn—a pestilent and mystic vapour, dull, sluggish, faintly discernible, and leaden-hued.

**Tagging Consideration:**  
Candidate for both `<amb>` and `<atmosphere>`. Evaluated for overlap between subjective perception  
and sensory environmental dread.

**Tagging Decision:**  
Tagged with both `<amb>` and `<atmosphere>`, applied to separate portions of the sentence.

**Rationale:**  
- The narrator frames his vision as a **“strange fancy”** and calls it **“ridiculous,”** indicating self-doubt.  
- The belief in an atmosphere with **“no affinity with the air of heaven”** introduces **supernatural suggestion**, 
triggering `<amb>`.  
- The second half transitions into detailed **sensory imagery**: *“decayed trees,”* *“grey wall,”* *“pestilent vapour”*,
which fulfills the criteria for `<atmosphere>`.

**Category Boundaries Clarified:**  
- `<amb>` captures the narrator’s internal uncertainty and the suggestion of an unnatural influence.  
- `<atmosphere>` isolates the descriptive elements that evoke dread through decay, stillness, and visual gloom.  
- These tags are **functionally distinct**, even though they occur in the same sentence.

---

#### Annotation Note 6 — Uncanny Body as Atmosphere and Ambiguity

**Text:**  
> The ghastly pallor of the skin and the miraculous lustre of the eye startled and awed me. The hair, in its wild 
gossamer texture, floated rather than fell about the face. I could not, even with effort, connect its Arabesque 
expression with any idea of simple humanity.

**Tagging Consideration:**  
Evaluated for overlap between `<amb>` and `<atmosphere>` due to the shifting function of bodily description as both 
perceptual distortion and environmental dread.

**Tagging Decision:**  
Tagged with both `<amb>` and `<atmosphere>`, applied to distinct, sentence-level segments.

**Rationale:**  
- The narrator’s reaction to the unnatural pallor and luminous eyes conveys epistemic instability and awe, justifying 
`<amb>`.  
- The hair’s strange visual behavior (*“gossamer texture,”* *“floated rather than fell”*) produces atmospheric unease, 
qualifying for `<atmosphere>`.  
- The final sentence expresses full perceptual collapse (*“no idea of simple humanity”*), which completes the ambiguity 
arc and warrants a second `<amb>`.

**Category Boundaries Clarified:**  
- `<amb>` captures identity confusion and supernatural suggestion in physical perception.  
- `<atmosphere>` is applied when bodily traits are rendered in terms that evoke environmental dread or spatial 
strangeness.  
- The tags isolate structurally and functionally distinct suspense effects, even when occurring within a continuous 
character description.

---

#### Annotation Note 7 — Perceived Influence Without Suspense

**Text:**
> The result was discoverable, he added, in that silent, yet importunate and terrible influence which for centuries had 
moulded the destinies of his family, and which made him what I now saw him—what he was. Such opinions need no comment, 
and I will make none.

**Tagging Consideration:**  
Candidate for `<amb>` or `<delay type="withheld-info">` due to mention of an undefined influence and long-term familial 
impact.

**Tagging Decision:**

Not tagged.

**Rationale:**
- While the sentence references a vague and oppressive influence, its function is expository, summarizing beliefs 
already expressed.
- There is no semantic ambiguity (as defined by interpretive instability) or narrative withholding; the influence is 
already described and its effects broadly attributed.
- The narrator’s tone is reflective, not suspense-generating. The phrase “such opinions need no comment” signals 
closure, not uncertainty.

**Category Boundaries Clarified:**  
- `<amb>` requires conceptual instability or interpretive doubt.
- `<delay type="withheld-info">` applies only when narrative content is postponed or obscured.
- This sentence consolidates prior exposition and does not introduce new suspenseful uncertainty.

---

#### Annotation Note 8 — Transitional Time Clause Without Pacing

**Text:**  
> And now, some days of bitter grief having elapsed, an observable change came over the features of the mental disorder
of my friend.

**Tagging Consideration:**  
- Candidate for `<delay type="pacing">` due to fronted temporal clause and the emotional buffer before a shift in the 
character's mental state.

**Tagging Decision:**  
**Not tagged.**

**Rationale:**  
- The sentence introduces a new phase of psychological deterioration,  
  but does so through a brief, linear transition, not through syntactic or descriptive delay.  
- The temporal clause (“some days of bitter grief having elapsed”) functions as narrative framing,  
  not suspenseful slowdown.  
- The sentence structure is simple and direct, lacking the embedded or recursive constructions  
  typical of suspense-generating pacing.  
- The emotional register (grief) supports mood but does not extend or delay narrative progression.

**Category Boundaries Clarified:**  
- `<delay type="pacing">` requires meaningful structural slowing of narrative flow,  
  such as excessive descriptive buildup, syntactic complexity, or delayed resolution of a clause’s predicate.  
- Temporal framing devices or transitional clauses that do not interfere with sentence momentum  
  should remain untagged, even when adjacent to suspenseful developments.

---

#### Annotation Note 9 — Withheld Interpretation of Emotional Response

**Text:**  
> Could I have judged, indeed, by the wild overstrained air of vivacity with which he hearkened, or apparently 
hearkened, to the words of the tale, I might well have congratulated myself upon the success of my design.

**Tagging Consideration:**  
Candidate for `<amb>` or `<delay type="withheld-info">` due to the narrator’s uncertainty about Usher’s reaction and 
the vague description of attention and emotion.

**Tagging Decision:**  
Tagged as `<delay type="withheld-info">`.

**Rationale:**  
- The passage centers on a **narrative gap in the narrator’s understanding** of Usher’s emotional state.  
- While it contains some **epistemic phrasing** (e.g., “apparently hearkened”), the ambiguity lies not in meaning but 
in **access** —  
  the narrator **withholds interpretive certainty** and defers judgment.  
- The suspense comes from the **delayed resolution** of whether Usher is truly affected, feigning interest, or 
concealing something deeper.  
- The clause operates narratively as a **withheld conclusion**, not as a self-contained interpretive instability.

**Category Boundaries Clarified:**  
- `<amb>` is reserved for passages with **conceptual instability** or **blurred interpretations**.  
- `<delay type="withheld-info">` captures moments where a **relevant narrative judgment or insight is postponed**, even 
when speculation is present.

--- 

### The Judge's House

---

#### Annotation Note 9 — Ambiguous Perception via Anthropomorphized Rat

**Text:**  
> *There, on the great high-backed carved oak chair by the right side of the fire-place sat an enormous rat,  
steadily glaring at him with baleful eyes.*

**Tagging Consideration:**  
- Candidate for `<amb>` due to the surreal framing and emotionally charged presentation of the rat.
- The sentence introduces a stylized and psychologically disturbing image that invites interpretive hesitation.

**Tagging Decision:**  
- **Tagged as `<amb>`**

**Rationale:**  
- The description constructs an *uncanny tableau*, not merely a pest encounter:  
- *“Enormous rat”* signals unnatural proportions, outside normal expectations.  
- *“Glaring with baleful eyes”* assigns the rat human-like intent and hostility.  
- Its stillness and placement in a *“high-backed carved oak chair”* evoke a scene of unnatural poise and symbolism.  
- According to thepython --version
 annotation scheme, this constitutes **conceptual instability**, triggering the reader’s
hesitation between realism and supernatural symbolism.  
- The moment aligns with ambiguity because the perception of the rat transcends realism but is not
- definitively magical, it lives in the uncertain space between natural and preternatural interpretation.

**Category Boundaries Clarified:**  
- This is not `<delay type="withheld-info">`, since the narrator is not deferring a conclusion, the moment itself is
interpretively unstable.  
- Nor is it `<atmosphere>`, as the suspense is not built by mood but by *epistemic dissonance*.  
- This fits the `<amb>` tag’s core criterion: **blurred perception with supernatural suggestion** but without  
resolution.

---

#### Annotation Note 10 — No Withheld Information in Mrs. Witham’s Reaction

**Text:**  
> "Mercy on us," said Mrs. Witham, "an old devil, and sitting on a chair by the fireside! Take care, sir! take care! 
There's many a true word spoken in jest."

**Tagging Consideration:**  
- Initially considered for `<delay type="withheld-info">` due to its suggestive tone and indirect warning.

**Tagging Decision:**  
No tag assigned.

**Rationale:**  
- The `<delay type="withheld-info">` tag requires a **narrative or character-based deferral of relevant interpretive 
judgment**, typically where emotional, perceptual, or causal information is consciously withheld or postponed.
- In this case, **Mrs. Witham fully expresses her view**, drawing on superstition and folk logic. She does not defer 
clarification or withhold interpretive insight.
- The statement is **speculative**, not secretive or strategically opaque. There is no narrative suspense built around 
withheld knowledge.
- While the line is atmospheric and colorful, it is **not structurally or psychologically ambiguous** and does not align
with the criteria for `<amb>` or delay tags.

**Category Boundaries Clarified:**  
- Not `<delay type="withheld-info">` because no relevant insight is withheld or postponed.
- Not `<amb>` because the speaker is not engaging in interpretive hesitation, but rather expressing a folkloric 
superstition directly.

---  

### **Annotation Note 7 — Repetitive Rat Appearances as Pacing**

> **Text**  
"There, on the great old high-backed carved oak chair..."  
"The lamp almost fell from his hand... baleful eyes peering..."  
"There, in the judge's arm-chair... fiendish leer."  
"There, on the great high-backed carved oak chair sat the judge..."

**Tagging Consideration**  
- The rat and its associated eyes appear **repeatedly** in the same spatial position (the Judge’s chair), with each 
reappearance becoming more intense and uncanny. This recurrence does not just contribute to supernatural suggestion, but
serves a **rhythmic, temporal function** in building dread across the narrative arc.

**Tagging Decision**  
- These moments were tagged as `<delay type="pacing">` because the rat’s recurring presence in the same place **stalls 
narrative resolution** while escalating tension. 
- The **deliberate return to the same visual anchor** (the oak chair, the
baleful eyes) creates a **slow-burning ritual of fear** that paces the horror incrementally.

**Rationale**  
- According to the annotation scheme, `<delay type="pacing">` includes techniques that **draw out suspense** without 
immediate resolution. Repetition is one such technique when used to create **temporal hesitation** and emotional 
buildup. Each instance of the rat’s appearance prolongs the moment before climactic action (confrontation with the Judge
or death), making the narrative **stall in dread**.

 **Category Boundary Clarified**  
- While repetition might suggest a unique `<delay type="repetition">` tag, in this annotation framework, such repetitive
structural cues fall under **pacing** because their function is not semantic variety but **rhythmic suspense delay**. 
- The **ritualistic reappearance** of the rat marks temporal stasis and gradually climaxes into the Judge's embodiment, 
anchoring all four tags under pacing.


### The Monkey's Paw

---

#### Annotation Note 11 — Distraction as Pacing

**Text:**  
> “In the business of supper the talisman was partly forgotten, and afterward the three sat listening in an enthralled 
fashion to a second instalment of the soldier’s adventures in India.”

**Tagging Consideration:**  
- Initially considered for `<delay type="pacing">` due to its narrative deceleration and shift in focus away from the 
supernatural.

**Tagging Decision:**  
No tag assigned.

**Rationale:**  
- Although the sentence slows the narrative and redirects attention to the mundane (supper and travel tales), it lacks a
distinct suspense function per the tagging criteria.  
- The shift does not meaningfully delay or obstruct the development of suspenseful content; the tension resumes soon 
after without structural emphasis on suspenseful postponement.  
- This moment of mundane interlude functions more as *narrative filler* or domestic texture than a strategic delay.

**Category Boundaries Clarified:**  
- Not `<delay type="pacing">` because it does not significantly contribute to suspense through slowed narrative rhythm 
or strategic withholding of event progression.  
- Not `<delay type="withheld-info">` because no interpretive information is suspended.  
- Not `<amb>` because there is no interpretive uncertainty or semantic instability.

---

#### Annotation Note 12 — Deferment, Not Withheld-Info

**Text:**  
> “He has been dead ten days, and besides he—I would not tell you else…”

**Tagging Consideration:**  
- Initially considered for `<delay type="withheld-info">` due to the interruption and avoidance within the utterance.

**Tagging Decision:**  
No tag assigned.

**Rationale:**  
- While the statement delays full emotional access, it **does not strategically withhold information** in the sense 
required by `<delay type="withheld-info">`.
- The speaker is emotionally overwhelmed, not narratively evasive. The moment reads as **reactive discomfort**, 
not the conscious narrative postponement of relevant judgment or explanation.
- The pause is personal and affective, but **not structured to delay insight** for suspense purposes.

**Category Boundaries Clarified:**  
- Not `<delay type="withheld-info">`: the information (about recognition and horror) is expressed, just stammered.
- Not `<amb>`: there is no uncertainty or interpretive blur.
- Best treated as **unmarked emotional distress**, not formal suspense delay.

---

### Annotation Note 13 — Atmospheric Dread Through Post-Burial Silence

> **Text:**  
> `<atmosphere>In the huge new cemetery, some two miles distant, the old people buried their dead, and came back to a house steeped in shadow and silence.</atmosphere>`

**Tagging Consideration:**  
This sentence initially appeared transitional or descriptive, but on closer inspection, it fulfills the criteria for `<atmosphere>` by portraying a **setting suffused with emotional and environmental dread**. The reference to "shadow and silence" transforms the domestic space into a symbolically charged Gothic landscape.

**Tagging Decision:**  
`<atmosphere>`

**Rationale:**  
This clause evokes a profound **atmospheric tension** aligned with the annotation scheme’s criteria:
- The house is described as "steeped in shadow and silence", both of which are canonical Gothic markers of **oppressive quiet and psychological weight**.
- This quiet is unnatural and grief-laden, emphasizing **stillness after trauma**, akin to deathly suspension.
- The sentence is contextually placed right after the burial, intensifying its symbolic weight — **the home has become an extension of the cemetery**.

**Category Boundaries Clarified:**  
Though the passage is short, it conveys a concentrated sensory mood, meeting the threshold for `<atmosphere>` even without extensive descriptive layering. This confirms that **minimalist phrasing can qualify**, as long as the mood aligns with Gothic environmental dread.


---

#### Annotation Note 14 — Final Knock and Withheld Resolution

**Text:**  
> *A cold wind rushed up the staircase, and a long loud wail of disappointment and misery from his wife gave him courage t
> to run down to her side, and then to the gate beyond. The street lamp flickering opposite shone on a quiet and deserted 
road.*

**Tagging Consideration:**  
- Candidate for `<amb>` or `<delay type="cliffhanger">` due to the withheld outcome and emotional signals replacing 
resolution.

**Tagging Decision:**  
No tag assigned.

**Rationale:**  
- The passage withholds the expected supernatural climax, instead presenting **indirect sensory cues**: a cold wind, 
a wail, and a quiet street.  
- However, while this creates **suspense through omission**, it does not contain **enough textual framing** or finality 
to qualify as a tagged cliffhanger.  
- The moment is strongly suggestive, but the structure lacks **explicit narrative emphasis on suspenseful deferral**.  
- It also does not qualify as `<amb>`: though the outcome is unknown, the **reader’s interpretive hesitation** is brief 
and doesn’t pervade the surrounding context.

**Category Boundaries Clarified:**  
- Not `<delay type="cliffhanger">` because although the final image suspends resolution, it does not use 
**foregrounded narrative structure** to delay a climax; the silence implies closure, not suspenseful expectation.  
- Not `<amb>` because the lack of resolution does not foster **sustained conceptual instability**.  
- While emotionally evocative, this moment is better treated as **unmarked closure by absence**, not formal suspense 
delay.

---

#### Annotation Note 15 — Ambiguity of Corporate Speech and Emotional Truth

**Text:**  
> “I was to say that ‘Maw and Meggins’ disclaim all responsibility,” continued the other. “They admit no liability at 
> all,”

**Tagging Consideration:**  
Considered skipping the tag due to the apparent clarity of the statement. Ultimately chosen as `<amb>` because the 
passage presents a subtle dissonance between **surface-level legal language** and the **emotional truth** it suppresses.

**Tagging Decision:**  
Tagged as `<amb>`.

**Rationale:**  
- The speaker **quotes** the company’s official message, but the **formality and detachment** of the statement contrasts
with the traumatic emotional context (the death of a child).  
- There is an **implicit tension** between what is said (“no liability”) and what is felt or morally implied (a sense 
of responsibility).  
- The company’s denial is presented through an intermediary (the visitor), further **distancing** the speaker from the 
content and introducing **interpretive ambiguity**: is this emotionally sincere? Legally evasive? A reflection of 
indifference?  
- The line **invites interpretation**, but no single reading is confirmed, the **emotional subtext is unstable**.

**Category Boundaries Clarified:**  
- Not a delay of withheld information, as the **company’s response is explicitly stated**.  
- Instead, this is **a classic case of `<amb>`**, where the reader must navigate the **gap between legalistic discourse 
and emotional resonance**, with no final narrative judgment offered.

---

### Annotation Note 8 — Casual Remark as Foreshadowing

**Text:**  
> *“Herbert will have some more of his funny remarks, I expect, when he comes home,” she said, as they sat at dinner.*

**Tagging Consideration:**  
- Appears lighthearted and casual, spoken during an ordinary domestic moment.  
- Introduces the expectation of Herbert’s safe return, which creates narrative tension once the reader knows his fate.  

**Tagging Decision:**  
**Tagged as `<delay type="foreshadowing">`**

**Rationale:**  
- Foreshadowing applies when future tragic events are hinted at through seemingly innocent or ironic remarks.  
- The mother's comment is oblivious to the horror to come - Herbert’s death and his potential return in altered form.  
- The line primes dramatic irony and reader anxiety, aligning with foreshadowing criteria in the scheme.

**Category Boundaries Clarified:**  
- Not ambiguity: there’s no interpretive uncertainty.  
- Not pacing: it doesn’t delay plot progression.  
- A clear instance of verbal foreshadowing based on dramatic irony and doomed expectation.




### The Signal-Man

---

#### Annotation Note 15 — Overlap Between Ambiguity and Atmosphere

**Text:**  
> *“His post was in as solitary and dismal a place as ever I saw... so much cold wind rushed through it, that it struck 
chill to me, as if I had left the natural world.”*

**Tagging Consideration:**  
- Candidate for `<amb>` due to the phrase "as if I had left the natural world", which introduces a momentary interpretive 
hesitation suggestive of supernatural estrangement. However, also eligible for `<atmosphere>` given the overwhelmingly 
sensory and environmental focus.

**Tagging Decision:**  
**Tagged as `<atmosphere>`** (not dual-tagged).

**Rationale:**  
- The sentence builds sensory dread and psychological discomfort through setting: dripping walls, black tunnel, earthy 
smell, cold wind.
- The phrase "as if I had left the natural world" intensifies the eerie tone, but metaphorically. It expresses affective
displacement, not ontological uncertainty.
- The narrator’s perception remains metaphorical, and no genuine interpretive instability is invited.
- Thus, the suspense created here is immersive and tonal, not cognitive.

**Category Boundaries Clarified:**  
- Not `<amb>` because the metaphoric phrase does not suggest real narrative ambiguity about whether a supernatural event
has occurred.
- Appropriately `<atmosphere>` because it constructs a setting of sensory claustrophobia, physical discomfort, and 
Gothic unease.

---

### Annotation Note 16 — Cliffhanger over Retrospective Ambiguity

> *“I cannot describe the thrill that seized upon me, when, close at the mouth of the tunnel, I saw the appearance of a 
> man, with his left sleeve across his eyes, passionately waving his right arm.”*

**Tagging Consideration:**  

**Tagging Decision:**  
`<delay type="cliffhanger">`  
Not tagged as `<amb>`, but overlap noted.

**Rationale:**  
- Structurally, the sentence introduces a **jarring halt in narrative progression**, inducing suspense just before clarification (“the horror passed in a moment…”).
- The placement at the top of the descent visually and emotionally mirrors earlier uncanny events, **delaying interpretive certainty** and drawing the reader into a momentary narrative gap.
- Although the ambiguity is clarified shortly after, this hesitation functions as a **cliffhanger device**, pulling the reader into suspense before revealing the mundane explanation.

**Category Boundaries Clarified:**  
- Not `<amb>`: ambiguity is immediately resolved.
- Not `<delay type="foreshadowing">`: the death has already occurred; this is post-event recognition, not anticipatory.
- Strong match for `<delay type="cliffhanger">`, but worth documenting for its **visual and referential overlap** with earlier ambiguous gestures. The repetition contributes to Gothic recurrence and emotional suspense, not just plot delay.









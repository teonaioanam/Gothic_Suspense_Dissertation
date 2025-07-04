import matplotlib.pyplot as plt
import networkx as nx

# Define cue structure
cue_structure = {
    "amb": ["modal verbs", "perceptual/epistemic verbs", "uncertainty/illusion"],
    "delay_foreshadowing": ["prophetic verbs", "symbolic objects", "ominous phrasing"],
    "delay_cliffhanger": ["abrupt breaks", "punctuation-based suspense"],
    "delay_withheld_info": ["hedging", "vague reference", "narrative opacity"],
    "delay_pacing": ["syntactic embedding", "slow narrative tempo"],
    "atmosphere": ["environmental decay", "spatial confinement", "stillness/silence"]
}

# Create graph
G = nx.DiGraph()

# Tag colors
color_map = {
    "amb": "#6a1b9a",
    "delay_foreshadowing": "#7b1fa2",
    "delay_cliffhanger": "#c62828",
    "delay_withheld_info": "#ef6c00",
    "delay_pacing": "#2e7d32",
    "atmosphere": "#4e342e"
}

# Add nodes and edges
node_colors = []
for tag, subcues in cue_structure.items():
    G.add_node(tag)
    node_colors.append(color_map[tag])
    for sub in subcues:
        G.add_node(f"{tag}_{sub}")
        G.add_edge(tag, f"{tag}_{sub}")
        node_colors.append("#d7ccc8")  # neutral subcue color

# Layout
pos = nx.spring_layout(G, k=1.3, seed=42)

# Draw
plt.figure(figsize=(12, 8))
nx.draw(
    G, pos,
    with_labels=True,
    node_color=node_colors,
    node_size=2200,
    font_size=9,
    font_family="serif",
    edge_color="#888888",
    arrows=False
)

plt.title("Cue Lexicon Structure for Suspense Tagging", fontsize=14, fontweight="bold", pad=20)
plt.tight_layout()
plt.show()

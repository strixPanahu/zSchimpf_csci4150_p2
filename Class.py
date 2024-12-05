from matplotlib import pyplot
import networkx
import numpy as np


classes = [
    ("Aliphatic", "Aliphatic", 197),
    ("Aliphatic", "Aromatic", 155),
    ("Fixed cation", "Aliphatic", 127),
    ("Hydroxylic", "Aliphatic", 116),
    ("Aromatic", "Aliphatic", 86),
    ("Thiol", "Aliphatic", 79),
    ("Aliphatic", "Hydroxylic", 76),
    ("Aliphatic", "Thiol", 63),
    ("Aliphatic", "Amide", 62),
    ("Fixed cation", "Anion", 61),
    ("Aliphatic", "Cyclic", 58),
    ("Cyclic", "Cyclic", 54),
    ("Hydroxylic", "Cyclic", 50),
    ("Cyclic", "Fixed cation", 49),
    ("Amide", "Hydroxylic", 44),
    ("Aromatic", "Hydroxylic", 41),
    ("Aliphatic", "Fixed cation", 40),
    ("Amide", "Cation", 40),
    ("Anion", "Hydroxylic", 40),
    ("Aromatic", "Anion", 36),
    ("Hydroxylic", "Fixed cation", 33),
    ("Aliphatic", "Anion", 30),
    ("Cation", "Cation", 29),
    ("Cation", "Fixed cation", 29),
    ("Cyclic", "Aliphatic", 28),
    ("Hydroxylic", "Amide", 25),
    ("Cationic", "Hydroxylic", 25),
    ("Anion", "Fixed cation", 23),
    ("Anion", "Cation", 22),
    ("Hydroxylic", "Cationic", 21),
    ("Anion", "Aliphatic", 21),
    ("Aromatic", "Aromatic", 19),
    ("Amide", "Amide", 19),
    ("Cation", "Hydroxylic", 19),
    ("Amide", "Aliphatic", 18),
    ("Cationic", "Aliphatic", 18),
    ("Cyclic", "Cationic", 16),
    ("Thioether", "Aromatic", 16),
    ("Thioether", "Thiol", 16),
    ("Cyclic", "Amide", 15),
    ("Cation", "Amide", 14),
    ("Amide", "Fixed cation", 13),
    ("Amide", "Thioether", 12),
    ("Anion", "Amide", 12),
    ("Aliphatic", "Cationic", 9),
    ("Anion", "Thioether", 9),
    ("Aromatic", "Thioether", 8),
    ("Cationic", "Thioether", 3),
]

# Create directed graph
connectivity = networkx.DiGraph()

# Add edges
for source, target, weight in classes:
    connectivity.add_edge(source, target, weight=weight)

# Visualization
weights = [d['weight'] for (_, _, d) in connectivity.edges(data=True)]
nodes = [
    "Cyclic", "Hydroxylic", "Aliphatic", "Aromatic", "Fixed cation",
    "Anion", "Amide", "Cationic", "Thioether", "Cation", "Thiol"
]
positions = {  # iterate to complete the list geometrically
    node: (np.cos(2 * np.pi * i / len(nodes)), np.sin(2 * np.pi * i / len(nodes)))
    for i, node in enumerate(nodes)
}

# Draw the graph
pyplot.figure(figsize=(14, 12))
networkx.draw_networkx_nodes(connectivity, positions, node_size=1000, node_color="skyblue")
networkx.draw_networkx_edges(
    connectivity, positions, width=[w / 20 for w in weights],
    alpha=0.7, edge_color="black"
)
networkx.draw_networkx_labels(connectivity, positions, font_size=12, font_color="black")

# Add edge labels (weights)
edge_labels = networkx.get_edge_attributes(connectivity, 'weight')
networkx.draw_networkx_edge_labels(connectivity, positions, edge_labels=edge_labels, font_size=8)

pyplot.title("Amino Acid Classification Connectivity with Hendecagon Layout")
pyplot.show()
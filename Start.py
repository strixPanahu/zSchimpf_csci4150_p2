import networkx
from  matplotlib import pyplot

stop_codons = [
    ("Leucine", "Tryptophan", 11),
    ("Leucine", "Cysteine", 11),
    ("Leucine", "Tryptophan", 10),
    ("Leucine", "Cysteine", 12),
    ("Methionine", "Tryptophan", 4),
    ("Methionine", "Cysteine", 9),
    ("Methionine", "Tryptophan", 12),
    ("Methionine", "Cysteine", 7),
    ("Valine", "Tryptophan", 9),
    ("Valine", "Cysteine", 11),
    ("Valine", "Tryptophan", 9),
    ("Valine", "Cysteine", 9),
]

# Aggregate edge weights
weights = {}
for source, target, weight in stop_codons:
    weights[(source, target)] = weights.get((source, target), 0) + weight

# Direct the graph
amino_acids = networkx.DiGraph()

# Add edges weights
for (source, target), weight in weights.items():
    amino_acids.add_edge(source, target, weight=weight)

# Extract edge weights
weight_output = [d['weight'] for (_, _, d) in amino_acids.edges(data=True)]

# Assign colors
first_column_nodes = {source for source, _, _ in stop_codons}
second_column_nodes = {target for _, target, _ in stop_codons}

# Map colors
node_colors_amino_acids = [
    "skyblue" if node in first_column_nodes else "lightgreen" for node in amino_acids.nodes()
]

# Adjust nodes
amino_acids_pos = {
    "Leucine": (0.0, 0.0),      # Top center
    "Valine": (1.0, 1.0),       # Top right
    "Methionine": (0.5, -1.0),  # Bottom center
    "Tryptophan": (2.0, 0.0),   # Far right
    "Cysteine": (-1.0, 0.0),    # Far left
}

# Draw graph
pyplot.figure(figsize=(10, 8))
networkx.draw_networkx_nodes(
    amino_acids, amino_acids_pos,  node_size=1000, node_color=node_colors_amino_acids
)
networkx.draw_networkx_edges(
    amino_acids,
    amino_acids_pos,
    width=[w / 2 for w in weight_output],
    edge_color="gray",
    alpha=0.7,
)
networkx.draw_networkx_labels(amino_acids, amino_acids_pos, font_size=12, font_color="black")

# Add edge labels
edge_labels = networkx.get_edge_attributes(amino_acids, 'weight')
networkx.draw_networkx_edge_labels(amino_acids, amino_acids_pos, edge_labels=edge_labels, font_size=10)

pyplot.title("Start Codon Succeeding Amino Acid Connectivity")
pyplot.show()
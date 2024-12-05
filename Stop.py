import networkx
from  matplotlib import pyplot

stop_codons = [
    ("Isoleucine", "Glutamine", 9),
    ("Leucine", "Glutamine", 2),
    ("Valine", "Glutamine", 6),
    ("Leucine", "Glutamine", 16),
    ("Isoleucine", "Glutamine", 4),
    ("Leucine", "Glutamine", 1),
    ("Valine", "Glutamine", 5),
    ("Leucine", "Glutamine", 5),
    ("Methionine", "Tryptophan", 4),
    ("Leucine", "Tryptophan", 12),
    ("Valine", "Tryptophan", 9),
    ("Leucine", "Tryptophan", 11),
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

# Adjust positioning
amino_acids_pos = networkx.spring_layout(amino_acids, seed=42, k=3)

# Draw the graph
pyplot.figure(figsize=(10, 8))
networkx.draw_networkx_nodes(
    amino_acids, amino_acids_pos, node_size=1000, node_color=node_colors_amino_acids
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

pyplot.title("Stop Codon Preceding Amino Acid Connectivity")
pyplot.show()
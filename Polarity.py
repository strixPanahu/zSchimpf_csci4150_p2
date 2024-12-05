import networkx
from matplotlib import pyplot


G_connectivity = networkx.DiGraph()
connectivity_data = [
    ("Nonpolar", "Nonpolar", 541),
    ("Polar", "Nonpolar", 344),
    ("Nonpolar", "Polar", 290),
    ("Polar", "Polar", 180),
    ("Nonpolar", "Acid", 128),
    ("Acid", "Nonpolar", 110),
    ("Acid", "Polar", 80),
    ("Base", "Polar", 75),
    ("Nonpolar", "Base", 66),
    ("Polar", "Base", 61),
    ("Polar", "Acid", 40),
    ("Base", "Nonpolar", 30),
    ("Acid", "Acid", 29),
    ("Base", "Acid", 22)]

# Add edges with weights
for source, target, weight in connectivity_data:
    G_connectivity.add_edge(source, target, weight=weight)

# Extract edge weights
weights_connectivity = [d['weight'] for (_, _, d) in G_connectivity.edges(data=True)]

# Draw the graph
pyplot.figure(figsize=(10, 8))
amino_acids_pos = networkx.spring_layout(G_connectivity, seed=42)

# Draw nodes and edges
networkx.draw_networkx_nodes(G_connectivity, amino_acids_pos, node_size=1000, node_color="lightblue")
networkx.draw_networkx_edges(
    G_connectivity, amino_acids_pos, width=[w / 20 for w in weights_connectivity], alpha=0.7, edge_color="gray"
)

networkx.draw_networkx_labels(G_connectivity, amino_acids_pos, font_size=12, font_color="black")

# Add edge labels
edge_labels_connectivity = networkx.get_edge_attributes(G_connectivity, 'weight')
networkx.draw_networkx_edge_labels(G_connectivity, amino_acids_pos, edge_labels=edge_labels_connectivity, font_size=10)

pyplot.title("Amino Acid Polarity/Acidity Connectivity")

pyplot.show()
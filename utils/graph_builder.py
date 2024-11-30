import networkx as nx

def build_graph(entities, relationships):
    graph = nx.DiGraph()

    # Add nodes for entities
    for entity in entities:
        graph.add_node(entity['text'], label=entity['label'])

    # Add edges for relationships
    for rel in relationships:
        graph.add_edge(rel['source'], rel['target'], relation=rel['relation'])

    # Convert graph to D3.js-compatible format
    graph_data = {
        "nodes": [{"id": node, "group": graph.nodes[node]["label"]} for node in graph.nodes],
        "links": [{"source": u, "target": v, "value": data['relation']} for u, v, data in graph.edges(data=True)],
    }

    return graph_data

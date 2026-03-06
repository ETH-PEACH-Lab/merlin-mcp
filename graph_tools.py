from utils import to_merlin, ID, Edge, ValueType, ColorType

def define_graph(graph_name: str,
                 nodes: list[ID],
                 value: list[ValueType],
                 edges: list[Edge],
                 color: list[ColorType] | None = None,
                 arrow: list[ValueType] | None = None,
                 hidden: list[bool] | None = None,
                 above: str | None = None,
                 below: str | None = None,
                 left: str | None = None,
                 right: str | None = None
                 ) -> str:
    """
    Generates Merlin code to define a graph.

    :param graph_name: The name of the graph to define
    :param nodes: List of node identifiers (strings)
    :param value: List of values for each node (can be numbers, strings, or None)
    :param edges: List of tuples representing edges between nodes (source, target)
    :param color: Optional list of colors for each node
    :param arrow: Optional list of arrow styles for each node
    :param hidden: Optional list of booleans indicating which nodes are hidden
    :param above: Optional text to the above the graph
    :param below: Optional text to the below the graph
    :param left: Optional text to the left of the graph
    :param right: Optional text to the right of the graph
    """
    merlin_code = f"""graph {graph_name} = {{
  nodes: {to_merlin(nodes)}
  value: {to_merlin(value)}
  edges: {to_merlin(edges)}
"""
    
    if color is not None:
        merlin_code += f"  color: {to_merlin(color)}]\n"
    if arrow is not None:
        merlin_code += f"  arrow: {to_merlin(arrow)}\n"
    if hidden is not None:
        merlin_code += f"  hidden: {to_merlin(hidden)}\n"
    if above is not None:
        merlin_code += f"  above: {to_merlin(above)}\n"
    if below is not None:
        merlin_code += f"  above: {to_merlin(below)}\n"
    if left is not None:
        merlin_code += f"  above: {to_merlin(left)}\n"
    if right is not None:
        merlin_code += f"  above: {to_merlin(right)}\n"
    
    merlin_code += "}"
    return merlin_code

def graph_set_label(graph_name: str, text: str | None, position: str) -> str:
    """
    Generates Merlin code to set or remove label at a specific position.

    Text can be a string, the name of a Merlin text object or None. Use None to remove the label.
    Position must be one of "above", "below", "left" and "right".

    :param graph_name: The name of the graph to be updated.
    :param text: The text of the label.
    :param position: The position of the label.
    """
    return f"{graph_name}.setText({to_merlin(text)}, {to_merlin(position)})"

def graph_add_node(graph_name: str, name: ID, value: ValueType = None) -> str:
    """
    Generates Merlin code to add a node.

    :param graph_name: The name of the graph to be updated.
    :param name: The identifier of the node.
    :param value: The value of the node. Pass None for an empty value.
    """
    parameters = to_merlin(name)
    if value is not None:
        parameters += ", " + to_merlin(value)
    return f"{graph_name}.addNode({parameters})"

def graph_remove_node(graph_name: str, name: ID) -> str:
    """
    Generates Merlin code to remove a node.
    
    :param graph_name: The name of the graph to be updated.
    :param name: The identifier of the node.
    """
    return f"{graph_name}.removeNode({to_merlin(name)})"

def graph_set_value_for_node(graph_name: str, name: int | ID, value: ValueType) -> str:
    """
    Generates Merlin code to set the value of a node

    :param graph_name: The name of the graph to be updated.
    :param name: The indentifier of the node. Can be either an integer or its ID.
    :param value: The new value of the node. Pass None to remove its value.
    """
    return f"{graph_name}.setValue({to_merlin(name)}, {to_merlin(value)})"

def graph_set_color_for_node(graph_name: str, name: int | ID, color: ColorType) -> str:
    """
    Generates Merlin code to set the color of a node

    :param graph_name: The name of the graph to be updated.
    :param name: The indentifier of the node. Can be either an integer or its ID.
    :param value: The new color of the node. Pass None to clear its color.
    """
    return f"{graph_name}.setColor({to_merlin(name)}, {to_merlin(color)})"

def graph_set_arrow_for_node(graph_name: str, name: int | ID, arrow: ValueType) -> str:
    """
    Generates Merlin code to set the arrow of a node

    :param graph_name: The name of the graph to be updated.
    :param name: The indentifier of the node. Can be either an integer or its ID.
    :param value: The new arrow of the node. Pass None to remove its arrow.
    """
    return f"{graph_name}.setArrow({to_merlin(name)}, {to_merlin(arrow)})"

def graph_set_hidden_for_node(graph_name: str, name: int | ID, hidden: bool) -> str:
    """
    Generates Merlin code to set the visibility of a node

    :param graph_name: The name of the graph to be updated.
    :param name: The indentifier of the node. Can be either an integer or its ID.
    :param hidden: The new hidden status of the node.
    """
    return f"{graph_name}.setHidden({to_merlin(name)}, {to_merlin(hidden)})"

def graph_add_edge(graph_name: str, edge: Edge) -> str:
    """
    Generates Merlin code to add an edge.

    :param graph_name: The name of the graph to be updated.
    :param edge: The IDs of the two nodes to which to add an edge.
    """
    return f"{graph_name}.addEdge({to_merlin(edge)})"

def graph_remove_edge(graph_name: str, edge: Edge) -> str:
    """
    Generates Merlin code to remove an edge.

    :param graph_name: The name of the graph to be updated.
    :param edge: The IDs of the two nodes from which to remove an edge.
    """
    return f"{graph_name}.removeEdge({to_merlin(edge)})"

def graph_set_values(graph_name: str, values: list[ValueType]) -> str:
    """
    Generates Merlin code to set values for several node values.

    :param graph_name: The name of the graph to be updated.
    :param values: The new values of the elements.
    """
    return f"{graph_name}.setValues({to_merlin(values)})"

def graph_set_colors(graph_name: str, colors: list[str | None]) -> str:
    """
    Generates Merlin code to set colors for several nodes.

    :param graph_name: The name of the graph to be updated.
    :param colors: The new colors of the nodes.
    """
    return f"{graph_name}.setColors({to_merlin(colors)})"

def graph_set_arrows(graph_name: str, arrows: list[ValueType]) -> str:
    """
    Generates Merlin code to set arrows for several nodes.

    :param graph_name: The name of the graph to be updated.
    :param arrows: The new arrows of the nodes.
    """
    return f"{graph_name}.setArrows({to_merlin(arrows)})"

def graph_set_edges(graph_name: str, edges: list[Edge]) -> str:
    """
    Generates Merlin code to add multiple edges.

    :param graph_name: The name of the graph to be updated.
    :param edges: The list of edges to add.
    """
    return f"{graph_name}.setEdges({to_merlin(edges)})"

def graph_set_hidden(graph_name: str, hidden: list[bool]) -> str:
    """
    Generates Merlin code to set the visibility for several nodes.

    :param graph_name: The name of the graph to be updated.
    :param hidden: The new hidden status of the nodes.
    """
    return f"{graph_name}.setHidden({to_merlin(hidden)})"


if __name__ == "__main__":
    print(define_graph("GraphName", [ID(value = "1")], ["3"], [], ["blue"], ["arrow"], [True, False, False]))
    edge = Edge(source = ID(value = "4"), target = ID(value = "5"))
    print(graph_add_edge("GraphName", edge))
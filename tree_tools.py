from utils import to_merlin, ID, ValueType, ColorType

def define_tree(tree_name: str,
                nodes: list[ID],
                children: list[list[ID]] | None = None,
                value: list[ValueType] | None = None,
                color: list[ColorType] | None = None,
                arrow: list[ValueType] | None = None,
                above: str | None = None,
                below: str | None = None,
                left: str | None = None,
                right: str | None = None
                ) -> str:
    """
    Generates Merlin code to define a tree.

    :param tree_name: The variable name of the tree.
    :param nodes: A list of string IDs for the nodes.
    :param children: A list of tuples of IDs (parent, child).
    :param value: A list of values of the nodes.
    :param color: A list of colors of the nodes.
    :param arrow: A list of arrows for the nodes.
    :param above: Optional label above the array. Can be a string or the variable name of a Merlin text object.
    :param below: Optional label below the array. Can be a string or the variable name of a Merlin text object.
    :param left: Optional label to the left of the array. Can be a string or the variable name of a Merlin text object.
    :param right: Optional label to the right of the array. Can be a string or the variable name of a Merlin text object.
    """
    merlin_code = f"""tree {tree_name} = {{
  nodes: {to_merlin(nodes)}
"""
    
    if children is not None:
        merlin_code += f"  children: {to_merlin(children)}\n"
    if value is not None:
        merlin_code += f"  value: {to_merlin(value)}\n"
    if color is not None:
        merlin_code += f"  color: {to_merlin(color)}\n"
    if arrow is not None:
        merlin_code += f"  arrow: {to_merlin(arrow)}\n"
    if above is not None:
        merlin_code += f"  above: {to_merlin(above)}\n"
    if below is not None:
        merlin_code += f"  below: {to_merlin(below)}\n"
    if left is not None:
        merlin_code += f"  left: {to_merlin(left)}\n"
    if right is not None:
        merlin_code += f"  right: {to_merlin(right)}\n"
    
    merlin_code += "}"
    return merlin_code

def tree_set_label(tree_name: str, text: str | None, position: str) -> str:
    """
    Generates Merlin code to set or remove label at a specific position.

    Text can be a string, the name of a Merlin text object or None. Use None to remove the label.
    Position must be one of "above", "below", "left" and "right".

    :param tree_name: The name of the tree to be updated.
    :param text: The text of the label.
    :param position: The position of the label.
    """
    return f"{tree_name}.setText({to_merlin(text)}, {to_merlin(position)})"

def tree_add_node(tree_name: str, name: ID, value: ValueType = None) -> str:
    """
    Generates Merlin code to add a node.

    :param tree_name: The name of the tree to be updated.
    :param name: The identifier of the node.
    :param value: The value of the node. Pass None for an empty value.
    """
    return f"{tree_name}.addNode({to_merlin(name)}, {to_merlin(value)})"

def tree_remove_node(tree_name: str, name: ID) -> str:
    """
    Generates Merlin code to remove a node.

    :param tree_name: The name of the tree to be updated.
    :param name: The identifier of the node.
    """
    return f"{tree_name}.removeNode({to_merlin(name)})"

def tree_set_value_of_node(tree_name: str, name: int | ID, value: ValueType) -> str:
    """
    Generates Merlin code to set the value of a node

    :param tree_name: The name of the tree to be updated.
    :param name: The indentifier of the node. Can be either an integer or its ID.
    :param value: The new value of the node. Pass None to remove its value.
    """
    return f"{tree_name}.setValue({to_merlin(name)}, {to_merlin(value)})"

def tree_set_color_of_node(tree_name: str, name: int | ID, color: ColorType) -> str:
    """
    Generates Merlin code to set the color of a node

    :param tree_name: The name of the tree to be updated.
    :param name: The indentifier of the node. Can be either an integer or its ID.
    :param value: The new color of the node. Pass None to clear its color.
    """
    return f"{tree_name}.setColor({to_merlin(name)}, {to_merlin(color)})"

def tree_set_arrow_of_node(tree_name: str, name: int | ID, arrow: ValueType) -> str:
    """
    Generates Merlin code to set the arrow of a node

    :param tree_name: The name of the tree to be updated.
    :param name: The indentifier of the node. Can be either an integer or its ID.
    :param value: The new arrow of the node. Pass None to remove its arrow.
    """
    return f"{tree_name}.setColor({to_merlin(name)}, {to_merlin(arrow)})"

def tree_add_child(tree_name: str, edge: list[int | ID], value: ValueType = None) -> str:
    """
    Generates Merlin code to add a child to a parent.
    The parent's int or ID must exist. The child's int or ID is a new one.

    :param tree_name: The name of the tree to be updated.
    :param edge: The resulting edge. Must be a tuple (parent, child).
    :param value: Optional value of the new child.
    """
    return f"{tree_name}.addChild({to_merlin(edge)}, {to_merlin(value)})"

def tree_set_child(tree_name: str, edge: list[int | ID]) -> str:
    """
    Generates Merlin code to set a node as the child of another node.

    :param tree_name: The name of the tree to be updated.
    :param edge: The resulting edge. Must be a tuple (parent, child).
    """
    return f"{tree_name}.setChild({to_merlin(edge)})"

def tree_remove_subtree(tree_name: str, node: int | ID) -> str:
    """
    Generates Merlin code to remove a node and its subtree

    :param tree_name: The name of the tree to be updated.
    :param node: The int or ID of the node to be removed.
    """
    return f"{tree_name}.removeSubtree({to_merlin(node)})"

def tree_set_values(tree_name: str, values: list[ValueType]) -> str:
    """
    Generates Merlin code to set the values of multiple nodes.

    The update starts at node 0. Use the skip token "_" to leave specific 
    nodes unchanged.

    :param tree_name: The name of the tree to be updated.
    :param values: A list of new values.
    """
    return f"{tree_name}.setValues({to_merlin(values)})"

def tree_set_colors(tree_name: str, colors: list[ColorType]) -> str:
    """
    Generates Merlin code to set the colors of multiple nodes.

    The update starts at node 0. Use the skip token "_" to leave specific 
    nodes unchanged. Use None to clear a node's color.

    :param array_name: The name of the tree to be updated.
    :param colors: A list of colors (each hex #RRGGBB, HTML name, "_" or None).
    """
    return f"{tree_name}.setColors({to_merlin(colors)})"

def tree_set_arrows(tree_name: str, arrows: list[ValueType]) -> str:
    """
    Generates Merlin code to set the arrows of multiple nodes.

    The update starts at index 0. Use the skip token "_" to leave specific 
    ndoes unchanged. Use None to remove.

    :param array_name: The name of the tree to be updated.
    :param arrows: A list of labels for the arrows.
    """
    return f"{tree_name}.setArrows({to_merlin(arrows)})"
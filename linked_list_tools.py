from utils import to_merlin, ID, ValueType, ColorType

def define_linked_list(linked_list_name: str,
                       nodes: list[ID],
                       value: list[ValueType],
                       color: list[ColorType] | None = None,
                       arrow: list[ValueType] | None = None,
                       above: str | None = None,
                       below: str | None = None,
                       left: str | None = None,
                       right: str | None = None
                       ) -> str:
    """
    Generates Merlin code to define a linked list.

    :param linked_list_name: The name of the linked list to define
    :param nodes: List of node identifiers (strings)
    :param value: List of values for each node (can be numbers, strings, or None)
    :param color: Optional list of colors for each node
    :param arrow: Optional list of arrow styles for each node
    :param above: Optional text above the linked list
    :param below: Optional text below the linked list
    :param left: Optional text to the left of the linked list
    :param right: Optional text to the right of the linked list
    """
    merlin_code = f"""linkedlist {linked_list_name} = {{
  nodes: {to_merlin(nodes)}
  value: {to_merlin(value)}
"""
    
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

def linked_list_set_label(linked_list_name: str, text: str | None, position: str) -> str:
    """
    Generates Merlin code to set or remove label at a specific position.

    Text can be a string, the name of a Merlin text object or None. Use None to remove the label.
    Position must be one of "above", "below", "left" and "right".

    :param linked_list_name: The name of the linked list to be updated.
    :param text: The text of the label.
    :param position: The position of the label.
    """
    return f"{linked_list_name}.setText({to_merlin(text)}, {to_merlin(position)})"

def linked_list_add_node(linked_list_name: str, name: ID, value: ValueType = None) -> str:
    """
    Generates Merlin code to add a node at the end of the linked list.

    :param linked_list_name: The name of the linked list to be updated.
    :param name: The identifier of the node.
    :param value: The value to be added. Can be None.
    """
    return f"{linked_list_name}.addNode({name}, {to_merlin(value)})"

def linked_list_insert_node(linked_list_name: str, index: int | ID, name: ID, value: ValueType = None) -> str:
    """
    Generates Merlin code to add a node at a specific index or node's ID.

    :param linked_list_name: The variable name of the target stack in Merlin.
    :param index: The index of the node is to be inserted. Can be an integer or another node's ID.
    :param name: The ID of the node to be inserted.
    :param value: The value of the element to be added.
    """
    return f"{linked_list_name}.insertNode({to_merlin(index)}, {name}, {to_merlin(value)})"

def linked_list_remove_node(linked_list_name: str, name: ID) -> str:
    """
    Generates Merlin code to remove a node.

    :param linked_list_name: The variable name of the target stack in Merlin.
    :param name: The ID of the node to be removed.
    """
    return f"{linked_list_name}.removeNode({name})"

def linked_list_set_value_for_node(linked_list_name: str, name: int | ID, value: ValueType) -> str:
    """
    Generates Merlin code to set the value of a node

    :param linked_list_name: The name of the linked list to be updated.
    :param name: The identifier of the node. Can be either an integer or its ID.
    :param value: The new value of the node. Pass None to remove its value.
    """
    return f"{linked_list_name}.setValue({to_merlin(name)}, {to_merlin(value)})"

def linked_list_set_color_for_node(linked_list_name: str, name: int | ID, color: ColorType) -> str:
    """
    Generates Merlin code to set the color of a node

    :param linked_list_name: The name of the linked list to be updated.
    :param name: The identifier of the node. Can be either an integer or its ID.
    :param color: The new color of the node. Pass None to clear its color.
    """
    return f"{linked_list_name}.setColor({to_merlin(name)}, {to_merlin(color)})"

def linked_list_set_arrow_for_node(linked_list_name: str, name: int | ID, arrow: ValueType) -> str:
    """
    Generates Merlin code to set the arrow of a node

    :param linked_list_name: The name of the linked list to be updated.
    :param name: The identifier of the node. Can be either an integer or its ID.
    :param arrow: The new arrow of the node. Pass None to remove its arrow.
    """
    return f"{linked_list_name}.setArrow({to_merlin(name)}, {to_merlin(arrow)})"

def linked_list_add_value(linked_list_name: str, value: ValueType) -> str:
    """
    Generates Merlin code to add a node at the end of the linked list.

    :param linked_list_name: The name of the linked list to be updated.
    :param value: The value to be added.
    """
    return f"{linked_list_name}.addValue({to_merlin(value)})"

def linked_list_remove_value(linked_list_name: str, value: ValueType) -> str:
    """
    Generates Merlin code to remove the first occurrence of a value in a linked list.

    :param linked_list_name: The name of the linked list to be updated.
    :param value: The value to be removed.
    """
    return f"{linked_list_name}.removeValue({to_merlin(value)})"

def linked_list_remove_at_index(linked_list_name: str, index: int) -> str:
    """
    Generates Merlin code to remove the node at a specific index of a linked list.

    :param linked_list_name: The name of the linked list to be updated.
    :param index: The index of the node to be removed.
    """
    return f"{linked_list_name}.removeAt({index})"

def linked_list_set_values(linked_list_name: str, values: list[ValueType]) -> str:
    """
    Generates Merlin code to update a linked list prefix with new values.
    
    The update starts at index 0. Use the skip token "_" to leave specific 
    nodes unchanged.

    :param linked_list_name: The variable name of the linked list to be updated.
    :param values: A list of new values.
    """
    return f"{linked_list_name}.setValues({to_merlin(values)})"

def linked_list_set_colors(linked_list_name: str, colors: list[ColorType]) -> str:
    """
    Generates Merlin code to update the colors of a linked list prefix
    
    The update starts at index 0. Use the skip token "_" to leave specific 
    nodes unchanged. Use None to clear a node's color.

    :param linked_list_name: The variable name of the target linked list in Merlin.
    :param colors: A list of colors (each hex #RRGGBB, HTML name, "_" or None).
    """
    return f"{linked_list_name}.setColors({to_merlin(colors)})"

def linked_list_set_arrows(linked_list_name: str, arrows: list[ValueType]) -> str:
    """
    Generates Merlin code to update the arrows of a linked list prefix.
    
    The update starts at index 0. Use the skip token "_" to leave specific 
    nodes unchanged. Use None to remove.

    :param linked_list_name: The variable name of the target linked list in Merlin.
    :param arrows: A list of labels for the arrows.
    """
    return f"{linked_list_name}.setArrows({to_merlin(arrows)})"
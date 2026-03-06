from utils import to_merlin, ValueType, ColorType

def define_stack(stack_name: str,
                 values: list[ValueType],
                 color: list[ColorType] | None = None,
                 arrow: list[ValueType] | None = None,
                 above: str | None = None,
                 below: str | None = None,
                 left: str | None = None,
                 right: str | None = None
                 ) -> str:
    """
    Generates Merlin code to define a stack.

    :param stack_name: The variable name of the stack.
    :param values: A list of elements of the stack. Each element can be a number, string, or None.
    :param color: Optional list of colors for each element. Each color can be a hex code, HTML name, or None.
    :param arrow: Optional list of labels for the arrow of each element. Each label can be a number, string, or None.
    :param above: Optional label above the stack. Can be a string or the variable name of a Merlin text object.
    :param below: Optional label below the stack. Can be a string or the variable name of a Merlin text object.
    :param left: Optional label to the left of the stack. Can be a string or the variable name of a Merlin text object.
    :param right: Optional label to the right of the stack. Can be a string or the variable name of a Merlin text object.
    """
    merlin_code = f"""stack {stack_name} = {{
  value: {to_merlin(values)}
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

def stack_set_label(stack_name: str, text: str | None, position: str) -> str:
    """
    Generates Merlin code to set or remove label at a specific position.

    Text can be a string, the name of a Merlin text object or None. Use None to remove the label.
    Position must be one of "above", "below", "left" and "right".

    :param stack_name: The name of the stack to be updated.
    :param text: The text of the label.
    :param position: The position of the label.
    """
    return f"{stack_name}.setText({to_merlin(text)}, {to_merlin(position)})"

def stack_set_value(stack_name: str, index: int, value: ValueType) -> str:
    """
    Generates Merlin code to set the value of an element at a specific index.

    :param stack_name: The name of the stack to be updated.
    :param index: The index of the element to be updated.
    :param value: The new value of the element.
    """
    return f"{stack_name}.setValue({index}, {to_merlin(value)})"

def stack_set_color(stack_name: str, index: int, color: ColorType) -> str:
    """
    Generates Merlin code to update the color for a specific element.
    
    :param stack_name: The name of the stack to be updated.
    :param index: The index of the element to be recolored.
    :param color: The new color (hex #RRGGBB or HTML name). Pass None to clear the color.
    """
    return f"{stack_name}.setColor({index}, {to_merlin(color)})"

def stack_set_arrow(stack_name: str, index: int, arrow: ValueType) -> str:
    """
    Generates Merlin code to update the arrow for a specific element.

    :param stack_name: The variable name of the target stack.
    :param index: The index of the element to be updated.
    :param arrow: The label for the arrow (Number or String). Pass None to remove.
    """
    return f"{stack_name}.setArrow({index}, {to_merlin(arrow)})"

def stack_set_values(stack_name: str, values: list[ValueType]) -> str:
    """
    Generates Merlin code to update a stack prefix with new values.
    
    The update starts at index 0. Use the skip token "_" to leave specific 
    elements unchanged.

    :param stack_name: The variable name of the stack to be updated.
    :param values: A list of new values.
    """
    return f"{stack_name}.setValues({to_merlin(values)})"

def stack_set_colors(stack_name: str, colors: list[ColorType]) -> str:
    """
    Generates Merlin code to update the colors of a stack prefix
    
    The update starts at index 0. Use the skip token "_" to leave specific 
    elements unchanged. Use None to clear an element's color.

    :param stack_name: The variable name of the target stack in Merlin.
    :param colors: A list of colors (each hex #RRGGBB, HTML name, "_" or None).
    """
    return f"{stack_name}.setColors({to_merlin(colors)})"

def stack_set_arrows(stack_name: str, arrows: list[ValueType]) -> str:
    """
    Generates Merlin code to update the arrows of a stack prefix.
    
    The update starts at index 0. Use the skip token "_" to leave specific 
    elements unchanged. Use None to remove.

    :param stack_name: The variable name of the target stack in Merlin.
    :param arrows: A list of labels for the arrows.
    """
    return f"{stack_name}.setArrows({to_merlin(arrows)})"

def stack_add_value(stack_name: str, value: list[ValueType]) -> str:
    """
    Generates Merlin code to add an element on top of the stack.

    :param stack_name: The variable name of the target stack in Merlin.
    :param value: The value of the element to be added.
    """
    return f"{stack_name}.addValue({to_merlin(value)})"

def stack_insert_value(stack_name: str, index: int, value: ValueType) -> str:
    """
    Generates Merlin code to insert an element at a specific index.

    :param stack_name: The variable name of the target stack in Merlin.
    :param index: The index of the element to be inserted.
    :param value: The value of the element to be added.
    """
    return f"{stack_name}.insertValue({index}, {to_merlin(value)})"

def stack_remove_value(stack_name: str, value: ValueType) -> str:
    """
    Generates Merlin code to remove the first occurrence of a value in a stack.

    :param stack_name: The name of the stack to be updated.
    :param value: The value to be removed.
    """
    return f"{stack_name}.removeValue({to_merlin(value)})"

def stack_remove_at_index(stack_name: str, index: int) -> str:
    """
    Generates Merlin code to remove the element at a specific index of a stack.

    :param stack_name: The name of the stack to be updated.
    :param index: The index of the value to be removed.
    """
    return f"{stack_name}.removeAt({index})"
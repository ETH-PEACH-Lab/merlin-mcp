from utils import to_merlin, ValueType, ColorType

def define_array(array_name: str,
                 values: list[ValueType],
                 color: list[ColorType] | None = None,
                 arrow: list[ValueType] | None = None,
                 above: str | None = None,
                 below: str | None = None,
                 left: str | None = None,
                 right: str | None = None
                 ) -> str:
    """
    Generates Merlin code to define an array.

    Use None to get a null element.

    :param array_name: The variable name of the array.
    :param values: A list of elements of the array. Each element can be a number, string, or None.
    :param arrow: Optional list of labels for the arrow of each element. Each label can be a number, string, or None.
    :param above: Optional label above the array. Can be a string or the variable name of a Merlin text object.
    :param below: Optional label below the array. Can be a string or the variable name of a Merlin text object.
    :param left: Optional label to the left of the array. Can be a string or the variable name of a Merlin text object.
    :param right: Optional label to the right of the array. Can be a string or the variable name of a Merlin text object.
    """
    merlin_code = f"""array {array_name} = {{
  value: {to_merlin(values)}"""
    
    if color is not None:
        merlin_code += "\n  color: " + to_merlin(color)
    if arrow is not None:
        merlin_code += "\n  arrow: " + to_merlin(arrow)
    if above is not None:
        merlin_code += "\n  above: \"" + above + "\""
    if below is not None:
        merlin_code += "\n  below: \"" + below + "\""
    if left is not None:
        merlin_code += "\n  left: \"" + left + "\""
    if right is not None:
        merlin_code += "\n  right: \"" + right + "\""

    merlin_code += "\n}"
    return merlin_code

def array_set_label(array_name: str, text: str | None, position: str) -> str:
    """
    Generates Merlin code to set or remove label at a specific position.

    Text can be a string, the name of a Merlin text object or None. Use None to remove the label.
    Position must be one of "above", "below", "left" and "right".

    :param array_name: The name of the array to be updated.
    :param text: The text of the label.
    :param position: The position of the label.
    """
    return f"{array_name}.setText({to_merlin(text)}, {to_merlin(position)})"

def array_set_value_at_index(array_name: str, index: int, value: ValueType) -> str:
    """
    Generates Merlin code to update the value of the element at a specific index.
    
    :param array_name: The name of the array to be updated.
    :param index: The index of the element to be updated.
    :param value: The new value of the element.
    """
    return f"{array_name}.setValue({index}, {to_merlin(value)})"

def array_set_color_at_index(array_name: str, index: int, color: ColorType) -> str:
    """
    Generates Merlin code to update the color for a specific element.
    
    :param array_name: The name of the array to be updated.
    :param index: The index of the element to be recolored.
    :param color: The new color (hex #RRGGBB or HTML name). Pass None to clear the color.
    """
    return f"{array_name}.setColor({index}, {to_merlin(color)})"

def array_set_arrow_at_index(array_name: str, index: int, arrow: ValueType) -> str:
    """
    Generates Merlin code to update the arrow for a specific element.

    :param array_name: The variable name of the target array.
    :param index: The index of the element to be updated.
    :param arrow: The label for the arrow (Number or String). Pass None to remove.
    """
    return f"{array_name}.setArrow({index}, {to_merlin(arrow)})"

def array_set_values(array_name: str, values: list[ValueType]) -> str:
    """
    Generates Merlin code to update an array prefix with new values.
    
    The update starts at index 0. Use the skip token "_" to leave specific 
    elements unchanged.

    :param array_name: The variable name of the array to be updated.
    :param values: A list of new values.
    """
    return f"{array_name}.setValues({to_merlin(values)})"

def array_set_colors(array_name: str, colors: list[ColorType]) -> str:
    """
    Generates Merlin code to update the colors of an array prefix
    
    The update starts at index 0. Use the skip token "_" to leave specific 
    elements unchanged. Use None to clear an element's color.

    :param array_name: The variable name of the target array in Merlin.
    :param colors: A list of colors (each hex #RRGGBB, HTML name, "_" or None).
    """
    return f"{array_name}.setColors({to_merlin(colors)})"

def array_set_arrows(array_name: str, arrows: list[ValueType]) -> str:
    """
    Generates Merlin code to update the arrows of an array prefix.
    
    The update starts at index 0. Use the skip token "_" to leave specific 
    elements unchanged. Use None to remove.

    :param array_name: The variable name of the target array in Merlin.
    :param arrows: A list of labels for the arrows.
    """
    return f"{array_name}.setArrows({to_merlin(arrows)})"

def array_add_value(array_name: str, value: ValueType) -> str:
    """
    Generates Merlin code to add a value at the end of an array.

    :param array_name: The name of the array to be updated.
    :param value: The value to be added.
    """
    return f"{array_name}.addValue({to_merlin(value)})"

def array_insert_value(array_name: str, index: int, value: ValueType) -> str:
    """
    Generates Merlin code to insert a value at a specific index of an array.

    :param array_name: The name of the array to be updated.
    :param index: The index of the value to be inserted.
    :param value: The value to be added.
    """
    return f"{array_name}.insertValue({index}, {to_merlin(value)})"

def array_remove_value(array_name: str, value: ValueType) -> str:
    """
    Generates Merlin code to remove the first occurrence of a value in an array.

    :param array_name: The name of the array to be updated.
    :param value: The value to be removed.
    """
    return f"{array_name}.removeValue({to_merlin(value)})"

def array_remove_at_index(array_name: str, index: int) -> str:
    """
    Generates Merlin code to remove the element at a specific index of an array.

    :param array_name: The name of the array to be updated.
    :param index: The index of the value to be removed.
    """
    return f"{array_name}.removeAt({index})"
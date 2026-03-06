from utils import to_merlin, ValueType, ColorType

def define_matrix(matrix_name: str,
                  value: list[list[ValueType]],
                  color: list[list[ColorType]] | None = None,
                  arrow: list[list[ValueType]] | None = None,
                  above: str | None = None,
                  below: str | None = None,
                  left: str | None = None,
                  right: str | None = None
                  ) -> str:
    """
    Generates Merlin code to define a matrix.

    Use None to get a null element.

    :param matrix_name: The variable name of the matrix.
    :param value: A list of lists representing the rows of the matrix. Each element can be a number, string, or None.
    :param color: Optional matrix of colors (list of lists). Corresponds to the structure of values.
    :param arrow: Optional matrix of labels for the arrow of each element. Corresponds to the structure of values.
    :param above: Optional label above the matrix.
    :param below: Optional label below the matrix.
    :param left: Optional label to the left of the matrix.
    :param right: Optional label to the right of the matrix.
    """
    merlin_code = f"""matrix {matrix_name} = {{
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

def matrix_set_label(matrix_name: str, text: str | None, position: str) -> str:
    """
    Generates Merlin code to set or remove label at a specific position.

    Text can be a string, the name of a Merlin text object or None. Use None to remove the label.
    Position must be one of "above", "below", "left" and "right".

    :param array_name: The name of the matrix to be updated.
    :param text: The text of the label.
    :param position: The position of the label.
    """
    return f"{matrix_name}.setText({to_merlin(text)}, {to_merlin(position)})"

def matrix_set_value_at_index(matrix_name: str, row: int, column: int, value: ValueType) -> str:
    """
    Generates Merlin code to update the value of the element at a specific row and column.
    
    :param matrix_name: The name of the matrix to be updated.
    :param row: The row index of the element.
    :param col: The column index of the element.
    :param value: The new value of the element.
    """
    return f"{matrix_name}.setValue({row}, {column}, {to_merlin(value)})"

def matrix_set_color_at_index(matrix_name: str, row: int, column: int, color: ColorType) -> str:
    """
    Generates Merlin code to update the color for a specific element at a specific row and column.
    
    :param matrix_name: The name of the matrix to be updated.
    :param row: The row index of the element.
    :param col: The column index of the element.
    :param color: The new color (hex #RRGGBB or HTML name). Pass None to clear the color.
    """
    return f"{matrix_name}.setColor({row}, {column}, {to_merlin(color)})"

def matrix_set_arrow_at_index(matrix_name: str, row: int, column: int, arrow: ValueType) -> str:
    """
    Generates Merlin code to update the arrow for a specific element at a specific row and column.

    :param matrix_name: The variable name of the target matrix.
    :param row: The row index of the element.
    :param col: The column index of the element.
    :param arrow: The label for the arrow (Number or String). Pass None to remove.
    """
    return f"{matrix_name}.setArrow({row}, {column}, {to_merlin(arrow)})"

def matrix_set_values(matrix_name: str, values: list[list[ValueType]]) -> str:
    """
    Generates Merlin code to update a matrix sub-grid (prefix) with new values.
    
    The update starts at (0,0). Use the skip token "_" inside the rows to leave specific 
    elements unchanged.

    :param matrix_name: The variable name of the matrix to be updated.
    :param values: A list of lists (rows) containing new values.
    """
    return f"{matrix_name}.setValues({to_merlin(values)})"

def matrix_set_colors(matrix_name: str, colors: list[list[ColorType]]) -> str:
    """
    Generates Merlin code to update the colors of a matrix sub-grid (prefix).
    
    The update starts at (0,0). Use the skip token "_" inside the rows to leave specific 
    elements unchanged. Use None to clear an element's color.

    :param matrix_name: The variable name of the target matrix in Merlin.
    :param colors: A list of lists (rows) of colors (hex #RRGGBB, HTML name, "_" or None).
    """
    return f"{matrix_name}.setColors({to_merlin(colors)})"

def matrix_set_arrows(matrix_name: str, arrows: list[list[ValueType]]) -> str:
    """
    Generates Merlin code to update the arrows of a matrix sub-grid (prefix).
    
    The update starts at (0,0). Use the skip token "_" inside the rows to leave specific 
    elements unchanged. Use None to remove.

    :param matrix_name: The variable name of the target matrix in Merlin.
    :param arrows: A list of lists (rows) of labels for the arrows.
    """
    return f"{matrix_name}.setArrows({to_merlin(arrows)})"

def matrix_add_row(matrix_name: str, values: list[ValueType] | None) -> str:
    """
    Generates Merlin code to add a new row at the bottom of the matrix.

    The values can be a list or None. Use None to create a row with empty values.

    :param matrix_name: The name of the matrix to be updated.
    :param values: A list of values for the new row.
    """
    return f"{matrix_name}.addRow({to_merlin(values)})"

def matrix_add_column(matrix_name: str, values: list[ValueType] | None) -> str:
    """
    Generates Merlin code to add a new column at the right of the matrix.

    The values can be a list or None. Use None to create a column with empty values.

    :param matrix_name: The name of the matrix to be updated.
    :param values: A list of values for the new column.
    """
    return f"{matrix_name}.addColumn({to_merlin(values)})"

def matrix_insert_row(matrix_name: str, index: int, values: list[ValueType] | None) -> str:
    """
    Generates Merlin code to insert a new row at a specific index.

    The values can be a list or None. Use None to create a column with empty values.

    :param matrix_name: The name of the matrix to be updated.
    :param index: The row index where the new row should be inserted.
    :param values: A list of values for the new row.
    """
    return f"{matrix_name}.insertRow({index}, {to_merlin(values)})"

def matrix_insert_column(matrix_name: str, index: int, values: list[ValueType] | None) -> str:
    """
    Generates Merlin code to insert a new column at a specific index.

    The values can be a list or None. Use None to create a column with empty values.

    :param matrix_name: The name of the matrix to be updated.
    :param index: The column index where the new column should be inserted.
    :param values: A list of values for the new column.
    """
    return f"{matrix_name}.insertColumn({index}, {to_merlin(values)})"

def matrix_remove_row(matrix_name: str, index: int) -> str:
    """
    Generates Merlin code to remove a row at a specific index.

    :param matrix_name: The name of the matrix to be updated.
    :param index: The index of the row to be removed.
    """
    return f"{matrix_name}.removeRow({index})"

def matrix_remove_column(matrix_name: str, index: int) -> str:
    """
    Generates Merlin code to remove a column at a specific index.

    :param matrix_name: The name of the matrix to be updated.
    :param index: The index of the column to be removed.
    """
    return f"{matrix_name}.removeColumn({index})"

def matrix_add_border(matrix_name: str, value: ValueType, color: ColorType = None) -> str:
    """
    Generates Merlin code to add a border of elements around the matrix.

    :param matrix_name: The name of the matrix to be updated.
    :param value: The value of the elements of the border.
    :param color: The color of the border (hex #RRGGBB or HTML name). Pass None for no color.
    """
    parameters = to_merlin(value)
    if color is not None:
        parameters += ", " + to_merlin(color)
    return f"{matrix_name}.addBorder({parameters})"

if __name__ == "__main__":
    print(
        define_matrix(
            matrix_name = "matrix_name",
            value = [[1, 2, 3], [4, " ", 6]],
            color = [[None, None, "green"], [None, "#5f3759df", None]]
        )
    )
from utils import to_merlin, ColorType

def define_text(name: str,
                value: str | list[str],
                fontSize: int | float | list[int | float] | None = None,
                color: ColorType | list[ColorType] = None,
                fontWeight: str | list[str | None] | None = None,
                fontFamily: str | list[str | None] | None = None,
                align: str | list[str | None] | None = None,
                lineSpacing: int | float | None = None,
                width: int | float | None = None,
                height: int | float | None = None
                ):
    """
    Get the Merlin code for a text object.

    :param name: The variable name of the text.
    :type name: str
    :param value: The content of the text. It can be a string or, for multiline, a list of strings.
    :type value: str or list[str]
    :param fontSize: Optional font size of the text. It can be a number or, for multiline, a list of numbers.
    :type fontSize: int or float or list[int or float] or None
    :param color: Optional color of the text. It can be a string or, for multiline, a list of strings.
    :type color: str or list[str | None] or None
    :return: The Merlin code for the text object.
    :rtype: str
    """
    merlin_code = f"""text {name} = {{
  value: {to_merlin(value)}
"""
    
    if fontSize is not None:
        merlin_code += f"  fontSize: {to_merlin(fontSize)}\n"
    if color is not None:
        merlin_code += f"  color: {to_merlin(color)}\n"
    if fontWeight is not None:
        merlin_code += f"  fontWeight: {to_merlin(fontWeight)}\n"
    if fontFamily is not None:
        merlin_code += f"  fontWeight: {to_merlin(fontFamily)}\n"
    if align is not None:
        merlin_code += f"  align: {to_merlin(align)}\n"
    if lineSpacing is not None:
        merlin_code += f"  lineSpacing: {to_merlin(lineSpacing)}\n"
    if width is not None:
        merlin_code += f"  width: {to_merlin(width)}\n"
    if height is not None:
        merlin_code += f"  height: {to_merlin(height)}\n"
    
    merlin_code += "}"
    return merlin_code
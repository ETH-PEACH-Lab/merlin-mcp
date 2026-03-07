from utils import to_merlin

def define_text(name: str,
                value: str | list[str],
                fontSize: int | float | list[int | float] | None = None,
                color: str | list[str | None] | None = None,
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
        value: {to_merlin(value)}"""
    
    if fontSize is not None:
        merlin_code += "\n  fontSize: " + to_merlin(fontSize)
    if color is not None:
        merlin_code += "\n  color: " + to_merlin(color)
    
    merlin_code += "\n}"
    return merlin_code
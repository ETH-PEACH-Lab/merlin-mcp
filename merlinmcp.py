import inspect
from mcp.server.fastmcp import FastMCP
from utils import to_merlin

merlin_mcp = FastMCP("merlin")

import array_tools
for name, obj in inspect.getmembers(array_tools):
    # The following check prevents registering imported utils like 'to_merlin' or 'Number'
    if inspect.isfunction(obj) and obj.__module__ == array_tools.__name__:
        merlin_mcp.tool()(obj)

import matrix_tools
for name, obj in inspect.getmembers(matrix_tools):
    if inspect.isfunction(obj) and obj.__module__ == matrix_tools.__name__:
        merlin_mcp.tool()(obj)

import graph_tools
for name, obj in inspect.getmembers(graph_tools):
    if inspect.isfunction(obj) and obj.__module__ == graph_tools.__name__:
        merlin_mcp.tool()(obj)

import tree_tools
for name, obj in inspect.getmembers(tree_tools):
    if inspect.isfunction(obj) and obj.__module__ == tree_tools.__name__:
        merlin_mcp.tool()(obj)

import stack_tools
for name, obj in inspect.getmembers(stack_tools):
    if inspect.isfunction(obj) and obj.__module__ == stack_tools.__name__:
        merlin_mcp.tool()(obj)

import linked_list_tools
for name, obj in inspect.getmembers(linked_list_tools):
    if inspect.isfunction(obj) and obj.__module__ == linked_list_tools.__name__:
        merlin_mcp.tool()(obj)

@merlin_mcp.tool()
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
    :type fontSize: Number or list[Number] or None
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

@merlin_mcp.tool()
def create_page() -> str:
    return "page"

@merlin_mcp.tool()
def show_datastructure(name: str) -> str:
    return f"show {name}"

@merlin_mcp.tool()
def hide_datastructure(name: str) -> str:
    return f"hide {name}"

if __name__ == "__main__":
    merlin_mcp.run()
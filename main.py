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

import text_tools
for name, obj in inspect.getmembers(text_tools):
    if inspect.isfunction(obj) and obj.__module__ == text_tools.__name__:
        merlin_mcp.tool()(obj)

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
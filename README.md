# Merlin MCP Server

This is the Model Context Protocol (MCP) server designed to be interacted with LLMs to generate Merlin code.

## Installation

After pulling this repo in any folder of your choice, you first need to make sure that you have all the dependencies. The official python MCP library uses `uv`, so we will too. You can get here https://docs.astral.sh/uv/#installation.

Then you can install all dependencies with
```
uv pip install -r pyproject.toml
```

Technically you can now run the MCP server with `uv run main.py` but you probably want to use this with your favorite editor. Follow the next paragraph to learn how.

## Usage

Every code editor and LLM has its own usage usage and there are thousands of ways that you can install MCP servers, such as project-specific or system-wide. You can always check out the official guide of your preferred editor or LLM, but here we describe 3 possible scenarios:
- VS Code with the standard integrated Github Copilot
- VS Code with the Gemini Code Assist extension
- Cursor Editor

### VS Code (Standard)

We follow the simplest official way to [use and configure MCP servers](https://code.visualstudio.com/docs/copilot/customization/mcp-servers).

Open the command palette (`Ctrl/Cmd + Shift + P`) and select "MCP: Add Server...".
Then select "Command (stdio)" and input the command `uv run main.py`.

### VS Code (Gemini)

Download [Gemini Code Assist](https://marketplace.visualstudio.com/items?itemName=Google.geminicodeassist) from the extensions marketplace and follow its installation instructions. Gemini Code Assist defines its available MCP servers in `~/.gemini/settings.json`. Open or create it and, after replacing `FOLDER_PATH` with the filepath of the folder where you installed the server, copy-paste this:

```
{
  "mcpServers": {
    "merlin-mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "FOLDER_PATH",
        "run",
        "python",
        "main.py"
      ]
    }
  }
}
```

Restart VS Code, open the Gemini Code Assist Extension and toggle Agent Mode in the prompt panel.

### Cursor Editor

Cursor defines its MCP server under Settings > Cursor Settings > Tools & MCP.
Go there and click on "New MCP Server", which opens a .json file. With `FOLDER_PATH` replaced with the filepath of folder where you installed the server, copy-paste the same content as the one in VS Code (Gemini):

```
{
  "mcpServers": {
    "merlin-mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "FOLDER_PATH",
        "run",
        "python",
        "main.py"
      ]
    }
  }
}
```

A green dot should confirm the connection.

## Teaching the AI with Few-Shot Examples

In `merlin-mcp-examples.md` are examples that show the LMM how to use the Merlin MCP server's tools. It is recommended to give your LLM those examples, so it can learn from it for example how to write comments. As usual there are many way to do that, but here are the ones that work system-wide:

### VS Code (Standard)

Open the command palette (`Ctrl/Cmd + Shift + P`) and select "Chat: New Instructions File..." and then "User Data". Give the file a name (f.e. again `merlin-mcp-examples`). Copy-paste the contents of `merlin-mcp-examples.md` into the new file.

### VS Code (Gemini)

Run the command `cp merlin-mcp-examples.md ~/.gemini/GEMINI.md`.


### Cursor

Go to Settings > Cursor Settings > Rules, Skills, Subagents. Click in Rules on "+ New" and add a user rule. Copy-paste the contents of `merlin-mcp-examples.md` in there.
# Merlin MCP Server

This is the Model Context Protocol (short MCP) server designed to be interacted with LLMs to generate Merlin code.

## Getting Started (Terminal)

If you want to run or test the server directly from your terminal using uv, follow these steps:

Install Dependencies

Ensure you have the required packages installed in your environment:

```
uv add "mcp[cli]" httpx pydantic
```

Run the Server

You do not need to manually source the virtual environment if you use ```uv run```. It will automatically detect the .venv in your folder:

```
uv run merlinmcp.py
```

Note: The server uses stdio transport, so it will sit silently waiting for JSON-RPC input. To test if it is working, use the MCP Inspector:

```
npx @modelcontextprotocol/inspector uv run merlinmcp.py
```

## Editor Integration

Here are two ways to integrate this MCP with editors.

### Gemini Code Assist in VS Code

To use Merlin in VS Code with Gemini:

Open or create ```~/.gemini/settings.json```.

Add the following configuration (replace with your absolute paths):

```
{
  "mcpServers": {
    "merlin-mcp": {
      "command": "uv",
      "args": ["--directory", "/Users/YOUR_USER/Path/To/Merlin MCP", "run", "merlinmcp.py"],
      "env": { "PYTHONUNBUFFERED": "1" }
    }
  }
}
```

Restart VS Code and toggle Agent Mode in the Gemini panel.

### Cursor Editor

To add Merlin to Cursor:

Go to Settings > Models > MCP.

Click + Add New MCP Server.

Set Type to command and use:

```uv --directory "/Users/YOUR_USER/Path/To/Merlin MCP" run merlinmcp.py```

Look for the Green Dot to confirm the connection.

## Teaching the AI with Few-Shot Examples

To ensure the LLM uses the MCP tools correctly, you can provide context files.

### For Gemini Code Assist
Create a GEMINI.md file in your project root. Gemini reads this to understand your specific workflow.

### For Cursor
Create a .cursorrules file in your project root. Cursor automatically includes this in the "System Prompt" for the Agent.
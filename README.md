Merlin MCP Server
Merlin MCP is a Model Context Protocol (MCP) server designed to handle complex matrix definitions and data structure visualizations for LLMs.

Getting Started (Terminal)
If you want to run or test the server directly from your terminal using uv, follow these steps:

Install Dependencies Ensure you have the required packages installed in your environment:

Bash

uv add "mcp[cli]" httpx pydantic
Run the Server You do not need to manually source the virtual environment if you use uv run. It will automatically detect the .venv in your folder:

Bash

uv run merlinmcp.py
Note: The server uses stdio transport, so it will sit silently waiting for JSON-RPC input. To test if it is working, use the MCP Inspector:

Bash

npx @modelcontextprotocol/inspector uv run merlinmcp.py
Editor Integration
1. Gemini Code Assist (VS Code)
To use Merlin in VS Code with Gemini:

Open or create ~/.gemini/settings.json.

Add the following configuration (replace with your absolute paths):

JSON

{
  "mcpServers": {
    "merlin-mcp": {
      "command": "uv",
      "args": ["--directory", "/Users/YOUR_USER/Path/To/Merlin MCP", "run", "merlinmcp.py"],
      "env": { "PYTHONUNBUFFERED": "1" }
    }
  }
}
Restart VS Code and toggle Agent Mode in the Gemini panel.

2. Cursor
To use Merlin in Cursor:

Go to Settings > Models > MCP.

Click + Add New MCP Server.

Set Type to command and use:

Command: uv --directory "/Users/YOUR_USER/Path/To/Merlin MCP" run merlinmcp.py

Look for the Green Dot to confirm the connection.

Teaching the AI (Few-Shot Examples)
To ensure the LLM uses the matrix tools correctly and follows the "Post-Action" rule (calling show_datastructure), you must provide context files.

For Gemini Code Assist
Create a GEMINI.md file in your project root. Gemini reads this to understand your specific workflow.

For Cursor
Create a .cursorrules file in your project root. Cursor automatically includes this in the "System Prompt" for the Agent.

General Rules
No standard prints: All internal logging must go to sys.stderr to avoid corrupting the MCP JSON stream.

ValueType: The server supports int, float, str, and null within matrix cells.

Would you like me to help you add a "Troubleshooting" section to this README based on the ENOENT or connecting errors we solved earlier?
"""
fastmcp-server-starter: Main Application Entry Point

This file serves as the primary bootstrap script for initializing and running the
FastMCP server application. It is kept at the project root for easy execution
and separation from the core application logic located in the 'src/' directory.

Usage:
  1. Ensure the virtual environment is active (pipenv shell).
  2. Run the server using the fastmcp CLI wrapper:
     $ fastmcp run main.py:mcp
  3. Run the server using the fastmcp with http
     $ fastmcp run main.py:mcp --transport http --port 8000 
  
Dependencies:
  - Requires the 'fastmcp' library to be installed via Pipenv.
  - Depends on the 'mcp_server' instance defined within 'src/mcp_logic/tools.py'.

Note:
  This script handles environment setup and calls the mcp_server.run() method;
  all core business logic (Tools and Resources) resides in the 'src/' package.
"""
# --- Metadata ---
# Author: Arun Gopi
# License: MIT
# Date: 2025-10-03

from fastmcp import FastMCP

print('Fastmcp Server running..')

mcp = FastMCP("My MCP Server")

@mcp.tool
def greeting(name : str) -> str:
    return f'Hello {name}, Welcome!'

if __name__ == 'main':
    # mcp.run() # for stdio use
    mcp.run(transport='http', port=8000)
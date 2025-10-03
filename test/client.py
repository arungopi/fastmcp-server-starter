"""
client.py: Test entry point

This file serves as testing entry point for MCP server

Usage:
  1. Ensure the virtual environment is active (pipenv shell).
  2. Run the server using   
     $ python test/client.py
  
Dependencies:
  - Requires the 'fastmcp' library to be installed via Pipenv.
  - Depends on the 'mcp_server' instance defined within 'src/mcp_logic/tools.py'.

Note:
  This script handles environment setup and calls the mcp_server.run() method;
  all core business logic (Tools and Resources) resides in the 'src/' package.
"""

import asyncio
from fastmcp import Client

test_client = Client("http://localhost:8000/mcp")

async def call_greeting_tool(name : str):
    async with test_client:
        result = await test_client.call_tool("greeting", {"name": name})
        print(result)

asyncio.run(call_greeting_tool("Leo"))
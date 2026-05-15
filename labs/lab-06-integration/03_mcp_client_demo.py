"""
Lab 06 · step 3b — MCP client called from a watsonx agent.

Spawns the local MCP server from MCP_SERVER_CMD over stdio, lists its tools,
and invokes `get_account_status`. In production you would feed those tools
to an agent (LangChain, LangGraph, CrewAI) so the LLM decides when to call
them — MCP gives you that *without* writing custom integrations per tool.

Run:
    python 03_mcp_client_demo.py
"""
import asyncio
import os
from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

async def main():
    cmd_parts = os.environ["MCP_SERVER_CMD"].split()
    params = StdioServerParameters(command=cmd_parts[0], args=cmd_parts[1:])
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            print("Tools exposed by the MCP server:")
            for t in tools.tools:
                print(f"  - {t.name}: {t.description}")

            print("\nCalling get_account_status(account_id='882') ...")
            result = await session.call_tool(
                "get_account_status", {"account_id": "882"},
            )
            for item in result.content:
                print(item.text)

if __name__ == "__main__":
    asyncio.run(main())

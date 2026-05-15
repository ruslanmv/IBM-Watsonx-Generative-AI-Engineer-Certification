"""
Lab 06 · step 3a — Minimal Model Context Protocol (MCP) server.

Exposes ONE tool (`get_account_status`) over the stdio transport so any
MCP client — LangChain agent, IDE plugin, watsonx orchestrator — can call
it in a vendor-neutral way.

Run (it will block waiting for an MCP client to connect on stdin/stdout):
    python 03_mcp_server_demo.py
"""
import asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

ACCOUNTS = {
    "882": {"name": "ACME GmbH",  "tier": "enterprise", "status": "active"},
    "123": {"name": "Globex Ltd", "tier": "standard",   "status": "suspended"},
}

server = Server("acme-account-mcp")

@server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="get_account_status",
            description="Return name, tier and status for an account ID.",
            inputSchema={
                "type": "object",
                "properties": {"account_id": {"type": "string"}},
                "required": ["account_id"],
            },
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    if name != "get_account_status":
        raise ValueError(f"Unknown tool: {name}")
    aid = (arguments or {}).get("account_id", "")
    record = ACCOUNTS.get(aid, {"error": "account not found"})
    return [TextContent(type="text", text=str(record))]


async def main():
    async with stdio_server() as (read, write):
        await server.run(read, write, server.create_initialization_options())

if __name__ == "__main__":
    asyncio.run(main())

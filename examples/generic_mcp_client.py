"""A2A Retailmedia — reference MCP client (streamable-HTTP). Lists the tools, reads one banner card, runs the gate.
pip install mcp
"""
import asyncio
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

URL = "https://mcp.a2a-retailmedia.ai/mcp"
READ = ("get_banner_card", {"market": "FR", "banner": "carrefour"})
GATE = ("gate_transaction", {"market": "FR", "actor_class": "maker"})


async def main():
    async with streamablehttp_client(URL) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            print(len(tools.tools), "tools:", ", ".join(t.name for t in tools.tools))
            card = await session.call_tool(*READ)
            gate = await session.call_tool(*GATE)
            print(card.content[0].text[:400]); print(gate.content[0].text[:300])


if __name__ == "__main__":
    asyncio.run(main())

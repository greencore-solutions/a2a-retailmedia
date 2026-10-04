"""A2A Retailmedia on Azure Semantic Kernel — the stock MCPStreamableHttpPlugin, no adapter.
pip install semantic-kernel
"""
import asyncio
from semantic_kernel.connectors.mcp import MCPStreamableHttpPlugin

URL = "https://mcp.a2a-retailmedia.ai/mcp"
READ = ("get_banner_card", {"market": "FR", "banner": "carrefour"})
GATE = ("gate_transaction", {"market": "FR", "actor_class": "maker"})


async def main():
    plugin = MCPStreamableHttpPlugin(name="a2a_retailmedia", url=URL)
    await plugin.connect()
    try:
        print(len((await plugin.session.list_tools()).tools), "tools")
        print((await plugin.session.call_tool(*READ)).content[0].text[:400])
        print((await plugin.session.call_tool(*GATE)).content[0].text[:300])
    finally:
        await plugin.close()


if __name__ == "__main__":
    asyncio.run(main())

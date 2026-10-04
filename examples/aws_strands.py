"""A2A Retailmedia on AWS Strands — the stock MCPClient, no adapter.
pip install strands-agents mcp
"""
from mcp.client.streamable_http import streamablehttp_client
from strands.tools.mcp import MCPClient

URL = "https://mcp.a2a-retailmedia.ai/mcp"
READ = ("get_banner_card", {"market": "FR", "banner": "carrefour"})
GATE = ("gate_transaction", {"market": "FR", "actor_class": "maker"})

client = MCPClient(lambda: streamablehttp_client(URL))
with client:
    tools = client.list_tools_sync()
    print(len(tools), "tools")
    print(client.call_tool_sync(tool_use_id="rm-1", name=READ[0], arguments=READ[1]))
    print(client.call_tool_sync(tool_use_id="rm-2", name=GATE[0], arguments=GATE[1]))

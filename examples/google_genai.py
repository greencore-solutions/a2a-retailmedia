"""A2A Retailmedia with google-genai — the MCP ClientSession passed as a tool, no adapter. Set GEMINI_API_KEY to let the model call the door.
pip install google-genai mcp
"""
import asyncio, os
from google import genai
from google.genai import types
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

URL = "https://mcp.a2a-retailmedia.ai/mcp"


async def main():
    async with streamablehttp_client(URL) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print(len((await session.list_tools()).tools), "tools")
            if os.environ.get("GEMINI_API_KEY"):
                client = genai.Client()
                r = await client.aio.models.generate_content(model="gemini-2.5-flash", contents="Which grocery banners in the UK list a retail media program? Use the tools.",
                                                             config=types.GenerateContentConfig(tools=[session]))
                print(r.text)


if __name__ == "__main__":
    asyncio.run(main())

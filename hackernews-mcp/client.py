import asyncio
import json
from pathlib import Path
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main() -> None:
    server = StdioServerParameters(
        command=sys.executable,
        args=[str(Path(__file__).with_name("server.py").resolve())],
    )
    async with asyncio.timeout(20):
        async with stdio_client(server) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                tools = await session.list_tools()
                print("可用工具:", ", ".join(tool.name for tool in tools.tools))

                result = await session.call_tool("get_top_stories", {"limit": 3})
                if result.is_error:
                    raise RuntimeError(f"工具调用失败: {result.content}")
                print("\n前 3 条模拟新闻:")
                for item in result.content:
                    if item.type == "text":
                        print(json.dumps(json.loads(item.text), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    asyncio.run(main())

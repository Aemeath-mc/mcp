# hackernews-mcp

Hacker News MCP stdio demo using 10 fixed mock stories. No network access or API key required. Requires MCP Python SDK 2.3.x or later within the 2.x series.

## Tools

| Tool | Description | Arguments |
|------|-------------|-----------|
| `get_top_stories` | Fixed mock HN stories | `limit` (int, default 10; clamped to 1–10) |

## Install

```bash
python -m pip install -r requirements.txt
```

## Run

Run the complete demo, which starts the server, initializes an MCP session, lists tools, and requests three mock stories:

```bash
python client.py
```

To start only the server, run `python server.py`. A stdio server waits for MCP messages on standard input; it does not print the stories by itself. Use `client.py` or an MCP-compatible application to communicate with it. Keep server logs on standard error so they do not interfere with protocol messages.

## Config

```json
{
  "mcpServers": {
    "hackernews": {
      "command": "python",
      "args": ["/absolute/path/to/mcp/server.py"]
    }
  }
}
```

## Keywords

「帮我看一下 Hacker News 现在的热门」
「用 MCP 拉一下 HN top stories」
「获取 Hacker News 前 10 条」
「调用 get_top_stories」
「用 hackernews 这个 MCP 查一下」

## License

MIT

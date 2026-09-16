import os

from aurelius.server import mcp


if __name__ == "__main__":
    mcp.settings.host = "0.0.0.0"
    mcp.settings.port = int(os.environ.get("PORT", "8000"))

    mcp.run(
        transport="streamable-http",
    )

import os

from aurelius.server import mcp
from mcp.server.transport_security import TransportSecuritySettings


if __name__ == "__main__":
    mcp.settings.host = "0.0.0.0"
    mcp.settings.port = int(os.environ.get("PORT", "8000"))

    mcp.settings.transport_security = TransportSecuritySettings(
        enable_dns_rebinding_protection=True,
        allowed_hosts=[
            "aurelius-remote.onrender.com",
            "aurelius-remote.onrender.com:*",
        ],
        allowed_origins=[
            "https://aurelius-remote.onrender.com",
            "https://aurelius-remote.onrender.com:*",
        ],
    )

    mcp.run(
        transport="streamable-http",
    )

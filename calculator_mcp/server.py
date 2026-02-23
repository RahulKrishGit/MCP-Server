import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()

# Initialize FastMCP server
mcp = FastMCP("calculator", host="0.0.0.0", port=8050)


@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract two numbers."""
    return a - b


@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    # Get the transport method from the environment or default to stdio
    transport = os.environ.get("transport", "stdio").lower()

    if transport == "sse":
        print("Starting SSE server on 0.0.0.0:8050...")
        # For SSE, start the server on the specified host and port
        mcp.run(transport="sse")
    else:
        # For stdio, it runs normally via standard input/output
        mcp.run(transport="stdio")

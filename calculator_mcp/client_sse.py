import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client


async def main():
    print("Initializing SSE client...")
    url = "http://127.0.0.1:8050/sse"

    try:
        async with sse_client(url) as (read, write):
            async with ClientSession(read, write) as session:
                # Initialize connection
                await session.initialize()
                print("Connected to server.")

                # List tools
                tools_response = await session.list_tools()
                print("\nAvailable tools:")
                for tool in tools_response.tools:
                    print(f"- {tool.name}: {tool.description}")

                # Execute examples
                print("\nExecuting examples:")

                # Add
                result_add = await session.call_tool("add", arguments={"a": 15, "b": 5})
                print(f"add(15, 5) = {result_add.content[0].text}")

                # Subtract
                result_sub = await session.call_tool(
                    "subtract", arguments={"a": 30, "b": 10}
                )
                print(f"subtract(30, 10) = {result_sub.content[0].text}")

                # Multiply
                result_mul = await session.call_tool(
                    "multiply", arguments={"a": 8, "b": 9}
                )
                print(f"multiply(8, 9) = {result_mul.content[0].text}")

                # Divide
                result_div = await session.call_tool(
                    "divide", arguments={"a": 50, "b": 2}
                )
                print(f"divide(50, 2) = {result_div.content[0].text}")
    except Exception as e:
        print(f"Failed to connect or execute: {e}")


if __name__ == "__main__":
    asyncio.run(main())

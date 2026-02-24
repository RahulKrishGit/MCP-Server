import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    print("Initializing stdio client...")
    import sys
    import os

    env = os.environ.copy()
    env["transport"] = "stdio"

    server_params = StdioServerParameters(
        command=sys.executable, args=["server.py"], env=env
    )

    async with stdio_client(server_params) as (read, write):
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
            result_add = await session.call_tool("add", arguments={"a": 5, "b": 3})
            print(f"add(5, 3) = {result_add.content[0].text}")

            # Subtract
            result_sub = await session.call_tool(
                "subtract", arguments={"a": 10, "b": 4}
            )
            print(f"subtract(10, 4) = {result_sub.content[0].text}")

            # Multiply
            result_mul = await session.call_tool("multiply", arguments={"a": 6, "b": 7})
            print(f"multiply(6, 7) = {result_mul.content[0].text}")

            # Divide
            result_div = await session.call_tool("divide", arguments={"a": 20, "b": 4})
            print(f"divide(20, 4) = {result_div.content[0].text}")


if __name__ == "__main__":
    asyncio.run(main())

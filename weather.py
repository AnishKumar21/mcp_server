from mcp.server.fastmcp import FastMCP 

mcp = FastMCP("weather")

@mcp.tool()
async def get_weather(location:str)->str:
    """
    

    Args:
        location (str): _description_

    Returns:
        str: _description_
    """
    return "weather in bangalore is rainy"


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
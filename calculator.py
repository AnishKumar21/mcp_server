from mcp.server.fastmcp import FastMCP


mcp = FastMCP("math")

@mcp.tool() #this tool will be exposed to the mcp server 
def add(a:int, b:int)->int:
    """_summary_

    Args:
        a (int): _description_
        b (int): _description_

    Returns:
        int: _description_
    """
    return a+b

@mcp.tool()
def multiply(a:int, b:int)->int:
    """_summary_

    Args:
        a (int): _description_
        b (int): _description_

    Returns:
        int: _description_
    """
    return a*b



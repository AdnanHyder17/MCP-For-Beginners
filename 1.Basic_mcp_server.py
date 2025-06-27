from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("Weather Service")

# Tool implementation
@mcp.tool()
def get_weather(location: str) -> str:
    """Get the current weather for the specified location."""
    return f"Weather for the {location}: Cloudy, 20°C"

# Resource implementation
@mcp.resource("weather://{location}")
def weather_resource(location: str) -> str:
    """Provide weather data as a resource."""
    return f"Weather data for the {location}: Cloudy, 20°C"

# Prompt implementation
@mcp.prompt()
def weather_report(location: str) -> str:
    """Create a weather report prompt"""
    return f"You are a weather reporter. Weather report for {location}?"


# Run the server
if __name__ == "__main__":
    mcp.run()
    
# Note: Enter this command in terminal to run: mcp dev Basic_mcp_server.py
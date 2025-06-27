"""
With this setup, your letter counter function is now accessible through:
1. A traditional Gradio web interface for human interaction
2. An MCP Server that can be connected to compatible clients


How it Works Behind the Scences

When you set mcp_server=True in launch(), several things happen:

Gradio functions are automatically converted to MCP Tools
Input components map to tool argument schemas
Output components determine the response format
The Gradio server now also listens for MCP protocol messages
JSON-RPC over HTTP+SSE is set up for client-server communication


Key Feature 

Tool Conversion: 
Each API endpoint in your Gradio app is automatically converted into an MCP tool with a corresponding name, 
description, and input schema. To view the tools and schemas, visit http://your-server:port/gradio_api/mcp/schema 
or go to the “View API” link in the footer of your Gradio app, and then click on “MCP”.


Troubleshooting Tips

Type Hints and Docstrings: Ensure you provide type hints and valid docstrings for your functions. The docstring should include an “Args:” block with indented parameter names.
String Inputs: When in doubt, accept input arguments as str and convert them to the desired type inside the function.
Restart: If you encounter connection issues, try restarting both your MCP Client and MCP Server.
"""

import gradio as gr

def letter_counter(word: str, letter: str) -> int:
    """
    Count the number of occurrences of a letter in a word or text.

    Args:
        word (str): The input text to search through
        letter (str): The letter to search for

    Returns:
        int: The number of times the letter appears in the text
    """
    word = word.lower()
    letter = letter.lower()
    count = word.count(letter)
    return count

# Create a standard Gradio interface
demo = gr.Interface(
    fn=letter_counter,
    inputs=["textbox", "textbox"],
    outputs="number",
    title="Letter Counter",
    description="Enter text and a letter to count how many times the letter appears in the text."
)

# Launch both the Gradio web interface and the MCP server
if __name__ == "__main__":
    demo.launch(mcp_server=True)
"""
Gradio provides a straightforward way to create MCP servers by automatically converting your Python functions into MCP tools. 
When you set mcp_server=True in launch(), Gradio:

Automatically converts your functions into MCP Tools
Maps input components to tool argument schemas
Determines response formats from output components
Sets up JSON-RPC over HTTP+SSE for client-server communication
Creates both a web interface and an MCP server endpoint


Troubleshooting Tips

1) Type Hints and Docstrings:

Always provide type hints for your function parameters and return values
Include a docstring with an “Args:” block for each parameter
This helps Gradio generate accurate MCP tool schemas

2) String Inputs:

When in doubt, accept input arguments as str
Convert them to the desired type inside the function
This provides better compatibility with MCP clients

3) SSE Support:

Some MCP clients don’t support SSE-based MCP Servers, In those cases, use mcp-remote.

4) Connection Issues:

If you encounter connection problems, try restarting both the client and server
Check that the server is running and accessible
Verify that the MCP schema is available at the expected URL

"""

import json
import gradio as gr
from textblob import TextBlob 

def sentiment_analysis(text: str) -> str:
    """
    Analyze the sentiment of the given text
    
    Args:
        text (str): The text to analyze
    
    Returns:
        str: A JSON string containing polarity, subjectivity, and assessment
    """
    
    blob = TextBlob(text) # Uses TextBlob to analyze the sentiment
    sentiment = blob.sentiment
    
    # Return a dictionary
    result = {
        "polarity": round(sentiment.polarity, 2),  # -1 (negative) to 1 (positive)
        "subjectivity": round(sentiment.subjectivity, 2),  # 0 (objective) to 1 (subjective)
        "assessment": "positive" if sentiment.polarity > 0 else "negative" if sentiment.polarity < 0 else "neutral"
    }
    
    return json.dumps(result)


# gr.Interface creates both the web UI and MCP server
demo = gr.Interface(
    fn = sentiment_analysis,
    inputs = gr.Textbox(placeholder="Enter text to analyze..."),
    outputs = gr.Textbox(), # Changed from gr.JSON() to gr.Textbox()
    title = "Text Sentiment Analysis",
    description="Analyze the sentiment of text using TextBlob"
)

# Launch the interface and MCP server
if __name__ == "__main__":
    demo.launch(mcp_server=True) 
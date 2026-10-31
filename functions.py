
import anthropic
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    raise ValueError("ANTHROPIC_API_KEY is missing from .env")

client = anthropic.Anthropic(api_key=api_key)

# Simulated inventory database
inventory = {
    "maize flour": 120,
    "wheat flour": 85,
    "rice": 200,
    "sugar": 0,
    "cooking oil": 45
}

# Simulated product prices
prices = {
    "maize flour": 2800,
    "wheat flour": 3200,
    "rice": 4500,
    
}


# Tool 1: Check stock levels
def get_stock_level(product_name):
    product = product_name.lower()

    if product in inventory:
        qty = inventory[product]

        if qty == 0:
            return f"{product_name} is currently out of stock."

        return f"{product_name}: {qty} bags in stock."

    return f"Product '{product_name}' not found in the system."


# Tool 2: Check product prices
def get_price(product_name):
    p = product_name.lower()

    if p in prices:
        return f"{product_name}: KES {prices[p]:,} per bag"

    return f"Price not found for '{product_name}'"


# Define both AI tools
tools = [
    {
        "name": "get_stock_level",
        "description": "Get the current stock quantity for a product at Kamau Stores.",
        "input_schema": {
            "type": "object",
            "properties": {
                "product_name": {
                    "type": "string",
                    "description": "The name of the product to check."
                }
            },
            "required": ["product_name"]
        }
    },
    {
        "name": "get_price",
        "description": "Get the current selling price per bag of a product at Kamau Stores.",
        "input_schema": {
            "type": "object",
            "properties": {
                "product_name": {
                    "type": "string",
                    "description": "The name of the product to check."
                }
            },
            "required": ["product_name"]
        }
    }
]


# User inquiry
user_question = "How much does a bag of rice cost and how many do we have?"


# Send request to Claude
response = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=512,
    tools=tools,
    system=(
        "You are an inventory assistant for Kamau Stores. "
        "Use get_price for price questions and get_stock_level "
        "for stock questions. If a question asks for both price "
        "and stock, call both tools."
    ),
    messages=[
        {
            "role": "user",
            "content": user_question
        }
    ]
)


# Process all requested tool calls
if response.stop_reason == "tool_use":

    for tool_use in response.content:

        if tool_use.type == "tool_use":

            fn_name = tool_use.name
            fn_input = tool_use.input

            # Execute the appropriate function
            if fn_name == "get_stock_level":
                result = get_stock_level(
                    fn_input["product_name"]
                )

            elif fn_name == "get_price":
                result = get_price(
                    fn_input["product_name"]
                )

            else:
                result = f"Unknown tool: {fn_name}"

            # Display the function call and result
            print(f"Function called: {fn_name}({fn_input})")
            print(f"Result: {result}")

else:
    for block in response.content:
        if block.type == "text":
            print(block.text)

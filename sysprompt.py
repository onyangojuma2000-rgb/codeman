import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)
system_prompt = """Extract the order details from the customer message.
Return ONLY valid JSON in this format:
{"product": "...", "quantity": ..., "urgency": "normal" or "urgent"}
No explanation. No markdown. Just the JSON."""

message = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=512,
    system=system_prompt,
    messages=[{"role": "user", "content": "I need 30 bags of rice urgently for tomorrow's event"}]
)
print(message.content[0].text)
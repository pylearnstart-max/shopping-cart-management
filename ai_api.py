from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.responses.create(
    model="gpt-5.4-mini",
    input="Explain shopping cart in one simple sentence."
)

print(response.output_text)
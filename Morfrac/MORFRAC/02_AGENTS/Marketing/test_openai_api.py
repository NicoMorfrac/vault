from openai import OpenAI

print("Starting API test...")

client = OpenAI()

print("Client created. Sending request...")

response = client.responses.create(
    model="gpt-5.4-mini",
    input="Reply with one short sentence confirming the MORFRAC marketing API layer is working.",
)

print("Response received:")
print(response.output_text)
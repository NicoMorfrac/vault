import subprocess

MODEL = "qwen2.5:7b"

prompt = """
You are MORFRAC's marketing analyst.
Reply with one short sentence confirming you can analyze marketing reports.
"""

result = subprocess.run(
    ["ollama", "run", MODEL],
    input=prompt,
    text=True,
    capture_output=True,
    encoding="utf-8"
)

print(result.stdout)

if result.stderr.strip():
    print("ERROR:")
    print(result.stderr)
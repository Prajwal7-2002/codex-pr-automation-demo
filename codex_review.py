import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

with open("diff.txt") as f:
    diff = f.read()

prompt = f"""
You are acting as a pull request review assistant.

Tasks:
- Generate a PR title
- Generate a concise PR description
- Identify missing tests
- Provide non-blocking review comments

Rules:
- Use only the provided diff
- Do not assume missing context
- If unsure, say so explicitly and be precise

Diff:
{diff}
"""

response = client.responses.create(
    model="gpt-4.1",
    input=prompt
)

with open("review.txt", "w") as f:
    f.write(response.output_text)

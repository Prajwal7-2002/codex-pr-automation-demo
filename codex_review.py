import os
from groq import Groq

client = Groq(api_key=os.environ["GROQ_API_KEY"])

with open("diff.txt", "r", encoding="utf-8") as f:
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

response = client.chat.completions.create(
    model="meta-llama/llama-4-maverick-17b-128e-instruct",
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=0.2,
)

review_text = response.choices[0].message.content

with open("review.txt", "w", encoding="utf-8") as f:
    f.write(review_text)

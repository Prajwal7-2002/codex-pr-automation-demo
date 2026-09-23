# AI Pull Request Review Assistant

An automated GitHub pull-request review tool that uses a LLaMA model through Groq to turn code changes into useful, non-blocking engineering feedback.

The project is designed to help teams review pull requests faster while keeping developers in control of the final decision. It reads the pull-request diff, generates a concise review, identifies missing tests, and publishes the result directly to the pull request through GitHub Actions.

## Why this project exists

Code review is essential, but repetitive review work can slow teams down:

- Pull requests may wait for an initial review.
- Small changes still require context switching.
- Test gaps can be easy to overlook.
- Review quality can vary depending on reviewer availability.

This project adds an AI-powered first pass to the development workflow. It does not replace human reviewers or approve changes automatically. Instead, it provides fast, consistent suggestions that help engineers focus their attention where it matters most.

## What it does

When a pull request is opened or updated, the workflow:

1. Checks out the repository.
2. Generates the pull-request diff.
3. Sends the diff to a LLaMA model hosted through Groq.
4. Produces:
   - a suggested pull-request title
   - a concise change summary
   - potential missing tests
   - non-blocking review comments
5. Publishes the generated review as a pull-request comment.

The model is instructed to use only the supplied diff and to state when context is uncertain. This keeps the output focused and reduces unsupported assumptions.

## How it works

### Local review generation

[codex_review.py](./codex_review.py) is the review-generation script. It:

- reads `GROQ_API_KEY` from the environment
- loads the pull-request diff from `diff.txt`
- sends a structured prompt to the Groq chat-completions API
- writes the model response to `review.txt`

Run it locally with:

```bash
set GROQ_API_KEY=your_key_here
python codex_review.py
```

The script expects `diff.txt` to exist in the repository root.

### GitHub Actions automation

[.github/workflows/codex-review.yml](./.github/workflows/codex-review.yml) automates the complete process for pull requests:

- triggers on `opened` and `synchronize` events
- uses Python 3.11
- installs the required review dependencies
- extracts the diff with Git
- runs the review assistant
- posts `review.txt` to the pull request using the GitHub API

The workflow uses:

- `GROQ_API_KEY` for model access
- `GITHUB_TOKEN` for posting the review comment

## Project structure

```text
.
├── .github/
│   └── workflows/
│       └── codex-review.yml    # GitHub Actions automation
├── app/
│   └── utils.py                # reusable utility functions
├── tests/
│   └── test_utils.py           # unit tests
├── codex_review.py             # LLaMA/Groq review assistant
├── requirements.txt             # Python dependencies
├── .gitignore
└── README.md
```

## Quick start

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure the API key

Set the Groq API key in your shell:

**Windows PowerShell**

```powershell
$env:GROQ_API_KEY = "your_key_here"
```

**macOS/Linux**

```bash
export GROQ_API_KEY="your_key_here"
```

### Generate a review locally

Create a `diff.txt` file containing the pull-request diff, then run:

```bash
python codex_review.py
```

The generated review is saved to `review.txt`.

### Run tests

```bash
pytest
```

## GitHub setup

To enable the automated workflow:

1. Add `GROQ_API_KEY` as a repository secret.
2. Ensure GitHub Actions are enabled.
3. Open or update a pull request.
4. Review the generated comment alongside the human review.

The workflow requires pull-request write permission so it can publish the generated feedback.

## Engineering highlights

- **LLM integration:** Connects a real development workflow to a hosted LLaMA model through Groq.
- **CI/CD automation:** Runs automatically as part of the pull-request lifecycle.
- **Human-in-the-loop design:** Produces suggestions without blocking merges or replacing engineering judgment.
- **Diff-scoped analysis:** Directs the model to review only the provided code changes.
- **Actionable output:** Combines summaries, test recommendations, and review comments in one place.
- **Secure configuration:** Keeps API credentials in environment variables and GitHub Secrets rather than source code.
- **Simple integration surface:** Uses standard Python, GitHub Actions, and GitHub's API.

## Why it is valuable for recruiters

This project demonstrates more than a basic API call. It shows the ability to:

- identify a real software-development bottleneck
- integrate an LLM into an existing engineering process
- design an automated CI workflow
- work with Git diffs and pull-request events
- manage secrets through environment configuration
- produce developer-focused, actionable output
- preserve human oversight in an AI-assisted system

It is a practical example of applied AI engineering: the model is connected to a useful workflow, constrained by a clear prompt, and delivered through a familiar tool developers already use.

## Limitations and future improvements

The current implementation is intentionally lightweight. Potential next steps include:

- adding structured JSON output for easier parsing
- posting inline review comments against specific changed lines
- adding configurable review categories
- limiting diff size and handling very large pull requests
- adding retry and error-reporting behavior for API failures
- supporting multiple model providers
- adding tests for prompt construction and API response handling

## License

This project is intended as a demonstration of AI-assisted developer tooling.

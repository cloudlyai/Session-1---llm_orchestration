# Session 2: LLM Orchestration

Part of the **AI Engineering Course** - a hands-on video course for software engineers transitioning into AI engineering. This session covers the fundamentals of making calls to LLMs and chaining multiple providers together.

## What This Session Covers

- Chat completions API structure (messages array, roles: system / user / assistant)
- Calling three different LLM providers: OpenAI, Anthropic, and Google Gemini
- Multi-LLM chaining - the output of one model is passed as context to the next
- The difference between using native provider SDKs vs a unified abstraction layer (LiteLLM)
- Environment variable management with `.env` and `python-dotenv`

## The Demo: Multi-LLM Puzzle Chain

Both programs implement the same orchestration flow across three providers:
```
OpenAI (gpt-4o-mini)       ->  generates a puzzle
Anthropic (claude-3-haiku)  ->  receives the puzzle, generates a hint
Google (gemini-2.0-flash)   ->  receives puzzle + hint, generates the solution
```

Each model's response is appended to the shared message history using `role: assistant` before being passed to the next model. This is the core pattern of multi-LLM chaining.

## Programs

### `llm_orchestration_standard.py`

Uses each provider's native SDK directly:

- `openai.OpenAI` for GPT
- `anthropic.Anthropic` for Claude
- `openai.OpenAI` with a custom `base_url` for Gemini (OpenAI-compatible endpoint)

Good for seeing how each provider structures its SDK and response objects - they are similar but not identical.

### `llm_orchestration_litellm.py`

The same orchestration, but using [LiteLLM](https://github.com/BerriAI/litellm) as a unified interface. A single `completion()` call works across all three providers - only the `model` string changes.

This shows what provider abstraction looks like in practice: you can swap models without touching your integration code.

## Setup

**Prerequisites:** Python 3.9+

1. Clone the repo:
```bash
   git clone https://github.com/cloudlyai/Session-1---llm_orchestration.git
   cd Session-1---llm_orchestration
```

2. Create and activate a virtual environment:
```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
```

3. Install dependencies:
```bash
   pip install openai anthropic litellm python-dotenv
```

4. Create a `.env` file in the project root with your API keys:
```
   OPENAI_API_KEY=your_openai_key
   ANTHROPIC_API_KEY=your_anthropic_key
   GEMINI_API_KEY=your_gemini_key
```

## Running
```bash
# Standard SDK approach
python llm_orchestration_standard.py

# LiteLLM unified approach
python llm_orchestration_litellm.py
```

## Tech Stack

| Component | Detail |
|-----------|--------|
| Language | Python |
| LLM Providers | OpenAI, Anthropic, Google Gemini |
| Models | gpt-4o-mini, claude-3-haiku-20240307, gemini-2.0-flash |
| Libraries | openai, anthropic, litellm, python-dotenv |

## Course Context

This is **Session 2** of the AI Engineering Course. The full course arc(tbc):

| Session | Topic |
|---------|-------|
| Session 1 | Introduction |
| **Session 2** | **Making calls to LLMs - multi-provider orchestration** <- you are here |
| Session 4 | Reliability - retries, timeouts, cost tracking |
| Session 6 | Streamlit Chat UI |

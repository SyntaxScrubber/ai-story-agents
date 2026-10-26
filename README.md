# AI Story Agents

Two small, finishable AI agents that work as a team to make
kid-friendly short drama stories — script first, visuals second,
human director in the loop throughout.

## The team

### Agent 1 — Script Writer (`agent_v1.py`)
- **Core job, fixed:** write a short drama script from a brief.
- **Variable direction, per run:** theme, audience/tone,
  length, characters, setting, conflict, cliffhanger yes/no,
  what to avoid — all from the brief.
- **Output, fixed:** Title → Characters → Setting → Script →
  Cliffhanger → Video notes (3–5 scene prompts for Agent 2).

### Agent 2 — Visual Generator (`agent_v2_visual.py`)
- **Core job, fixed:** turn a finalized script's video notes
  into visual prompts, one per scene.
- **Style, fixed:** cartoonish / unrealistic, not photorealistic.
  Simple shapes, big expressions, characters kept consistent.
- **Output, fixed, per scene:** visual prompt, duration/format
  note, director note (anything that looks off, or needs a redo).

## How it runs

1. You write a brief (see `brief-template.md`).
2. Agent 1 writes a script. You finalize it — cut, fix, keep.
3. Agent 2 turns the finalized video notes into visual prompts.
   You finalize those too.
4. Those finalized prompts go to an image / video tool to make
   the actual clips. Nothing publishes automatically.

## Setup

- Python, and `pip install google-genai`
- A Gemini API key from Google AI Studio, set as an
  environment variable — never in the code, never in a file
  you share here:
  - Windows PowerShell: `$env:GEMINI_API_KEY="your-key-here"`
  - Mac / Linux: `export GEMINI_API_KEY="your-key-here"`

Run, in the project folder, one command at a time:
```
python agent_v1.py
python agent_v2_visual.py
```

To save an output instead of just reading it in the terminal:
```
python agent_v1.py > script1.txt
python agent_v2_visual.py > visuals1.txt
```

## Model note

This project uses `gemini-3.8-flash`. Earlier versions used
`gemini-2.5-flash`, which Google no longer offers to new users
(404 NOT_FOUND, "no longer available to new users") — that is
why the model name changed.

## First episode made with these agents

Halloween, kid-friendly, cozy fantasy — Wrenna the witch,
Bo the ghost who is terrible at being scary, and Pip the
pumpkin with opinions. Script, visuals, and four scene
pictures were made with this pipeline in October 2026.

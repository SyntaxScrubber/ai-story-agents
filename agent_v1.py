"""
AI Story Agent v1 — brand new, clean version.

An agent is just:
  1. A role prompt (who the agent is, what its job is)
  2. A brief (what you want this time)
  3. A call to an AI model (the API)
  4. The output, printed for you to finalize

SETUP (do this once):
  1. Go to Google AI Studio and get a Gemini API key.
     Keep it secret. Never paste it in chat, never put it in a
     file you share on GitHub.
  2. On your computer, set it as an environment variable:
       Windows (PowerShell):  $env:GEMINI_API_KEY="your-key-here"
       Mac / Linux:           export GEMINI_API_KEY="your-key-here"
  3. Install the Gemini Python package:
       pip install google-genai

RUN (in PowerShell, in the AI Story folder, and nothing else):
  python agent_v1.py

If you don't have a key yet, the script will tell you, and stop
safely. It will not spend anything until you run it with a key.
"""

import os
import sys

# --- The brief: this is the variable direction you change each time ---
BRIEF = """
Theme: October — Halloween, cozy fantasy
Audience / tone: kid-friendly, silly, cartoonish
Length: about 2 minutes
Characters: Wrenna, a witch who runs a pumpkin patch stand;
  Bo, a ghost who is terrible at being scary;
  Pip, a small pumpkin with opinions
Setting: a pumpkin patch at dusk
Core conflict: a glow-charm wakes up every pumpkin at the worst moment
Cliffhanger: yes — a driverless wagon rolls up the road
What to avoid: no cruelty, no real scares, no adult themes
"""

# --- The core role prompt: this is the agent's fixed job ---
ROLE_PROMPT = """
You are a short-drama script writer for a cozy-fantasy serial.
Write ONLY from the brief you are given.
Short and playable dialogue. No cruelty for its own sake.
End with a cliffhanger ONLY if the brief asks for one.
Output format, always:
1. Title
2. Characters
3. Setting
4. Script — scenes with dialogue, in order
5. Cliffhanger / ending line
6. Video notes — 3-5 short scene prompts for a visual agent
This script is a draft for a human director to finalize.
It is not published automatically.
"""


def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("No GEMINI_API_KEY found.")
        print("Set it as an environment variable first, then run again.")
        print("See the setup notes at the top of this file.")
        sys.exit(1)

    from google import genai

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=ROLE_PROMPT + "\n\nBRIEF:\n" + BRIEF,
    )

    print(response.text)
    print("\n--- Human finalize step ---")
    print("Read it, cut what doesn't fit, keep what works.")


if __name__ == "__main__":
    main()

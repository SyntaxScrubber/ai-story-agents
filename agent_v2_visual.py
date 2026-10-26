"""
AI Story Agent v2 — Visual Generator.

This is Agent 2. It takes a finalized script's video notes and
turns them into visual prompts — one per scene — that you can
feed to an image / video tool later.

It does NOT rewrite the script, and it does NOT make video
files by itself. It makes the prompts. You finalize those too.

SETUP: same as agent_v1.py.
  - GEMINI_API_KEY as an environment variable (same window)
  - pip install google-genai (already done if you ran v1)

RUN (in PowerShell, in the AI Story folder, and nothing else):
  python agent_v2_visual.py
"""

import os
import sys

# --- The input: video notes from your finalized script ---
# Replace these with the video notes from whatever script you
# just finalized. These are the notes from script 1.
VIDEO_NOTES = """
1. Wide Shot / Establishing: Golden hour over a cozy patch;
   fairy lights twinkling, rustic wooden stand, purple
   twilight hills in the background.
2. Medium Shot / Physical Comedy: Bo sneezes a puff of
   sparkles, causing Wrenna's wand to misfire a golden
   dandelion-firework into the patch.
3. Animated Detail Shot: Rows of pumpkins suddenly pop open
   glowing eyes and start bickering, with Pip grinning smugly
   on his stand cushion.
4. Final Mystery Shot: A spooky, empty driver's bench on a
   creaking wooden wagon rolling silently through the fog
   toward the patch gate.
"""

# --- The core role prompt: this is the agent's fixed job ---
ROLE_PROMPT = """
You are a Visual Generator for a cozy-fantasy, kid-friendly
cartoon serial. You turn video notes into visual prompts.

Core rules, fixed every run:
- Visual style is cartoonish / unrealistic, not photorealistic.
  Simple shapes, big expressions, no realistic human faces
  or hands to get wrong.
- Keep characters consistent: same look, same colours, same
  simple shapes across scenes.
- One clear idea per scene, no clutter.
- Do not rewrite the story, do not change the plot.
- If a scene cannot be made safely / kid-friendly, say so
  and stop — do not invent a workaround that changes the story.

Output format, fixed, for each scene in order:
- Scene number + title
- Visual prompt (setting, characters, action, mood, style)
- Duration / format note (e.g. short clip, still image with zoom)
- Director note (anything that looks off, or needs a redo)

This is a draft for a human director to finalize.
Nothing publishes automatically.
"""


def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("No GEMINI_API_KEY found.")
        print("Set it as an environment variable first, then run again.")
        sys.exit(1)

    from google import genai

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=ROLE_PROMPT + "\n\nVIDEO NOTES:\n" + VIDEO_NOTES,
    )

    print(response.text)
    print("\n--- Human finalize step ---")
    print("Read the visual prompts, cut what doesn't fit,")
    print("keep what works, then feed them to an image /")
    print("video tool to make the actual clips.")


if __name__ == "__main__":
    main()

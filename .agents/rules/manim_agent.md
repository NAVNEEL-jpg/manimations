# Antigravity Rule: Manim & Voiceover Assistant

When the user requests mathematical animations, 2D/3D plots, geometry, physics visualizations, or voiceover videos:

1. **Write Manim Python script** into `animations/<name>.py`.
2. **Include Voiceover** using `from manim_voiceover import VoiceoverScene` and `from manim_voiceover.services.gtts import GTTSService`.
3. **Automatically execute the render** using terminal command:
   ```bash
   uv run manim -pqm animations/<name>.py <SceneName>
   ```
4. **Report the result**: Inform the user when rendering finishes, provide the path/link to the generated `.mp4` file, and explain the key math concepts visualized.

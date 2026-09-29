# 🎙️ Instagram & Educational Voice Directory (Ranked)

This guide ranks all neural AI voices available in this studio from **Best to Good**, describing their tone, vibe, and ideal use case for Instagram Reels, YouTube Shorts, and teaching videos.

All voices are powered by the **[`EdgeTTSService`](src/manimations/edge_service.py)** (free, neural, zero robotic artifacting).

---

## 🏆 Tier 1: The S-Tier (Best for Instagram Reels & Viral Teaching)

These are the most realistic, human-sounding voices. They have natural cadence, authentic breathing, and zero robotic monotone.

| Rank | Voice ID | Gender | Accent | Tone & Personality | Best Used For |
| :---: | :--- | :---: | :---: | :--- | :--- |
| **#1** | `en-US-AndrewMultilingualNeural` | 👨 Male | American | **Warm, Confident, Authentic** <br>Sounds like a modern tech educator or podcaster. Very reassuring and pleasant to listen to. | **#1 Recommended for Math, Physics, and 3D visual explanations.** |
| **#2** | `en-US-BrianMultilingualNeural` | 👨 Male | American | **Approachable, Casual, Punchy** <br>The viral "TikTok/Reels" style voice. Energetic, youthful, and grabs attention in the first 2 seconds. | **Fast-paced Instagram Reels, math hacks, and quick concept shorts.** |
| **#3** | `en-US-AvaMultilingualNeural` | 👩 Female | American | **Expressive, Caring, Friendly** <br>Very expressive with natural emotional inflections. Warm and inviting tone that keeps viewer retention high. | **Intuitive conceptual walkthroughs, step-by-step problem solving.** |
| **#4** | `en-US-EmmaMultilingualNeural` | 👩 Female | American | **Cheerful, Crystal-Clear, Academic** <br>Sounds like an enthusiastic university lecturer or YouTube educator (like 3Blue1Brown or Khan Academy style). | **Calculus, geometry proofs, and classroom explanations.** |
| **#5** | `en-IN-PrabhatNeural` | 👨 Male | Indian | **Articulate, Calm, Reassuring** <br>Clean Indian English accent without exaggerated inflection. Sounds like a top IIT/university professor. | **Indian curriculum, JEE / NEET prep, and technical STEM lectures.** |
| **#6** | `en-IN-NeerjaExpressiveNeural` | 👩 Female | Indian | **Polished, Engaging, Expressive** <br>Clear diction, natural Indian English rhythm with great emphasis on key formula terms. | **Conceptual physics/math shorts for Indian and international audiences.** |

---

## 🎖️ Tier 2: The A-Tier (High-Authority & Specialized Tones)

Ideal when you want a specific vibe: deep documentary narration, dramatic energy, or formal British lecture style.

| Rank | Voice ID | Gender | Accent | Tone & Personality | Best Used For |
| :---: | :--- | :---: | :---: | :--- | :--- |
| **#7** | `en-US-ChristopherNeural` | 👨 Male | American | **Deep, Authoritative, Cinematic** <br>Sounds like a BBC / National Geographic narrator or audio book voice. Commanding and serious. | **Astrophysics, historical math discoveries, deep theorems.** |
| **#8** | `en-US-GuyNeural` | 👨 Male | American | **Passionate, Dramatic, Intense** <br>Dynamic delivery with conviction and energy. | **Mind-blowing math paradoxes, "Did you know?" hooks.** |
| **#9** | `en-US-JennyNeural` | 👩 Female | American | **Balanced, Considerate, Neutral** <br>Professional, steady, and easy to understand at any playback speed. | **Textbook-style educational material and longer videos.** |
| **#10** | `en-GB-RyanNeural` | 👨 Male | British | **Sophisticated, Articulate, Calm** <br>Classic Oxford/Cambridge style British accent. Intellectual and polished. | **Pure mathematics, formal proofs, higher-level academic content.** |
| **#11** | `en-GB-SoniaNeural` | 👩 Female | British | **Gentle, Friendly, Articulate** <br>Warm British tone, gentle cadence that doesn't overwhelm the listener. | **Elementary to high school math concepts.** |
| **#12** | `en-US-EricNeural` | 👨 Male | American | **Rational, Precise, Analytical** <br>Methodical and analytical tone without emotional distraction. | **Engineering, algorithms, and computational math.** |

---

## 🌏 Tier 3: The B-Tier (International & Regional Accents)

High-quality neural voices tailored for regional English audiences across the globe.

### 🇮🇳 Indian English
- `en-IN-NeerjaNeural` (Female): Traditional clear Indian English educator tone.
- `en-IN-PrabhatNeural` (Male): Calm and articulate Indian English tutor.

### 🇬🇧 British English
- `en-GB-ThomasNeural` (Male): Formal, crisp UK presentation style.
- `en-GB-LibbyNeural` (Female): Friendly, casual UK schoolteacher voice.
- `en-GB-MaisieNeural` (Female): Youthful, conversational British cadence.

### 🇦🇺 Australian English
- `en-AU-WilliamMultilingualNeural` (Male): Friendly, laid-back, articulate Australian tone.
- `en-AU-NatashaNeural` (Female): Crisp, energetic Australian educator voice.

### 🇨🇦 Canadian English
- `en-CA-LiamNeural` (Male): Clean North American cadence with gentle delivery.
- `en-CA-ClaraNeural` (Female): Polite, articulate Canadian educator voice.

### 🇮🇪 Irish English
- `en-IE-ConnorNeural` (Male): Rich Irish lilt, very engaging for storytelling math.
- `en-IE-EmilyNeural` (Female): Friendly, expressive Irish delivery.

### 🇸🇬 & 🇵🇭 Asian English
- `en-SG-WayneNeural` (Male): Clear Singaporean international English.
- `en-PH-JamesNeural` (Male): Smooth, clear Philippine English tone.

---

## 💻 How to Change Voices in Your Animation

In your animation script, simply pass the voice name into `EdgeTTSService`:

```python
from manim import *
from manim_voiceover import VoiceoverScene
from manimations import EdgeTTSService

class MyScene(VoiceoverScene):
    def construct(self):
        # 1. Choose your preferred voice:
        self.set_speech_service(
            EdgeTTSService(
                voice="en-US-AndrewMultilingualNeural", # Change to any voice above
                rate="+0%",                              # Speed: e.g. "+10%" for faster Reels
                pitch="+0Hz"                             # Pitch adjustment
            )
        )
        
        # 2. Your animations:
        with self.voiceover(text="Welcome! Today we explore...") as tracker:
            self.play(...)
```

---

## ⚡ Pro-Tips for Instagram Reels

1. **Boost Speed by +10% to +15%:**
   Instagram audiences prefer snappy delivery. Use:
   ```python
   EdgeTTSService(voice="en-US-BrianMultilingualNeural", rate="+10%")
   ```
2. **Hook in First 3 Seconds:**
   Make your first voiceover punchy (e.g. *"Why is this curve called a saddle point?"* instead of *"Hello everyone, in today's video..."*).
3. **Use 9:16 Vertical Ratio:**
   Keep `config.frame_height = 16.0` and `config.frame_width = 9.0` for full-screen phone viewing.

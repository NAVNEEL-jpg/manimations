# 🎬 Manim AI Studio

Welcome to your AI-assisted mathematical animation studio! This repository is designed to let educators and researchers create stunning 2D/3D math animations and voiceover videos **without needing to code manually or understand complex AI tools**.

---

## 🚀 Quick Start (In 3 Easy Steps)

### Step 1: Install Antigravity IDE
Download and install **Google Antigravity IDE**:
👉 **[Download Antigravity IDE](https://antigravity.google)**

*(If you already have Antigravity installed, proceed to Step 2.)*

---

### Step 2: Set Up the Studio (Single Command)

Open **PowerShell** (or Command Prompt) on your computer, paste this single command, and press **Enter**:

```powershell
git clone https://github.com/NAVNEEL-jpg/manimations.git manim-studio; cd manim-studio; .\setup.bat
```

> 💡 **What `setup.bat` does automatically:**
> - Checks and sets up Python and package tools (`uv`).
> - Installs `manim` and the `manim-voiceover` audio engine.
> - Checks video renderer (`FFmpeg`).
> - Opens this project directly inside Antigravity IDE.

---

### Step 3: Just Ask for Any Animation!

1. In Antigravity IDE, look at the **AI Chat Sidebar** on the right (or press `Ctrl + L`).
2. Simply type in **plain English** what graph, concept, or 3D animation you want.
3. Antigravity will write the math script, synchronize the voiceover, render the video, and give you the playable `.mp4` file!

---

## 💬 Example Prompts You Can Copy & Paste

Here are real examples you can directly paste into the Antigravity chat:

### 1. 3D Surface & Geometry
> *"Create a 3D animated plot of a rotating saddle surface $z = x^2 - y^2$, and add a voiceover explaining why the origin is a saddle point."*

### 2. Calculus & Functions
> *"Animate the curve $y = \sin(x)$ along with its moving tangent line. Include a voiceover explaining how the derivative represents the slope of the tangent."*

### 3. Linear Algebra & Vectors
> *"Show a 2D coordinate grid undergoing a linear transformation matrix [[2, 1], [0, 2]]. Have the voiceover explain what basis vectors are and how they stretch space."*

### 4. Physics Simulation
> *"Animate a pendulum swinging with damped harmonic motion, plotting its angle $\theta(t)$ vs time below the pendulum."*

---

## 🎙️ Neural Voiceover Engine (Instagram & Reels Ready)

This studio includes **Microsoft Azure Neural Voices** powered by `EdgeTTSService`:
- **Studio Quality:** Zero robotic tone—sounds like a real human educator or content creator.
- **100% Free:** No API keys, no subscriptions, unlimited voice generations.
- **Ranked Voice Directory:** Browse **[`VOICES.md`](VOICES.md)** for a complete ranked list of voices (with descriptions of each tone, accent, and style).

To change the voice, simply specify the voice name:
```python
from manimations import EdgeTTSService

# Andrew (Warm & Confident - #1 for Math/Physics):
self.set_speech_service(EdgeTTSService(voice="en-US-AndrewMultilingualNeural"))

# Brian (Casual & Punchy - #1 for Viral Reels):
self.set_speech_service(EdgeTTSService(voice="en-US-BrianMultilingualNeural", rate="+10%"))

# Prabhat (Calm Indian English Professor):
self.set_speech_service(EdgeTTSService(voice="en-IN-PrabhatNeural"))
```

---

## 📂 Project Structure

```text
├── animations/         # All generated Manim animation scripts live here
├── media/videos/       # Rendered MP4 videos ready to watch and share
├── AGENTS.md           # Instructions that guide the AI agent
├── setup.bat           # 1-Click setup script for Windows
├── setup.sh            # 1-Click setup script for macOS / Linux
└── pyproject.toml      # Project configuration and dependencies
```

---

## 🛠️ Handy Commands (Optional)

If you ever want to manually render a specific script yourself from the terminal:

- **Quick Draft Preview (Fast, 480p):**
  ```bash
  uv run manim -pql animations/sample_demo.py Demo3DAnimation
  ```
- **Standard Video (720p - Recommended):**
  ```bash
  uv run manim -pqm animations/sample_demo.py Demo3DAnimation
  ```
- **High Definition (1080p 60fps for YouTube/Presentations):**
  ```bash
  uv run manim -pqh animations/sample_demo.py Demo3DAnimation
  ```

---

## ❓ Frequently Asked Questions (FAQ)

**Q: Do I need to learn Python or Manim syntax?**  
**A:** No! Antigravity writes and executes all the code for you. If you want to make adjustments (like changing colors or text), just tell Antigravity: *"Make the surface gold and slow down the camera rotation"*.

**Q: Where are the final videos saved?**  
**A:** Rendered video files are saved in the `media/videos/` folder inside this directory as standard `.mp4` files that you can play with VLC, Windows Media Player, PowerPoint, or upload to YouTube.

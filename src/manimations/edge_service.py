import asyncio
from pathlib import Path
from manim_voiceover.services.base import SpeechService
from manim_voiceover.helper import remove_bookmarks
import edge_tts

class EdgeTTSService(SpeechService):
    """
    SpeechService for Microsoft Edge Neural TTS voices (powered by https://github.com/rany2/edge-tts).
    
    100% Free, No API Key, Studio Quality Neural Voices for Instagram Reels and educational videos.
    Popular Voices:
      - 'en-US-AndrewMultilingualNeural' (Warm, engaging, conversational male - perfect for Reels)
      - 'en-US-AvaMultilingualNeural' (Pleasant, friendly female)
      - 'en-US-BrianMultilingualNeural' (Casual, sincere male - viral TikTok/Reels voice)
      - 'en-US-EmmaMultilingualNeural' (Clear, enthusiastic female teacher voice)
      - 'en-US-ChristopherNeural' (Authoritative documentary/BBC style male)
      - 'en-IN-PrabhatNeural' (Clear Indian English male educator)
      - 'en-IN-NeerjaExpressiveNeural' (Expressive Indian English female educator)
    """

    def __init__(
        self,
        voice: str = "en-US-AndrewMultilingualNeural",
        rate: str = "+0%",
        pitch: str = "+0Hz",
        **kwargs
    ):
        super().__init__(**kwargs)
        self.voice = voice
        self.rate = rate
        self.pitch = pitch

    def generate_from_text(self, text: str, cache_dir=None, path=None, **kwargs):
        if cache_dir is None:
            cache_dir = self.cache_dir

        input_text = remove_bookmarks(text)
        voice = kwargs.get("voice", self.voice)
        rate = kwargs.get("rate", self.rate)
        pitch = kwargs.get("pitch", self.pitch)

        input_data = {
            "input_text": input_text,
            "service": "edge-tts",
            "voice": voice,
            "rate": rate,
            "pitch": pitch,
        }

        cached_result = self.get_cached_result(input_data, cache_dir)
        if cached_result is not None:
            return cached_result

        if path is None:
            audio_path = self.get_audio_basename(input_data) + ".mp3"
        else:
            audio_path = str(path)

        target_file = Path(cache_dir) / audio_path

        async def _synthesize():
            communicate = edge_tts.Communicate(input_text, voice, rate=rate, pitch=pitch)
            await communicate.save(str(target_file))

        asyncio.run(_synthesize())

        return {
            "input_text": text,
            "input_data": input_data,
            "original_audio": audio_path,
        }

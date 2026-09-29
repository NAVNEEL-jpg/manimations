from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class Demo3DAnimation(VoiceoverScene, ThreeDScene):
    def construct(self):
        # Initialize free Google TTS service
        self.set_speech_service(GTTSService(lang="en"))
        
        # Create 3D Axes
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-3, 3, 1],
            x_length=6,
            y_length=6,
            z_length=4
        )
        
        # Create a hyperbolic paraboloid (saddle surface: z = x^2 - y^2)
        surface = Surface(
            lambda u, v: np.array([u, v, 0.5 * (u**2 - v**2)]),
            u_range=[-2, 2],
            v_range=[-2, 2],
            resolution=(25, 25),
        )
        surface.set_style(fill_opacity=0.8, fill_color=BLUE, stroke_color=YELLOW, stroke_width=0.5)
        
        # Set initial camera view
        self.set_camera_orientation(phi=65 * DEGREES, theta=-45 * DEGREES)
        
        # Section 1: Intro with synchronized voiceover
        with self.voiceover(text="Welcome! Today we are visualizing a hyperbolic paraboloid, commonly known as a saddle surface.") as tracker:
            self.play(Create(axes), Create(surface), run_time=tracker.duration)
        
        # Section 2: Camera rotation explaining curvature
        with self.voiceover(text="Notice how the surface curves upward along one direction, but curves downward along another.") as tracker:
            self.begin_ambient_camera_rotation(rate=0.4)
            self.wait(tracker.duration)
            self.stop_ambient_camera_rotation()
            
        # Section 3: Saddle point conclusion
        with self.voiceover(text="The origin is a saddle point: a stationary point that is neither a local maximum nor a local minimum.") as tracker:
            dot = Dot3D(point=ORIGIN, color=RED, radius=0.15)
            self.play(FadeIn(dot))
            self.wait(tracker.duration)

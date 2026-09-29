from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
import numpy as np

def create_spring(start_point, end_point, num_coils=10, width=0.3):
    """Creates a zigzag spring connecting start_point and end_point."""
    vec = end_point - start_point
    length = np.linalg.norm(vec)
    if length < 0.2:
        return Line(start_point, end_point, color=GRAY_A)
    u_vec = vec / length
    perp_vec = np.array([-u_vec[1], u_vec[0], 0])
    
    lead_in = 0.25
    coil_span = max(0.1, length - 2 * lead_in)
    step = coil_span / num_coils
    
    pts = [start_point, start_point + lead_in * u_vec]
    for i in range(num_coils):
        sign = 1 if i % 2 == 0 else -1
        pt = start_point + (lead_in + (i + 0.5) * step) * u_vec + sign * width * perp_vec
        pts.append(pt)
    pts.append(end_point - lead_in * u_vec)
    pts.append(end_point)
    
    return VMobject().set_points_as_corners(pts).set_color(GRAY_A).set_stroke(width=3)

class SimpleHarmonicMotionScene(VoiceoverScene):
    def construct(self):
        # 1. Setup speech service
        self.set_speech_service(GTTSService(lang="en"))
        
        # Title
        title = Title("Simple Harmonic Motion (SHM)", color=BLUE_B).scale(0.85)
        self.add(title)
        
        # 2. Physics Model: Mass on a Spring (Top half of the screen)
        wall_x = -5.0
        y_level = 1.6
        wall = Line(np.array([wall_x, y_level - 0.8, 0]), np.array([wall_x, y_level + 0.8, 0]), stroke_width=6, color=LIGHT_GRAY)
        floor = Line(np.array([wall_x, y_level - 0.6, 0]), np.array([2.5, y_level - 0.6, 0]), stroke_width=2, color=GRAY)
        
        equilibrium_x = -1.5
        amplitude = 2.0
        period = 4.0
        omega = 2 * np.pi / period
        
        t_tracker = ValueTracker(0)
        
        # Equilibrium dashed line
        eq_line = DashedLine(
            np.array([equilibrium_x, y_level - 0.7, 0]),
            np.array([equilibrium_x, y_level + 0.7, 0]),
            color=YELLOW_C
        )
        eq_label = MathTex("x = 0", color=YELLOW_C).scale(0.6).next_to(eq_line, UP, buff=0.1)
        
        # Dynamic Block and Spring
        def get_block_center():
            t = t_tracker.get_value()
            return np.array([equilibrium_x + amplitude * np.cos(omega * t), y_level, 0])
        
        block = always_redraw(lambda: 
            Square(side_length=1.1, fill_color=TEAL_E, fill_opacity=0.9, stroke_color=WHITE, stroke_width=2)
            .move_to(get_block_center())
        )
        block_label = always_redraw(lambda:
            MathTex("m", color=WHITE).scale(0.8).move_to(block.get_center())
        )
        
        spring = always_redraw(lambda:
            create_spring(
                np.array([wall_x, y_level, 0]),
                block.get_left()
            )
        )
        
        # Formula: Hooke's Law
        hooke_formula = MathTex(r"F = -k x", color=YELLOW).scale(0.85).to_corner(UR, buff=0.8)
        shm_eq = MathTex(r"x(t) = A \cos(\omega t)", color=BLUE_C).scale(0.85).next_to(hooke_formula, DOWN, buff=0.3)
        
        # 3. Waveform Graph (Bottom half of the screen)
        axes = Axes(
            x_range=[0, 8, 2],
            y_range=[-2.5, 2.5, 1],
            x_length=7.5,
            y_length=2.6,
            axis_config={"color": GRAY, "stroke_width": 2},
            tips=False
        ).shift(DOWN * 2.0 + LEFT * 0.5)
        
        x_axis_label = axes.get_x_axis_label(MathTex(r"t \text{ (time)}").scale(0.6), edge=RIGHT, direction=DOWN)
        y_axis_label = axes.get_y_axis_label(MathTex(r"x(t)").scale(0.6), edge=UP, direction=LEFT)
        
        # Tracer dot and live plotted curve
        tracer_dot = always_redraw(lambda:
            Dot(
                axes.c2p(t_tracker.get_value(), amplitude * np.cos(omega * t_tracker.get_value())),
                color=RED,
                radius=0.08
            )
        )
        
        drawn_curve = always_redraw(lambda:
            axes.plot(
                lambda t: amplitude * np.cos(omega * t),
                x_range=[0, max(0.001, t_tracker.get_value())],
                color=RED_B,
                stroke_width=3
            )
        )
        
        # Sequence with Voiceover
        with self.voiceover(text="Simple Harmonic Motion occurs when the restoring force is directly proportional to displacement, known as Hooke's Law.") as tracker:
            self.play(Create(wall), Create(floor), Create(eq_line), Write(eq_label))
            self.play(Create(spring), FadeIn(block), FadeIn(block_label), Write(hooke_formula), run_time=tracker.duration * 0.6)
            
        with self.voiceover(text="When released from a displacement A, the mass oscillates back and forth about its equilibrium position.") as tracker:
            self.play(Write(shm_eq))
            self.play(Create(axes), Write(x_axis_label), Write(y_axis_label), run_time=1.5)
            self.add(drawn_curve, tracer_dot)
            self.play(t_tracker.animate.set_value(4.0), run_time=tracker.duration, rate_func=linear)
            
        with self.voiceover(text="Notice how the displacement over time traces a pure sinusoidal cosine wave, completing one full cycle every period T.") as tracker:
            self.play(t_tracker.animate.set_value(8.0), run_time=tracker.duration, rate_func=linear)
            
        self.wait(1)

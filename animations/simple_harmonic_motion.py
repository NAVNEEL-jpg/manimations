from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
import numpy as np

# 9:16 Vertical Aspect Ratio configuration (Shorts / Reels / Mobile)
config.pixel_width = 720
config.pixel_height = 1280
config.frame_height = 16.0
config.frame_width = 9.0

def create_spring(start_point, end_point, num_coils=9, width=0.28):
    """Creates a zigzag spring connecting start_point and end_point."""
    vec = end_point - start_point
    length = np.linalg.norm(vec)
    if length < 0.2:
        return Line(start_point, end_point, color=GRAY_A)
    u_vec = vec / length
    perp_vec = np.array([-u_vec[1], u_vec[0], 0])
    
    lead_in = 0.2
    coil_span = max(0.1, length - 2 * lead_in)
    step = coil_span / num_coils
    
    pts = [start_point, start_point + lead_in * u_vec]
    for i in range(num_coils):
        sign = 1 if i % 2 == 0 else -1
        pt = start_point + (lead_in + (i + 0.5) * step) * u_vec + sign * width * perp_vec
        pts.append(pt)
    pts.append(end_point - lead_in * u_vec)
    pts.append(end_point)
    
    return VMobject().set_points_as_corners(pts).set_color(GRAY_A).set_stroke(width=3.5)

class SimpleHarmonicMotionScene(VoiceoverScene):
    def construct(self):
        # 1. Setup Speech Service
        self.set_speech_service(GTTSService(lang="en"))
        
        # 2. Header Section (Top of 9:16 Frame)
        title = Text("Simple Harmonic Motion", font_size=38, weight=BOLD, color=BLUE_B).to_edge(UP, buff=1.0)
        subtitle = Text("SHM: Spring-Mass Oscillator", font_size=24, color=GRAY_A).next_to(title, DOWN, buff=0.25)
        self.add(title, subtitle)
        
        # 3. Formulas Card (Upper Middle)
        formula_box = RoundedRectangle(
            corner_radius=0.2,
            height=1.8,
            width=7.2,
            fill_color=DARK_GRAY,
            fill_opacity=0.35,
            stroke_color=BLUE_D,
            stroke_width=1.5
        ).move_to(np.array([0, 4.3, 0]))
        
        hooke_formula = MathTex(r"F = -k x", color=YELLOW_B).scale(0.85).move_to(formula_box.get_center() + LEFT * 1.8)
        shm_eq = MathTex(r"x(t) = A \cos(\omega t)", color=TEAL_B).scale(0.85).move_to(formula_box.get_center() + RIGHT * 1.6)
        
        # 4. Physical Model Section (Middle)
        wall_x = -3.4
        y_level = 1.2
        wall = Line(np.array([wall_x, y_level - 0.7, 0]), np.array([wall_x, y_level + 0.7, 0]), stroke_width=6, color=LIGHT_GRAY)
        floor = Line(np.array([wall_x, y_level - 0.5, 0]), np.array([3.4, y_level - 0.5, 0]), stroke_width=2.5, color=GRAY)
        
        equilibrium_x = 0.0
        amplitude = 1.8
        period = 4.0
        omega = 2 * np.pi / period
        
        t_tracker = ValueTracker(0)
        
        # Equilibrium line at x = 0
        eq_line = DashedLine(
            np.array([equilibrium_x, y_level - 0.65, 0]),
            np.array([equilibrium_x, y_level + 0.65, 0]),
            color=YELLOW_C,
            dash_length=0.1
        )
        eq_label = MathTex(r"x = 0", color=YELLOW_C).scale(0.6).next_to(eq_line, UP, buff=0.15)
        
        # Dynamic Block and Spring
        def get_block_center():
            t = t_tracker.get_value()
            return np.array([equilibrium_x + amplitude * np.cos(omega * t), y_level, 0])
        
        block = always_redraw(lambda: 
            Square(side_length=0.95, fill_color=TEAL_E, fill_opacity=0.9, stroke_color=WHITE, stroke_width=2)
            .move_to(get_block_center())
        )
        block_label = always_redraw(lambda:
            MathTex("m", color=WHITE).scale(0.75).move_to(block.get_center())
        )
        
        spring = always_redraw(lambda:
            create_spring(
                np.array([wall_x, y_level, 0]),
                block.get_left()
            )
        )
        
        # 5. Waveform Graph Section (Lower Half)
        axes = Axes(
            x_range=[0, 8, 2],
            y_range=[-2.2, 2.2, 1],
            x_length=6.4,
            y_length=3.4,
            axis_config={"color": GRAY, "stroke_width": 2},
            tips=False
        ).move_to(np.array([0, -3.8, 0]))
        
        x_axis_label = axes.get_x_axis_label(MathTex(r"t\text{ (time)}").scale(0.55), edge=RIGHT, direction=DOWN)
        y_axis_label = axes.get_y_axis_label(MathTex(r"x(t)").scale(0.55), edge=UP, direction=LEFT)
        
        # Live plotted curve and tracer dot
        tracer_dot = always_redraw(lambda:
            Dot(
                axes.c2p(t_tracker.get_value(), amplitude * np.cos(omega * t_tracker.get_value())),
                color=RED,
                radius=0.1
            )
        )
        
        drawn_curve = always_redraw(lambda:
            axes.plot(
                lambda t: amplitude * np.cos(omega * t),
                x_range=[0, max(0.001, t_tracker.get_value())],
                color=RED_B,
                stroke_width=3.5
            )
        )
        
        # 6. Animation Sequence with Synchronized Voiceover
        with self.voiceover(text="Simple Harmonic Motion occurs when a restoring force pulls an object back toward equilibrium, directly proportional to its displacement.") as tracker:
            self.play(FadeIn(formula_box), Write(hooke_formula))
            self.play(Create(wall), Create(floor), Create(eq_line), Write(eq_label))
            self.play(Create(spring), FadeIn(block), FadeIn(block_label), run_time=tracker.duration * 0.4)
            
        with self.voiceover(text="When released from amplitude A, the mass oscillates back and forth perpetually under ideal conditions.") as tracker:
            self.play(Write(shm_eq))
            self.play(Create(axes), Write(x_axis_label), Write(y_axis_label), run_time=1.4)
            self.add(drawn_curve, tracer_dot)
            self.play(t_tracker.animate.set_value(4.0), run_time=tracker.duration, rate_func=linear)
            
        with self.voiceover(text="The displacement over time traces a smooth cosine wave, repeating its cycle every period T.") as tracker:
            self.play(t_tracker.animate.set_value(8.0), run_time=tracker.duration, rate_func=linear)
            
        self.wait(1)

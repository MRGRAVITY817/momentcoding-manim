from manim import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()
        square.rotate(PI/4)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class SectionParts(Scene):
    def construct(self):
        sq = Square()
        sq.round_corners(radius=0.5)
        # each section needs at least one animation
        self.add(sq)
        self.wait()
        self.next_section()

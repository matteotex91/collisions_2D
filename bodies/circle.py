from bodies.body import Body
import numpy as np


class Circle(Body):
    radius_: float
    mass_: float

    def __init__(
        self,
        position: np.ndarray = np.array([0, 0]),
        speed: np.ndarray = np.array([0, 0]),
        angle: float = 0,
        omega: float = 0,
        mass: float = 0,
        radius: float = 0,
        inmom=None,
    ):
        if inmom is None:
            inmom = 0.5 * mass * np.square(radius)
        super().__init__(
            position=position,
            speed=speed,
            angle=angle,
            omega=omega,
            mass=mass,
            inmom=inmom,
        )
        self.radius_ = radius

    def collides(self, b: Body) -> bool:
        if type(b) is Circle:
            b.__class__ = Circle
            return bool(
                np.linalg.norm(self.position_ - b.position_) < self.radius_ + b.radius_
            )
        else:
            return False

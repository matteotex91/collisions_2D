from bodies.body import Body
import numpy as np


class Circle(Body):
    radius_: np.double
    mass_: np.double

    def __init__(
        self,
        position: np.ndarray = np.array([0, 0]),
        speed: np.ndarray = np.array([0, 0]),
        angle: np.double = np.double(0),
        omega: np.double = np.double(0),
        mass: np.double = np.double(1),
        radius: np.double = np.double(1),
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

    def collides(self, b: Body) -> np.bool_:
        if type(b) is Circle:
            b.__class__ = Circle
            return np.bool_(
                np.linalg.norm(self.position_ - b.position_) < self.radius_ + b.radius_
            )
        else:
            return False

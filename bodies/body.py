from __future__ import annotations
import numpy as np


class Body:
    position_: np.ndarray
    speed_: np.ndarray
    angle_: float
    omega_: float
    mass_: float
    inmom_: float

    def __init__(
        self,
        position: np.ndarray = np.array([0, 0]),
        speed: np.ndarray = np.array([0, 0]),
        angle: float = 0,
        omega: float = 0,
        mass: float = 0,
        inmom: float = 0,
    ):
        self.position_ = position
        self.speed_ = speed
        self.angle_ = angle
        self.omega_ = omega
        self.mass_ = mass
        self.inmom_ = inmom

    def collides(self, b: Body) -> bool:
        raise NotImplementedError()

    def collision(self, b: Body) -> None:
        pass

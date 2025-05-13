from __future__ import annotations
import numpy as np


class Body:
    position_: np.ndarray
    speed_: np.ndarray
    angle_: np.double
    omega_: np.double
    mass_: np.double
    inmom_: np.double

    def __init__(
        self,
        position: np.ndarray = np.array([0, 0]),
        speed: np.ndarray = np.array([0, 0]),
        angle: np.double = np.double(0),
        omega: np.double = np.double(0),
        mass: np.double = np.double(0),
        inmom: np.double = np.double(0),
    ):
        self.position_ = position
        self.speed_ = speed
        self.angle_ = angle
        self.omega_ = omega
        self.mass_ = mass
        self.inmom_ = inmom

    def collides(self, b: Body) -> np.bool_:
        raise NotImplementedError()

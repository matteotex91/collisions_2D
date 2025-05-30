from bodies.body import Body
import numpy as np


class polygon(Body):
    points: list
    transformed_points: list

    def __init__(
        self,
        points: list,
        position: np.ndarray,
        speed: np.ndarray,
        angle: float,
        omega: float,
        mass: float,
        inmom: float,
    ):
        super().__init__(
            position=position,
            speed=speed,
            angle=angle,
            omega=omega,
            mass=mass,
            inmom=inmom,
        )
        self.points = points

    def update_transformed_points(self):
        ct = np.cos(self.angle_)
        st = np.sin(self.angle_)
        R = np.array([[ct, st], [-st, ct]])
        self.transformed_points = list()
        for p in self.points:
            self.transformed_points.append(self.position_ + np.dot(R, p))


if __name__ == "__main__":
    points = list()
    points.append(np.array([0, 0]))
    points.append(np.array([1, 0]))
    points.append(np.array([1, 1]))
    points.append(np.array([0, 1]))
    position = np.array([0, 0])
    speed = np.array([0, 0])
    p = polygon(points, position, speed, 0, 0, 1, 1)
    p.update_transformed_points()
    print(p.transformed_points)

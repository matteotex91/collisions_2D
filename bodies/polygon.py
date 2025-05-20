from bodies.body import Body
import numpy as np


class polygon(Body):
    points: np.ndarray

    def __init__(self):
        super().__init__()

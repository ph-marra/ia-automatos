import numpy as np
import cv2
import random
from CellularAutomata import CellularAutomata


class Others(CellularAutomata):

    def __init__(self, n: int, rule: int, type: str):

        self.pattern_type = type

        type_dict = {'25%': '1000', '50%': '10', '75%': '1110'}

        self.pattern = type_dict.get(self.pattern_type)
        if self.pattern is None:
            self.pattern_type, self.pattern = random.choice(list(type_dict.items()))

        inivalues = (self.pattern * n)[0:n]

        super().__init__(n, inivalues, rule)


    def __str__(self):
        return f"(rule={str(self.nrule).zfill(3)}, t={str(self.t).zfill(2)}, {self.currentvalues}, type=others({self.pattern_type}))"
    

    def export_history(self):
        img = np.array(self.vhistory, dtype=np.int8)
        img = np.where(img == 0, 255, 0)
        cv2.imwrite(f'rule={self.nrule}_iters={len(self.vhistory)}_type=others({self.pattern_type}).png', img)
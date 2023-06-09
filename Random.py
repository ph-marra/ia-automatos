import numpy as np
import cv2
import random
from CellularAutomata import CellularAutomata

class Random(CellularAutomata):

    def __init__(self, n: int, rule: int):

        vs = [str(random.randint(0,1)) for c in range(n)]
        inivalues = ''
        for v in vs:
            inivalues += v
        type = random.choice(['left', 'center', 'right'])

        super().__init__(n=n, rule=rule, inivalues=inivalues, type=type)

    def __str__(self):
        return f"(rule={str(self.nrule).zfill(3)}, t={str(self.t).zfill(2)}, {self.currentvalues}, type=random)"
    

    def export_history(self):
        img = np.array(self.vhistory, dtype=np.int8)
        img = np.where(img == 0, 255, 0)
        cv2.imwrite(f'inivalues={self.inivalues}_rule={self.nrule}_iters={len(self.vhistory)}_type=random.png', img)

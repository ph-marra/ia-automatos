import numpy as np
import cv2
from CellularAutomata import CellularAutomata


class Impulse(CellularAutomata):

    
    def __init__(self, n: int, rule: int, left=False, center=True, right=False):

        self.left = left
        self.center = center
        self.right = right

        values_list = list('0' * n)
        
        if self.left:
            values_list[0] = '1'
        if self.center:
            values_list[int(n / 2)] = '1'
        if self.right:
            values_list[n-1] = '1'

        inivalues = ''
        for c in values_list:
            inivalues += c
        
        super().__init__(n, inivalues, rule)


    def __str__(self):
        return f"(rule={str(self.nrule).zfill(3)}, t={str(self.t).zfill(2)}, {self.currentvalues}, type=impulse({self.left}, {self.center}, {self.right}))"


    def export_history(self):
        img = np.array(self.vhistory, dtype=np.int8)
        img = np.where(img == 0, 255, 0)
        cv2.imwrite(f'rule={self.nrule}_iters={len(self.vhistory)}_type=impulse({self.left}, {self.center}, {self.right}).png', img)
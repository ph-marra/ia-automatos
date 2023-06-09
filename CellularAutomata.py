import numpy as np
import cv2

class CellularAutomata:


    def __init__(self, n: int, inivalues: str, rule: int, type='center'):
        
        self.rmax = 8

        if n < 10 or n > 30 or rule < 0 or rule > 255 or len(inivalues) > 30:
            raise Exception('Invalid input!')
        
        self.t = 0
        self.n = n
        
        self.type = type

        type_dict = {'center': inivalues.center, 'right': inivalues.rjust, 'left': inivalues.ljust}
        self.currentvalues = type_dict.get(type)(self.n, '0')
        self.inivalues = self.currentvalues

        self.nrule = rule
        self.vhistory = [list(self.currentvalues)]

        rule = bin(rule)[2:][::-1].ljust(self.rmax, '0')

        self.rule = dict()

        for i in range(0, self.rmax):
            j = str(bin(i)[2:]).zfill(3)
            self.rule.update({j: rule[i]})
    

    def __update__(self):
        vlen = len(self.currentvalues)
        newvalues = ''
        for ir in range(vlen):
            previous = self.currentvalues[(ir-1) % vlen]
            current = self.currentvalues[ir % vlen]
            subsequent = self.currentvalues[(ir+1) % vlen]
            newvalues += self.rule.get(f"{previous}{current}{subsequent}")

        self.currentvalues = newvalues
        self.t += 1
        self.vhistory.append(list(self.currentvalues))


    def evolution(self, iters=1, show=True):
        if show:
            print("Cellular automata with the following rules:")
            print(self.rule, end='\n\n')

        print(self)

        for i in range(iters):
            self.__update__()
            if show:
                print(self)


    def __str__(self):
        return f"(rule={str(self.nrule).zfill(3)}, t={str(self.t).zfill(2)}, {self.currentvalues})"


    def export_history(self):
        img = np.array(self.vhistory, dtype=np.int8)
        img = np.where(img == 0, 255, 0)
        cv2.imwrite(f'inivalues={self.inivalues}_rule={self.nrule}_iters={len(self.vhistory)}_type={self.type}.png', img)

class AutomatoCelular:

    def __init__(self, n: int, rinicial: str, regra: int):
        
        if n < 10 or n > 30 or regra < 0 or regra > 255:
            raise Exception('Valores de entrada inválidos!')
        
        self.t = 0
        self.n = n
        self.rmax = 8
        self.rlen = 3
        self.rinicial = list(rinicial)

        regra = bin(regra)[2:][::-1].ljust(self.rmax, '0')

        self.regra = dict()

        for i in range(0, self.rmax):
            j = bin(i)[2:].ljust(self.rlen, '0')
            self.regra.update({j: regra[i]})
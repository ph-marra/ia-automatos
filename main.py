from CellularAutomata import CellularAutomata
from Impulse import Impulse
from Others import Others
import sys
import random

try:
    n = int(sys.argv[sys.argv.index('--n')+1])
except:
    n = random.randint(10, 30)

try:
    rule = int(sys.argv[sys.argv.index('--rule')+1])
except:
    rule = random.randint(0, 255)

try:
    iters = int(sys.argv[sys.argv.index('--iters')+1])
except:
    iters = random.randint(5, 100)

try:
    starting = sys.argv[sys.argv.index('--starting')+1]
except:
    starting = random.choice(['impulse', '25%', '50%', '75%', 'random'])

if starting == 'impulse':
    try:
        left = sys.argv.index('-left')
        left = True
    except:
        left = False

    try:
        center = sys.argv.index('-center')
        center = True
    except:
        center = False

    try:
        right = sys.argv.index('-right')
        right = True
    except:
        right = False

    automata = Impulse(n=n, rule=rule, left=left, center=center, right=right)

else:
    automata = Others(n=n, rule=rule, type=starting)

automata.evolution(iters-1)
automata.export_history()
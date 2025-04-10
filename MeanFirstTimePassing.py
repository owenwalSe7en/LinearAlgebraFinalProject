from sympy import *

# Define symbolic variables for h values
h0, h1, h2, h3, h4 = symbols('h0 h1 h2 h3 h4')  # h5 = 0
h = [h0, h1, h2, h3, h4]

# Define the transition matrix rows (only needed for i ≠ F)
P = [
    [0,     Rational(3,4), Rational(1,4), 0,     0,     0],         # From A
    [Rational(3,8), 0,     Rational(2,8), 0,     Rational(3,8), 0], # From B
    [Rational(1,9), Rational(2,9), 0,     Rational(4,9), Rational(2,9), 0],  # From C
    [0,     0,     Rational(4,5), 0,     0,     Rational(1,5)],     # From D
    [0,     Rational(3,6), Rational(2,6), 0,     0,     Rational(1,6)]  # From E
]

# Create the equations
eqs = []
for i in range(5):  # For A through E
    expected = 1
    for j in range(5):  # Don't include h5 because it's 0
        expected += P[i][j] * h[j]
    eqs.append(Eq(h[i], expected))

# Solve the system
solution = solve(eqs, h)
pprint(solution)
from sympy import *

a, b, c, d, e, f = symbols('a b c d e f')
v = Matrix([a, b, c, d, e, f])

P = Matrix([
    [0,     Rational(3, 4), Rational(1, 4), 0,     0,     0],
    [Rational(3, 8), 0,     Rational(2, 8), 0,     Rational(3, 8), 0],
    [Rational(1, 9), Rational(2, 9), 0,     Rational(4, 9), Rational(2, 9), 0],
    [0,     0,     Rational(4, 5), 0,     0,     Rational(1, 5)],
    [0,     Rational(3, 6), Rational(2, 6), 0,     0,     Rational(1, 6)],
    [0,     0,     0,     0,     Rational(1, 2), Rational(1, 2)]
])

# Identity matrix
I = Matrix.eye(6)

# Set up the steady state equation: (P.T - I) * v = 0
steady_eq = (P.T - I) * v

# Convert matrix equation into list of scalar equations
eqs = [Eq(expr, 0) for expr in steady_eq] + [Eq(a + b + c + d + e + f, 1)]

# Solve the system
solution = solve(eqs, (a, b, c, d, e, f), dict=True)

# Display solution
pprint(solution)
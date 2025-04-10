# Linear Algebra Final Project: Steady State & Mean First Passage Analysis

<p align="center">
  <img src="https://github.com/user-attachments/assets/e19b485d-710a-4028-88ce-ddcf716743dd" alt="Description of the image">
</p>



This repository contains my final project for my Linear Algebra course. The project focuses on analyzing a Markov chain represented by the above graph, and it solves for:

- **The Steady State Vector**
- **The Mean First Passage Time**

## Project Overview

The project uses symbolic computation with Python's [Sympy](https://www.sympy.org/) library to analyze the behavior of a Markov chain. The chain is modeled using a transition matrix derived from the provided graph (see `image.png`). Two primary tasks are accomplished:

1. **Steady State Analysis:**  
   `SteadyStateVector.py` sets up and solves the linear system \((P^T - I)v = 0\), along with the normalization condition \(a + b + c + d + e + f = 1\) to determine the long-term distribution of states.

2. **Mean First Passage Time:**  
   `MeanFirstTimePassing.py` defines and solves a system of equations representing the expected number of steps before the process reaches an absorbing state. The starting states are all nodes but the F node while the F node is the absorbing state. This script computes the mean first passage times for the states (other than the absorbing state).





## Requirements

- **Python 3.x**
- **Sympy Library**

To install the required dependency, run:

```bash
pip install sympy


"""Simple branching process utilities (placeholder for later import)."""
import numpy as np

def simulate_branching(p=0.5, max_steps=1000, seed=None):
    """Simulate a Galton–Watson branching process with binary offspring (0 or 2) with prob p.
    Returns the total population at each generation until extinction or max_steps.
    """
    rng = np.random.default_rng(seed)
    pop = [1]
    while pop[-1] > 0 and len(pop) < max_steps:
        # Each individual gives birth to 2 with prob p, else 0
        births = rng.binomial(n=pop[-1], p=p) * 2
        pop.append(int(births))
    return np.array(pop)

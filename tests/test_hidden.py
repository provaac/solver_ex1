import pytest
from solucio import resol

def generar_vectors(n: int = 300, seed: int = 42):
    """
    Genera 'n' vectors de longitud entre 1 i 7 (ambdós inclosos),
    amb enters entre -3000 i 3000 (ambdós inclosos).
    S'usa una llavor fixa per garantir reproductibilitat.
    """
    rng = random.Random(seed)
    casos = []
    for _ in range(n):
        L = rng.randint(1, 7)
        v = [rng.randint(-3000, 3000) for _ in range(L)]
        casos.append((v, sum(v)))
    return casos

# Combina els casos d'exemple amb els generats
CASOS = generar_vectors(n=300, seed=42)

@pytest.mark.parametrize("entrada,esperat", CASOS)
def test_sum_vectors(entrada, esperat):
    assert resol(entrada) == esperat

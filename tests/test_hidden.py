import pytest
from solucio import resol

@pytest.mark.parametrize(
    "entrada,esperat",
    [
        ([1, -2, 3], 4),
        ([1, -2, 4], 5),
        ([0, 0, 0], 0),
    ],
    ids=[
        "point 1 -2 3 -> 4",
        "point 1 -2 4 -> 5",
        "point 0 0 0 -> 0",
    ],
)
def test_sum_positius(entrada, esperat):
    obtingut = resol(entrada)
    # Log clar al workflow (gràcies a -s)
    print(f"[LOG] entrada={entrada} | esperat={esperat} | obtingut={obtingut}")
    assert obtingut == esperat, (
        f"Fallada: entrada={entrada}; esperat={esperat}; obtingut={obtingut}"
    )

import pytest
from solucio import resol

@pytest.mark.parametrize("entrada,esperat", [
    ([1, -2, 3], 2),
    ([0, 2, 0], 2),
    ([-5, -1], -6),
])
def test_sum_positius(entrada, esperat):
    assert resol(entrada) == esperat

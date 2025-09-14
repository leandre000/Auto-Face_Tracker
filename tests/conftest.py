import pytest

@pytest.fixture
def mock_frame():
    import numpy as np
    return np.zeros((480,640,3), dtype=np.uint8)

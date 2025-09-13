from src.tracker_utils import *

def test_calculate_center():
    assert calculate_center((10,10,20,20))==(20,20)

def test_calculate_offset():
    assert calculate_offset((100,100),(50,50))==50

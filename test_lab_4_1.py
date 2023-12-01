from solution import calcular_promedios


def test_promedios():
    inputs = [
        ("200 250 700 700", "400 400 400 400"),
        ("500 400", "300 400"),
        ("293", "799"),
        ("400 400 400 400 400 400 401", "400 400 400 400 400 400 400"),
        ("707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707", "707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707 707"),
    ]
    
    outputs = [
        2,
        0,
        0,
        6,
        0,
    ]
    
    
    for inp, out in zip(inputs, outputs):
        assert calcular_promedios(*inp) == out

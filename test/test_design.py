import mldoe


def test_design_init():
    assert(mldoe.TLdesign(16, [1, 2, 4, 8]).n_runs == 16)
    assert(mldoe.MLdesign(16, [[1, 2, 3]], [4, 8]).n_runs == 16)

def test_design_array():
    pass
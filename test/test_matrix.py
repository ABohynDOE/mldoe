import matrix
import numpy as np


def test_rmat():
    r_mat = matrix.rmat(4)
    (N, n) = r_mat.shape
    nbr_zeros = len(np.nonzero(r_mat)[0])
    assert ((16, 4) == (N, n))
    assert ((N * n / 2) == nbr_zeros)


def test_gmat():
    g_mat = matrix.gmat(4)
    (r, Nm1) = g_mat.shape
    assert ((4, 15) == (r, Nm1))


def test_bmat():
    b_mat = matrix.bmat(4)
    assert ((16, 15) == b_mat.shape)
    assert all(b_mat.sum(0) == 8)
    b_mat_not_bin = b_mat*2-1
    assert all(np.diag(np.matmul(b_mat_not_bin,b_mat_not_bin.T)//15) == 1)

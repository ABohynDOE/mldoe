# -*- coding: utf-8 -*-
"""
MPP
========
Module containing the numba-cached function for computing the MPP
"""

# Packages
import numpy as np
from numba import njit


# Helper functions
@njit(cache=True)
def dd(mat):
    """Distance distribution of an array.
    A vector of hamming weights (B) where B_i = j if there are j rows with i entries of 1.

    :param mat: 2-D binary array
    :type mat: numpy.array
    :return: 1-D vector of hamming weights
    :rtype: numpy.array
    """
    vec = np.zeros((mat.shape[1] + 1, 1))
    s = mat.sum(1)
    for i in range(mat.shape[0]):
        vec[s[i]] += 1
    return vec


@njit(cache=True)
def delCol(arr, num):
    """Delete-one-factor projection (DOP) of an array. Numba implementation of the np.delete function.
    Deletes the column, referred in num, of the array

    :param arr: 2-D array
    :type arr: numpy.array
    :param num: column to delete
    :type num: int
    :return: DOP of the input 2-D array
    :rtype: numpy.array
    """
    n_runs, n_cols = arr.shape
    arr_flat = arr.T.flatten()
    mask = np.zeros(n_runs * n_cols, dtype=np.int64) == 0
    mask[n_runs * num:n_runs * (num + 1)] = False
    new_arr = arr_flat[mask]
    return np.reshape(new_arr, (n_cols - 1, n_runs)).T


@njit(cache=True)
def kt_value(mat, q=1, t=10):
    """Moment projection pattern.
    Frequency vector of the t-th power Kt moment values.
    Values are computed on the projections of the input matrix into n-1, ..., n-q factors.
    For q=1 the MPP is a n-by-1 vector.
    For q=2 the MPP is a n-by-(n-1) matrix.

    :param mat: 2-D binary array
    :type mat: numpy.array
    :param q: level of projection, defaults to 1, maximum is 2
    :type q: int, optional
    :param t: power of the Kt moment, defaults to 10
    :type t: int, optional
    :return: tuple of the frequency vector for q=1 and the frequency matrix for q=2
    :rtype: tuple
    """
    n_cols = mat.shape[1]
    vec_q1 = np.zeros(n_cols)
    vec_q2 = np.zeros((n_cols, n_cols - 1))
    for i in range(n_cols):
        mat_dop = delCol(mat, i)
        mat_dop_dd = dd(mat_dop)
        kt_val = 0.0
        for idx, val in enumerate(mat_dop_dd):
            kt_val += (n_cols - 1 - idx) ** t * val[0]
        vec_q1[i] = kt_val

        if q == 2:
            for j in range(n_cols - 1):
                mat_dop2 = delCol(mat_dop, j)
                mat_dop2_dd = dd(mat_dop2)
                kt_val2 = 0.0
                for idx2, val2 in enumerate(mat_dop2_dd):
                    kt_val2 += (n_cols - 2 - idx2) ** t * val2[0]
                vec_q2[i, j] = kt_val2
    return vec_q1, vec_q2


class Kt:
    def __init__(self, arr, q=2, t=10):
        """
        Class for the t-th power moment projection pattern (MPP).
        Computation is based on the K_t(D) equation in section 3.3 of Xu (2009): Algorithmic Construction of Efficient
        Fractional Factorial Designs With Large Run Sizes.

        :param arr: design matrix
        :param q: depth of matrix projection
        :param t: power of the moment
        """
        self.arr = arr
        if q not in [1, 2]:
            raise ValueError('Unsupported value for q')
        if t < 5:
            raise ValueError('Value for t is too small')
        self.q = q
        self.t = t
        self.mpp_vecs_tuple = kt_value(self.arr, self.q, self.t)

    def ID(self):
        """
        Unique identifier for the MPP of the design.

        :return: a string corresponding to the unique identifier.
        """
        mpp_val_list = self.mpp_vecs_tuple[self.q - 1].flatten().tolist()
        return ''.join(map(str, map(int, sorted(mpp_val_list))))


if __name__ == "__main__":
    print('MPP class compiled and imported')

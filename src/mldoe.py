# -*-coding: utf-8-*-
"""
File defining the design (meta)class and the two classes:
- Two-level designs
- Mixed-level designs (four- and two-levels)
"""


class Design:
    def __init__(self, n_runs, cols_lst):
        self.n_runs = n_runs
        self.cols_lst = cols_lst
        pass

    def __repr__(self):
        return f'Design in {self.n_runs} runs with columns {self.cols_lst}'


class TLdesign(Design):
    def __init__(self, n_runs, cols_lst):
        super().__init__(n_runs, cols_lst)


class MLdesign(Design):
    def __init__(self, n_runs, pf_lst, cols_lst):
        super().__init__(n_runs, cols_lst)
        self.pf_lst = pf_lst

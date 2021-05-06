"""
Enumeration of all mixed-level designs (MLD) in 32 runs
"""

from src.mldoe.design import MLD
from src.mldoe.enumeration import nauty_reduction

# Create the basic design
N = 32
pf = [[1, 2, 3]]
cols = [4, 8, 16]
# parent_p1 = [MLD(32, pf, cols + [i]) for i in [6,12,13,28,30]]
root = [MLD(32, pf, cols + [i]) for i in range(1, N) if i not in [1, 2, 3, 4, 8, 16]]
parent_p1 = nauty_reduction(root)
candi_lst = []
for d in parent_p1:
    for i in range(1, N):
        if i in [1, 2, 4, 8, 16, 3]:
            continue
        else:
            candi_lst.append(MLD(d.n_runs, d.pf_lst, d.cols + [i]))

parent_p2 = nauty_reduction(candi_lst)
for d in parent_p2:
    print(d.cols[-2:])
    print([int(i) for i in d.wlp[3:]])

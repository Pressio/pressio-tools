#!/bin/python

python test_version.py

# test data structures
mpirun -np 4 python test_vec_n4.py
mpirun -np 4 python test_mv_n4.py

# yaml parsing
cd test_yaml_rw
python test_yaml.py
cd ..

# io array
cd test_io
mpirun -np 3 python test_binary_io_n3.py
mpirun -np 3 python test_ascii_io_n3.py
cd ..

# qr, svd, pseudoinv
mpirun -np 1 python test_qr_n1.py
mpirun -np 3 python test_qr_n3.py
mpirun -np 3 python test_qr_nonuniform_n3.py
mpirun -np 1 python test_svd_n1.py
mpirun -np 3 python test_svd_n3.py
mpirun -np 1 python test_pseudoinv_n1.py
mpirun -np 3 python test_pseudoinv_n3.py

# lev scores functions
mpirun -np 3 python test_levscores_n3.py

# sample mesh with lev scores
mpirun -np 3 python test_sm_levscores_n3.py

# galerkin projector functions
mpirun -np 3 python test_sm_galerkin_projector_n3.py

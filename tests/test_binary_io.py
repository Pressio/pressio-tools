
import pathlib, sys
file_path = pathlib.Path(__file__).parent.absolute()
sys.path.append(str(file_path) + "/../..")
sys.path.append(str(file_path) + "/../driver-scripts")

import numpy as np
from mpi4py import MPI
import pressiotools as pt
from array_io import *
import scipy.linalg as la

np.set_printoptions(linewidth=140,precision=14)
tol = 1e-14

def run():
  comm = MPI.COMM_WORLD
  rank = comm.Get_rank()
  assert(comm.Get_size() == 3)

  np.random.seed(223)

  # random distributed matrix by selecting
  # rows of a random matrix
  numCols = 4
  mat0 = np.asfortranarray(np.random.rand(15,numCols))
  vec0 = mat0[:,0] 

  myNumRows = 5
  myStartRow = rank*myNumRows
  mat = pt.MultiVector(mat0[myStartRow:myStartRow+myNumRows, :])
  vec = pt.Vector(vec0[myStartRow:myStartRow+myNumRows])
  
  if rank==0:
    print(mat0)
    print("---------\n")



  # test read
  
  # serial read
  if rank==0:
    mat0_gold = read_array("matrix.bin.gold",numCols)
    assert(np.all(np.abs(mat0_gold - mat0) < tol))

    vec0_gold = read_array("vector.bin.gold",1)
    assert(np.all(np.abs(vec0_gold - vec0) < tol))

  # distributed read
  mat_gold = read_array_distributed("matrix.bin.gold",numCols)
  assert(np.all(np.abs(mat_gold.data() - mat.data()) < tol))

  vec_gold = read_array_distributed("vector.bin.gold",1)
  assert(np.all(np.abs(vec_gold.data() - vec.data()) < tol))



  # test write (+ read)
  
  # serial write
  if rank==0:
    write_array(mat0,"matrix.bin")
    mat0_in = read_array("matrix.bin",numCols)
    assert(np.all(np.abs(mat0_in - mat0) < tol))

    write_array(vec0,"vector.bin")
    vec0_in = read_array("vector.bin",1)
    assert(np.all(np.abs(vec0_in - vec0) < tol))

  # distributed write
  write_array_distributed(mat,"matrix.bin")
  mat_in = read_array_distributed("matrix.bin",numCols)
  assert(np.all(np.abs(mat_in.data() - mat.data()) < tol))

  write_array_distributed(vec,"vector.bin")
  vec_in = read_array_distributed("vector.bin",1)
  assert(np.all(np.abs(vec_in.data() - vec.data()) < tol))



if __name__ == '__main__':
  run()

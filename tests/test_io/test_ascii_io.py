
import pathlib, sys
file_path = pathlib.Path(__file__).parent.absolute()
sys.path.append(str(file_path) + "/../../srcpy")

import numpy as np
import pressiotools as pt
from array_io import *
import scipy.linalg as la

np.set_printoptions(linewidth=140,precision=14)
tol = 1e-14

def run():
  np.random.seed(223)

  numCols = 4
  mat0 = np.asfortranarray(np.random.rand(15,numCols))
  vec0 = mat0[:,0]

  print(mat0)
  print("---------\n")

  mat0_gold = read_array("matrix.txt.gold",numCols,isBinary=False)
  assert(np.all(np.abs(mat0_gold - mat0) < tol))

  vec0_gold = read_array("vector.txt.gold",1,isBinary=False)
  assert(np.all(np.abs(vec0_gold - vec0) < tol))

  write_array(mat0,"matrix.txt",isBinary=False)
  mat0_in = read_array("matrix.txt",numCols,isBinary=False)
  assert(np.all(np.abs(mat0_in - mat0) < tol))

  write_array(vec0,"vector.txt",isBinary=False)
  vec0_in = read_array("vector.txt",1,isBinary=False)
  assert(np.all(np.abs(vec0_in - vec0) < tol))

if __name__ == '__main__':
  run()


import numpy as np
from pressiotools import linalg as ptla

np.set_printoptions(linewidth=140)

def svd_run(comm):
  rank = comm.Get_rank()
  np.random.seed(312367)
  A = np.asfortranarray(np.random.rand(10,4))

  U0,s0,VT0 = np.linalg.svd(A, full_matrices=False)
  print(s0)
  print(U0)
  print(VT0)
  print(np.dot(U0[:,0], U0[:,1]))
  print("----")

  A1   = ptla.MultiVector(A)
  svdO = ptla.Svd()
  svdO.computeThin(A1)
  U1 = svdO.viewLeftSingVectorsLocal()
  S1 = svdO.viewSingValues()
  VT1 = svdO.viewRightSingVectorsT()
  print(S1)
  print(U1)
  print(VT1)
  print(np.dot(U1[:,0], U1[:,1]))

  assert(np.allclose(np.abs(s0), np.abs(S1),  atol=1e-10))
  assert(np.allclose(np.abs(U0), np.abs(U1),  atol=1e-10))
  assert(np.allclose(np.abs(VT0),np.abs(VT1), atol=1e-10))

if __name__ == '__main__':
  from mpi4py import MPI
  comm = MPI.COMM_WORLD
  assert(comm.Get_size() == 1)
  svd_run(comm)

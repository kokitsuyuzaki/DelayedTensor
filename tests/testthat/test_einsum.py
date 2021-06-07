import numpy as np

arrA = np.random.rand(3)
arrB = np.random.rand(3)
arrC = np.random.rand(3,3)
arrD = np.random.rand(3,4)
arrE = np.random.rand(3,3,3)
arrF = np.random.rand(3,4,5)
arrG = np.random.rand(3,3,3,3)
arrH = np.random.rand(3,4,5,6)

# transpose
np.einsum('ij->ji', arrD)

np.einsum('ijk->ikj', arrF)
np.einsum('ijk->jik', arrF)
np.einsum('ijk->jki', arrF)
np.einsum('ijk->kij', arrF)
np.einsum('ijk->kji', arrF)

np.einsum('ijkl->ijlk', arrG)
np.einsum('ijkl->ikjl', arrG)
np.einsum('ijkl->iklj', arrG)
np.einsum('ijkl->iljk', arrG)
np.einsum('ijkl->iljk', arrG)
np.einsum('ijkl->jikl', arrG)
np.einsum('ijkl->jilk', arrG)
np.einsum('ijkl->jkil', arrG)
np.einsum('ijkl->jkli', arrG)
np.einsum('ijkl->jlik', arrG)
np.einsum('ijkl->jlki', arrG)
np.einsum('ijkl->kijl', arrG)
np.einsum('ijkl->kilj', arrG)
np.einsum('ijkl->kjil', arrG)
np.einsum('ijkl->kjli', arrG)
np.einsum('ijkl->klij', arrG)
np.einsum('ijkl->klji', arrG)
np.einsum('ijkl->lijk', arrG)
np.einsum('ijkl->likj', arrG)
np.einsum('ijkl->ljik', arrG)
np.einsum('ijkl->ljki', arrG)
np.einsum('ijkl->lkij', arrG)
np.einsum('ijkl->lkji', arrG)

# sum（including colSum, rowSum, modeSum）
np.einsum('i->', arrA)
np.einsum('ij->', arrD)
np.einsum('ij->i', arrD)
np.einsum('ij->j', arrD)
np.einsum('ijk->', arrF)
np.einsum('ijk->i', arrF)
np.einsum('ijk->j', arrF)
np.einsum('ijk->k', arrF)
np.einsum('ijk->ij', arrF)
np.einsum('ijk->jk', arrF)
np.einsum('ijk->ik', arrF)

np.einsum('ijkl->i', arrG)
np.einsum('ijkl->j', arrG)
np.einsum('ijkl->k', arrG)
np.einsum('ijkl->l', arrG)
np.einsum('ijkl->ij', arrG)
np.einsum('ijkl->ik', arrG)
np.einsum('ijkl->il', arrG)
np.einsum('ijkl->ji', arrG)
np.einsum('ijkl->jk', arrG)
np.einsum('ijkl->jl', arrG)
np.einsum('ijkl->ki', arrG)
np.einsum('ijkl->kj', arrG)
np.einsum('ijkl->kl', arrG)
np.einsum('ijkl->li', arrG)
np.einsum('ijkl->lj', arrG)
np.einsum('ijkl->lk', arrG)
np.einsum('ijkl->ijk', arrG)
np.einsum('ijkl->ijl', arrG)
np.einsum('ijkl->ikj', arrG)
np.einsum('ijkl->ikl', arrG)
np.einsum('ijkl->ilj', arrG)
np.einsum('ijkl->ilk', arrG)
np.einsum('ijkl->jik', arrG)
np.einsum('ijkl->jil', arrG)
np.einsum('ijkl->jki', arrG)
np.einsum('ijkl->jkl', arrG)
np.einsum('ijkl->jli', arrG)
np.einsum('ijkl->jlk', arrG)
np.einsum('ijkl->kij', arrG)
np.einsum('ijkl->kil', arrG)
np.einsum('ijkl->kji', arrG)
np.einsum('ijkl->kjl', arrG)
np.einsum('ijkl->kli', arrG)
np.einsum('ijkl->klj', arrG)
np.einsum('ijkl->lij', arrG)
np.einsum('ijkl->lik', arrG)
np.einsum('ijkl->lji', arrG)
np.einsum('ijkl->ljk', arrG)
np.einsum('ijkl->lki', arrG)
np.einsum('ijkl->lkj', arrG)

# multiply (diagonal elements)
np.einsum('ii->i', arrC)
np.einsum('iii->i', arrE)
np.einsum('iiii->i', arrG)

# sum + multiply（Hadamard Product）
np.einsum('i,i->i', arrA, arrA)
np.einsum('ij,ij->ij', arrD, arrD)
np.einsum('ijk,ijk->ijk', arrF, arrF)
np.einsum('ijkl,ijkl->ijkl', arrG, arrG)

# sum + multiply（Sum of squares, Frobenius norm if you take sqrt）
np.einsum('i,i->', arrA, arrA)
np.einsum('ij,ij->', arrD, arrD)
np.einsum('ijk,ijk->', arrF, arrF)
np.einsum('ijkl,ijkl->', arrG, arrG)

# multiply + sum + transpose
#（Include different ones, adamantine products, inner products,
# matrix products, and contraction products）
np.einsum('ij,jk->', arrC, arrD)
np.einsum('ij,jk->i', arrC, arrD)
np.einsum('ij,jk->j', arrC, arrD)
np.einsum('ij,jk->k', arrC, arrD)
np.einsum('ij,jk->ij', arrC, arrD)
np.einsum('ij,jk->ji', arrC, arrD)
np.einsum('ij,jk->jk', arrC, arrD)
np.einsum('ij,jk->kj', arrC, arrD)
np.einsum('ij,jk->ik', arrC, arrD)
np.einsum('ij,jk->ki', arrC, arrD)

np.einsum('ij,jk->ijk', arrC, arrD)
np.einsum('ij,jk->ikj', arrC, arrD)
np.einsum('ij,jk->jik', arrC, arrD)
np.einsum('ij,jk->jki', arrC, arrD)
np.einsum('ij,jk->kij', arrC, arrD)
np.einsum('ij,jk->kji', arrC, arrD)

np.einsum('ij,ijk->', arrC, arrE)
np.einsum('ij,ijk->i', arrC, arrE)
np.einsum('ij,ijk->j', arrC, arrE)
np.einsum('ij,ijk->k', arrC, arrE)
np.einsum('ij,ijk->ij', arrC, arrE)
np.einsum('ij,ijk->ji', arrC, arrE)
np.einsum('ij,ijk->jk', arrC, arrE)
np.einsum('ij,ijk->kj', arrC, arrE)
np.einsum('ij,ijk->ik', arrC, arrE)
np.einsum('ij,ijk->ki', arrC, arrE)
np.einsum('ij,ijk->ijk', arrC, arrE)

np.einsum('ijk,ijkl->', arrE, arrG)
np.einsum('ijk,ijkl->i', arrE, arrG)
np.einsum('ijk,ijkl->j', arrE, arrG)
np.einsum('ijk,ijkl->k', arrE, arrG)
np.einsum('ijk,ijkl->l', arrE, arrG)
np.einsum('ijk,ijkl->ij', arrE, arrG)
np.einsum('ijk,ijkl->ji', arrE, arrG)
np.einsum('ijk,ijkl->ik', arrE, arrG)
np.einsum('ijk,ijkl->ki', arrE, arrG)
np.einsum('ijk,ijkl->il', arrE, arrG)
np.einsum('ijk,ijkl->li', arrE, arrG)
np.einsum('ijk,ijkl->jk', arrE, arrG)
np.einsum('ijk,ijkl->kj', arrE, arrG)
np.einsum('ijk,ijkl->jl', arrE, arrG)
np.einsum('ijk,ijkl->lj', arrE, arrG)
np.einsum('ijk,ijkl->kl', arrE, arrG)
np.einsum('ijk,ijkl->lk', arrE, arrG)

np.einsum('ijk,ijkl->ijk', arrE, arrG)
np.einsum('ijk,ijkl->ikj', arrE, arrG)
np.einsum('ijk,ijkl->jik', arrE, arrG)
np.einsum('ijk,ijkl->jki', arrE, arrG)
np.einsum('ijk,ijkl->kij', arrE, arrG)
np.einsum('ijk,ijkl->kji', arrE, arrG)
np.einsum('ijk,ijkl->ijl', arrE, arrG)
np.einsum('ijk,ijkl->ilj', arrE, arrG)
np.einsum('ijk,ijkl->jil', arrE, arrG)
np.einsum('ijk,ijkl->jli', arrE, arrG)
np.einsum('ijk,ijkl->lij', arrE, arrG)
np.einsum('ijk,ijkl->lji', arrE, arrG)
np.einsum('ijk,ijkl->ikl', arrE, arrG)
np.einsum('ijk,ijkl->ilk', arrE, arrG)
np.einsum('ijk,ijkl->kil', arrE, arrG)
np.einsum('ijk,ijkl->kli', arrE, arrG)
np.einsum('ijk,ijkl->lik', arrE, arrG)
np.einsum('ijk,ijkl->lki', arrE, arrG)

np.einsum('ijk,ijkl->jkl', arrE, arrG)
np.einsum('ijk,ijkl->jlk', arrE, arrG)
np.einsum('ijk,ijkl->kjl', arrE, arrG)
np.einsum('ijk,ijkl->klj', arrE, arrG)
np.einsum('ijk,ijkl->ljk', arrE, arrG)
np.einsum('ijk,ijkl->lkj', arrE, arrG)


arr1 = np.array(
	[[1,3,5],
	[2,4,6]])
arr2 = np.array(
	[[20,16,12,8,4],
	[19,15,11,7,3],
	[18,14,10,6,2],
	[17,13,9,5,1]])
np.kron(arr1, arr2)
np.einsum('ij,kl->ikjl', arr1, arr2).reshape(8,15)

# Ref
# https://ajcr.net/Basic-guide-to-einsum/
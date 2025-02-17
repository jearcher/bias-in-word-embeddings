# -*- coding: utf-8 -*-
""" conceptor_fxns.py

This is code to calculate the conceptor, as well as boolean operators

"""
"""## Conceptor code"""

import numpy as np

def train_Conceptor(x, alpha = 1):
  print("starting...")
  #x = orig_embd.vectors
  print(x.shape)
  
  #Calculate the correlation matrix
  R = x.dot(x.T)/(x.shape[1])
  print("R calculated")
  
  #Calculate the conceptor matrix
  C = R @ (np.linalg.inv(R + alpha ** (-2) * np.eye(x.shape[0])))
  print("C calculated")
    
  return C, R

def NOT(C, out_mode = "simple"):
  """
  Compute NOT operation of conceptor.
  
  @param R: conceptor matrix
  @param out_mode: output mode ("simple"/"complete")
  
  @return not_C: NOT C
  @return U: eigen vectors of not_C
  @return S: eigen values of not_C
  """
  
  dim = C.shape[0]
  
  not_C = np.eye(dim) - C
  

  if out_mode == "complete":
    U, S, _ = np.linalg.svd(not_C)
    return not_C, U, S
  else:
    return not_C

def AND(C, B, out_mode = "simple", tol = 1e-14):
  """
  Compute AND Operation of two conceptor matrices
  
  @param C: a conceptor matrix
  @param B: another conceptor matrix
  @param out_mode: output mode ("simple"/"complete")
  @param tol: adjust parameter for almost zero
  
  @return C_and_B: C AND B
  @return U: eigen vectors of C_and_B
  @return S: eigen values of C_and_B
  """
  
  dim = C.shape[0]
  
  UC, SC, _ = np.linalg.svd(C)
  UB, SB, _ = np.linalg.svd(B)
  
  num_rank_C = np.sum((SC > tol).astype(float))
  num_rank_B = np.sum((SB > tol).astype(float))
  
  UC0 = UC[:, int(num_rank_C):]
  UB0 = UB[:, int(num_rank_B):]
  
  W, sigma, _ = np.linalg.svd(UC0.dot(UC0.T) + UB0.dot(UB0.T))
  num_rank_sigma = np.sum((sigma > tol).astype(float))
  Wgk = W[:, int(num_rank_sigma):]
  
  C_and_B = Wgk.dot(np.linalg.inv(Wgk.T.dot(np.linalg.pinv(C, tol) + np.linalg.pinv(B, tol) - np.eye(dim)).dot(Wgk))).dot(Wgk.T)
  

  if out_mode =="complete":
    U, S, _ = np.linalg.svd(C_and_B)
    return C_and_B, U, S
  else:
    return C_and_B

#Compute the conceptor matrix
def post_process_cn_matrix(x, alpha = 1):
  C, R = train_Conceptor(x, alpha=alpha)
  
  #Calculate the negation of the conceptor matrix
  negC = NOT(C)
  print("negC calculated")
  
  #Post-process the vocab matrix
  newX = (negC @ x).T
  print(newX.shape)
  return negC, newX, R
##################################
# For computing Conceptor
def process_cn_matrix(subspace, alpha = 2):
  """Returns the conceptor negation matrix
  Arguments
           subspace : n x d matrix of word vectors from a oarticular subspace
           alpha : Tunable parameter
  """
  # Compute the conceptor matrix
  C,_ = train_Conceptor(subspace, alpha)
  
  # Calculate the negation of the conceptor matrix
  negC = NOT(C)
  
  return negC

def apply_conceptor(x, C):
  """Returns the conceptored embeddings
  Arguments
           x : n x d matrix of all words to be conceptored
           C : d x d conceptor matrix
  """
  # Post-process the vocab matrix
  newX = (C @ x).T
  
  return newX



def load_all_vectors(embd, wikiWordsPath):
  """Loads all word vectors for all words in the list of words as a matrix
  Arguments
           embd : Dictonary of word-to-embedding for all words
           wikiWordsPath : URL to the path where all embeddings are stored
  Returns
          all_words_index : Dictonary of words to the row-number of the corresponding word in the matrix
          all_words_mat : Matrix of word vectors stored row-wise
  """
  all_words_index = {}
  all_words_mat = []
  with open(wikiWordsPath, "r+") as f_in:
    ind = 0
    for line in f_in:
      word = line.split(' ')[0]
      if word in embd:
        all_words_index[word] = ind
        all_words_mat.append(embd[word])
        ind = ind+1
        
  return all_words_index, all_words_mat

def load_subspace_vectors(embd, subspace_words):
  """Loads all word vectors for the particular subspace in the list of words as a matrix
  Arguments
           embd : Dictonary of word-to-embedding for all words
           subspace_words : List of words representing a particular subspace
  Returns
          subspace_embd_mat : Matrix of word vectors stored row-wise
  """
  subspace_embd_mat = []
  ind = 0
  for word in subspace_words:
    if word in embd:
      subspace_embd_mat.append(embd[word])
      ind = ind+1
      
  return subspace_embd_mat
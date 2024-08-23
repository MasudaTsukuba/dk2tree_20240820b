//
// Created by hugo on 19-2-19.
//

#ifndef DKTREE_PARAMETERS
#define DKTREE_PARAMETERS

/// The three main parameters for the TTree and LTree representation
static const unsigned int k = 2; // The `k` in the k2-tree
static const unsigned int BLOCK_SIZE =  k * k; // The number of bits in one block of the bit vector  //// 4
static const unsigned int B = 256 - BLOCK_SIZE; // The maximum size (in bits) of a leaf bitvector  //// 252

/// The maximum/minimum number of children/blocks an internal node/leaf node
/// is allowed to have, as per the rules of the B+tree
static const unsigned int nodeSizeMax = 3;
static const unsigned int nodeSizeMin = (nodeSizeMax + 1) / 2;  //// 2
static const unsigned int leafSizeMax = B / BLOCK_SIZE;  //// 63
static const unsigned int leafSizeMin = (leafSizeMax + 1) / 2;  //// 32

// template<unsigned long LENGTH = (B + BLOCK_SIZE + 63) / 64>
#define LENGTH 4
static const unsigned long length0 = (B + BLOCK_SIZE + 63) / 64;  ////  4

#endif // DKTREE_PARAMETERS

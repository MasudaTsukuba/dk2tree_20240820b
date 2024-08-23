%module dktree

%{
#include "DKTree.h"
#include <algorithm>
#include <vector>
#include <utility>

%}

/* SWIG typemap to ensure memory is freed for std::vector<std::pair<unsigned long, unsigned long>> */
// %typemap(freearg) std::vector<unsigned long>* {
//     delete $1;
// }

/* SWIG typemap to ensure that the vector's memory is properly allocated */
// %typemap(out) std::vector<unsigned long>* {
//     $result = SWIG_NewPointerObj(new std::vector<unsigned long>(*$1), $1_descriptor, SWIG_POINTER_OWN);
// }

%include <std_vector.i>
// %include <std_pair.i>

/* Tell SWIG to wrap the C++ standard vector for unsigned long */
namespace std {
    %template(ULongVector) std::vector<unsigned long>;
}
// namespace std {
//     %template(ULongPairVector) std::vector<std::pair<unsigned long, unsigned long>>;
// }

%include "DKTree.h"


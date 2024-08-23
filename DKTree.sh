## common commands
rm DKTree_wrap.cxx 
swig -python -c++ DKTree.i 

## for Ubuntu / g++
g++ -std=c++11 -c -fPIC DKTree.cpp TTree.cpp LTree.cpp BitVector.cpp DKTree_wrap.cxx $(python3-config --cflags) -I$(python3-config --includes)
g++ -shared DKTree.o TTree.o LTree.o BitVector.o DKTree_wrap.o -o _dktree.so $(python3-config --ldflags) -L$(python3-config --prefix)/lib -lpython3.10
python3 DKTreeMain.py


## for MacOS with clang and Pthon installed with brew install python@3.12, and not use anaconda/python3
clang++ -std=c++11 -shared -fPIC -arch arm64 DKTree.cpp TTree.cpp LTree.cpp BitVector.cpp DKTree_wrap.cxx -o _dktree.so -I/opt/homebrew/Cellar/python@3.12/3.12.5/Frameworks/Python.framework/Versions/3.12/include/python3.12 -L/opt/homebrew//Cellar/python@3.12/3.12.5/Frameworks/Python.framework/Versions/3.12/lib -lpython3.12
/opt/homebrew/bin/python3 DKTreeMain.py


## for MacOS with clang and Pthon installed with brew install python@3.12

clang++ -std=c++11 -shared -fPIC -arch arm64 DKTree.cpp TTree.cpp LTree.cpp BitVector.cpp DKTree_wrap.cxx -o _dktree.so -I$(python3-config --includes) -L$(python3-config --prefix)/lib -lpython3.12
python3 DKTreeMain.py

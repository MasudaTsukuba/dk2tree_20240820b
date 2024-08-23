## common commands
rm BitVector_wrap.cxx 
swig -python -c++ BitVector.i 

## for Ubuntu / g++
g++ -std=c++11 -shared -fPIC BitVector_wrap.cxx BitVector.cpp -o _bitvector.so -I$(python3-config --includes) -L$(python3-config --prefix)/lib -lpython3.10
python3 BitVectorMain.py


## for MacOS with clang and Pthon installed with brew install python@3.12, and not use anaconda/python3
clang++ -std=c++11 -shared BitVector_wrap.cxx BitVector.cpp -o _bitvector.so -I$(python3-config --includes) -L$(python3-config --prefix)/lib -lpython3.9
clang++ -std=c++11 -shared -fPIC -arch arm64 BitVector_wrap.cxx BitVector.cpp -o _bitvector.so -I/opt/homebrew/Cellar/python@3.12/3.12.5/Frameworks/Python.framework/Versions/3.12/include/python3.12 -L/opt/homebrew//Cellar/python@3.12/3.12.5/Frameworks/Python.framework/Versions/3.12/lib -lpython3.12
/opt/homebrew/bin/python3 BitVectorMain.py


## for MacOS with clang and Pthon installed with brew install python@3.12
clang++ -std=c++11 -shared -fPIC -arch arm64 BitVector_wrap.cxx BitVector.cpp -o _bitvector.so -I$(python3-config --includes) -L$(python3-config --prefix)/lib -lpython3.12
# clang++ -std=c++11 -shared -fPIC BitVector_wrap.cxx BitVector.cpp -o _bitvector.so -I$(python3-config --includes) -L$(python3-config --prefix)/lib -lpython3.12
python3 BitVectorMain.py

#include <iostream>
#include "BitVector.h"

using namespace std;

int main(){
    cout << "//// Hello 6\n\n\n\n";
    BitVector bv = BitVector();
    bv.hello();
    bv.set(0, true);
    bool ans = bv.get(0);
    cout << "//// " << ans << endl;
    ans = bv.get(1);
    cout << "//// " << ans << endl;
}
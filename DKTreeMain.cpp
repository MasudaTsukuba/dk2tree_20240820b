#include <iostream>
#include "DKTree.cpp"

int main(){
    std::cout << "//// DKTreeMain.cpp\n";
    unsigned long nrOfNodes = 10;
    DKTree* tree = new DKTree();
    for(int i = 0; i < nrOfNodes; i++){
        tree->insertEntry();
    }
    tree->addEdge(1, 2);
    tree->addEdge(2, 3);
    vector<unsigned long> allNodes(nrOfNodes);
    for(unsigned long i = 0; i < nrOfNodes; i++){
        allNodes[i] = i;
    }
    auto results = tree->reportAllEdges(allNodes, allNodes);
    tree->reportAllEdges2(allNodes, allNodes);
    return 0;
}
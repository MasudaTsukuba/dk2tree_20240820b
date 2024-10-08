#include <iostream>
#include <fstream>
using namespace std;

#include "DKTree.cpp"
#include "MakeGraphFromFile.cpp"
// #include "parameters.cpp"
#include "Parameters.h"  ////
#include "LargeGraphTest.cpp"
#include "Timer.h"


int main(int argc, char **argv) {

    if (argc != 6) {
        std::cout << "error: invalid number of arguments" << std::endl;
        std::cout << "expected: dk2tree inputfilename outputfilename posEdges negEdges numberOfNodes" << std::endl;
        return 1;
    }
    ofstream myFile;
    myFile.open(argv[2], ios::app);
    myFile << std::endl << "running " << argv[0] << std::endl;
    myFile << "number of nodes = " << atoi(argv[5]) << std::endl;
    myFile << "processing " << argv[1] << std::endl;

    auto tree = makeGraphFromFile(argv[1]);

    myFile << argv[1] << " has size: " << tree->memoryUsage() << std::endl;

    Timer timer;
    double average = 0;
    unsigned long counter = 0;

    ifstream negEdgesFile(argv[4]);
    unsigned long from, to;
    while (negEdgesFile >> from >> to) {
        timer.start();
        tree->addEdge(from, to);
        timer.stop();
        counter++;
        average += timer.read();
    }
    myFile << argv[1] << " average time to add an edge: " << average/counter << std::endl;

    average = 0;
    counter = 0;
    negEdgesFile.clear();
    negEdgesFile.seekg(0, ios::beg);
    while (negEdgesFile >> from >> to) {
        timer.start();
        if(from == 10){  //// debug
            int xxx = 0;  //// debug
        }  //// debug
        tree->removeEdge(from, to);
        timer.stop();
        counter++;
        average += timer.read();
    }
    myFile << argv[1] << " average time to delete an edge: " << average/counter << std::endl;


    average = 0;
    counter = 0;
    negEdgesFile.clear();
    negEdgesFile.seekg(0, ios::beg);
    while (negEdgesFile >> from >> to) {
        timer.start();
        tree->reportEdge(from, to);
        timer.stop();
        counter++;
        average += timer.read();
    }
    myFile << argv[1] << " average time to report 1 negative edge: " << average/counter << std::endl;
    negEdgesFile.close();

    average = 0;
    counter = 0;
    ifstream posEdgesFile(argv[3]);
    while (posEdgesFile >> from >> to) {
        timer.start();
        tree->reportEdge(from, to);
        timer.stop();
        counter++;
        average += timer.read();
    }
    myFile << argv[1] <<"average time to report 1 positive edge: " <<  average/counter << std::endl;

    posEdgesFile.close();


    unsigned long nrOfNodes = strtol(argv[5], nullptr, 10);
    vector<unsigned long> allNodes(nrOfNodes);
    for(unsigned long i = 0; i < nrOfNodes; i++){
        allNodes[i] = i;
    }
    average = 0;
    counter = 0;
    for(unsigned long i = 0; i < 10; i++){
        timer.start();
        tree->reportAllEdges(allNodes, allNodes);
        timer.stop();
        counter++;
        average += timer.read();
    }
    myFile << argv[1] <<" average time to report all edges: " <<  average/counter << std::endl;

    myFile.close();
    delete tree;

    return 0;
}



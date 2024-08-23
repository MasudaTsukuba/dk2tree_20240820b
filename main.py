"""
main.py << main.cpp
2024/7/30, T.Masuda
Amagasa Laboratory, University of Tsukuba
"""

# #include <iostream>
# #include <fstream>
# using namespace std;
#
# #include "DKTree.cpp"
# #include "MakeGraphFromFile.cpp"
# #include "parameters.cpp"
# #include "LargeGraphTest.cpp"
import sys
import time
from MakeGraphFromFile import make_graph_from_file
#
# int main(int argc, char **argv) {


def main():
    # if (argc != 6) {
    if len(sys.argv) != 6:
        # std::cout << "error: invalid number of arguments" << std::endl;
        print("error: invalid number of arguments")
#       std::cout << "expected: dk2tree inputfilename outputfilename posEdges negEdges numberOfNodes" << std::endl;
        print("expected: dk2tree inputfilename outputfilename posEdges negEdges numberOfNodes")
#       return 1;
        return 1
#   }
#   ofstream myFile;
#   myFile.open(argv[2], ios::app);
    with open(sys.argv[2], 'w') as myFile:
        # myFile << std::endl << "running " << argv[0] << std::endl;
        myFile.write(f"running {sys.argv[0]}\n")
#       myFile << "number of nodes = " << atoi(argv[5]) << std::endl;
        myFile.write(f"number of nodes = {sys.argv[5]}\n")
#       myFile << "processing " << argv[1] << std::endl;
        myFile.write(f"processing {sys.argv[1]}\n")
#       auto tree = makeGraphFromFile(argv[1]);
        tree = make_graph_from_file(sys.argv[1])
#
#       myFile << argv[1] << " has size: " << tree->memoryUsage() << std::endl;
        # myFile.write(f"{sys.argv[1]} has size: {tree.memory_usage()}\n")
        myFile.write(f"{sys.argv[1]} has size: {tree.memoryUsage()}\n")

        #       Timer timer;
        average = 0
        #       double average = 0;
        counter = 0
        #       unsigned long counter = 0;

        with open(sys.argv[4], 'r') as negEdgesFile:
            #       ifstream negEdgesFile(argv[4]);
            # unsigned long from, to;
            for line in negEdgesFile:
                # while (negEdgesFile >> from >> to) {
                # values = line.split(' ')
                values = line.split()  # 2024/8/20
                from_ = int(values[0])
                to_ = int(values[1])
                #       timer.start();
                start_time = time.time()
                #       tree->addEdge(from, to);
                # tree.add_edge(from_, to_)
                tree.addEdge(from_, to_)
                #       timer.stop();
                end_time = time.time()
                #       counter++;
                counter += 1
                #       average += timer.read();
                average += end_time - start_time
                #       }
        myFile.write(f"{sys.argv[1]} average time to add an edge:\t\t\t\t{average/counter}\n")
        #       myFile << argv[1] << " average time to add an edge: " << average/counter << std::endl;

        average = 0
        #       average = 0;
        counter = 0
        #       counter = 0;
        #       negEdgesFile.clear();
        #       negEdgesFile.seekg(0, ios::beg);
        with open(sys.argv[4], 'r') as negEdgesFile:
            # while (negEdgesFile >> from >> to) {
            for line in negEdgesFile:
                # values = line.split(' ')
                values = line.split()  # 2024/8/20
                from_ = int(values[0])
                to_ = int(values[1])
                #               timer.start();
                start_time = time.time()
                #               tree->removeEdge(from, to);
                tree.removeEdge(from_, to_)
                #               timer.stop();
                end_time = time.time()
                #               counter++;
                counter += 1
                #               average += timer.read();
                average += end_time - start_time
                #       }
        myFile.write(f"{sys.argv[1]} average time to delete an edge:\t\t\t{average/counter}\n")
        #       myFile << argv[1] << " average time to delete an edge: " << average/counter << std::endl;

        average = 0
        #       average = 0;
        counter = 0
        #       counter = 0;
        #       negEdgesFile.clear();
        #       negEdgesFile.seekg(0, ios::beg);
        with open(sys.argv[4], 'r') as negEdgesFile:
            #           while (negEdgesFile >> from >> to) {
            for line in negEdgesFile:
                # values = line.split(' ')
                values = line.split()  # 2024/8/20
                from_ = int(values[0])
                to_ = int(values[1])
                #               timer.start();
                start_time = time.time()
                #               tree->reportEdge(from, to);
                tree.reportEdge(from_, to_)
                #               timer.stop();
                end_time = time.time()
                #               counter++;
                counter += 1
                #               average += timer.read();
                average += end_time - start_time
                #           }
        myFile.write(f"{sys.argv[1]} average time to report 1 negative edge:\t{average/counter}\n")
        #       myFile << argv[1] << " average time to report 1 negative edge: " << average/counter << std::endl;
        #       negEdgesFile.close();

        average = 0
        #       average = 0;
        counter = 0
        #       counter = 0;
        with open(sys.argv[3], 'r') as posEdgesFile:
            #       ifstream posEdgesFile(argv[3]);
            for line in posEdgesFile:
                #           while (posEdgesFile >> from >> to) {
                # values = line.split(' ')
                values = line.split()  # 2024/8/20
                from_ = int(values[0])
                to_ = int(values[1])
                #               timer.start();
                start_time = time.time()
                #               tree->reportEdge(from, to);
                tree.reportEdge(from_, to_)
                #               timer.stop();
                end_time = time.time()
                #               counter++;
                counter += 1
                #               average += timer.read();
                average += end_time - start_time
                #           }
        myFile.write(f"{sys.argv[1]} average time to report 1 positive edge:\t{average / counter}\n")
        #       myFile << argv[1] <<"average time to report 1 positive edge: " <<  average/counter << std::endl;
        #       posEdgesFile.close();

        nrOfNodes = int(sys.argv[5])
        #       unsigned long nrOfNodes = strtol(argv[5], nullptr, 10);
        allNodes = [i for i in range(nrOfNodes)]
        #       vector<unsigned long> allNodes(nrOfNodes);
        #       for(unsigned long i = 0; i < nrOfNodes; i++){
        #           allNodes[i] = i;
        #       }
        average = 0
        #       average = 0;
        counter = 0
        #       counter = 0;
        #       for(unsigned long i = 0; i < 10; i++){
        for i in range(10):
            #           timer.start();
            start_time = time.time()
            #           tree->reportAllEdges(allNodes, allNodes);
            findings = tree.reportAllEdges(allNodes, allNodes)
        #     print(findings)  # debug
            #           timer.stop();
            end_time = time.time()
            #           counter++;
            counter += 1
            #           average += timer.read();
            average += end_time - start_time
            #       }
        myFile.write(f"{sys.argv[1]} average time to report all edge:\t\t\t{average / counter}\n")
        #       myFile << argv[1] <<" average time to report all edges: " <<  average/counter << std::endl;

        #       myFile.close();
        #       delete tree;

        #       return 0;
        #   }
        pass


if __name__ == '__main__':
    main()

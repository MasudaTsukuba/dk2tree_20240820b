"""
makeGraphFromFile.py << makeGraphFromFile.cpp
2024/7/30, T. Masuda
Amagasa Laboratory, University of Tsukuba
"""
# //
# // Created by hugo on 01/03/19.
# //
#
# #include <fstream>
# #include "DKTree.h"
#
# using std::string;
# using std::ifstream;
# using std::cin;
# from DKTree import DKTree
import dktree  # 2024/8/20

#
# /**
#  * Reads an edge-list file with the given name and loads a DKTree from it
#  * @param name the location of the file to load
#  * @return a DKTree containing exactly the edges specified by the file
#  */
# DKTree *makeGraphFromFile(const string &name, bool verbose = false) {


def make_graph_from_file(name, verbose=False):
#     tree = DKTree()
    tree = dktree.DKTree()
#   ifstream file(name);
    with open(name, 'r') as file:
        # auto tree = new DKTree();
        # unsigned long size = 0;
        size = 0
#       unsigned long n = 1;
        n = 1
#       tree->insertEntry();
        # tree.insert_entry()
        tree.insertEntry()
#       // Read the two integer from each line, as long as that is possible
#       unsigned long a, b;
#       while (file >> a >> b) {
        for line in file:
        #     values = line.split(' ')
            values = line.split()  # 2024/8/20
            a = int(values[0])
            b = int(values[1])
    #         if (verbose && n % 10000 == 0) {
            if verbose and n % 10000 == 0:
                # std::cout << n << '\r';
                print(n)
    #           std::cout.flush();
    #       }
    #       n++;
            n += 1
            # print(n)  #
    #       // Make sure that the tree has nodes for a and b, so that we can connect
    #       // them properly
            while a >= size or b >= size:
                #       while (a >= size || b >= size) {
                # tree->insertEntry();
                # tree.insert_entry()
                tree.insertEntry()
                #           size++;
                size += 1
                #       }
            pass
            #       // Then add the edge
            #       tree->addEdge(a, b);
        #     tree.add_edge(a, b)
            tree.addEdge(a, b)
#   }
#   file.close();
#   return tree;
    return tree
# }

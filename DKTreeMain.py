"""
DKTreeMain.py
2024/8/20, T. Masuda
"""
import dktree

tree = dktree.DKTree()
number_of_nodes = 10
for i in range(number_of_nodes+1):
    tree.insertEntry()
tree.addEdge(1, 2)
tree.addEdge(2, 3)
all_nodes = [i for i in range(1, number_of_nodes + 1)]
print(all_nodes)
# tree.reportAllEdges2(all_nodes, all_nodes)

result = tree.reportEdge(1, 2)
print(result)
result = tree.reportEdge(2, 1)
print(result)
# findings = tree.reportAllEdges2(all_nodes, all_nodes)
# print(tree.findings_index)
# for i in range(0, tree.findings_index, 2):
#     print(findings.get[i], findings.get[i+1])

# findings_global = tree.findings_global
# xxx = tree.get_findings_global()
# print(xxx)
# print(findings_global)

findings = tree.reportAllEdges(all_nodes, all_nodes)
print(findings)
# xxx = tree.get_findings_global()
# print(xxx)


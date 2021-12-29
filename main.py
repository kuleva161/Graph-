from Graph import Graph

if __name__ == '__main__':
    print("Вариант 45")

    graph = Graph()
    graph.addVer("A", ["B", "C"])
    graph.addVer("B", ["D", "E"])
    graph.addVer("C", ["D"])
    graph.addVer("D", ["E", "F"])
    graph.addVer("E", ["G", "H"])
    graph.addVer("F", ["H"])
    graph.addVer("G", [])
    graph.addVer("H", [])

    graph.buildGraph()
    graph.printMatrix()
    print()
    graph.printPaths()
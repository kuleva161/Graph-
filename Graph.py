class Graph:
    __graph = {}
    matrix = {}

    # добавлеение данных в граф
    def addVer(self, nameVer: str, neighbours: []):
        self.__graph[nameVer] = neighbours

    # создание графа (заполнение матрицы смежности)
    def buildGraph(self):
        vertexes = []
        # записываем все имеющиеся вершины
        for ver in self.__graph:
            vertexes.append(ver)

        # формируем матрицу смежности
        for ver in self.__graph:
            self.matrix[ver] = []
            for vertex in vertexes:
                if ver == vertex or vertex in self.__graph[ver]:
                    self.matrix[ver].append(1)
                else:
                    self.matrix[ver].append(0)

    # вывод в терминал матрицы смежности
    def printMatrix(self):
        print("#", end="  ")
        for item in self.__graph.keys():
            print(item, end="  ")

        print()
        for key in self.matrix.keys():
            print(key, end="  ")
            for value in self.matrix[key]:
                print(value, end="  ")
            print()

    # вывод всех маршрутов в графе
    def printPaths(self):
        lastVertex = []  # список конечных вершин
        paths = []  # список всех путей
        vertex = []  # список всех вершин графа
        for item in self.__graph.keys():
            vertex.append(item)

        # добавление путей от стартовой вершины
        for i in range(1, len(self.matrix[vertex[0]])):
            if self.matrix[vertex[0]][i] != 0:
                path = [vertex[0], self.findKey(i)]
                paths.append(path)
        vertex.remove(vertex[0])

        # проверка всех "непроверенных" вершин
        while len(vertex) > 0:
            countNeighbors = -1  # кол-во соседей у вершины
            for i in self.matrix[vertex[0]]:
                if i != 0:
                    countNeighbors += 1

            # варинат, если у вершины нет соседей (конечная)
            if countNeighbors == 0:
                lastVertex.append(vertex[0])
                vertex.remove(vertex[0])
                continue

            # вариант, если есть только 1 продолжение маршрута
            if countNeighbors == 1:
                for i in range(len(self.matrix[vertex[0]])):
                    if self.matrix[vertex[0]][i] != 0 and self.findKey(i) != vertex[0]:
                        # проверяем все пути, и добавляем вершину в нужный
                        for path in paths:
                            if path[len(path) - 1] == vertex[0]:
                                path.append(self.findKey(i))
                vertex.remove(vertex[0])
                continue

            # вариант, когда есть несколько вариантов маршрута
            else:
                pathsToCopy = []  # пути, которые надо дополнить
                for path in paths:
                    if path[len(path) - 1] == vertex[0]:
                        pathsToCopy.append(path[:])

                # "размножаем" маршруты, которые будем дополнять
                for i in range(1, countNeighbors):
                    for path in pathsToCopy:
                        paths.append(path[:])

                # вносим вершины в нужные пути
                for i in range(len(self.matrix[vertex[0]])):
                    if self.matrix[vertex[0]][i] != 0 and self.findKey(i) != vertex[0]:
                        # проверяем все пути, и добавляем вершину в нужный
                        # findKey(i) = необходимая вершина, продолжающая маршрут
                        for item1 in pathsToCopy:
                            itemNew = item1[:]
                            itemNew.append(self.findKey(i))
                            paths.append(itemNew)

                vertex.remove(vertex[0])
                continue

        # вывод полученного результата
        print("Все пути ациклического графа")
        for path in paths:
            if path[len(path)-1] not in lastVertex:
                continue
            for ver in path:
                print(ver, end=" ")
            print()

    # поиск нужной вершины по ключу
    def findKey(self, count: int):
        x = 0
        for i in self.matrix.keys():
            if x == count:
                return i
            x += 1

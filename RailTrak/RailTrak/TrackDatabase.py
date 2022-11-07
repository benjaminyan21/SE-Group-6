class TrackDB:

    def __init__(self):
        self.station_graph = [[]]
        self.station_dict = {}

    def addStation(self, name):
        index = len(self.station_graph)
        self.stationdict[index] = name
        for i in range(index):
            self.station_graph[i] = self.station_graph[i] + 0
        self.station_graph[index] = [0] * (index + 1)

    def addEdge(self, station1, station2, weight):
        index = (self.station_dict[station1],  self.station_dict[station2])
        self.station_graph[index[0]][index[1]] = weight
        self.station_graph[index[1]][index[0]] = weight

    def shortestPath( itenerary ):
        # Implement Dijkstra's algorithm to find shortest path






from cgi import test
import Path

# The track database keeps track of all of the stations and how they are connected. The track data base will also calculate shortest paths as well.
class TrackDB:
    
    # Initializes the track adjacency matrix and a dictionary for the station names
    def __init__(self):
        self.station_graph = []
        self.station_dict = {}

    # Expand the adjacency matrix and dictionary to include a new station
    def addStation(self, name):
        index = len(self.station_graph)
        self.station_dict[name] = index
        for i in range(index):
            self.station_graph[i] = self.station_graph[i] + [0]
        self.station_graph = self.station_graph + [[0] * (index + 1)]

    # Adds a weight between two stations
    def addEdge(self, station1, station2, weight):
        index = (self.station_dict[station1],  self.station_dict[station2])
        self.station_graph[index[0]][index[1]] = weight
        self.station_graph[index[1]][index[0]] = weight

    # Returns a Path of stations corresponding to the shortest path
    # Itenerary is a list of strings representing the stops the train will make
    def shortestPath( itenerary ):
        # Implement Dijkstra's algorithm to find shortest path
        test_path = Path()
        test_path.eta = 1.5
        test_path.route = ['Dallas', 'Austin', 'Houstin']
        return 0

db = TrackDB()
db.addStation('San Francisco')
db.addStation('Dallas')
db.addStation('New York City')
db.addEdge('Dallas', 'New York City', 0.5)


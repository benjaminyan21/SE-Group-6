from asyncio.windows_events import NULL
from cgi import test
import Path as p

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
    def shortestPath(self,  itenerary ):
        # Implement Dijkstra's algorithm to find shortest path
        path = p.Path()

        for i in range(len(itenerary)-1):
            subpath = self._shortestPath(itenerary[i], itenerary[i+1])
            if subpath[0] == float('inf') or subpath[0] < 0:
                return p.Path(subpath[0], subpath[1])
            path.eta += subpath[0]
            path.route = path.route + subpath[1][0 : len(subpath[1])-1]

        path.route += [itenerary[len(itenerary)-1]]

        return path

    def _shortestPath(self, start, end):
        start_i = self.station_dict[start]
        end_i = self.station_dict[end]

        stations = {}
        p_queue =[]
        for name in self.station_dict.keys():
            index = self.station_dict[name]
            stations[index] = [float('inf'), index, name, [name]]
            p_queue += [stations[index]]
        stations[start_i][0] = 0

        while p_queue:
            p_queue.sort()
            current = p_queue[0]
            if current[1] == end_i:
                return (current[0], current[3])

            p_queue = p_queue[1 : len(p_queue)]
            i = current[1]

            for j in range(len(self.station_graph)):
                weight = self.station_graph[i][j]
                if weight > 0 and stations[j][0] > current[0]+weight:
                    stations[j][0] = current[0] + weight
                    stations[j][3] = current[3] + [stations[j][2]]

        return (-1, [])
        
    def initialize(self):
        self.addStation('New York City')
        self.addStation('Buffalo')
        self.addStation('Albany')
        self.addStation('New Haven')
        self.addStation('Philadelphia')
        self.addStation('Clevland')
        self.addStation('Pitsburg')
        self.addStation('Chicago')
        self.addStation('Boston')
        self.addStation('Washington DC')

        
        self.addEdge('Chicago', 'Buffalo', 4)
        self.addEdge('Buffalo', 'Albany', 1)
        self.addEdge('Albany', 'Boston', 1)
        self.addEdge('Albany', 'New York City', 1)
        self.addEdge('Boston', 'New Haven', .5)
        self.addEdge('New Haven', 'New York City', 1)
        self.addEdge('New York City', 'Philadelphia', 1)
        self.addEdge('Philadelphia', 'Washington DC', 1)
        self.addEdge('Washington DC', 'Pitsburg', 2)
        self.addEdge('Pitsburg', 'Clevland', 1)
        self.addEdge('Clevland', 'Chicago', 4)


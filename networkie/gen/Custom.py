import networkx as nx

class LoadFromFile(object):
    def __init__(self):
        """
        Initiate variables for the class.
        """
        self.g = nx.Graph()

        pass

    def from_edgelist(self, path):
        '''
        Read graph in edgelist txt format from `path`.

        Parameters
        ----------
        path: `str`
            The path to the edgelist text file. Note that the node index must start from 0.

        Returns
        -------
        G: `NetworkX graph`
            The parsed graph.

        '''

        edgelist = []
        with open(path, 'r') as f:
            for line in f:
                node_pair = line.replace('\n', '').split(' ')
                edgelist += [node_pair]
        self.g.add_edges_from(edgelist)
        print(nx.info(self.g))
        print('Edgelist txt data successfully loaded into a networkx Graph!')
        return self.g

    def from_in_class_network(self, in_class_network):  # This is Prob. 3-a.
        '''
        Write your code documentation here.  # This is Prob. 4-a.
        這個function將接受結構和in-class_network相同的資料，先將讀進來的檔案，用'\t'切割後存在data中，
        取 ID 去和 IDs-of-acquaintances 中的每一個node配對後存在edgelist中，最後用 add_edges_from 存，
        如果 IDs-of-acquaintances 是空字串，就用add_node 存 ID。

        '''
        data = []
        edgelist = []

        with open(in_class_network, 'r') as f:
            for line in f:
                cur = line.replace('\n', '').split('\t')
                data += [cur]
        for i in range(len(data)):
            data[i][1] = data[i][1].split(',')

        for i in range(1, len(data)):
            if data[i][1] != [' ']:
                for j in range(len(data[i][1])):
                    edgelist += [[data[i][0], data[i][1][j]]]
            else:
                self.g.add_node(data[i][0])

        self.g.add_edges_from(edgelist)
        return self.g

# This is Prob. 3-b.
g = LoadFromFile()
G = g.from_in_class_network('In-class_network.txt')

b = nx.info(G).split('\n')
print('3-b', b[2], b[3], b[4], sep = '\n') # This is Prob. 3-b-(i, ii, iii).

print('average path length:', len(list(G.edges()))/len(list(G.nodes()))) # This is Prob. 3-b-(iv).

graphs = max(nx.connected_component_subgraphs(G), key=len)
print('The size of the largest connected component:',graphs.size()) # This is Prob. 3-b-(v).


# This is Prob. 3-c.
num_node = len(list(G.nodes()))
max_edge = num_node * (num_node - 1) / 2
print('\n3-c\ne/e_max:', len(list(G.edges())) / max_edge)


# This is Prob. 3-e.
edgelist = {}
node = list(G.nodes())
for i in node:
    if len(G.edges(i)) != 0:
        cur = []
        for j in list(G.edges(i)):
            cur.append(j[1])
        edgelist[i] = cur
tri = []
for i in list(edgelist.keys()):
    for j in edgelist[i]:
        for k in edgelist[j]:
            if i in edgelist[k] and sorted([i, j, k]) not in tri:
                tri.append(sorted([i, j, k]))      
print('\n3-e\nthe total number of triangles in the network:', len(tri))
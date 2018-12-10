graph = {}

graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['fin'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}

# costs
infinity = float('inf')

costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

# parent node
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = []


def find_lowest_cost_node(costs_dict):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs_dict:
        cost = costs_dict[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def dijkstra(G):
    node = find_lowest_cost_node(costs)  # find the lowest cost node (from start)
    while node is not None:
        cost = costs[node]
        neighbors = G[node]  # get lowest cost nodes's neighbors
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]  # compare the and update the cost from start to neighbors
            if costs[n] > new_cost:
                costs[n] = new_cost  # if cost from start to neighbor is lower than existing cost, then update the cost
                parents[n] = node  # update the parent node for path that has lowest cost to the neighbor
        processed.append(node)
        node = find_lowest_cost_node(costs)


if __name__ == '__main__':
    dijkstra(graph)
    print(costs)
    print(processed)
    print(parents)

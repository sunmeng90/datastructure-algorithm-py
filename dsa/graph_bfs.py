from pprint import pprint
from collections import deque

#  use hash table to store graph: key for each node, value is a list of adjacent nodes
#  use queue to store the nodes to match against
#  use a list to store all the nodes that already checked (avoid infinite loop)
#  1. begin with the start node(current node)
#  2. enqueue all the nodes that are adjacent with current node
#  3. pop first node from queue and compare it with target node
#  4. if matched then return
#  5. if not append current node the the list of searched nodes
#  6. goto step 2


def graph_bfs(start, end, g):
    search_queue = deque()
    search_queue += g[start]
    searched = []
    step = 0
    while search_queue:
        person = search_queue.popleft()
        print("-" * step + "> %s" % person)
        step += 1
        if person not in searched:  # skip searched people to avoid infinite loop
            if person == end:
                print("found %s" % person)
                return True
            else:
                searched.append(person)
                search_queue += g[person]
    return False


graph = {"you": ["alice", "bob", "claire"],
         "bob": ["anuj", "peggy"],
         "alice": ["peggy"],
         "claire": ["thom", "jonny"],
         "anuj": [],
         "peggy": [],
         "thom": [],
         "jonny": []}

if __name__ == '__main__':
    pprint(graph)
    graph_bfs("you", "thom", graph)
    print("-" * 10)
    graph_bfs("you", "anuj", graph)
    print("-" * 10)
    graph_bfs("you", "jonny", graph)
    print("-" * 10)
    graph_bfs("you", "", graph)


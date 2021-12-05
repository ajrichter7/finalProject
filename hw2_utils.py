import time
from graphspace_python.api.client import GraphSpace
from graphspace_python.graphs.classes.gsgraph import GSGraph

## connect to the GraphSpace client.
## Prompts the user for their email and password.
def get_connection():
    email = input('Enter Email:')
    password = input('Enter Password:')
    gs = GraphSpace(email,password)
    print('GraphSpace successfully connected.')
    return gs

## Post the graph and share it with the BIO331F21 group
## gs: GraphSpace object
## G: GSGraph object (the graph you want to post)
## graph_name: the name of the graph
def post(gs,G,graph_name):
    group = 'BIO331F21'
    try: ## If graph does not yet exist...
        graph = gs.post_graph(G)
        gs.share_graph(graph=graph,group_name=group)
    except: ## Otherwise, graph exists.
        print('Graph exists! Removing and re-posting (takes a few secs)...')
        graph = gs.get_graph(graph_name=graph_name)
        gs.delete_graph(graph=graph)
        time.sleep(1) # pause for 1 second
        graph = gs.post_graph(G)
        gs.share_graph(graph=graph,group_name=group)
    print('Graph successfully posted to %s group.' % (group))
    groupid = gs.get_group(group_name=group).id
    print('Visit http://graphspace.org/groups/%d to view.' % (groupid))
    return

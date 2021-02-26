# Dijkstra's Algorithm implementation -By Balaji ChandraBose
# Please inform me about the loopholes or implementation errors
# @ thebrokencoder@gmail.com ,Thank You 

graph = {
"A" :{"B":6,"C":3},
"B" :{"C":4 ,"D":1 ,"A":6},
"C" :{"D":5,"B":4 ,"A" :3},
"D" :{"C":5,"B":1},
}
# bidirectional graph is used in this implementation

dist ={
    "A": 0,
    "B": 9999999,
    "C": 9999999,
    "D": 9999999,
}

# I have assumed 9999999 as infinity

visited_list =[]
unvisited=[]

#this function is to initiate dist grpah with infinity or 999
def graph_relaxer(graph,source):
    for k in graph:
        if k == source:
            dist[k]= 0
        else:
            dist[k]=999
    

#decides which node should be visited next 
def decider(queue):
    for key in list(queue):
        if key in visited_list:
            queue.pop(key)
        
    new = dict(sorted(queue.items(), key=lambda item: item[1]))
    return list(new)
    
#this function is to formulate the cost
#and assign the minimum cost to
#the neighbours of current node
def pacifier(q,s):
    for i in list(q.copy()):
        if i not in visited_list:
            if dist[i] > q[i] + dist[s]:
                dist[i] = q[i] + dist[s]
            if i not in unvisited:
                unvisited.append(i)
            
        
        else:
            continue
    q.pop(i)
            

#this function retrieves the neighbours of a given node
#and maintains the other function calls
def queuemaker(graph,s):
    neighbours={}
    temp ={}
    for i,j in graph.items():
        if i==s:
            if len(j) == 0:
                print("reached end")
                return
            for node in j:
                neighbours[node]= j[node] 
                print(node+ ':', j[node])

    


    print("neighbours of",s,"=",neighbours)
    temp = neighbours.copy()
    while len(temp) > 0:
        pacifier(temp,s)
    visited_list.append(s)

    newnode=decider(neighbours)
    if len(newnode)!=0:
        nextnode=newnode.pop(0)
    else:
        return
    print("Selected=",nextnode)
    
    print("Visited=",visited_list)
    print("unVisited=",unvisited)
    print("dist=",dist)

    if nextnode not in visited_list:
        dijsktras(graph,nextnode)

        

#main function ,could have been the queuemaker itself     
def dijsktras(graph,source):
    print("Current=>",source)
    if source in unvisited:
        unvisited.remove(source)
    queuemaker(graph,source)
    
    
#running function ,just to check all the Nodes 
def runAlgo():
    print("Initial graph =",dist)
    root=str(input("Enter a root node from where to start=\t"))
    root= root.upper()
    graph_relaxer(graph,root)
    dijsktras(graph,root)
    print("Unvisited=",unvisited)
    print("updated graph after exploring all vertices=",dist)
    try :
        option = int(input("Enter 1. to Retry \t 2. to Exit \t="))
        if option == 1:
            unvisited.clear()
            visited_list.clear()
            runAlgo()
        elif option == 2:
            exit
    except ValueError :
        print("Please Select a valid option")

runAlgo()

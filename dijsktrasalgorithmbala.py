graph = {
"A" :{"B":4,"C":3},
"B" :{"C":4 },
"C" :{"D":4},
"D" :{"E":2,"F":5},
"E" :{"F":2},
"F" :{}

}

dist ={
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "E": 0,
    "F": 0
}

visited_list =[]
unvisited=[]
root="A"
def decider(queue):
    new = dict(sorted(queue.items(), key=lambda item: item[1]))
    return list(new)
    
def repeatChecker(l,l2):
    for n in l:
        if n not in l2:
            l.remove(n)
        else:
            return

def pacifier(q,nextnode,s):
    if s!=root:
        if dist[nextnode] > q[nextnode] + dist[s]:
            dist[nextnode] = q[nextnode] + q[s]
        elif dist[nextnode]==0:
            dist[nextnode]=q[nextnode]+dist[s]
    else:
        dist[nextnode] = q[nextnode]

def leftover():
    for i in unvisited:
        print("popped =",i)
        unvisited.remove(i)
        if i in graph:
            x=graph[i]
            for n in x:
                if n in visited_list:
                    dist[i] = graph[root][i]
    
def queuemaker(graph,s):
    pqueue={}
    for i,j in graph.items():
        if i==s:
            if len(j)==0:
                print("end")
                return
            for node in j:
                if node not in visited_list:
                    unvisited.append(node)
                    pqueue[node]= j[node]
                    print(node+ ':', j[node])
                else:
                    unvisited.remove(node)
                    #pqueue.pop(node)
    
                
    newnode=decider(pqueue)
    repeatChecker(newnode,unvisited)
    nextnode=newnode.pop(0)
    pacifier(pqueue,nextnode,s)
    
    print("Selected=",nextnode)
    print("Visited=",visited_list)
    print("unVisited=",unvisited)
    print("updated queue=",pqueue)
    print("dist=",dist)
    dijsktras(graph,nextnode)
    while len(unvisited)>0:
        leftover()
        
            
    
def dijsktras(graph,source):
    print("Current=>",source)
    if source not in visited_list:
        visited_list.append(source)
        if source in unvisited:
            unvisited.remove(source)
        
        queuemaker(graph,source)
    
    
    
    

                
print("Initial graph =",dist)         
                
dijsktras(graph,"A")
print(unvisited)
print("updated graph after exploring all vertices=",dist)
print("Shortest Path =",*visited_list,
      "with a cost of =",dist[visited_list[-1]])

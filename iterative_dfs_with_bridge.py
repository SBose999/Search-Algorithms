# When changing recursive into iterative, it is better to iterate as if it was a recursion
from collections import defaultdict
adj=defaultdict(list)
MAX_NO_OF_NODES=100001
visited=[False]*(MAX_NO_OF_NODES)
intime=[0]*(MAX_NO_OF_NODES)
outtime=[0]*(MAX_NO_OF_NODES)
res=[]
bridge=False
timer=0
def dfs(root,p):
	global adj, visited, intime, outtime, res, bridge,timer
	visited[root]=True
	intime[root]=timer 
	outtime[root]=timer
	timer+=1
	bridge=False
	stack = [(root, p, adj[root].__iter__())] # stack stores the current state of dfs
	while stack:
		node,par,i = stack.pop()
		try:
			j = next(i)
			stack.append((node,par,i))
			#previsit (node,parent)
			if j==par:
				continue 
			if visited[j]:
				outtime[node]=min(outtime[node],intime[j])
				if intime[node]>intime[j]:
					res.append((node,j))
			else:
				'''the things which are done initially when we enter a dfs call is done just before pushing state of dfs into the stack'''
				visited[j]=True 
				intime[j]=outtime[j]=timer; timer+=1
				stack.append((j,node,adj[j].__iter__()))
		except StopIteration:
			if node==root:
				#postvisit of root
				continue
			#postvisit-> when state of dfs(node,par)
			#things which are done just after dfs(node,par is called)
			if outtime[node]>intime[par]:
				bridge=True 
				return
			res.append((par,node))
			outtime[par]=min(outtime[par],outtime[node])

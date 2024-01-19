import heapq

data = open("in.txt", "r").read().strip()
data = data.split("\n")

G = [[c for c in line] for line in data]
R = len(G)
C = len(G[0])

def f(p2):
  queue = [(0,0,0,-1,-1)]
  distances = {}
  while queue:
    dist,r,c,dir_,indir = heapq.heappop(queue)
    if (r,c,dir_,indir) in distances:
      continue
    distances[(r,c,dir_,indir)] = dist
    for i,(moveR,moveC) in enumerate([[-1,0],[0,1],[1,0],[0,-1]]):
      nextR = r+moveR
      nextC = c+moveC
      new_dir = i
      new_indir = (1 if new_dir!=dir_ else indir+1)

      isnt_reverse = ((new_dir + 2)%4 != dir_)

      isvalid_part1 = (new_indir<=3)
      isvalid_part2 = (new_indir<=10 and (new_dir==dir_ or indir>=4 or indir==-1))
      isvalid = (isvalid_part2 if p2 else isvalid_part1)

      if 0<=nextR<R and 0<=nextC<C and isnt_reverse and isvalid:
        cost = int(G[nextR][nextC])
        heapq.heappush(queue, (dist+cost, nextR,nextC,new_dir,new_indir))

  ans = 9999
  for (r,c,dir_,indir),v in distances.items():
    if r==R-1 and c==C-1:
      ans = min(ans, v)
  return ans

def fastest (): 
    queue = [(0,0,0)]
    distances = {}
    while queue:
        d,r,c = heapq.heappop(queue)
        if (r,c) in distances:
            continue
        distances[(r,c)] = d
        for i,(moveR,moveC) in enumerate([[-1,0],[0,1],[1,0],[0,-1]]):
            nextR = r+moveR
            nextC = c+moveC
            if 0<=nextR<R and 0<=nextC<C:
                cost = int(G[nextR][nextC])
                heapq.heappush(queue, (d+cost,nextR, nextC))
    print ("fastest path without rules:", distances[(R-1, C-1)])
                    
def part1():
    print(f(False))

def part2():
    print(f(True))

part1()
part2()

fastest()

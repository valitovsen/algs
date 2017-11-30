
def knapsack_rec(items,limit, solution=False, big=False):
    '''
    knapsack_rec(items, limit, solution=False, big=False) ->
                                    value of optimal solution, solution set

    Recursively finds solution to a 0-1 knapsack problem
    given values and weights of items and total weight limit:
        items: list of tuples (value,weigth), contains only positive integers
        limit: positive integer for total weight limitation
        solution: boolean, return a list of items in optimal solution if True
        big: boolean, recommended to toggle True if a number of items exceeds 10^3

    A.Valitov 2017
    '''
    class RecCont:
        'Recursion container to neatly hold nonlocal variables'
        def __init__(self,items,limit, solution):
            self.count = len(items)
            self.return_solution = solution
            self.items = [None] + items # add placeholder so that item i has index i
            self.visited = {}
            self.limit = limit
            self.solution = set()

        def eval_state(self,i,x):
            '''Recursively calculates optimal value for
            subproblem with i items and weight limit x'''
            if not self.visited.get(i,{}).get(x):
                #1. Base case
                if i == 0:
                    val = 0
                #2. General case
                else:
                    #2.a Option 1 - don't include i-th item
                    if not self.visited.get(i-1,{}).get(x):
                        self.eval_state(i-1,x)
                    opt1 = self.visited[i-1][x]
                    #2.b Option 2 - include i-th item if possible
                    if x < self.items[i][1]:
                        opt2 = 0
                    else:
                        if not self.visited.get(i-1,{}).get(x-self.items[i][1]):
                            self.eval_state(i-1,x-self.items[i][1])
                        opt2 = self.visited[i-1][x-self.items[i][1]] + self.items[i][0]
                    #2.c Choose option with maximum value
                    val = max(opt1,opt2)

                #3. Update visited
                if i in self.visited:
                    self.visited[i].update({x:val})
                else:
                    self.visited.update({i:{x:val}})

        def find_solution(self):
            'Finds set of items in optimal solution'
            solution = set()
            x = self.limit
            for i in range(self.count,0,-1):
                # Option 1 - don't include
                opt1 = self.visited[i-1][x]
                # Option 2 - include
                if x < self.items[i][1]:
                    opt2 = 0
                else:
                    opt2 = self.visited[i-1][x-self.items[i][1]]+self.items[i][0]
                # Include if opt2 > opt1
                if opt2 > opt1:
                    self.solution.add(i)
                    x -= self.items[i][1]

        def run(self):
            self.eval_state(self.count,self.limit)
            if self.return_solution:
                self.find_solution()
                return self.visited[count][limit],self.solution
            return self.visited[count][limit]

    inst = RecCont(items, limit, solution)
    return inst.run()


if __name__ == '__main__':
    '''Run as a script
    - set recursion limit and stack size
    - redirect input
    - allocate more memory
    '''
    pass

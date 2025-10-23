class Solution:
    def findAllRecipesOptimized(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        """
        Optimized

        The code that creates the adjacency list is the same, but the main difference is that this version
        of the code keeps track of all supplies that have already been used. 

        While we're still doing a DFS inside a loop,
        we don't end up completing the DFS every time, since there are cases where 
        we already know we have all supplies for a given recipe, so instead of O(R * (R + I)), its just O(R + I)
        
        Example (with cycle):
        recipes = ["bread", "yeast"]
        ingredients = [["yeast"], ["bread"]]
        supplies = ["flour"]
    
        1st call:
        if we start with bread,
        supplies = {flour: true}
        bread is not in supplies (since its a recipe), so we set
        supplies: {flour: true, bread: false}, and continue to the loop below
        we see that "yeast" is one of the ingredients, so we visit "yeast"

        2nd call:
        we see that "yeast" is not in supplies,
        {flour: true, bread: false, yeast: false}, so we continue to the loop below,
        we get "bread" as one of the ingredients,

        3rd call:
        here, we can see that "bread" is present in supplies, but its set to false, which shows
        that we've already visited it in this path, so there's a cycle

        Example (not enough supplies):
        recipes = ["bread"]
        ingredients = [["yeast", "flour"]]
        supplies = ["flour"]
         
        supplies = {flour: true}

        1st call
        we start with bread,
        bread is not in supplies, so we set
        supplies: {flour: true, bread: false} and continue to the loop below
        "yeast" is one of the ingredients

        2nd call:
        yeast is not in supplies
        however, this is where the 2nd base case kicks in,
        we notice that yeast is not in supplies AND it's also not a recipe, so therefore,
        its a MISSING SUPPLY. So we need to return False

        """
        adjacency = {}
        for i in range(len(recipes)):
            adjacency[recipes[i]] = []
        # the indices of recipes corresponds with the incides of ingredients,
        # i.e ingredients[0] tells you what the ingredients for recipes[0] is
        for i in range(len(ingredients)):
            for ingredient in ingredients[i]:
                adjacency[recipes[i]].append(ingredient)
                # also add the ingredient itself to the adjacency if
                # it wasn't already added since
                # a recipe can also be an ingredient
                if ingredient not in adjacency:
                    adjacency[ingredient] = []

        # the reason why we set this to True is because initially,
        # we have all the starting supplies ready, but as we recur,
        # recipes can also be supplies and will be added
        # to this dictionary (defaulting to false)
        availableSupplies = {s: True for s in supplies}
        def dfs(root):
            # base case: if we've already seen this supply, return its result. True if
            # its been used, but False if its a cycle
            if root in availableSupplies:
                return availableSupplies[root]
            # if its not a recipe and also not in our available supplies,
            # this tells us that one of our supplies is not available
            if root not in recipesSet:
                return False
            # originally, we set this as false so in the case we have a cycle,
            # we will return False, because if we see the same supply twice in the same path,
            # that means its a cycle, so our base case will return false
            availableSupplies[root] = False
            for edge in adjacency[root]:
                if not dfs(edge):
                    return False 
            # if we get to this statement,
            # we know for certain there's no cycle, we can set this back to True
            availableSupplies[root] = True
            return availableSupplies[root]

        return [r for r in recipes if dfs(r)]

    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        """
        My First try:

        try to represent this as an adjacency list similar to the course schedule problem,
        which is a directed graph

        The bare ingredients (that are not made from something else on the list) would be 
        the edges of the list. For example,
        yeast and flour both have edges with Bread.

        Since this is a directed graph, for the purposes of graph traversal, it might be easier to represent the ingredients
        outgoing edges as the "ingredients necessary to make this recipe/ingredient", so we can start
        at a given node, and see how many nodes it can visit based on the direction. 

        Yeast <-
                Bread  
        Flour <-

        for example, bread is made of "yeast" and "flour". But "yeast" and "flour"
        are not made of anything else on the list so it has no outwards edges

        In the sandwich example:

        Yeast <-
                Bread <- Sandwich -> Meat  
        Flour <-

        Bread is made of yeast and flour, and sandwich is made of bread and meat

        Now say if we want to make "bread", we would locate bread in the graph, and then
        perform a DFS and check to see if all of its ingredient nodes are visited (yeast and flour). If so,
        that means we can create this recipe.

        We would iterate through the recipes list and perform DFS on each one.

        Time complexity: O(R * (R + I)), where I is the number of ingredients and R is the number of recipes, since its performing a DFS for each recipe which is (R + I) work
        Space: O(R + I)
        
        This isn't the most optimal solution, there's extra work being done when visiting all nodes from a given recipe,
        and then figuring out if every node was in the supplies set. There's a case where we might've already visited certain recipes,
        so we may end up re-visiting them. The optimal solution is explained above

        """
        recipesSet = set(recipes)
        adjacency = {}
        for i in range(len(recipes)):
            adjacency[recipes[i]] = []
        # the indices of recipes corresponds with the incides of ingredients,
        # i.e ingredients[0] tells you what the ingredients for recipes[0] is
        for i in range(len(ingredients)):
            for ingredient in ingredients[i]:
                adjacency[recipes[i]].append(ingredient)
                # also add the ingredient itself to the adjacency if
                # it wasn't already added since
                # a recipe can also be an ingredient
                if ingredient not in adjacency:
                    adjacency[ingredient] = []

        visited = set()
        cycle = set()

        # perform the same cycle detection as in "Course Schedule"
        def dfs(root):
            if root in cycle:
                return False
            if root in visited:
                return True
            cycle.add(root)
            for node in adjacency[root]:
                if not dfs(node):
                    return False
            cycle.remove(root)
            visited.add(root)
            return True

        res = []
        for i in range(len(recipes)):
            # some of the ingredients can also create cycles (which would be impossible),
            # so we need to detect cycles
            if not dfs(recipes[i]):
                visited = set()
                cycle = set()
                continue
            # check if all items in the visited set are present in the supplies set,
            # if so, that means we can make this recipe.
            # note that we ignore visited ingredients that are also "recipes",
            # since these would not be in the supplies set by default
            flag = True
            for item in visited:
                if item not in suppliesSet and item not in recipesSet:
                    flag = False
                    break
            if flag:
                res.append(recipes[i])
            
            # reset the evaluation for the next recipe 
            visited = set()
            cycle = set()
            
        return res

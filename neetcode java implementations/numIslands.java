class Pair {
    int x;
    int y;
    Pair(int x, int y){
        this.x = x;
        this.y = y;
    }
    public int getX(){
        return this.x;
    }
    public int getY(){
        return this.y;
    }
}
class Solution {
    public void printMatrix(int rows, int cols, boolean[][] grid){
        for (int i = 0; i < rows; ++i){
            for (int j = 0; j < cols; ++j){
                System.out.print(grid[i][j]);
                System.out.print(" ");
            }
            System.out.println("\n");
        }
    }
    public int numIslands(char[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int res = 0;
        boolean[][] visited = new boolean[rows][cols];
        for (int i = 0; i < rows; ++i){
            for (int j = 0; j < cols; ++j){
                visited[i][j] = false;
            }
        }
        for (int i = 0; i < rows; ++i){
            for (int j = 0; j < cols; ++j){
                if (grid[i][j] == '1' && !visited[i][j]){
                    this.dfs(i,j,grid,visited);
                    ++res;
                }
            }
        }
        return res;
    }
    public boolean inBounds(int i, int j, int rows, int cols){
        return i >= 0 && i < rows && j >= 0 && j < cols;
    }
    public void dfs(int i, int j, char[][] grid, boolean[][] visited){
        List<Pair> directions = Arrays.asList(
            new Pair(0, 1),
            new Pair(0, -1),
            new Pair(1, 0),
            new Pair(-1, 0)
        );
        for (Pair p: directions){
            int x = p.getX();
            int y = p.getY();
            int newX = i + x;
            int newY = j + y;
            if (
                this.inBounds(newX, newY, grid.length, grid[0].length) && 
                !visited[newX][newY] && 
                grid[newX][newY] == '1'){
                visited[newX][newY] = true;
                this.dfs(newX, newY, grid, visited);
            }
        }
        return;
    }
}

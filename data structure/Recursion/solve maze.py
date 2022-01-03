def search_from(maze,start_row,start_column):
    maze.update_position(start_row,start_column)
    if maze[start_row][start_column]=='OBSTACLE':
        return False
    if maze[start_row][start_column]=='TRIED':
        return False
    if maze.is_exit(start_row,start_column,'PART OF PART'):
      return True
    maze.update_position(start_row,start_column,'TRIED')
    found=search_from(maze,start_row-1,start_column) or \
          search_from(maze, start_row + 1, start_column) or \
          search_from(maze, start_row, start_column - 1) or \
    search_from(maze, start_row, start_column + 1)
    if found:
        maze.update_position(start_row,start_column,'PART OF PATH')
    else:
        maze.update_position(start_row,start_column,'DEAD_END')
    return found
search_from(50,67)

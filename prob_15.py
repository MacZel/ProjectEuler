def lattice_paths(grid_dim):
    line = [1] * grid_dim
    for i in range(grid_dim):
        for j in range(i):
            line[j] = line[j] + line[j - 1]
        line[i] = 2 * line[i - 1]
    return line[grid_dim - 1]
 
print ("Solution: ", lattice_paths(20), sep='', end='\n')

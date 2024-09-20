import sys

def find_path(pyramid, target):
    n = len(pyramid)

    def dfs(row, index, product, path):
        if row == n:
            if product == target:
                return path
            return None
        
        left_path = dfs(row + 1, index, product * pyramid[row][index], path + "L")
        if left_path:
            return left_path
        
        right_path = dfs(row + 1, index + 1, product * pyramid[row][index + 1], path + "R")
        if right_path:
            return right_path
        
        return None

    return dfs(1, 0, pyramid[0][0], "")

def parse_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    target = int(lines[0].strip())
    pyramid = [list(map(int, line.strip().split(','))) for line in lines[1:]]
    return pyramid, target

def main():
    if len(sys.argv) != 2:
        print("Usage: python pyramid_descent.py <input_file>")
        return

    input_file = sys.argv[1]
    pyramid, target = parse_input(input_file)

    # Run the solver
    result = find_path(pyramid, target)
    if result:
        print(f"Path: {result}")
    else:
        print("No path found")

if __name__ == "__main__":
    main()

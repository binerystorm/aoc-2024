#! /bin/python3

class Board():
    def __init__(self, data: str):
        self.board = data.strip().split()
        self.w = len(self.board[0])
        self.h = len(self.board)

    def out_of_bounds(self, x, y):
        return x >= self.w or y >= self.h or x < 0 or y < 0

    def print(self):
        for r in self.board:
            print(r)
        print()

    def enumerate(self):
        for y, row in enumerate(self.board):
            for x, col in enumerate(row):
                yield (x, y), col
        
    def __iter__(self):
        yield from self.board

    def __getitem__(self, index):
        if type(index) == tuple:
            x,y = index
            if self.out_of_bounds(x,y):
                return None
            else:
                return self.board[y][x]
        else:
            return board[index]


class Region:
    def __init__(self, area = 0, perim = 0):
        self.plots = set()
        self.area = area
        self.perim = perim
        self.sides = 0
        self.t_sides = {}
        self.b_sides = {}
        self.l_sides = {}
        self.r_sides = {}
    def join(self, other):
        self.area += other.area
        self.perim += other.perim
        self.plots |= other.plots
        for k,v in other.t_sides.items():
            if k in self.t_sides:
                self.t_sides[k].extend(v)
            else:
                self.t_sides[k] = v
        for k,v in other.b_sides.items():
            if k in self.b_sides:
                self.b_sides[k].extend(v)
            else:
                self.b_sides[k] = v
        for k,v in other.l_sides.items():
            if k in self.l_sides:
                self.l_sides[k].extend(v)
            else:
                self.l_sides[k] = v
        for k,v in other.r_sides.items():
            if k in self.r_sides:
                self.r_sides[k].extend(v)
            else:
                self.r_sides[k] = v
    def count_sides(self):
        for col in self.r_sides.values():
            prev = -2
            # print(col)
            col.sort()
            for next in col:
                if prev + 1 < next:
                    self.sides += 1
                prev = next
        for col in self.l_sides.values():
            prev = -2
            # print(col)
            col.sort()
            for next in col:
                if prev + 1 < next:
                    self.sides += 1
                prev = next
        for row in self.t_sides.values():
            prev = -2
            # print(row)
            row.sort()
            for next in row:
                if prev + 1 < next:
                    self.sides += 1
                prev = next
        for row in self.b_sides.values():
            prev = -2
            # print(row)
            row.sort()
            for next in row:
                if prev + 1 < next:
                    self.sides += 1
                prev = next


    def __repr__(self):
        area = self.area
        perim = self.perim
        price = self.area * self.perim
        return f"({area=}, {perim=}, {price=})"
    def __add__(self, other):
        return Region(self.area+other.area, self.perim+other.perim)
        

def get_perim_and_sides(x, y, board, region):
    perim = 0
    plot = board[x,y]
    assert plot != None
    for dx in [-1, 1]:
        if board[x+dx,y] != plot:
            if dx == -1:
                if x in region.l_sides:
                    region.l_sides[x].append(y)
                else:
                    region.l_sides[x] = [y]
            else:
                if x in region.r_sides:
                    region.r_sides[x].append(y)
                else:
                    region.r_sides[x] = [y]

            perim +=1
    for dy in [-1,1]:
        if board[x,y+dy] != plot:
            if dy == -1:
                if y in region.t_sides:
                    region.t_sides[y].append(x)
                else:
                    region.t_sides[y] = [x]
            else:
                if y in region.b_sides:
                    region.b_sides[y].append(x)
                else:
                    region.b_sides[y] = [x]
            perim +=1
    return perim

    
def get_region(x, y, regions, board):
    plot = board[x,y]
    touching_regions = set()
    for region in regions:
        if (x-1, y) in region.plots: 
            touching_regions.add(region)
        elif (x, y-1) in region.plots:
            touching_regions.add(region)
    if len(touching_regions) == 0:
        ret = Region()
        regions.add(ret)
    elif len(touching_regions) == 1:
        ret = touching_regions.pop()
    else:
        ret = Region()
        for region in touching_regions:
            ret.join(region)
        regions -= touching_regions
        regions.add(ret)
    ret.plots.add((x,y))
    return ret



def solve(plot, board):
    area = 0
    perim = 0
    regions = set()

    for (x,y), current_plot in board.enumerate():
        if plot == current_plot:
            region = get_region(x,y,regions,board)
            region.area += 1
            region.perim += get_perim_and_sides(x,y,board,region)
    # print(plot)
    for r in regions:
        r.count_sides()
    #     print(r.sides)
    # print()

    #return sum(map(lambda x: x.perim * x.area, regions))
    return sum(map(lambda x: x.sides * x.area, regions))

                

def main():
    with open("./input") as f:
        board = Board(f.read())
        plots = set()
        for r in board:
            for c in r:
                if c not in plots:
                    plots.add(c)

    total = 0
    for plot in plots:
        p = solve(plot, board)
        #print(f"{plot=}, {p=}")
        total += p
    print(f"{total=}")


if __name__ == "__main__":
    main()

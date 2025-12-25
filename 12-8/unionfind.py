
# union find implementation

class UnionFind():

    def __init__(self, N):
        self.parents = [i for i in range(N)]
        self.size = [1 for _ in range(N)]
        self.N = N
        self.merge_counter = 0

    def find(self, val):

        if self.parents[val] != val:
            self.parents[val] = self.find(self.parents[val])

        return self.parents[val]

    def union(self, val1, val2):
        r1 = self.find(val1)
        r2 = self.find(val2)

        if r1 == r2:
            return

        if self.size[r1] <= self.size[r2]:
            self.parents[r1] = r2
            self.size[r2] += self.size[r1]
        else:
            self.parents[r2] = r1
            self.size[r1] += self.size[r2]
        
        self.merge_counter += 1
    
    def find_product_of_three_largest(self):
        '''
        return the three largest disjoint sets values
        in the form
        number_1_largest * number_2_largest * number_3_largest
        '''
        temp = []

        for i in range(len(self.parents)):
            if i == self.parents[i]:
                temp.append(self.size[i])

        temp.sort(reverse=True)
        return temp[0] * temp[1] * temp[2]

    def is_all_merged(self):
        return self.merge_counter == self.N - 1
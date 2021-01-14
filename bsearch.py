class Search:
    def __init__(self):
        self.search_list = []
        self.to_search = 0
        self.left = 0
        self.right = 0

    def binary_search(self):  # O(Log n)
        if self.right >= 1:
            mid = (self.left + self.right)//2

            if self.search_list[mid] == self.to_search:
                return mid
            elif self.search_list[mid] > self.to_search: #left subarray
                self.right = mid
                return self.binary_search()
            else:
                self.left = mid
                return self.binary_search()
        elif self.search_list[self.right] == self.to_search:
            return 1 #Only one element and found
        else:
            return -1 # One element and not found
        return 1


search = Search()
search.search_list = [2, 3, 4, 10, 40]
search.to_search = 10
search.left = 0
search.right = len(search.search_list) - 1
flag = search.binary_search()
print(flag)

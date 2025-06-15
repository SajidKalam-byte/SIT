class InsertionSort:
    def __init__(self, list):
        self.list = list

    def insertion_sort(self):
        l = len(self.list)
        i = 1
        while i < l:
            item = self.list[i]
            ind = i - 1
            while ind >= 0 and item < self.list[ind]:
                self.list[ind + 1] = self.list[ind]
                ind -= 1
            self.list[ind + 1] = item
            i += 1
        return self.list

print("Enter the list of numbers: ")
user_input = input()
numbers = [int(x) for x in user_input.split()]
sorter = InsertionSort(numbers)
print(sorter.insertion_sort())

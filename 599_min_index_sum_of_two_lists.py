from collections import defaultdict
class Solution:
    def findRestaurant(self, list1: list, list2: list) -> list:
        if not len(list1) * len(list2):
            return []
        index_sum = float('inf')
        restaurent_map = dict()
        result_map = defaultdict(list)

        if len(list1) > len(list2):
            list1, list2 = list2, list1

        for index in range(len(list2)):
            restaurent_map[list2[index]] = index

        for idx in range(len(list1)):
            if list1[idx] in restaurent_map:
                result_map[idx+restaurent_map[list1[idx]]].append(list1[idx])

        return result_map[min(result_map.keys())]


if __name__ == '__main__':
    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    sol = Solution()
    print(sol.findRestaurant(list1, list2))
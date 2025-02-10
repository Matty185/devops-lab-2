nums = lsit(map(int, input("Enter numbers seperated by a space: ").split()))
print("Average:" sum(nums) / len(nums) if nums else "No numbers provided")

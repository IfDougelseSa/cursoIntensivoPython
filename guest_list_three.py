list = ["raul seixas", "joey ramone", "marie curie"]


print(f'You have been invited for a dinner {list[0].title()}.')
print(f'You have been invited for a dinner {list[1].title()}.')
print(f'You have been invited for a dinner {list[2].title()}.')


remove_guest = list.pop(0)


print(f'{remove_guest.title()} could not come.')


list.insert(0, "sabrina")


print(f'You have been invited for a dinner {list[0].title()}.')
print(f'You have been invited for a dinner {list[1].title()}.')
print(f'You have been invited for a dinner {list[2].title()}.')


list.insert(0, "michael jackson")
list.insert(2, "albert einsten")
list.append("linus torvalds")

print("Nova lista:")
print(f'You have been invited for a dinner {list[0].title()}.')
print(f'You have been invited for a dinner {list[1].title()}.')
print(f'You have been invited for a dinner {list[2].title()}.')
print(f'You have been invited for a dinner {list[3].title()}.')
print(f'You have been invited for a dinner {list[4].title()}.')
print(f'You have been invited for a dinner {list[5].title()}.')


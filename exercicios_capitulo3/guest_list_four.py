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

print("New list:")
print(f'You have been invited for a dinner {list[0].title()}.')
print(f'You have been invited for a dinner {list[1].title()}.')
print(f'You have been invited for a dinner {list[2].title()}.')
print(f'You have been invited for a dinner {list[3].title()}.')
print(f'You have been invited for a dinner {list[4].title()}.')
print(f'You have been invited for a dinner {list[5].title()}.')
print(list)

print("Uninvited list")


guest = list.pop(0)
guest2 = list.pop(1)
guest3 = list.pop(2)
guest4 = list.pop(2)



print(f"You aren't invited to the dinner anymore, i'm sorry {guest.title()}")
print(f"You aren't invited to the dinner anymore, i'm sorry {guest2.title()}")
print(f"You aren't invited to the dinner anymore, i'm sorry {guest3.title()}")
print(f"You aren't invited to the dinner anymore, i'm sorry {guest4.title()}")


print(list)


print("The new guest list:")


print(f'You are still invited to the dinner {list[0].title()}.')
print(f'You are still invited to the dinner {list[1].title()}.')


del list[0]
del list[0]


print(list)



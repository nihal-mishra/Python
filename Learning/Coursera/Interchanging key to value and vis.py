def groups_per_user(group_dictionary):
	user_groups = {}
	lis = []
	# Go through group_dictionary
	for key, val in group_dictionary.items():
		for value in val:
			if value not in user_groups:
				user_groups[value] = []
			user_groups[value].append(key)

	return user_groups


print(groups_per_user({"local": ["admin", "userA"],
					   "public": ["admin", "userB"],
					   "administrator": ["admin"]}))

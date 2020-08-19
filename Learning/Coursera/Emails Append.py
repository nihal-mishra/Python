def email_list(domains):
	emails = []
	for domain_name, users in domains.items():
		for us in users:
			emails.append(f"{us}@{domain_name}")

	return emails


print(email_list(
	{"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"],
	 "hotmail.com": ["bruce.wayne"]}))

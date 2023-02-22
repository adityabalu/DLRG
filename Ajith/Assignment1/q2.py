def concat(str_lst1, str_lst2):

	def lowercase(str_lst):
		lowercase = []
		for word in str_lst:
			lowercase.append(word.lower())
		return lowercase

	def combine(str_lst):
		result = []
		for i in str_lst:
			result.append(' '.join(i))
		return result

	str_lst = list(zip(lowercase(str_lst1), lowercase(str_lst2)))

	return combine(str_lst)


print(concat(["HellO", "ByE"], ["WoRlD", "wORLd"]))
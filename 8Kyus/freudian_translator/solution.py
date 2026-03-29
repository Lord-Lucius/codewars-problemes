def to_freud(sentence):
	wlist = sentence.split()
	return " ".join("sex" for _ in wlist)

print(to_freud("test"))
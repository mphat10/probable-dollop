def function():
	words= set(line.strip() for line in open('words.txt'))
	d={}
	for w in words:
		if len(w) not in d:
			d[len(w)]=w
		elif len(w) in d:
			d.update({len(w):w})
	return d

print(function())
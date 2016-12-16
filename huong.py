def function():
	words= set(line.strip() for line in open('words.txt'))
	d={}
	for w in words:
		if len(w) not in d:
			d[len(w)]=w
		elif len(w) in d:
			key = str(len(w))
			d.setdefault(key, [])
			d[key].append(w)
				
  			
	return d

print(function())
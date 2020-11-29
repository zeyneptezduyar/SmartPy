def sortByBuckets(bucket):
	return sorted(bucket, key=lambda x: x[1])

def leitnerStart(wordList):
	buckets = []
	for i in range(len(wordList)):
		buckets.append([wordList[i], 2])
	return buckets

def leitnerUpdate(buckets):
	return

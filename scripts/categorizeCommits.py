

correctiveKeyWords = []
adaptiveKeyWords = []
implementationKeyWords = []
nonfunctionalKeyWords = [] 
perfectiveKeyWords = [] 

correctiveCount = 0
adaptiveCount = 0
implementationCount = 0
nonfunctionalCount = 0
perfectiveCount = 0 

repoName = 'phpunit'
with open(repoName + "_largestcommits.txt") as f:

	for line in f:

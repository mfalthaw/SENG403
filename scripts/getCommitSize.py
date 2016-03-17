import subprocess

#var = subprocess.check_output(["ls"]).splitlines()

#fname.write(var)

#urls = [ "https://github.com/twitter-archive/kestrel" , " ", " ", ]


urls = [ 
#	"https://github.com/harvesthq/chosen",
#	"https://github.com/slimphp/Slim",
#	"https://github.com/twitter/gizzard",
#	"https://github.com/JakeWharton/ActionBarSherlock",
#	"https://github.com/thoughtbot/paperclip",
#	"https://github.com/mitsuhiko/flask",
#	"https://github.com/ariya/phantomjs",
#	"https://github.com/tornadoweb/tornado",
#	"https://github.com/scalatra/scalatra",
#	"https://github.com/sbt/sbt",
#	"https://github.com/twitter/finagle",
#	"https://github.com/antirez/redis",
#	"https://github.com/hbons/SparkleShare",
#	"https://github.com/ServiceStack/ServiceStack",
	"https://github.com/sebastianbergmann/phpunit"
	]





repoNames = [ 
#	"chosen",
#	"Slim",
#	"gizzard",
#	"ActionBarSherlock",
#	"paperclip",
#	"flask",
#	"phantomjs",
#	"tornado",
#	"scalatra",
#	"sbt",
#	"finagle",
#	"redis",
#	"SparkleShare",
#	"ServiceStack",
	"phpunit"
	]



index = 0
for url in urls:
	fname = open(repoNames[index]+"_commitlog.txt", 'w')
	fname.write(repoNames[index] + '\n')
	subprocess.call(["git", "clone", url])
	process = subprocess.Popen(["git", "-C", repoNames[index], "log" ,"--numstat"], stdout=subprocess.PIPE)
	out, err = process.communicate()
	subprocess.call(["rm", "-rf", repoNames[index]])
	index = index + 1

	#fname.write(str(out.splitlines()))
	count = 0
	for line in out.splitlines():
		if line.startswith('Author:') or line.startswith('Date:'):
			pass
		elif line.startswith('commit'):
			fname.write(str(line) + '\n')
			fname.write("File count: " + str(count) + '\n')
			fname.write("---------------------------------------------\n")
			fname.write(str(line) + '\n')
			count = 0
		else:
			if line.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-')):
				count = count + 1
				filename = ''.join([i for i in line if not i.isdigit() and i != '-'])
				fname.write(filename + '\n')
			else:
				fname.write(str(line) + '\n')
	fname.close()
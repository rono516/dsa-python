from collections import defaultdict

d = defaultdict(list)

d["python"].append("awesome")
d["something-else"].append("not relevant")
d["python"].append("language")
for i in d.items():
    print (i)

# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true
s ="run: to go faster than a walk : to go steadily by springing steps : to take part into a contest - ~ a marathon : to move at a fast gallop - he may occasionally run to and from work : flee, retreat, escape - drop the gun and run : to go without restraint : move freely about at will - let chickens ~ loose : consort - we run with our group \n" + "dog: canid wolves, foxes, and other dogs especially : a highly variable domestic mammal : a pet ~ : fellow, chap, a lazy person - you lucky dog\n" + "break: break a/the record to do something better than the best known speed, time, number, etc. previously achieved : to fail to keep a law, rule, or promise = ~ the law : These enzymes break down food in the stomach (= cause food to separate into smaller pieces). I needed something to break the monotony of my typing job. The phone rang, as to break my concentration. To ~ (of a storm) = to start suddenly: We arrived just as a storm was breaking. \n"

defs = s.split('\n')

rez = list()

for deff in defs:
  if deff == '':
    continue
  
  words = deff.split()
  word = words[0].replace(':', '')
  s = 0
  for x in words:
    if x == "~" or x == word:
      print(x)
      s += 1
  

  rez.append((word, s))

print(rez)

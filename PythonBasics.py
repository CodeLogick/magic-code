# Print table from 1 to 10
for n in range(1,11):
  print(list(range(n, (n*10+1),n)))
  

# count word in a para
st = 'Citibank is an internatinal bank !! A bank where we bank upon'    
words = st.split(' ')
words.sort()
print('word count is {}'.format(len(words)))
wordDict = dict([(v,c*0) for c,v in enumerate(words)])
for w in st.split(' '):
  if(w in words):
    wordDict[w] = wordDict[w] + 1
for k,v in wordDict.items():
  print(f'{k}, {v} times')


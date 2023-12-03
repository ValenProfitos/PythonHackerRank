if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

#Convert the map object to a list of int
scores = list(arr)

#Sort the scores in ascending order
sorted_scores = sorted(scores, reverse=True)

#Find the runner-up score
runnerUpScore = None
for score in sorted_scores:
    if score < max(sorted_scores):
        runnerUpScore = score
        break
    
print(runnerUpScore)
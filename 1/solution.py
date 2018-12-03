f = open("input")
txt = f.read()
data = [int(num) for num in txt.splitlines()]


def solution(data):
	return sum(map(int, data))


def solution2(data):
	res = 0
	freq = set()
	freq.add(sum)
	while True:
		for val in data:
			res += val
			if (res in freq):
				return res
			freq.add(res)
		
print(solution(data))
print(solution2(data))


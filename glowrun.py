import json

runners = [76, 48, 64, 52, 42, 41, 51, 38, 61, 46, 56, 55, 47, 77, 98, 62, 65, 66, 40, 67, 73, 72, 75, 74, 53, 54, 69, 71, 70, 58, 79, 44, 43, 63, 39, 59, 60, 36, 37, 1, 80, 78, 45, 83, 82, 81, 57, 68]

def main():
	#open the json file and load it into the data dict
	filename  = 'Glow_Run_2015_Sun_Oct_25_195258_2015_times.json'
	data = {}
	with open(filename) as data_file:
		data = json.load(data_file)

	times = list(reversed(data['rawtimes']['times']))
	times.remove('0:35:50')

	for i in range(len(times)):
		li = times[i].split(':')
		times[i] = '{0}:{1}'.format(li[1], li[2])
		print times[i]

	print 'Place\tTime\t\tBib Number\n'
	for i in range(len(runners)):
		print '{0}.\t{1}\t\t{2}'.format(i+1, times[i], runners[i])

if __name__ == '__main__':
	main()
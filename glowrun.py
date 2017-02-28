import json

#order that the runners finished based on physical tags
runners = [76, 48, 64, 52, 42, 41, 51, 38, 61, 46, 56, 55, 47, 77, 98, 62, 65, 66, 40, 67, 73, 72, 75, 74, 53, 54, 69, 71, 70, 58, 79, 44, 43, 63, 39, 59, 60, 36, 37, 1, 80, 78, 45, 83, 82, 81, 57, 68]

def main():
	#open the json file and load it into the data dict
	filename  = 'Glow_Run_2015_Sun_Oct_25_195258_2015_times.json'
	data = {}
	with open(filename) as data_file:
		data = json.load(data_file)

	times = list(reversed(data['rawtimes']['times']))

        #had an outlier data point due to a false press of the lap/finish timer
	times.remove('0:35:50')
        
        #go through and clean up the format of the time strings
	for i in range(len(times)):
		li = times[i].split(':')
		times[i] = '{0}:{1}'.format(li[1], li[2])
		#use this print statement for debugging the time formats
                #print times[i]
        
        #print the header for the results sheet
	print 'Place\tTime\t\tBib Number\n'

        #go through and print out all the runners results
        #we didn't have the names so we gave them acces to a file containing
        #this using output pipes to allow them to look up their time and place
        #by their bib number
	for i in range(len(runners)):
		print '{0}.\t{1}\t\t{2}'.format(i+1, times[i], runners[i])

if __name__ == '__main__':
	main()

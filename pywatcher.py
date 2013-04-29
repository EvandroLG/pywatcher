import os, time, argparse


def get_time_files(directory):
	times = []

	for item in os.listdir(directory):
		item_path = '%s%s' % (directory, item)
		mtime = os.path.getmtime(item_path)

		times.append(mtime)

	return times


def has_modification(current_times, past_times):
	for i, past in enumerate(past_times):
		if past != current_times[i]:
			return True

	return False


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--directory', '-d', required=True)
	parser.add_argument('--command', '-c', required=True)
	args = parser.parse_args()
	directory = args.directory
	command = args.command

	while True:
		current_times = get_time_files(directory)

		if 'past_times' in locals():
			has_change = has_modification(current_times, past_times)

			if has_change:
				os.system(command)

		past_times = current_times
		time.sleep(1)


if __name__ == '__main__':
	main()

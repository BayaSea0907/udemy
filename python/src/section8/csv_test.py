import csv


with open('test.csv', 'w') as csv_file:
	field_names = ['Name', 'Count']

	writer = csv.DictWriter(csv_file, fieldnames = field_names)
	writer.writeheader()

	writer.writerow({'Name': 'A', 'Count': 1})
	writer.writerow({'Name': 'Baya', 'Count': 2})
	writer.writerow({'Name': 'Sea', 'Count': 3})

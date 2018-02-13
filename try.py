import csv 
output_file = open("output.csv", "a")
out = csv.writer(output_file)

if 10 > 20:
	a  = ["1", "hello"]
	out.writerow(a)

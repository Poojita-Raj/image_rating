from flask import Flask , request , render_template
import csv
app = Flask(__name__)
file_name = 'main.csv'
# onlyfiles = [f for f in os.listdir("./static") if isfile(join("./static", f))]


'''
question = dict()
f = open("main.csv", "r")
for line in f:
	line = line.strip().split(",")
	question[str(line[0])] = line[1:]
''' 

csvfile = open(file_name,'r')
reader = csv.DictReader(csvfile,delimiter=',') # headers become keys of the dict
#data = next(reader) # dont want headings
#print("hello", data)

#output_file = open("output.csv","a")
#out = csv.writer(output_file)

def get_next_data():
	return next(reader)


@app.route('/', methods = ['GET','POST'])
def index():
	"""if request.method == 'POST':
		global data
		result = []
		for i in range(5):
			for j in range(4):
				index = "rating" + str(i) + str(j)
				result.append(data["question"])
				result.append(i)
				result.append(j)
				print(data)
				req = request.form
				print(req)
				result.append(request.form[index])
				print(result)
				outputfile= open("output.csv","a") 
				with outputfile:
					writer = csv.writer(outputfile)
    					writer.writerow(result)
				pass
		return "POST called"""
	if request.method == "POST":
		print(request.form["easy_rating"])
		print(request.form["hard_rating"])
		result = []
		result.append(request.form["easy_rating"])
		result.append(request.form["hard_rating"])
		with open("output.csv", "a") as fp:
    			wr = csv.writer(fp)
    			wr.writerow(result)
		data = get_next_data()	
		return render_template("index.html",data = data)
	#print(data)
	data = get_next_data() # dict with csv headers as key and one row as values		
	return render_template("index.html",data = data)


if __name__ == "__main__":
	app.run(debug=True)
	csvfile.close()

from flask import Flask, render_template, redirect, request

import Caption_it

# __name__ == __main__
app = Flask(__name__)


@app.route('/')
def hello():
	return render_template("homepage.html")


@app.route('/', methods= ['POST'])
def marks():
	if request.method == 'POST':

		f = request.files['userfile']
		path = "./static/{}".format(f.filename)# ./static/images.jpg
		f.save(path)

		caption = Caption_it.caption_this_image(path)
		
		result_dic = {
		'image' : path,
		'caption' : caption
		}

	return render_template("upload.html", your_result =result_dic)

@app.route('/developer',methods = ["GET","POST"])
def developer():
    	return render_template('dev.html')

if __name__ == '__main__':
	app.debug = True
	# due to versions of keras we need to pass another paramter threaded = Flase to this run function
	app.run(debug = True, threaded = False)

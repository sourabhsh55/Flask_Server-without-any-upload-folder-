from flask import Flask,request,render_template,redirect,flash,url_for
import numpy as np 
import cv2
import base64
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/index",methods=['GET','POST'])
def index():
	# Under post request.
	if request.method == "POST":
		file = request.files['img']
		data = file.stream.read()
		n = np.fromstring(data,np.uint8) # numpy array from string values.
		img = cv2.imdecode(n,cv2.IMREAD_COLOR)  # forming the pixels value into original image dimensions.
		img_str = cv2.imencode('.jpg',img)[1].tostring()
		encoded = base64.b64encode(img_str).decode("utf-8") 
		mime = "image/jpg;"
		out_image = f"data:{mime}base64,{encoded}"
		# rendering the image onto html page.
		return render_template("print.html",out_image=out_image) 

	# when request method is GET.
	return render_template("index.html")




if __name__ == "__main__":
	app.run(debug=True)
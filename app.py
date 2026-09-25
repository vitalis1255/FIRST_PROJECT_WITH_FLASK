from flask import Flask,render_template,request

app = Flask(__name__)

#Create list of dictionaries dummy data for all courses in the backend
COURSES = [
  {
    "id":1,"title":"Flask Beginner Foundations","category":"Backend","level":"Beginner","status":"Active"
  },
  {
    "id":2,"title":"HTML & Semantic Web Layouts","category":"Frontend","level":"Beginner","status":"Active"
  },
  {
    "id":3,"title":"Javascript Regular Expressions","category":"Backend","level":"Intermediate","status":"Coming Soon"
  },
  {
    "id":4,"title":"CorelDraw Vector Graphics & Design","category":"Design","level":"Beginner","status":"Active"
  }
]


#Create API ROUTE FOR HOME PAGE HTML
@app.route("/")
def index():
  return render_template("index.html")


#Create api route for courses
@app.route("/courses")
def courses():
  #capture query parameter: /courses?category=Backend
  category_filter = request.args.get("category")
  if category_filter:
    filtered_courses = [c for c in COURSES if c["category"].lower() == category_filter.lower()]
  else:
    filtered_courses = COURSES

  return render_template("courses.html", courses=filtered_courses)





if __name__ == "__main__":
  app.run(debug=True)
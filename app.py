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


#Using ID to get each course
@app.route("/course/<int:course_id>")#api for course_detail
def course_detail(course_id):
  #Find a matching integer ID
  # course = [c for c in COURSES if c["id"] == course_id[0]]
  course = next((c for c in COURSES if c["id"] == course_id))

  if not course:
    return "Course Not Found",404

  return render_template("course_detail.html",course=course)#help to display course details in the html.


#api for contact
@app.route("/contact", methods=["GET","POST"])
def contact():
  success = False
  name = " "

  if request.method == "POST":
    # Extract the data submitted in the form
    name = request.form.get("name")
    success = True

  return render_template("contact.html",success=success,name=name)





if __name__ == "__main__":
  app.run(debug=True)
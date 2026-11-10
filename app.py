from flask import Flask, render_template_string, request
app = Flask(__name__)

# HOME PAGE
@app.route('/')
def home():
    return render_template_string("""
    <html>
    <head>
        <title>College Enquiry Chatbot</title>
        <style>
            body {
                font-family: Arial;
                background: #f2f4f8;
                text-align: center;
                margin: 0;
            }
            header {
                background: #263b80;
                color: white;
                padding: 25px;
            }
            nav {
                background: #172653;
                padding: 18px;
            }
            nav a {
                color: white;
                text-decoration: none;
                margin: 12px;
            }
            .content {
                padding: 60px;
            }
            .btn {
                background: #263b80;
                color: white;
                padding: 12px 25px;
                text-decoration: none;
                border-radius: 5px;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>College Enquiry Chatbot</h1>
            <p>Your Guide to College Information</p>
        </header>

        <nav>
            <a href="/">Home</a>
            <a href="/admin-login">Admin Login</a>
            <a href="/student">Student Login</a>
        </nav>

        <div class="content">
            <h2>Welcome to Our College</h2>
            <p>Get all college information in one place.</p>
            <p>Explore courses, fees, placements and scholarships.</p>
            <br>
            <a href="/admin-login" class="btn">Admin Login</a>
        </div>
    </body>
    </html>
    """)


# ADMIN LOGIN PAGE
@app.route('/admin-login', methods=['GET', 'POST'])
def admin_login():

    message = ""

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'harshi' and password == 'harshi123':
            message = "Login successful! Welcome, Admin."
        else:
            message = "Invalid username or password."

    return render_template_string("""
    <html>
    <head>
        <title>Admin Login</title>
    </head>
    <body style="text-align:center; font-family:Arial; padding:50px;">

        <h1>Admin Login</h1>

        <form method="POST">
            <input type="text" name="username"
            placeholder="Enter Username" required>
            <br><br>

            <input type="password" name="password"
            placeholder="Enter Password" required>
            <br><br>

            <button type="submit">Login</button>
        </form>

        <p>{{ message }}</p>
        <a href="/">Back to Home</a>

    </body>
    </html>
    """, message=message)
@app.route('/student', methods=['GET', 'POST'])
def student_login():
    return render_template_string("""
    <html>
    <head>
        <title>Student Login</title>
    </head>
    <body style="background-color:#fce4ec;
                 font-family:Arial; text-align:center;">

        <h1>MAHARANI CLUSTER UNIVERSITY</h1>
        <h2>Student Login</h2>

        <form method="POST">
            <p>
                <input type="text" name="student_name"
                placeholder="Student Name" required>
            </p>

            <p>
                <input type="text" name="register_number"
                placeholder="Register Number" required>
            </p>

            <p>
                <input type="password" name="password"
                placeholder="Password" required>
            </p>

            <button type="submit">Login</button>
        </form>

        <p>New Student?
        <a href="/register">Register Here</a></p>

        <a href="/">Back to Home</a>

    </body>
    </html>
    """)
 
# STUDENT REGISTRATION PAGE
@app.route('/register', methods=['GET', 'POST'])
def register():

    message = ""

    if request.method == 'POST':
        name = request.form['name']
        regno = request.form['regno']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password == confirm_password:
            message = "Registration Successful!"
        else:
            message = "Passwords do not match!"

    return render_template_string("""
    <html>
    <head>
        <title>Student Registration</title>
    </head>

    <body style="background:#fce4ec;
                 font-family:Arial; text-align:center;">

        <h1>MAHARANI CLUSTER UNIVERSITY</h1>
        <h2>Student Registration</h2>

        <form method="POST">

            <p><input type="text" name="name"
            placeholder="Student Name" required></p>

            <p><input type="text" name="regno"
            placeholder="Register Number" required></p>

            <p><input type="email" name="email"
            placeholder="Email ID" required></p>

            <p><input type="tel" name="phone"
            placeholder="Phone Number" required></p>

            <p><input type="password" name="password"
            placeholder="Password" required></p>

            <p><input type="password" name="confirm_password"
            placeholder="Confirm Password" required></p>

            <button type="submit">Register</button>

        </form>

        <h3>{{ message }}</h3>

        <p>Already Registered?
        <a href="/student">Student Login</a></p>

        <a href="/">Back to Home</a>

    </body>
    </html>
    """, message=message)
    # COLLEGE DETAILS PAGE
@app.route('/college')
def college():
    return render_template_string("""
    <h1>College Details</h1>
    <p><b>College Name:</b> Maharani Cluster University</p>
    <p><b>Location:</b> Bengaluru, Karnataka</p>
    <p><b>Courses:</b> BCA, BBA, B.Com, BA, B.Sc</p>
    <p><b>Facilities:</b> Library, Computer Lab, Hostel</p>
    <a href="/">Back to Home</a>
    """)
    # COURSE DETAILS PAGE
@app.route('/courses')
def courses():
    return render_template_string("""
    <h1>Course Details</h1>

    <h3>Undergraduate Courses</h3>
    <ul>
        <li>BCA - Bachelor of Computer Applications</li>
        <li>BBA - Bachelor of Business Administration</li>
        <li>B.Com - Bachelor of Commerce</li>
        <li>BA - Bachelor of Arts</li>
        <li>B.Sc - Bachelor of Science</li>
    </ul>

    <a href="/">Back to Home</a>
    """)
# FEE STRUCTURE PAGE
@app.route('/fees')
def fees():
    return render_template_string("""
    <h1>Fee Structure</h1>
    <h3>Estimated Annual Course Fees</h3>

    <table border="1" cellpadding="10">
        <tr>
            <th>Course</th>
            <th>Annual Fees</th>
        </tr>
        <tr><td>BCA</td><td>Rs. 60,000</td></tr>
        <tr><td>BBA</td><td>Rs. 55,000</td></tr>
        <tr><td>B.Com</td><td>Rs. 40,000</td></tr>
        <tr><td>BA</td><td>Rs. 30,000</td></tr>
        <tr><td>B.Sc</td><td>Rs. 40,000</td></tr>
    </table>
    <p>Note: These are approximate fees for project purposes,
    not official university fees.</p>

    <a href="/">Back to Home</a>
    """)
    # PLACEMENT DETAILS PAGE
@app.route('/placement')
def placement():
    return render_template_string("""
    <h1>Placement Details</h1>

    <h3>Our Placement Cell</h3>
    <p>
    Our college provides placement support to students
    through training, career guidance and interview preparation.
    </p>

    <h3>Placement Activities</h3>
    <ul>
        <li>Resume Preparation</li>
        <li>Communication Skills Training</li>
        <li>Interview Preparation</li>
        <li>Group Discussion</li>
        <li>Campus Recruitment</li>
    </ul>

    <h3>Job Opportunities</h3>
    <ul>
        <li>Software Developer</li>
        <li>HR Executive</li>
        <li>Accountant</li>
        <li>Business Analyst</li>
        <li>Marketing Executive</li>
    </ul>

    <p><b>Note:</b> Placement opportunities depend on
    student skills and company requirements.</p>

    <a href="/">Back to Home</a>
    """)
    # SCHOLARSHIP DETAILS PAGE
@app.route('/scholarship')
def scholarship():
    return render_template_string("""
    <h1>Scholarship Details</h1>

    <h3>Scholarship Opportunities</h3>
    <p>
    Our college provides information and guidance
    about various scholarship opportunities for students.
    </p>

    <h3>Types of Scholarships</h3>
    <ul>
        <li>Government Scholarships</li>
        <li>Merit-Based Scholarships</li>
        <li>Minority Scholarships</li>
        <li>SC/ST Scholarships</li>
        <li>OBC Scholarships</li>
        <li>Financial Assistance for Students</li>
    </ul>

    <h3>Required Documents</h3>
    <ul>
        <li>Aadhaar Card</li>
        <li>Income Certificate</li>
        <li>Caste Certificate (if applicable)</li>
        <li>Previous Year Marks Card</li>
        <li>Bank Passbook</li>
        <li>College Admission Details</li>
    </ul>

    <p><b>Note:</b> Scholarship eligibility and amount
    depend on government rules and student qualifications.</p>

    <a href="/">Back to Home</a>
    """)
    # EVENTS DETAILS PAGE
@app.route('/events')
def events():
    return render_template_string("""
    <h1>College Events</h1>

    <h3>Academic Events</h3>
    <ul>
        <li>Seminars</li>
        <li>Workshops</li>
        <li>Guest Lectures</li>
        <li>Project Exhibitions</li>
    </ul>

    <h3>Cultural Events</h3>
    <ul>
        <li>Annual Day Celebration</li>
        <li>College Fest</li>
        <li>Traditional Day</li>
        <li>Dance and Singing Competitions</li>
    </ul>

    <h3>Sports Events</h3>
    <ul>
        <li>Badminton Competition</li>
        <li>Cricket Tournament</li>
        <li>Volleyball Competition</li>
        <li>Sports Day</li>
    </ul>

    <h3>Other Activities</h3>
    <ul>
        <li>National Festivals</li>
        <li>Freshers Day</li>
        <li>Farewell Day</li>
        <li>Social Awareness Programs</li>
    </ul>

    <p>Students are encouraged to participate
    in college events and activities.</p>

    <a href="/">Back to Home</a>
    """)
 # STUDENT HOSTEL DETAILS PAGE
@app.route('/hostel')
def hostel():
    return render_template_string("""
    <html>
    <head>
        <title>Hostel Details</title>
    </head>

    <body>
        <h1>Student Hostel Details</h1>

        <h3>Hostel Facilities</h3>

        <ul>
            <li>Separate accommodation for boys and girls</li>
            <li>Furnished rooms</li>
            <li>Drinking water facility</li>
            <li>Study room</li>
            <li>Wi-Fi facility</li>
            <li>Security and CCTV</li>
            <li>Indoor and outdoor activities</li>
            <li>Mess and dining facilities</li>
        </ul>

        <h3>Hostel Fee Structure</h3>

        <table border="1" cellpadding="10">
            <tr>
                <th>Facility</th>
                <th>Estimated Amount</th>
            </tr>

            <tr>
                <td>Hostel Accommodation</td>
                <td>Rs. 4,000</td>
            </tr>

            <tr>
                <td>Food and Mess</td>
                <td>Rs. 1,500</td>
            </tr>

            <tr>
                <td>Maintenance</td>
                <td>Rs. 500</td>
            </tr>

            <tr>
                <th>Total</th>
                <th>Rs. 6,000</th>
            </tr>
        </table>

        <p>
            Note: These are estimated sample fees
            for project purposes, not official university fees.
        </p>

        <br>
        <a href="/">Back to Home</a>

    </body>
    </html>
    """)     
if __name__ == '__main__':
    app.run(debug=True)   


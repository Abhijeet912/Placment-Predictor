<h1>Campus Placement Predictor</h1>
<p>The Campus Placement Predictor is a Flask web application that utilizes a pre-trained machine learning model to predict the likelihood of a student getting placed during campus placements. <br>The model takes into account various input features such as gender, specialization, degree type, work experience, and academic scores.
</p>
<h3>Features</h3>
<p>Predicts whether a student will be placed or needs to work harder for placement.
Displays the probability of placement along with a personalized message.
User-friendly web interface for inputting details and receiving predictions.</p>
<h3>Technologies Used</h3>
<li>Flask: A Python web framework.</li>
<li>Pickle: For loading the pre-trained Random Forest machine learning model.</li>
<li>HTML and Jinja: Templates for rendering dynamic content.</li>
<h3>Usage</h3>
Clone the Repository:
<bold>Copy code</bold>
git clone https://github.com/Abhijeet912/campus-placement-predictor.git
<hr>
<bold>Install Dependencies:</bold>
pip install -r requirements.txt
<hr>
<bold>Run the Application:</bold>
python app.py
<hr>
<bold>Access the Web Application:</bold>
Open your browser and navigate to http://localhost:5000.
<hr>
Project Structure
app.py: Main Flask application file.
campusplacementpredictor.pkl: Pre-trained Random Forest model.
templates/: HTML templates for rendering web pages.
<bold>Contributing</bold>
<p>Contributions are welcome! If you'd like to contribute to the project, please follow the standard GitHub fork and pull request workflow.</p>


Acknowledgments
The model used in this project was trained on a dataset obtained from Kaggle.
Special thanks to @Aakanksha16 for their valuable contributions.

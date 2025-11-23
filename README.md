💪 AI Fitness Coach

An AI-powered, interactive fitness assistant built with Streamlit and Google Gemini Pro.
This application provides personalized workout routines, nutrition plans, goal tracking, calorie burn calculation, and recommended fitness YouTube channels — all in a clean, easy-to-use interface.

🚀 Features
🥅 1. Set Fitness Goals

Define your personal fitness objectives such as:

Weight Loss

Muscle Gain

Endurance Improvement

Overall Health

Includes:

BMI calculation

Goal-based prompts and suggestions

Automatic goal adjustments using simple rule-based logic

🏋️‍♂️ 2. AI-Generated Workout Routines

Uses Google Gemini Pro to create customized workout plans based on:

Your fitness goal

Your age

Workout routines are streamed live and formatted cleanly inside the app.

🥗 3. AI-Generated Nutrition Plans

Automatically produces diet recommendations using Gemini Pro.
Personalized based on:

Desired fitness goal

Age

Ideal for aligning your diet with your workout strategy.

🔥 4. Calories Burned Calculator

Provides accurate calorie burning calculations based on:

Exercise type (Running, Cycling, Weightlifting, Skipping)

Duration (minutes)

Weight (kg)

Great for tracking your daily fitness output.

📈 5. Progress Tracker (Prototype)

Includes a partial progress tracking module.
Features methods for BMI calculation, calorie tracking, and recommendation support.
Can be expanded to store real historical data.

📺 6. YouTube Workout Channel Recommendations

AI-based suggestions for the best channels to follow, tailored to your:

Fitness goal

Training style

Powered by Gemini Pro, no YouTube API required.

🧠 Technologies Used
Component	Technology
UI Framework	Streamlit
AI Model	Google Gemini Pro (google.generativeai)
Environment Handling	python-dotenv
Language	Python 3
Deployment	Local Streamlit app / Cloud Deployment supported
📂 Project Structure
AI-Fitness-Coach/
│
├── App.py                          # Main landing page
├── .env                            # Stores GOOGLE_API_KEY
├── requirements.txt                # Dependencies
│
└── pages/
    ├── ASetGoals.py                # BMI, goal setting & adjustments
    ├── BWorkoutRoutine.py          # AI workout generator
    ├── CNutrition Recommendation.py# AI nutrition generator
    ├── DCalorieBurned.py           # Calorie calculator & tracker
    └── EYoutube Recommendation.py  # AI YouTube channel recommendations

🔧 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/yourusername/AI-Fitness-Coach.git
cd AI-Fitness-Coach

2️⃣ Create & Fill .env File

Inside the project root, create a .env file:

GOOGLE_API_KEY=your_api_key_here


Get your key from:
👉 https://ai.google.dev/

3️⃣ Install Requirements
pip install -r requirements.txt

4️⃣ Run the App
streamlit run App.py


The app will open in your browser automatically.

📌 How It Works
🔹 Streamlit handles the UI

Each feature is a separate page inside /pages/.

🔹 Gemini Pro handles AI logic

The app interacts with Gemini Pro using:

model = genai.GenerativeModel("gemini-pro")

🔹 Streamed Responses

Workout plans, nutrition plans, and channel suggestions are streamed chunk-by-chunk for smooth display.

🛠️ Future Improvements

🔄 Add a real database for storing progress and goals

📊 Visualize BMI, calorie burn trends, and workout history

🎥 Add pose detection for exercise form feedback

👤 User accounts with authentication

📱 Mobile-friendly UI redesign

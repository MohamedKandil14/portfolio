# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    user_data = {
        'name': 'Mohamed Ahmed Kandil',
        'title': 'Full Stack Developer | Python Developer',
        'email': 'mohamedkandil5295@gmail.com',
        'phone1': '+20 1114165160',
        'phone2': '+20 1017414332',
        'location': 'Faisal Street, Giza, Egypt',
        'linkedin_url': 'https://www.linkedin.com/in/Mohamed Kandil',
        'github_url': 'https://github.com/MohamedKandil14',
        'profile_image': 'Mo.jpg',
        'cv_download_link': 'static/Mohamed_Ahmed_Kandil_CV.pdf',

        'about': """
            Highly motivated and results-oriented Full Stack Developer with a Bachelor's degree in Industrial Electronics and Control and a Professional Diploma in Open-Source Applications Development from ITI. Possessing a solid foundation in Python, Django, and MERN stack technologies, with practical experience in web development, database management, and web scraping. Eager to leverage strong problem-solving and communication skills to contribute to innovative software development projects as a Python Developer.
        """,

        'technical_skills': {
            'Programming Languages': ['Python', 'JavaScript', 'TypeScript', 'C', 'C++'],
            'Web Frameworks (Backend)': ['Django', 'Node.js (Express)'],
            'Web Frameworks (Frontend)': ['React.js', 'Angular', 'HTML5', 'CSS3', 'Bootstrap', 'jQuery', 'ES6'],
            'Databases': ['MySQL', 'NoSQL (MongoDB)', 'SQLite', 'PostgreSQL'],
            'Web Knowledge': ['RESTful APIs', 'Web Services', 'Servlets', 'JSP', 'XML', 'JSON'],
            'Tools & Version Control': ['Git', 'GitHub', 'Docker'],
            'Administration': ['Bash Shell Scripting', 'Linux (Red Hat System Administration I, II)'],
            'Data Handling': ['Web Scraping (BeautifulSoup, Requests)'],
            'Concepts': ['Object-Oriented Programming (OOP)', 'MVC Architecture', 'CRUD operations']
        },
        'projects': [
            {
                'name': 'Task Management Application',
                'description': 'Developed a full-stack web application for personal task management, enabling users to register, log in, and perform CRUD operations (Create, Read, Update, Delete) on their individual tasks. The application ensures secure, user-specific task management and features a modern, intuitive user interface.',
                'technologies': 'Backend: Python, Django, Django Rest Framework, SQLite, djangorestframework-simplejwt (or TokenAuthentication), django-filter, django-cors-headers. Frontend: JavaScript, React.js, Material-UI (MUI), React Router DOM, Axios, React Toastify.',
                'link': 'https://github.com/MohamedKandil14/Django-React-Task-App.git'
            },
            {
                'name': 'Customer Churn Analysis',
                'description': 'Developed a comprehensive data analysis and machine learning project to identify factors contributing to customer churn and predict which customers are likely to leave, enabling targeted retention strategies.',
                'technologies': 'Python, Pandas, NumPy, Scikit-learn (for classification models like Logistic Regression, Decision Trees, or Random Forest), Matplotlib, Seaborn, Jupyter Notebooks, SQL (if data was retrieved from a database).',
                'link': 'https://github.com/MohamedKandil14/customer churn analysis.git'
            },
            {
                'name': 'House Price Prediction',
                'description': 'Developed a machine learning model to predict house prices based on various features and built an interactive dashboard to visualize the insights.',
                'technologies': 'Python, Scikit-learn, Pandas, NumPy, Matplotlib, Seaborn, Plotly, Streamlit (for dashboard/web app - if you implemented an interactive interface), Jupyter Notebooks.',
                'link': 'https://github.com/MohamedKandil14/house price prediction.git'
            },
            {
                'name': 'Product Price Comparator',
                'description': 'Developed a web app to compare product prices from various online stores.',
                'technologies': 'Python, Django, HTML, CSS, JavaScript, SQLite, requests, BeautifulSoup',
                'link': 'https://github.com/MohamedKandil14/product comparator.git'
            },
            {
                'name': 'Django E-commerce Site',
                'description': 'E-commerce platform built with Django demonstrating core functionalities.',
                'technologies': 'Python, Django, JavaScript, HTML, CSS, MySQL/PostgreSQL',
                'link': 'https://github.com/MohamedKandil14/Django E-commerce.git'
            },
            {
                'name': 'Web Scraper',
                'description': 'Dedicated tool to extract data from websites.',
                'technologies': 'Python, requests, BeautifulSoup',
                'link': 'https://github.com/MohamedKandil14/web scraper.git'
            },
            {
                'name': 'File Folder Organizer',
                'description': 'Script to automate file/folder organization.',
                'technologies': 'Python (os, shutil)',
                'link': 'https://github.com/MohamedKandil14/file folder organizer.git'
            },
            {
                'name': 'Bank Account System',
                'description': 'System simulating bank account operations.',
                'technologies': 'Python, SQLite/MySQL or file I/O',
                'link': 'https://github.com/MohamedKandil14/bank Account system.git'
            },
            {
                'name': 'Personal To-Do List App',
                'description': 'Personal task manager.',
                'technologies': 'Python, Django/Flask, HTML, CSS, JavaScript, SQLite/MySQL',
                'link': 'https://github.com/MohamedKandil14/Personal ToDo List App.git'
            },
            {
                'name': 'Expense Tracker',
                'description': 'App to track income and expenses.',
                'technologies': 'Python, SQLite/MySQL',
                'link': 'https://github.com/MohamedKandil14/expense-tracker.git'
            },
            {
                'name': 'Loly Store',
                'description': 'Basic e-commerce site.',
                'technologies': 'Python, Django',
                'link': 'https://github.com/MohamedKandil14/Loly store.git'
            },
            {
                'name': 'Django Task Management API',
                'description': 'A RESTful API built to manage user-specific tasks, enabling creation, retrieval, updating, and deletion of tasks with secure token-based authentication.',
                'technologies': 'Python, Django, Django REST Framework, SQLite (for development), Git',
                'link': 'https://github.com/MohamedKandil14/Django Task ManagementAPI.git'
            }
        ],
        'work_experience': [
            {
                'title': 'Engineering Courses Instructor',
                'company': 'Mind Valley Company',
                'duration': 'Oct 2023 - Present',
                'description': [
                    'Instruct web development using MERN stack, Artificial Intelligence, Robotics, and Arduino.',
                    'Taught Game Development (UNITY 2D & 3D) and Game Development for Children (Scratch, PictoBlox, Kodu).'
                ]
            },
            {
                'title': 'Coding Instructor',
                'company': 'Tatawar Training Academy',
                'duration': 'Jun 2023 - Oct 2023',
                'description': [
                    'Delivered instruction on Web Development (MERN Stack), Artificial Intelligence (AI), and Robotics (EV3, WEDO2.0, Arduino).'
                ]
            }
        ],
        'education': [
            {
                'degree': '9-Months Professional Diploma',
                'field': 'Open-Source Applications Development',
                'institution': 'Information Technology Institute (ITI) - Menofia Branch',
                'duration': 'Oct 2022 - Jun 2023'
            },
            {
                'degree': "Bachelor's Degree in Industrial Electronics and Control",
                'field': 'Electronics and Control Engineering',
                'institution': 'Faculty of Electronic Engineering, Menofia University',
                'duration': 'Sep 2015 - Jun 2019'
            }
        ],
        'training': [
            'InnovEgypt Program (TIEC)',
            'Robotics Workshop under Menoufia Robotics Club (Menofia University)'
        ],
        'personal_skills': ['Presentation Skills', 'Good Communicator', 'Leadership', 'Problem Solver', 'Reporting', 'Searching Skills', 'Quick Learner'],
        'languages': [
            {'lang': 'Arabic', 'level': 'Native'},
            {'lang': 'English', 'level': 'Very Good'}
        ],
        'extracurricular_interests': {
            'Volunteering': ['Hult Prize Foundation', 'Resala Charity'],
            'Hobbies & Interests': ['Learning languages', 'Reading', 'Travelling', 'Running']
        },
        'personal_info_details': {
            'Military Status': 'Completed (Reserved officer Nov 2019 - April 2022)',
            'Birth Date': '5 February 1995'
        }
    }
    return render_template('index.html', data=user_data)

if __name__ == '__main__':
    app.run(debug=True)
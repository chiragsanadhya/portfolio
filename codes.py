import streamlit as st
from PIL import Image

# Set up the page layout
st.set_page_config(page_title="Chirag's Portfolio", layout="wide", page_icon=":briefcase:")

# Cache the image loading to prevent reloading on each refresh
@st.cache_resource
def load_image(image_path):
    return Image.open(image_path)

# Cache the resume loading
@st.cache_data
def load_resume(resume_path):
    with open(resume_path, "rb") as file:
        return file.read()

# Sidebar setup
with st.sidebar:
    st.header("Navigation")
    st.markdown("About")
    st.markdown("Project")
    st.markdown("Skills")
    st.markdown("Certification")
    st.markdown("Contact")


    st.markdown("---")  # Divider
    st.header("Download Resume")
    resume_data = load_resume("RESUME.pdf")  # Ensure this file is in your directory
    st.download_button("📄 Download Resume", data=resume_data, file_name="Chirag_Resume.pdf", mime="application/pdf")

# Simplified CSS for the sidebar
st.markdown(
    """
    <style>
    /* Sidebar container styles */
    .css-1d391kg {
        background-color: #ffffff;  /* White background */
        padding: 20px;
        border-radius: 0;  /* No rounded corners */
        box-shadow: none;  /* No shadow */
    }

    /* Sidebar header styling */
    .css-1d391kg .css-1nrljmm {
        font-size: 18px;
        font-weight: bold;
        color: #333;  /* Dark text color for contrast */
        margin-bottom: 20px;
    }

    /* Sidebar link styling */
    .css-1d391kg .css-1v0mbdj {
        display: block;
        padding: 5px 0;
        color: #333;  /* Dark text color for visibility */
        text-decoration: none; /* Remove underline */
        font-size: 16px;
    }

    /* Hover effect for sidebar links (if desired) */
    .css-1d391kg .css-1v0mbdj:hover {
        color: #0073e6;  /* Change text color on hover */
    }

    /* Style for the download button */
    .css-1d391kg .css-4p3evm {
        margin-top: 20px;
        background-color: #0073e6;  /* Button background color */
        color: white;  /* Button text color */
        padding: 10px;
        border-radius: 5px;
        text-align: center;
        text-decoration: none;
    }
    .css-1d391kg .css-4p3evm:hover {
        background-color: #005bb5;  /* Button hover color */
    }
    </style>
    """,
    unsafe_allow_html=True
)





# CSS for navigation bar, project cards, and skills alignment
st.markdown(
    """
    <style>
    
    .card {
        background-color: #fff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin: 20px 0;
    }
    .skills-section {
        text-align: center;
    }
    .contact-links {
        margin-top: 20px;
        display: flex;
        justify-content: space-around;
        padding: 10px;
    }
    .contact-links a {
        background-color: #0073e6;
        padding: 12px 25px;
        color: white;
        border-radius: 8px;
        text-decoration: none;
        font-size: 16px;
        box-shadow: 3px 3px 10px rgba(0,0,0,0.2);
    }
    .contact-links a:hover {
        background-color: #005bb5;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# # Navigation Bar
# st.markdown(
#     """
#     <div class="nav">
#         <a href="#about">About</a>
#         <a href="#projects">Projects</a>
#         <a href="#skills">Skills</a>
#         <a href="#certifications">Certifications</a>
#         <a href="#contact">Contact</a>
#     </div>
#     """,
#     unsafe_allow_html=True
# )

# About Section
st.markdown("<h2 id='about'>About</h2>", unsafe_allow_html=True)
col1, col2 = st.columns(2, gap="medium")
with col1:
    image = load_image("20240206_212639.jpg")  # Replace with your image filename, cached for better performance
    st.image(image, use_column_width=True)
with col2:
    st.title("Hi, I'm Chirag!")
    st.write("""
    I'm a 3rd-year Artificial Intelligence and Data Science student, passionate about the fusion of cutting-edge technology and impactful solutions. 
    I have a strong background in machine learning, NLP, computer vision, and cloud computing. With a deep understanding of both theoretical concepts and practical applications, 
    I've developed multiple projects, ranging from sophisticated chatbots to automated data science tools like ModelMation.
    """)

# Projects Section
st.markdown("<h2 id='projects'>📂 Projects</h2>", unsafe_allow_html=True)
projects = {
    "ModelMatic": {
        "description": """
        A comprehensive data science automation tool that allows users to upload CSV files, select parameters, and train various models for regression or classification. 
        The project includes features like preprocessing, encoding, and detailed model evaluation. 
        Designed for ease of use, ModelMation streamlines the process of model training, making it accessible to both beginners and professionals.
        """,
        "tech_stack": ["Python", "Pandas", "Scikit-Learn", "Streamlit", "TensorFlow", "Docker"],
        "image": "Screenshot 2024-09-07 at 10.32.44 AM.png",  # Replace with your image filename
        "link": "https://github.com/chirag-sanadhya/ModelMatic"
    },
    "Plant Classification": {
        "description": """
        An advanced computer vision project that leverages deep learning models to accurately identify and classify different species of plants. 
        The project demonstrates expertise in image processing, feature extraction, and model optimization.
        """,
        "tech_stack": ["Python", "TensorFlow", "Keras", "OpenCV"],
        "image": "Screenshot 2024-09-07 at 10.35.28 AM.png",  # Replace with your image filename
        "link": "https://www.kaggle.com/code/chiragsanadhya/plant-disease-classification-using-cnn/notebook"
    },
    "Chatbot": {
        "description": """
        A sophisticated NLP-driven chatbot that utilizes transformer models for natural language understanding and response generation. 
        This project highlights my skills in NLP, dialogue management, and model fine-tuning, making it ideal for customer service or interactive applications.
        """,
        "tech_stack": ["Python", "Transformers", "Hugging Face", "TensorFlow", "Flask"],
        "image": "Screenshot 2024-09-07 at 10.42.34 AM.png",  # Replace with your image filename
        "link": "https://github.com/chiragsanadhya/chatbot-with-history"
    }
}

# Display project cards
for project, details in projects.items():
    st.markdown(f"### {project}")
    col1, col2 = st.columns([1, 2])
    with col1:
        project_image = load_image(details["image"])  # Cached image loading
        st.image(project_image, use_column_width=True)
    with col2:
        st.write(details["description"])
        st.write("**Tech Stack:** " + ", ".join(details["tech_stack"]))
        st.markdown(f"[View Project]({details['link']})", unsafe_allow_html=True)
    st.markdown("---")

# Skills Section
st.markdown("<h2 id='skills'>🛠️ Skills</h2>", unsafe_allow_html=True)

skills = {
    "Programming and Data Analysis": ["Python", "C++", "SQL", "NumPy", "Pandas", "Matplotlib", "Seaborn"],
    "Machine Learning and AI": ["Scikit-learn", "TensorFlow", "Keras", "Hugging Face Transformers", "Lamini (NLP and LLMs)", "Deep Learning", "Computer Vision", "NLP", "Large Language Models"],
    "Tools and Frameworks": ["OpenCV", "LangChain", "Groq"],
    "Cloud and Development": ["Docker", "Git", "GitHub", "CI/CD", "Flask", "Streamlit"]
}

# Display skills
for skill_category, skill_list in skills.items():
    st.markdown(f"### {skill_category}")
    st.markdown("<ul>" + "".join([f"<li>{skill}</li>" for skill in skill_list]) + "</ul>", unsafe_allow_html=True)
    st.markdown("---")

# Certifications Section
st.markdown("<h2 id='certifications'>🎓 Certifications</h2>", unsafe_allow_html=True)

certifications = {
    "Complete Machine Learning, NLP Bootcamp MLOPS & Deployment": {
        "author": "Krish Naik",
        "year": "2024",
        "description": "This bootcamp covered comprehensive topics in machine learning, NLP, MLOps, and deployment strategies, equipping me with advanced skills in building and managing ML models."
    },
    "Generative AI Bootcamp": {
        "author": "Krish Naik",
        "year": "2024",
        "description": "This bootcamp focused on generative AI techniques, including model training and fine-tuning for creating advanced AI solutions."
    }
}

# Display certifications
for cert, details in certifications.items():
    st.markdown(f"### {cert}")
    st.write(f"**Author:** {details['author']}")
    st.write(f"**Year:** {details['year']}")
    st.write(f"**Description:** {details['description']}")
    st.markdown("---")

# Contact Section
st.markdown("<h2 id='contact'>📧 Contact</h2>", unsafe_allow_html=True)

st.markdown("""
    <div class='contact-links'>
        <a href='https://www.linkedin.com/in/chirag-sanadhya/' target='_blank'>LinkedIn</a>
        <a href='https://github.com/chiragsanadhya' target='_blank'>GitHub</a>
        <a href='https://kaggle.com/chiragsanadhya' target='_blank'>Kaggle</a>
        <a href='https://x.com/Chirag5114' target='_blank'>Twitter</a>
        <a href='https://hashnode.com/@chiragsanadhya' target='_blank'>Hashnode</a>
        <a href='mailto:chiragsanadhya1411@gmail.com'>Email</a>
    </div>
""", unsafe_allow_html=True)

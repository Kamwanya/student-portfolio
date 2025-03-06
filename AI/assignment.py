import streamlit as st

# Set page config
st.set_page_config(page_title="My Digital Footprint", page_icon="🚀", layout="wide")

# Owner's Credentials (For Authentication)
OWNER_EMAIL = "umuhirenouswaibah@gmail.com"
OWNER_PASSWORD = "umuhire@250"

# Initialize session state for authentication
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Profile Details (Static)
PROFILE_DETAILS = {
    "name": "Umuhire Kamwanya",
    "location": "Musanze, Rwanda",
    "field_of_study": "Software Engineering, Year 3",
    "university": "INES Ruhengeri",
    "about_me": """I am Kamwanya, a passionate software engineering student graduating this year. 
    I am excited about technology’s ability to solve real-world problems and improve efficiency. 
    Currently, I am working on my final dissertation and a personal portfolio using Python Streamlit."""
}

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Skills", "Testimonials", "Contact", "Timeline"])

# Authentication Section
if page == "Home":
    st.title("🚀 My Digital Footprint – Showcasing My Journey")

    # Check if the user is authenticated
    if not st.session_state.authenticated:
        with st.form("login_form"):
            st.subheader("🔐 Admin Login (For Profile Editing)")
            email = st.text_input("Email")  # Removed type="email"
            password = st.text_input("Password", type="password")
            login_button = st.form_submit_button("Login")  # Fixed missing submit button

            if login_button:
                if email == OWNER_EMAIL and password == OWNER_PASSWORD:
                    st.session_state.authenticated = True
                    st.success("✅ Login successful! You can now update your profile picture.")
                else:
                    st.error("❌ Invalid email or password. Access denied!")

    # Display Profile Section
    st.subheader("👩‍💻 About Me")

    # Show current profile picture
    st.image("person.jpg", width=150, caption="Profile Picture")  

    # Allow only the owner to update profile picture after login
    if st.session_state.authenticated:
        uploaded_image = st.file_uploader("Upload a new profile picture", type=["jpg", "png"])
        if uploaded_image:
            with open("person.jpg", "wb") as file:
                file.write(uploaded_image.getbuffer())
            st.success("✅ Profile picture updated successfully! Refresh to see changes.")

    # Display Profile Details (Static)
    st.write(f"📍 **Location:** {PROFILE_DETAILS['location']}")
    st.write(f"📚 **Field of Study:** {PROFILE_DETAILS['field_of_study']}")
    st.write(f"🎓 **University:** {PROFILE_DETAILS['university']}")
    st.write(f"📝 **About Me:** {PROFILE_DETAILS['about_me']}")

    # Download Resume
    try:
        with open("resume1.pdf", "rb") as file:
            resume_bytes = file.read()
        st.download_button(label="📄 Download Resume", data=resume_bytes, file_name="resume1.pdf", mime="application/pdf")
    except FileNotFoundError:
        st.warning("⚠ Resume file not found. Please upload your resume.")

# Projects Page
elif page == "Projects":
    st.title("💻 My Projects")
    
    project_filter = st.selectbox("Filter by Category", ["All", "Year 1", "Year 2", "Year 3", "Dissertation"])
    
    projects = {
        "Year 1": "Library Management System - Python & SQLite",
        "Year 2": "Hotel Management System - Java & MySQL",
        "Year 3": "Car Rental System - Python & SQLite",
        "Dissertation": "Community Hub Group Management Platform - Java & MySQL"
    }
    
    for year, description in projects.items():
        if project_filter == "All" or project_filter == year:
            with st.expander(f"📌 {year} - {description}"):
                st.write(f"**Project Type:** Individual")
                st.write(f"**Description:** A system designed for {description}.")
                st.write("🔗 [GitHub](https://github.com/Kamwanya)")

# Skills Page
elif page == "Skills":
    st.title("⚡ Skills and Achievements")
    
    st.subheader("Programming Skills")
    skill_python = st.slider("Python", 0, 100, 90)
    st.progress(skill_python)
    
    skill_js = st.slider("JavaScript", 0, 100, 75)
    st.progress(skill_js)
    
    skill_AI = st.slider("Artificial Intelligence", 0, 100, 65)
    st.progress(skill_AI)

    skill_MachineLearning = st.slider("Machine Learning", 0, 100, 75)
    st.progress(skill_MachineLearning)

    skill_React = st.slider("React Js", 0, 100, 75)
    st.progress(skill_React)

    st.subheader("🏆 Certifications & Achievements")
    st.write("✔ High School Diploma in Education, from MIPC, 2019, Rwanda.")
    st.write("✔ University Transcript (Computer Science), from INES, 2023, Rwanda.")
    st.write("✔ Certificate of Good Food Prefect in High School, from MIPC, 2018, Rwanda.")

# Contact Page
elif page == "Contact":
    st.title("📬 Contact Me")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send Message")

        if submitted:
            st.success("✅ Message sent successfully!")

    st.write("📧 Email: umuhirenouswaibah@.com")
    st.write("[🔗 LinkedIn](https://linkedin.com/in/umuhire-kamwanya-4979071ab)")
    st.write("[📂 GitHub](https://github.com/Kamwanya)")

# Testimonials Page
elif page == "Testimonials":
    st.title("🗣️ Testimonials")

    st.write("🌟 *They used to say 'Girls can't code' 😏 but here my sister Kamwanya proved them wrong🤗 #GirlsPower💪!* – ULaurene")
    
    st.markdown("---")
    
    # Allow classmates or mentors to leave testimonials
    st.subheader("✍ Leave a Testimonial")
    
    with st.form("testimonial_form"):
        name = st.text_input("Your Name")
        relationship = st.selectbox("Your Relationship", ["Classmate", "Mentor", "Teammate", "Other"])
        testimonial_message = st.text_area("Your Testimonial")
        
        submitted = st.form_submit_button("Submit Testimonial")
        if submitted:
            if name and testimonial_message:
                st.success(f"✅ Thank you, {name}! Your testimonial has been submitted.")
                # Display the testimonial after submission
                st.write(f"🗨 {testimonial_message} — {name} ({relationship})")
            else:
                st.error("⚠ Please fill in all fields before submitting.")

# Timeline Section
elif page == "Timeline":
    st.title("⏳ Academic & Project Milestones")
    milestones = [
        "✅ Year 1: Completed First Major Project",
        "🏆 Year 2: Deep learning about different things",
        "💼 Year 3: Internship at IKIGUGU Company",
        "🌐 08-10-2025: Dissertation Submission",
    ]
    for milestone in milestones:
        st.write(milestone)

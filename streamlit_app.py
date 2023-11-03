import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

#Display Title and Description 
st.title("Welcome to this months classroom engagement survey")
st.markdown("Fill out the survey below")

conn = st.connection("gsheets",type=GSheetsConnection)

existing_data = conn.read(worksheet="Entries", usecols=list(range(12)), ttl=5)
existing_data = existing_data.dropna(how="all")

st.dataframe(existing_data)

# # Display Title and Description
# st.title("Teacher Classroom Survey")
# st.markdown("Please fill out the survey below to provide insights about your classroom and teaching environment.")

# # Demographic Information
# st.header("Demographics")
# teacher_name = st.text_input("Your Name")
# school_name = st.text_input("School Name")
# grade_level = st.selectbox("Grade Level", ["Pre-K", "Elementary", "Middle School", "High School"])
# city = st.text_input("City")
# state = st.text_input("State")
# country = st.text_input("Country")

# # Classroom Resources
# st.header("Classroom Resources")
# resources_used = st.multiselect("Select the resources you use in your classroom (check all that apply)", 
#     ["Textbooks", "Interactive Whiteboard", "Laptops or Computers", "Art Supplies", "Educational Apps", "Other"])
# other_resource = ""
# if "Other" in resources_used:
#     other_resource = st.text_input("Please specify other resources:")

# # Multiple Choice Question
# st.header("Popular Classroom Tools and Assets")
# popular_choices = [
#     "SmartBoard",
#     "Document Camera",
#     "Tablet or iPad",
#     "Projector",
#     "Graphing Calculator",
#     "Classroom Library",
# ]

# selected_assets = st.multiselect("Select the tools/assets you use in your classroom (check all that apply)", popular_choices)

# # Teaching Environment
# st.header("Teaching Environment")
# class_size = st.slider("Average Class Size", min_value=1, max_value=50)
# teaching_style = st.radio("Teaching Style", ["Traditional", "Interactive", "Project-Based", "Other"])
# if teaching_style == "Other":
#     custom_teaching_style = st.text_input("Please specify your teaching style:")

# challenges = st.text_area("What are the biggest challenges you face in your classroom?")

# # Submit Button
# st.markdown("Your feedback is important. Click the button below to submit your survey.")
# submit_button = st.button("Submit Your Classroom Survey")

# # If the submit button is pressed
# if submit_button:
#     survey_data = pd.DataFrame(
#         {
#             "Teacher Name": [teacher_name],
#             "School Name": [school_name],
#             "Grade Level": [grade_level],
#             "City": [city],
#             "State": [state],
#             "Country": [country],
#             "Resources Used": [", ".join(resources_used)],
#             "Other Resources": [other_resource],
#             "Popular Tools/Assets": [", ".join(selected_assets)],
#             "Class Size": [class_size],
#             "Teaching Style": [custom_teaching_style if teaching_style == "Other" else teaching_style],
#             "Challenges": [challenges]
#         }
#     )
    
#     update_df = pd.concat([existing_data, survey_data], ignore_index=True)
    
#     conn.update(worksheet="Surveys", data=update_df)   
#     # Save or send the survey data as needed
#     st.write("Your Classroom Survey Has Been Submitted!")

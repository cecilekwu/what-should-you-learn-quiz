import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image


image = Image.open('L&D Quiz Banner.png')


# Function to display header image
def display_header_image():
   st.image(image, use_container_width=True)




# Intro page
def intro_page():
   display_header_image()
   st.title("What Kind of Learner Are You?")
   st.write("Just like different ski slopes, everyone's career journey has its own twists, turns, and peaks. Need help navigating your path to success? Take this quiz to find out what kind of learner you are, then get a ski pass to the perfect course to kickstart your Learning @ Snowflake journey. \n\nAfter getting your result, hit the slopes in your career development by checking out all offerings on the [Learning @ Snowflake site](https://thefridge--simpplr.vf.force.com/apex/simpplr__app?u=/site/a14Ui000001URGjIAO/dashboard) - including in-person, virtual, and self-guided lessons. \n\nFor internal sharing only.")
  
   if st.button("Start Quiz"):
       st.session_state.current_question_index = 1  # Move to the first question
       st.session_state.answers = {}  # Reset answers on quiz restart
       st.rerun()  # Trigger rerun to load the first question page




# Question pages
def question_page(question, options):
   display_header_image()
   st.title("What Kind of Learner Are You?")
  
   # Display the question number (Question 1, Question 2, etc.)
   question_number = st.session_state.current_question_index
   st.header(f"Question {question_number}:")
   st.write(question)
  
   # Radio button for selecting an answer
   selected_option = st.radio("Choose one:", options, key=f"q{question_number}")
  
   # Store the selected answer
   if selected_option:
       st.session_state[f"answer_{question_number}"] = selected_option
  
   # Only show the Next button when an answer has been selected
   if selected_option:
       if st.button("Next"):
           st.session_state.current_question_index += 1  # Move to the next question
           st.rerun()  # Trigger a rerun to show the next question




# Results page
def result_page():
   display_header_image()
   st.title("What Kind of Learner You Are...")
   st.write("Thank you for completing the quiz!")


   # Get answers
   answers = [st.session_state.get(f"answer_{i}") for i in range(1, 5)]


   # Determine personality
   personality = determine_personality(answers)


   # Display personality type
   st.write("**Your recommended course is:**", personality)


   # Display personality description and image
   personality_descriptions = {
       "People Leader Workshops": {
           "description": "You learn through action, not just theory. You absorb information best when you’re teaching or explaining it to someone else - because learning is also about paying it forward. You’ve never met a whiteboard you didn’t like, and you probably spend more time preparing for meetings than actually having them. You may or may not have made a few TED Talk-style presentations just for fun. \n\nIn [this program](https://https://wd5.myworkday.com/snowflake/learning/program/4686a758f52610014e452e4828200001?type=2d29754fdb8e100008b50ff6bc94003b), you will master the art of effective leadership. In 'Prioritizing With Your Team,' become a strategic 'Navigator' using frameworks like the Eisenhower Matrix, guided by our AI GPT coach. In 'Communicating with Clarity and Impact,' transform into a 'Conductor' who delivers impactful messages, develops clear templates, and refines your skills with our AI Communication Coach.",
           "image": "PLW.png"
       },
       "Irresistible: Building Your Brand": {
           "description": "You're the Architect. You know that success isn’t just about what you do, it’s about how people perceive your work. You’re constantly looking for ways to refine your presence, build credibility, and make a lasting impact. Whether it’s through storytelling, strategic networking, or simply showing up as your best self, you want to shape your reputation with intention. \n\nIn [this course](https://wd5.myworkday.com/snowflake/learning/course/4686a758f5261001b4ed3a045de60000?type=9882927d138b100019b6a2df1a46018b), you’ll identify the strengths that have propelled you forward and uncover habits that may be holding you back. Through interactive discussions and reflection exercises, you’ll walk away with a clear, confident personal brand that aligns with your next big career move.",
           "image": "BYB1.png"
       },
       "What Got You Here, Won’t Get You There": {
           "description": "You're the Trailblazer. You’re ambitious, driven, and always pushing forward, but sometimes, old habits can slow you down. You recognize that growth isn’t just about working harder; it’s about working smarter. You’re ready to let go of limiting behaviors and embrace the mindset shifts that will take your career to the next level. \n\n[In this course,](https://wd5.myworkday.com/snowflake/learning/course/6d6fc9e7540b10016e9979a636d40000?type=9882927d138b100019b6a2df1a46018b) you’ll explore common career roadblocks and develop strategies to overcome them. You’ll leave with a personalized action plan to refine your approach, enhance your effectiveness, and keep climbing.",
           "image": "WGY.png"
       },
       "Snowflake Technical Learning": {
           "description": "You’re a curious, experimental learner who loves understanding the ‘why’ behind everything. You’re constantly testing new ways to boost your brain so you can work smarter, not harder. You’ve probably had a mental debate over whether you should ‘optimize your circadian rhythm’ or just keep drinking coffee. You’ve definitely tried meditation at least once, but only after googling how. \n\n[In this course](https://wd5.myworkday.com/snowflake/learning/course/99397b597d241001e6f1a10379cb0000?type=9882927d138b100019b6a2df1a46018b) , offered through Data Camp, will explore all the way from Snowflake’s foundationals to mastering advanced SQL techniques. You'll start by uncovering Snowflake's distinct architecture and grasping fundamental database concepts, including DDL (Data Definition Language) and DML (Data Manipulation Language).",
           "image": "TL.png"
       }
   }


   if personality in personality_descriptions:
       st.write(personality_descriptions[personality]["description"])
       st.image(personality_descriptions[personality]["image"])
   else:
       st.write("No description available for this personality type.")




# Determine personality based on answers
def determine_personality(answers):
   # Define personality types and their corresponding answer combinations
   personality_types = {
       ("Being an effective people manager and leading my team to (professional) glory!", "Those big, visible moments where teamwork makes the dream work", "Assemble key partners and analyze the situation together", "A free-flowing class on a creative subject - like writing, music, or photography"): "People Leader Workshops",
       ("Being an effective people manager and leading my team to (professional) glory!", "Leading projects that align with my personal brand", "Assemble key partners and analyze the situation together", "A free-flowing class on a creative subject - like writing, music, or photography"): "People Leader Workshops",
       ("Being an effective people manager and leading my team to (professional) glory!", "Leading projects that align with my personal brand", "Gather more information, then propose an action plan to the team", "A free-flowing class on a creative subject - like writing, music, or photography"): "People Leader Workshops",
       ("Being an effective people manager and leading my team to (professional) glory!", "Those big, visible moments where teamwork makes the dream work", "Gather more information, then propose an action plan to the team", "A free-flowing class on a creative subject - like writing, music, or photography"): "People Leader Workshops",
       ("Honing my skills and understanding what makes me uniquely successful!", "Leading projects that align with my personal brand", "Gather more information, then propose an action plan to the team", "A free-flowing class on a creative subject - like writing, music, or photography"): "Irresistible: Building Your Brand",
       ("Honing my skills and understanding what makes me uniquely successful!", "Those big, visible moments where teamwork makes the dream work", "Gather more information, then propose an action plan to the team", "A free-flowing class on a creative subject - like writing, music, or photography"): "Irresistible: Building Your Brand",
       ("Honing my skills and understanding what makes me uniquely successful!", "Leading projects that align with my personal brand", "Assemble key partners and analyze the situation together", "A free-flowing class on a creative subject - like writing, music, or photography"): "Irresistible: Building Your Brand",
       ("Honing my skills and understanding what makes me uniquely successful!", "Those big, visible moments where teamwork makes the dream work", "Assemble key partners and analyze the situation together", "A free-flowing class on a creative subject - like writing, music, or photography"): "Irresistible: Building Your Brand",
       ("Being an effective people manager and leading my team to (professional) glory!", "Those big, visible moments where teamwork makes the dream work", "Gather more information, then propose an action plan to the team", "A structured class on a technical subject - like personal finance, physics, or architecture"): "What Got You Here, Won’t Get You There",
       ("Being an effective people manager and leading my team to (professional) glory!", "Leading projects that align with my personal brand", "Gather more information, then propose an action plan to the team", "A structured class on a technical subject - like personal finance, physics, or architecture"): "What Got You Here, Won’t Get You There",
       ("Being an effective people manager and leading my team to (professional) glory!", "Those big, visible moments where teamwork makes the dream work", "Assemble key partners and analyze the situation together", "A structured class on a technical subject - like personal finance, physics, or architecture"): "What Got You Here, Won’t Get You There",
       ("Being an effective people manager and leading my team to (professional) glory!", "Leading projects that align with my personal brand", "Assemble key partners and analyze the situation together", "A structured class on a technical subject - like personal finance, physics, or architecture"): "What Got You Here, Won’t Get You There",
       ("Honing my skills and understanding what makes me uniquely successful!", "Leading projects that align with my personal brand", "Gather more information, then propose an action plan to the team", "A structured class on a technical subject - like personal finance, physics, or architecture"): "Snowflake Technical Learning",
       ("Honing my skills and understanding what makes me uniquely successful!", "Those big, visible moments where teamwork makes the dream work", "Gather more information, then propose an action plan to the team", "A structured class on a technical subject - like personal finance, physics, or architecture"): "Snowflake Technical Learning",
       ("Honing my skills and understanding what makes me uniquely successful!", "Leading projects that align with my personal brand", "Assemble key partners and analyze the situation together", "A structured class on a technical subject - like personal finance, physics, or architecture"): "Snowflake Technical Learning",
       ("Honing my skills and understanding what makes me uniquely successful!", "Those big, visible moments where teamwork makes the dream work", "Assemble key partners and analyze the situation together", "A structured class on a technical subject - like personal finance, physics, or architecture"): "Snowflake Technical Learning",
   }


   # Check if the answers match any of the predefined combinations
   for combination, personality in personality_types.items():
       if all(answer in combination for answer in answers):
           return personality


   return "Unknown"




# Initialize current_question_index if not already initialized
if 'current_question_index' not in st.session_state:
   st.session_state.current_question_index = 0




# Main function
def main():
   if st.session_state.current_question_index == 0:
       intro_page()
   elif st.session_state.current_question_index <= 4:  # Ensure it's within the valid range of questions
       questions = [
           "What are you aspiring for in your career right now?",
           "What makes you feel fulfilled in your career?",
           "You've just spotted a potential issue with a project. Do you first...",
           "What type of class would you rather take?"
       ]
       options = [
           ("Being an effective people manager and leading my team to (professional) glory!", "Honing my skills and understanding what makes me uniquely successful!"),
           ("Those big, visible moments where teamwork makes the dream work", "Leading projects that align with my personal brand"),
           ("Assemble key partners and analyze the situation together", "Gather more information, then propose an action plan to the team"),
           ("A free-flowing class on a creative subject - like writing, music, or photography", "A structured class on a technical subject - like personal finance, physics, or architecture")
       ]
      
       question = questions[st.session_state.current_question_index - 1]
       option = options[st.session_state.current_question_index - 1]
       question_page(question, option)
   else:
       result_page()




if __name__ == "__main__":
   main()


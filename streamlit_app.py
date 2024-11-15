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
       "For Leaders: Communicating with Clarity and Impact": {
           "description": "You learn through action, not just theory. You absorb information best when you're teaching or explaining it to someone else - because learning is also about paying it forward. You've never met a whiteboard you didn't like, and you probably spend more time preparing for meetings than actually having them. You may or may not have made a few TED Talk-style presentations just for fun. \n\nIn [this course](https://wd5.myworkday.com/snowflake/learning/program/4686a758f52610014e452e4828200001?type=2d29754fdb8e100008b50ff6bc94003b), you'll practice crafting concise, clear, and tailored messages that meet your team's needs. Learn how to relay leadership updates effectively and develop your own communication template. You'll also gain hands-on experience with our AI Communication Coach to sharpen your skills in delivering messages that drive both understanding and action.",
           "image": "CC&impact.png"
       },
       "For Leaders: Feedback and Coaching": {
           "description": "You're a reflective learner who believes in growth through feedback - you see the importance of conversations, feedback loops, and collaboration. You love those 'Wow, I didn't think about it that way' moments, and later bestowing that wisdom on others. Your friends likely come to you for advice about their careers, relationships, and even which brand of toothpaste they should buy. \n\nIn [this course](https://wd5.myworkday.com/snowflake/learning/program/4686a758f52610014e452e4828200001?type=2d29754fdb8e100008b50ff6bc94003b), we'll focus on delivering quality feedback that supports development and performance growth. You'll get hands-on practice with the Situation-Behavior-Impact (SBI) model, learning not only from your peers but also with support from our AI Feedback Coach. Through interactive discussions and practice, you'll refine your skills to handle coaching conversations with confidence.",
           "image": "FC.png"
       },
       "Own Your Career": {
           "description": "You're a driven learner who learns best when you have control over your own pace and direction. You regularly evaluate where you can improve and what new skills you can acquire. You're likely trying to map out your 'personal brand.' You spend more time on LinkedIn than you'd like to admit, and your goals for the next 10 years are on a sticky note somewhere in your office. \n\n[The program](https://wd5.myworkday.com/snowflake/learning/program/a7a9f37b5bf41001bc095eab9b1d0000?type=2d29754fdb8e100008b50ff6bc94003b) includes a self-paced eLearning course and an opt-in virtual peer-breakout workshop. Learn the basics on your own then join us for a workshop to refine your plan with peer breakouts and facilitator support. These sessions are designed to complement each other, but can be taken separately for a flexible learning experience.",
           "image": "OYC.png"
       },
       "Your Brain at Work: Neuroscience of Success": {
           "description": "You're a curious, experimental learner who loves understanding the 'why' behind everything. You're constantly testing new ways to boost your brain so you can work smarter, not harder. You've probably had a mental debate over whether you should 'optimize your circadian rhythm' or just keep drinking coffee. You've definitely tried meditation at least once, but only after googling how. \n\n[This live workshop](https://wd5.myworkday.com/snowflake/learning/course/99397b597d241001e6f1a10379cb0000?type=9882927d138b100019b6a2df1a46018b) shares neuroscience-backed strategies that will help you learn how to create brain-friendly environments, leverage oxytocin-boosting collaboration models, and practice self-care techniques that optimize your neural performance.",
           "image": "brain.png"
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
        ("Being an effective people manager and leading my team to (professional) glory!", "Those big, visible moments where teamwork makes the dream work", "Assemble key partners and analyze the situation together", "A free-flowing class on a creative subject - like writing, music, or photography"): "For Leaders: Communicating with Clarity and Impact",
        ("Being an effective people manager and leading my team to (professional) glory!", "Leading projects that align with my personal brand", "Assemble key partners and analyze the situation together", "A free-flowing class on a creative subject - like writing, music, or photography"): "For Leaders: Communicating with Clarity and Impact",
        ("Being an effective people manager and leading my team to (professional) glory!", "Leading projects that align with my personal brand", "Gather more information, then propose an action plan to the team", "A free-flowing class on a creative subject - like writing, music, or photography"): "For Leaders: Communicating with Clarity and Impact",
        ("Being an effective people manager and leading my team to (professional) glory!", "Those big, visible moments where teamwork makes the dream work", "Gather more information, then propose an action plan to the team", "A free-flowing class on a creative subject - like writing, music, or photography"): "For Leaders: Communicating with Clarity and Impact",
        ("Honing my skills and understanding what makes me uniquely successful!", "Leading projects that align with my personal brand", "Gather more information, then propose an action plan to the team", "A free-flowing class on a creative subject - like writing, music, or photography"): "Own Your Career",
        ("Honing my skills and understanding what makes me uniquely successful!", "Those big, visible moments where teamwork makes the dream work", "Gather more information, then propose an action plan to the team", "A free-flowing class on a creative subject - like writing, music, or photography"): "Own Your Career",
        ("Honing my skills and understanding what makes me uniquely successful!", "Leading projects that align with my personal brand", "Assemble key partners and analyze the situation together", "A free-flowing class on a creative subject - like writing, music, or photography"): "Own Your Career",
        ("Honing my skills and understanding what makes me uniquely successful!", "Those big, visible moments where teamwork makes the dream work", "Assemble key partners and analyze the situation together", "A free-flowing class on a creative subject - like writing, music, or photography"): "Own Your Career",
        ("Being an effective people manager and leading my team to (professional) glory!", "Those big, visible moments where teamwork makes the dream work", "Gather more information, then propose an action plan to the team", "A structured class on a technical subject - like personal finance, physics, or architecture"): "For Leaders: Feedback and Coaching",
        ("Being an effective people manager and leading my team to (professional) glory!", "Leading projects that align with my personal brand", "Gather more information, then propose an action plan to the team", "A structured class on a technical subject - like personal finance, physics, or architecture"): "For Leaders: Feedback and Coaching",
        ("Being an effective people manager and leading my team to (professional) glory!", "Those big, visible moments where teamwork makes the dream work", "Assemble key partners and analyze the situation together", "A structured class on a technical subject - like personal finance, physics, or architecture"): "For Leaders: Feedback and Coaching",
        ("Being an effective people manager and leading my team to (professional) glory!", "Leading projects that align with my personal brand", "Assemble key partners and analyze the situation together", "A structured class on a technical subject - like personal finance, physics, or architecture"): "For Leaders: Feedback and Coaching",
        ("Honing my skills and understanding what makes me uniquely successful!", "Leading projects that align with my personal brand", "Gather more information, then propose an action plan to the team", "A structured class on a technical subject - like personal finance, physics, or architecture"): "Your Brain at Work: Neuroscience of Success",
        ("Honing my skills and understanding what makes me uniquely successful!", "Those big, visible moments where teamwork makes the dream work", "Gather more information, then propose an action plan to the team", "A structured class on a technical subject - like personal finance, physics, or architecture"): "Your Brain at Work: Neuroscience of Success",
        ("Honing my skills and understanding what makes me uniquely successful!", "Leading projects that align with my personal brand", "Assemble key partners and analyze the situation together", "A structured class on a technical subject - like personal finance, physics, or architecture"): "Your Brain at Work: Neuroscience of Success",
        ("Honing my skills and understanding what makes me uniquely successful!", "Those big, visible moments where teamwork makes the dream work", "Assemble key partners and analyze the situation together", "A structured class on a technical subject - like personal finance, physics, or architecture"): "Your Brain at Work: Neuroscience of Success",
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
            "What sounds like a good plan for your career right now?",
            "At work, besides free granola bars, what do you love?",
            "Crisis! You've just spotted a potential issue with a project. Do you first...",
            "Which type of class would you grab a seat in?"
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

import streamlit as st
import random
from PIL import Image

st.title("Guessing Game")
st.subheader("Guess the right number to win")

img = Image.open("gg.png")
st.sidebar.image(img)

st.sidebar.markdown(
    """## How to play?
    Choose a random number from 1 to 6
    Test your guessing Intuition
    """
)
st.sidebar.markdown(':flag-ng::flag-ng::flag-ng::balloon::balloon::balloon::flag-ng::flag-ng::flag-ng:')

st.image('dice.gif')

x = st.number_input("Choose a number from 1 - 6",step=1,min_value=1,max_value=6)
y = random.randint(1,6)

def game(x,y):
    if x > 6:
        st.error("Invalid Input: Please choose a number from 1 - 6")
    else:
        if x == y:
            st.balloons()
            return("Correct")
        else:
            st.write(f"Your selected number is {x}")
            st.write(f"Random number {y}")
            return ("wrong, try again")
if st.button("Try Your Luck"):
    st.write(game(x,y))

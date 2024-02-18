import streamlit as st

def run():
  st.set_page_config(
    page_title="Hello",
    page_icon="👋",
  )

  st.title("Machine Learning Notes")
  # Read contents from a file and display it
  with open("hello.txt") as f:
    st.write(f.read())
if __name__ == "__main__":
  run()
    


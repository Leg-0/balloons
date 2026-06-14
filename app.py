import streamlit as st
import time


def main():
    if st.button("Ballons for Jacob"):
        st.balloons()

    if st.button("Never ending balloons for Jacob [:red[DANGER]]"):
        while True:
            st.balloons()
            time.sleep(1)


if __name__ == "__main__":
    main()

import streamlit as st


def authenticated_menu():
    # st.sidebar.page_link("Welcome.py", label=f"Welcome {st.user.given_name}",icon="👋")
    # st.sidebar.page_link("pages/1_Topics.py", label="Topics → 🔖", icon="📚")
    st.sidebar.page_link("pages/2_YouTube.py", label="YouTube → 🔖", icon="📹")
    
def unauthenticated_menu():
#   st.sidebar.page_link("Welcome.py", label="Welcome Here",icon="👋")
  st.sidebar.page_link("pages/2_YouTube.py", label="YouTube → 🔖", icon="📹")
  
def menu():
    if st.user.is_logged_in == False:
        unauthenticated_menu()
        return
    authenticated_menu()

def menu_with_redirect():
    if st.user.is_logged_in == False:
        st.switch_page("Welcome.py")
    menu()
import streamlit as st
import pandas as pd
import uuid
import pyarrow as pa

st.set_page_config(page_title='NextReach', page_icon="📝")

hide_menu = """
<style>
#MainMenu{
visibility:hidden;
}
footer{visibility:hidden;}
 footer:after{
   visibility:visible;
   content:'Copyright @ 2023: Nabil Nabawi';
   display:block;
   position:relative;
   color:white;
 }
</style>
"""

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("pages/style2.css")

def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://raw.githubusercontent.com/nabilnabawi1234/projectpython/main/logo320.png);
                background-repeat: no-repeat;
                padding-top: 150px;
                background-position: 5px 5px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "        ";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

add_logo()

file_dir = 'pages'
file_name = 'df.csv'
filepath = f"{file_dir}/{file_name}"

def is_valid_skill(skill):
    return skill is not None and skill.strip() != '' and len(skill) <= 50

def main():
    df1 = pd.read_csv(filepath)
    skills_before_update = df1['skill'].tolist()

    with st.sidebar.form(key='df1', clear_on_submit=True):
        add_col1 = str(uuid.uuid4())
        add_col2 = st.text_input('Skill')
        submit_add = st.form_submit_button('Add Skill')

    with st.sidebar.form(key='delete_form', clear_on_submit=True):
        delete_col = st.selectbox('Select Skill to Delete', df1['skill'].tolist())
        submit_delete = st.form_submit_button('Delete Skill')

    with st.sidebar.form(key='update_form', clear_on_submit=True):
        update_col = st.selectbox('Select Skill to Update', df1['skill'].tolist())
        updated_value = st.text_input('Enter Updated Skill', value=update_col)
        submit_update = st.form_submit_button('Update Skill')

    if submit_add:
        if is_valid_skill(add_col2) and add_col2 not in df1['skill'].tolist():
            new_data = {'skill_ID': add_col1, 'skill': add_col2}
            new_row = pd.DataFrame([new_data])
            df1 = pd.concat([df1, new_row], ignore_index=True)
            df1.to_csv(filepath, index=False)
            st.success('Skill Added Successfully!')
        elif add_col2 in df1['skill'].tolist():
            st.error('Skill already exists in the database!')
        else:
            st.error('Invalid Skill! Please enter a non-empty skill with a maximum of 50 characters.')

    if submit_delete:
        df1 = df1[df1['skill'] != delete_col]
        df1.to_csv(filepath, index=False)
        st.success('Skill Deleted Successfully!')

    if submit_update:
        df1.loc[df1['skill'] == update_col, 'skill'] = updated_value
        df1.to_csv(filepath, index=False)
        st.success('Skill Updated Successfully!')

    table = pa.Table.from_pandas(df1[['skill']], schema=pa.schema([
        ('skill', pa.string())
    ]))

    st.header('Skills')
    st.table(df1[['skill']])

if __name__ == '__main__':
    main()

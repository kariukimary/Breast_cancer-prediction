import streamlit as st
import pickle
import mysql.connector

# Load the trained model
model = pickle.load(open('/home/mary/projects/fourth_year project/cancer_stage.pkl', 'rb'))

# Function to connect to MySQL database
def connect_to_database():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="new_password",
        database="streamlit_login"
    )
    return conn

# Function to save user inputs to the database
def save_user_inputs(T_stage, N_stage, grade, a_stage, tumor_size, estrogen_status, progesterone, regional_node_examined, regional_node_positive):
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        query = "INSERT INTO user_inputs (T_stage, N_stage, grade, a_stage, tumor_size, estrogen_status, progesterone, regional_node_examined, regional_node_positive) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (T_stage, N_stage, grade, a_stage, tumor_size, estrogen_status, progesterone, regional_node_examined, regional_node_positive))
        conn.commit()
        cursor.close()
        conn.close()

# Main function to create the Streamlit application
def stages():
    st.title("Breast Cancer Stage Prediction")

    # Input fields
    col1, col2 = st.columns(2)  

    with col1:
        T_stage_options = ['T1', 'T2', 'T3', 'T4']
        T_stage = st.selectbox("T Stage: (tumor stage)", T_stage_options)

        N_stage_options = ['N1', 'N2', 'N3']
        N_stage = st.selectbox("N Stage: (nodal stage)", N_stage_options)

        grade_options = ['Well differentiated; Grade I', 'Moderately differentiated; Grade II', 'Poorly differentiated; Grade III', 'Undifferentiated; anaplastic; Grade IV']
        grade = st.selectbox("Grade: (grade of the tumor under microscope)", grade_options)

        a_stage_options = ['Regional', 'Distant']
        a_stage = st.selectbox("A Stage: (extent of disease)", a_stage_options)
        tumor_size = st.number_input("Tumor Size: (size of the tumor)")
    
    with col2:
        estrogen_status_options = ['positive', 'negative']
        estrogen_status = st.selectbox("Estrogen Status:(receptors for estrogen)", estrogen_status_options)

        progesterone_options = ['positive', 'negative']
        progesterone = st.selectbox("Progesterone Status: (receptors for progesterone)", progesterone_options)

        regional_node_examined = st.number_input("Regional Node Examined: (lymph nodes )")
        regional_node_positive = st.number_input("Regional Node Positive: (positive lymph nodes )")

    # Converting string features to numeric values
    T_stage_mapping = {'T1': 0, 'T2': 1, 'T3': 2, 'T4': 3}
    N_stage_mapping = {'N1': 0, 'N2': 1, 'N3': 2}
    grade_mapping = {'Well differentiated; Grade I': 1, 'Moderately differentiated; Grade II': 2,
                     'Poorly differentiated; Grade III': 3, 'Undifferentiated; anaplastic; Grade IV': 4}
    a_stage_mapping = {'Regional': 1, 'Distant': 0}
    estrogen_status_mapping = {'positive': 1, 'negative': 0}
    progesterone_mapping = {'positive': 1, 'negative': 0}

    T_stage = T_stage_mapping.get(T_stage, 0)
    N_stage = N_stage_mapping.get(N_stage, 0)
    grade = grade_mapping.get(grade, 0)
    a_stage = a_stage_mapping.get(a_stage, 0)  
    estrogen_status = estrogen_status_mapping.get(estrogen_status, 0)
    progesterone = progesterone_mapping.get(progesterone, 0)

    # Prediction
    if st.button('Predict', key='predict_button'):
        input_data = [
            [T_stage, N_stage, grade, a_stage, tumor_size, estrogen_status, progesterone, regional_node_examined, regional_node_positive]
        ]
        
        prediction = model.predict(input_data)
        st.success(f'You are in Stage {prediction[0]}')

        # Save user inputs to the database
        save_user_inputs(T_stage, N_stage, grade, a_stage, tumor_size, estrogen_status, progesterone, regional_node_examined, regional_node_positive)

# Entry point of the application
if __name__ == '__main__':
    stages()

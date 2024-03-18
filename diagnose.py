import streamlit as st
import pickle
# import staging
from streamlit_extras.switch_page_button import switch_page

model = pickle.load(open('/home/mary/projects/fourth_year project/diagnoses2.pkl', 'rb'))

def cancer():
    st.title("Breast Cancer Prediction")

    col1, col2 = st.columns(2)  
    

    with col1:
        
        clump= st.text_input("clump_thickness: (cell thickness)")
        size = st.text_input("size_uniformity: (cell size)")
        shape = st.text_input("shape_uniformity: (cell shape)")
        marginal = st.text_input("marginal_adhesion:(cell attachment to surrounding tissues)")
        
    with col2:
        epith = st.text_input("epithelial_size:(lining of organs)")
        bland = st.text_input("bland_chromatin: (appearance of the chromatin)")
        normal = st.text_input("normal_nucleoli:(normal cells)")   
        mit = st.text_input("mitoses:(figures in tissues)")
     

    if st.button('Predict'):
        # Making prediction
        makeprediction = model.predict([[clump, size, shape,marginal, epith, bland,normal, mit,]])
        

        if makeprediction[0] == 4:
            st.success("You have breast cancer")
             
        
        else:
            
            st.success("You don't have breast cancer")
            
           
    col3, col4= st.columns(2) 
    with col3: 
        button2=st.button('stage of patient')
        if button2:

            switch_page('Staging')
    
    with col4:
        button3=st.button('advise patient')
        if button3:
            switch_page('patient')

  

if __name__ == "__main__":
    cancer()

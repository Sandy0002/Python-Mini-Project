import streamlit as st

wt_units = st.selectbox("Select weight units", ("Pounds", "Kilograms"))
st.write()
try:
    if (wt_units =="Pounds"):
        weight = st.text_input("Enter your weight (lbs)")
        wt= int(weight) # converting to kgs
        height = st.text_input("Enter your height (ft and inches) ")
        height = int(height[0])*12 + int(height[2:4])

    else:
        weight = st.text_input("Enter your weight (kgs)"
        wt = int(weight)

        height = st.text_input("Enter your height in (mts or cms)")
        if(float(height)<=2):
            height = float(height)
        else:
            height = int(height)/100


    bmi_cat = [(18.5,'Underweight'), (24.9,'Healthy Weight'), (29.9,'Overweight'),(float('inf'),'Obesity')]

    if (wt_units == "Pounds"):
        bmi_val = (wt*703)/height**2
    else:
        bmi_val = wt/(height**2)

    for i,j in bmi_cat:
        if(bmi_val<=i):
            st.write("Your bmi is %.2f means it is %s"%(bmi_val, j))
            break
except:
    pass

description = st.text_area("Any explanation:")

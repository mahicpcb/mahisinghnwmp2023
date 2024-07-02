import pandas as pd
import streamlit as st
import altair as alt
import matplotlib.pyplot as plt

# Function to load data
@st.cache
def load_data(file_path):
    return pd.read_excel(file_path)

background_color = """
<style>
body {
    background-color: #f0f0f0; /* Replace with your desired background color */
}
</style>
"""

# Display the custom CSS
st.markdown(background_color, unsafe_allow_html=True)
# Title and Header
st.title('NWMP Data-2023')
st.header('State-wise Data')

# Dropdown for selecting state-wise data 
file_name = st.selectbox(label='Choose State Data', options=[
    'ANDHRA PRADESH.xlsx', 'ARUNACHAL PRADESH.xlsx', 'ASSAM.xlsx', 'BIHAR.xlsx',
    'CHHATTISGARH.xlsx', 'DAMAN AND DIU, DADRA AND NAGAR HAVELI.xlsx', 'DELHI.xlsx',
    'GOA.xlsx', 'GUJARAT.xlsx', 'HARYANA.xlsx', 'HIMACHAL PRADESH.xlsx',
    'JAMMU & KASHMIR.xlsx', 'JHARKHAND.xlsx', 'KARNATAKA.xlsx', 'KERALA.xlsx',
    'LAKSHADWEEP.xlsx', 'MADHYA PRADESH.xlsx', 'MAHARASHTRA.xlsx', 'MANIPUR.xlsx',
    'MEGHALAYA.xlsx', 'MIZORAM.xlsx', 'NAGALAND.xlsx', 'ODISHA.xlsx',
    'PUDUCHERRY.xlsx', 'PUNJAB.xlsx', 'RAJASTHAN.xlsx', 'SIKKIM.xlsx',
    'TAMIL NADU.xlsx', 'TELANGANA.xlsx', 'TRIPURA.xlsx', 'UTTAR PRADESH.xlsx',
    'UTTARAKHAND.xlsx', 'WEST BENGAL.xlsx'])    

# Read selected state-wise data
state_by_data = pd.read_excel(file_name)

# Display the selected state name within the header
#st.header(f'2023 Data Status - {file_name.split(".")[0]}')

# Display state-wise data
st.dataframe(state_by_data)

st.header(f'2023 DATA STATUS - {file_name.split(".")[0]}')

# Compute metrics based on the selected state-wise data
col1, col2 = st.columns(2)
with col1:
    Minimum_DO = state_by_data['Min Dissolved Oxygen (mg/L)'].min()
    st.metric(label='Minimum Dissolved Oxygen (mg/L)', value=Minimum_DO)

    # Filter the DataFrame to get rows where Min Dissolved Oxygen (mg/L) equals Minimum_DO
    monitoring_location_min_DO = state_by_data.loc[state_by_data['Min Dissolved Oxygen (mg/L)'] == Minimum_DO, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_min_DO)
    

with col2:
    Maximum_DO = state_by_data['Max Dissolved Oxygen (mg/L)'].max()
    st.metric(label='Maximum Dissolved Oxygen (mg/L)', value=Maximum_DO)

    # Filter the DataFrame to get rows where Min Dissolved Oxygen (mg/L) equals Minimum_DO
    monitoring_location_max_DO = state_by_data.loc[state_by_data['Max Dissolved Oxygen (mg/L)'] == Maximum_DO, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_max_DO)

col3, col4 = st.columns(2)
with col3:
    Minimum_BOD = state_by_data['Min BOD (mg/L)'].min()
    st.metric(label='Minimum BOD (mg/L)', value=Minimum_BOD)
    monitoring_location_min_BOD = state_by_data.loc[state_by_data['Min BOD (mg/L)'] == Minimum_BOD, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_min_BOD)

with col4:
    Maximum_BOD = state_by_data['Max BOD (mg/L)'].max()
    st.metric(label='Maximum BOD (mg/L)', value=Maximum_BOD)
    monitoring_location_max_BOD = state_by_data.loc[state_by_data['Max BOD (mg/L)'] == Maximum_BOD, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_max_BOD)

col5, col6 = st.columns(2)

with col5:
    Minimum_pH = state_by_data['Min pH'].min()
    st.metric(label='Minimum pH', value=Minimum_pH)
    monitoring_location_min_pH = state_by_data.loc[state_by_data['Min pH'] == Minimum_pH, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_min_pH)

with col6:
    Maximum_pH = state_by_data['Max pH'].max()
    st.metric(label='Maximum pH', value=Maximum_pH)
    monitoring_location_max_pH = state_by_data.loc[state_by_data['Max pH'] == Maximum_pH, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_max_pH)


col7, col8 = st.columns(2)
with col7:
    Minimum_FC = state_by_data['Min Fecal Coliform  (MPN/100ml)'].min()
    st.metric(label='Min Fecal Coliform  (MPN/100ml)', value=Minimum_FC)
    monitoring_location_min_FC = state_by_data.loc[state_by_data['Min Fecal Coliform  (MPN/100ml)'] == Minimum_FC, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_min_FC)

with col8:
    Maximum_FC = state_by_data['Max Fecal Coliform  (MPN/100ml)'].max()
    st.metric(label='Max Fecal Coliform  (MPN/100ml)', value=Maximum_FC)
    monitoring_location_max_FC = state_by_data.loc[state_by_data['Max Fecal Coliform  (MPN/100ml)'] == Maximum_FC, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_max_FC)

col9, col10 = st.columns(2)

with col9:
    Minimum_Arsenic = state_by_data['Min Arsenic (mg/L)'].min()
    st.metric(label='Minimum Arsenic', value=Minimum_Arsenic)
    monitoring_location_min_Ar = state_by_data.loc[state_by_data['Min Arsenic (mg/L)'] == Minimum_Arsenic, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_min_Ar)

with col10:
    Maximum_Arsenic = state_by_data['Max Arsenic (mg/L)'].max()
    st.metric(label='Maximum Arsenic', value=Maximum_Arsenic)
    monitoring_location_max_Ar = state_by_data.loc[state_by_data['Max Arsenic (mg/L)'] == Maximum_Arsenic, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_max_Ar)



st.header('Water Body Wise Data')

# Dropdown for selecting water body-wise data
file_name2 = st.selectbox(label='Choose Water Body Data', options=[
    'RIVER.xlsx', 'LAKE.xlsx', 'CANAL.xlsx', 'DRAIN.xlsx', 'GROUND WATER.xlsx',
    'MARINE.xlsx', 'BEACH.xlsx', 'TANK.xlsx', 'RESERVOIR.xlsx', 'STP.xlsx',
    'WETLAND.xlsx', 'SEA.xlsx', 'CREEK.xlsx', 'POND.xlsx',
    'WATER TREATMENT PLANT (RAW WATER).xlsx', 'COSTAL.xlsx'])
water_body_by_data = pd.read_excel(file_name2)
st.dataframe(water_body_by_data)

st.header(f'2023 DATA STATUS - {file_name2.split(".")[0]}')

# Compute metrics based on the selected state-wise data
col1, col2 = st.columns(2)
with col1:
    Minimum_DO = water_body_by_data['Min Dissolved Oxygen (mg/L)'].min()
    st.metric(label='Minimum Dissolved Oxygen (mg/L)', value=Minimum_DO)

    # Filter the DataFrame to get rows where Min Dissolved Oxygen (mg/L) equals Minimum_DO
    monitoring_location_min_DO = water_body_by_data.loc[water_body_by_data['Min Dissolved Oxygen (mg/L)'] == Minimum_DO, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_min_DO)
    

with col2:
    Maximum_DO = water_body_by_data['Max Dissolved Oxygen (mg/L)'].max()
    st.metric(label='Maximum Dissolved Oxygen (mg/L)', value=Maximum_DO)

    # Filter the DataFrame to get rows where Min Dissolved Oxygen (mg/L) equals Minimum_DO
    monitoring_location_max_DO = water_body_by_data.loc[water_body_by_data['Max Dissolved Oxygen (mg/L)'] == Maximum_DO, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_max_DO)

col3, col4 = st.columns(2)
with col3:
    Minimum_BOD = water_body_by_data['Min BOD (mg/L)'].min()
    st.metric(label='Minimum BOD (mg/L)', value=Minimum_BOD)
    monitoring_location_min_BOD = water_body_by_data.loc[water_body_by_data['Min BOD (mg/L)'] == Minimum_BOD, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_min_BOD)

with col4:
    Maximum_BOD = water_body_by_data['Max BOD (mg/L)'].max()
    st.metric(label='Maximum BOD (mg/L)', value=Maximum_BOD)
    monitoring_location_max_BOD = water_body_by_data.loc[water_body_by_data['Max BOD (mg/L)'] == Maximum_BOD, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_max_BOD)

col5, col6 = st.columns(2)

with col5:
    Minimum_pH = water_body_by_data['Min pH'].min()
    st.metric(label='Minimum pH', value=Minimum_pH)
    monitoring_location_min_pH = water_body_by_data.loc[water_body_by_data['Min pH'] == Minimum_pH, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_min_pH)

with col6:
    Maximum_pH = water_body_by_data['Max pH'].max()
    st.metric(label='Maximum pH', value=Maximum_pH)
    monitoring_location_max_pH = water_body_by_data.loc[water_body_by_data['Max pH'] == Maximum_pH, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_max_pH)


col7, col8 = st.columns(2)
with col7:
    Minimum_FC = water_body_by_data['Min Fecal Coliform  (MPN/100ml)'].min()
    st.metric(label='Min Fecal Coliform  (MPN/100ml)', value=Minimum_FC)
    monitoring_location_min_FC = water_body_by_data.loc[water_body_by_data['Min Fecal Coliform  (MPN/100ml)'] == Minimum_FC, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_min_FC)

with col8:
    Maximum_FC = water_body_by_data['Max Fecal Coliform  (MPN/100ml)'].max()
    st.metric(label='Max Fecal Coliform  (MPN/100ml)', value=Maximum_FC)
    monitoring_location_max_FC = water_body_by_data.loc[water_body_by_data['Max Fecal Coliform  (MPN/100ml)'] == Maximum_FC, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_max_FC)

col9, col10 = st.columns(2)

with col9:
    Minimum_Arsenic = water_body_by_data['Min Arsenic (mg/L)'].min()
    st.metric(label='Minimum Arsenic', value=Minimum_Arsenic)
    monitoring_location_min_Ar = water_body_by_data.loc[water_body_by_data['Min Arsenic (mg/L)'] == Minimum_Arsenic, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_min_Ar)

with col10:
    Maximum_Arsenic = water_body_by_data['Max Arsenic (mg/L)'].max()
    st.metric(label='Maximum Arsenic', value=Maximum_Arsenic)
    monitoring_location_max_Ar = water_body_by_data.loc[water_body_by_data['Max Arsenic (mg/L)'] == Maximum_Arsenic, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_max_Ar)

st.header("Minimun & Maximum BOD (mg/L) Over Monitoring Location")
max_bod_chart = alt.Chart(water_body_by_data).mark_line(color='Red').encode(
    x='Monitoring Location',
    y='Max BOD (mg/L)',
    tooltip=['Monitoring Location', 'Max BOD (mg/L)']
).properties(
    width=600,
    height=400
)

min_bod_chart = alt.Chart(water_body_by_data).mark_line(color='Green').encode(
    x='Monitoring Location',
    y='Min BOD (mg/L)',
    tooltip=['Monitoring Location', 'Min BOD (mg/L)']
).properties(
    width=600,
    height=400
)

# Create a line for the standard line
standard_line = alt.Chart(pd.DataFrame({'Standard_Line': [3]})).mark_rule(color='Blue').encode(
    y='Standard_Line:Q'
)

# Combine the charts
chart_with_labels = (max_bod_chart + min_bod_chart + standard_line)

# Add data labels for Max BOD
max_text = max_bod_chart.mark_text(
    align='left',
    baseline='middle',
    dx=5,
    dy=-5,
    color='blue'
).encode(
    text='Max BOD (mg/L):Q'
)

# Add data labels for Min BOD
min_text = min_bod_chart.mark_text(
    align='left',
    baseline='middle',
    dx=5,
    dy=15,
    color='orange'
).encode(
    text='Min BOD (mg/L):Q'
)

# Add data labels for Standard Line
standard_text = standard_line.mark_text(
    align='left',
    baseline='middle',
    dx=5,
    dy=-25,
    color='green'
).encode(
    text=alt.value('3')
)

# Combine the line charts and the data labels
chart_with_labels = (chart_with_labels + max_text + min_text + standard_text)

# Render the chart using Streamlit
st.altair_chart(chart_with_labels, use_container_width=True)



st.header('River Wise Data')

file_name3 = st.selectbox(label='Choose River Data', options=[
    'GODAVARI.xlsx', 'KRISHNA.xlsx', 'BRAHMAPUTRA.xlsx', 'GANGA.xlsx', 'MAHANANDA.xlsx', 
    'MAHANADI.xlsx', 'YAMUNA.xlsx', 'MAHI.xlsx', 'TAPI.xlsx', 'GHAGGAR.xlsx','BEAS.xlsx', 'SATLUJ.xlsx', 
    'SUBARNAREKHA.xlsx', 'CAUVERY.xlsx', 'BAITARNI.xlsx', 'BRAHMANI.xlsx', 'PENNAR.xlsx', 'CHAMBAL.xlsx', 
    'SABARMATI.xlsx'])
River_by_data = pd.read_excel(file_name3)
st.dataframe(River_by_data)

st.header(f'2023 DATA STATUS - {file_name3.split(".")[0]}')

# Compute metrics based on the selected state-wise data
col1, col2 = st.columns(2)
with col1:
    Minimum_DO = River_by_data['Min Dissolved Oxygen (mg/L)'].min()
    st.metric(label='Minimum Dissolved Oxygen (mg/L)', value=Minimum_DO)

    # Filter the DataFrame to get rows where Min Dissolved Oxygen (mg/L) equals Minimum_DO
    monitoring_location_min_DO = River_by_data.loc[River_by_data['Min Dissolved Oxygen (mg/L)'] == Minimum_DO, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_min_DO)
    

with col2:
    Maximum_DO = River_by_data['Max Dissolved Oxygen (mg/L)'].max()
    st.metric(label='Maximum Dissolved Oxygen (mg/L)', value=Maximum_DO)

    # Filter the DataFrame to get rows where Min Dissolved Oxygen (mg/L) equals Minimum_DO
    monitoring_location_max_DO = River_by_data.loc[River_by_data['Max Dissolved Oxygen (mg/L)'] == Maximum_DO, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_max_DO)

col3, col4 = st.columns(2)
with col3:
    Minimum_BOD = River_by_data['Min BOD (mg/L)'].min()
    st.metric(label='Minimum BOD (mg/L)', value=Minimum_BOD)
    monitoring_location_min_BOD = River_by_data.loc[River_by_data['Min BOD (mg/L)'] == Minimum_BOD, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_min_BOD)

with col4:
    Maximum_BOD = River_by_data['Max BOD (mg/L)'].max()
    st.metric(label='Maximum BOD (mg/L)', value=Maximum_BOD)
    monitoring_location_max_BOD = River_by_data.loc[River_by_data['Max BOD (mg/L)'] == Maximum_BOD, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_max_BOD)

col5, col6 = st.columns(2)

with col5:
    Minimum_pH = River_by_data['Min pH'].min()
    st.metric(label='Minimum pH', value=Minimum_pH)
    monitoring_location_min_pH = River_by_data.loc[River_by_data['Min pH'] == Minimum_pH, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_min_pH)

with col6:
    Maximum_pH = River_by_data['Max pH'].max()
    st.metric(label='Maximum pH', value=Maximum_pH)
    monitoring_location_max_pH = River_by_data.loc[River_by_data['Max pH'] == Maximum_pH, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_max_pH)


col7, col8 = st.columns(2)
with col7:
    Minimum_FC = River_by_data['Min Fecal Coliform  (MPN/100ml)'].min()
    st.metric(label='Min Fecal Coliform  (MPN/100ml)', value=Minimum_FC)
    monitoring_location_min_FC = River_by_data.loc[River_by_data['Min Fecal Coliform  (MPN/100ml)'] == Minimum_FC, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_min_FC)

with col8:
    Maximum_FC = River_by_data['Max Fecal Coliform  (MPN/100ml)'].max()
    st.metric(label='Max Fecal Coliform  (MPN/100ml)', value=Maximum_FC)
    monitoring_location_max_FC = River_by_data.loc[River_by_data['Max Fecal Coliform  (MPN/100ml)'] == Maximum_FC, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_max_FC)

col9, col10 = st.columns(2)

with col9:
    Minimum_Arsenic = River_by_data['Min Arsenic (mg/L)'].min()
    st.metric(label='Minimum Arsenic', value=Minimum_Arsenic)
    monitoring_location_min_Ar = River_by_data.loc[River_by_data['Min Arsenic (mg/L)'] == Minimum_Arsenic, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_min_Ar)

with col10:
    Maximum_Arsenic = River_by_data['Max Arsenic (mg/L)'].max()
    st.metric(label='Maximum Arsenic', value=Maximum_Arsenic)
    monitoring_location_max_Ar = River_by_data.loc[River_by_data['Max Arsenic (mg/L)'] == Maximum_Arsenic, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_max_Ar)


st.header("Minimun & Maximum BOD (mg/L) Over Monitoring Location")
# st.line_chart(River_by_data.set_index('Monitoring Location')[['Max BOD (mg/L)','Min BOD (mg/L)']].assign(Standard_Line=3))

max_bod_chart = alt.Chart(River_by_data).mark_line(color='red').encode(
    x='Monitoring Location',
    y='Max BOD (mg/L)',
    tooltip=['Monitoring Location', 'Max BOD (mg/L)']
).properties(
    width=600,
    height=400
)

min_bod_chart = alt.Chart(River_by_data).mark_line(color='Green').encode(
    x='Monitoring Location',
    y='Min BOD (mg/L)',
    tooltip=['Monitoring Location', 'Min BOD (mg/L)']
).properties(
    width=600,
    height=400
)

# Create a line for the standard line
standard_line = alt.Chart(pd.DataFrame({'Standard_Line': [3]})).mark_rule(color='Blue').encode(
    y='Standard_Line:Q'
)

# Combine the charts
chart_with_labels = (max_bod_chart + min_bod_chart + standard_line)

# Add data labels for Max BOD
max_text = max_bod_chart.mark_text(
    align='left',
    baseline='middle',
    dx=5,
    dy=-5,
    color='blue'
).encode(
    text='Max BOD (mg/L):Q'
)

# Add data labels for Min BOD
min_text = min_bod_chart.mark_text(
    align='left',
    baseline='middle',
    dx=5,
    dy=15,
    color='orange'
).encode(
    text='Min BOD (mg/L):Q'
)

# Add data labels for Standard Line
standard_text = standard_line.mark_text(
    align='left',
    baseline='middle',
    dx=5,
    dy=-25,
    color='green'
).encode(
    text=alt.value('3')
)

# Combine the line charts and the data labels
chart_with_labels = (chart_with_labels + max_text + min_text + standard_text)

# Render the chart using Streamlit
st.altair_chart(chart_with_labels, use_container_width=True)

st.header('NWMP Wetland / Ramsar Locations ')
@st.cache_resource
def load_data(file_path):
    return pd.read_excel(file_path)

def main():
    # Button to trigger data loading and display
    if st.button('126 Ramsar Sites Locations on 76 Weland/Ramsar'):
        file_name = 'NWMP Wetland List.xlsx'  # Assuming fixed file name/path
        Wetland_Ramsar_data = load_data(file_name)
        st.dataframe(Wetland_Ramsar_data)

if __name__ == '__main__':
    main()



st.header('Medium & Minor River Data-2023')
@st.cache_resource
def load_data(file_path):
    return pd.read_excel(file_path)

def main():
    # Button to trigger data loading and display
    if st.button('Load Data'):
        file_name = 'Medium & Minor River data -2023.xlsx'  # Assuming fixed file name/path
        Medium_And_Minor_River = load_data(file_name)
        st.dataframe(Medium_And_Minor_River)


if __name__ == '__main__':
    main()



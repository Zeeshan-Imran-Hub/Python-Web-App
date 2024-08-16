import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Title and data loading
st.title("Graph Plotter Web App")
df = pd.read_excel("/Users/ASUS/Desktop/archive/Sales_v1.xlsx")

# Display column names
st.write("## Column Names")
for col in df.columns:
    st.write(f"- *{col}*")

# Display index values
st.write("## Index Values")
st.write(df.index.tolist())

# Index value input
index_value = st.number_input("Enter an index value to display the row information", min_value=0,
                              max_value=int(df.index.max()), step=1)
if index_value in df.index:
    st.write(f"## Row Information for Index {index_value}")
    st.write(df.loc[index_value])

# Column selection for data display and statistical analysis
column = st.selectbox("Select a column to display complete data and statistical values", df.columns)
if column:
    st.write(f"## Data for Column: {column}")
    st.write(df[column])

    st.write(f"## Statistical Analysis for Column: {column}")
    st.write(df[column].describe())

# Input for index range
st.write("## Select Columns and Index Range for Plotting")

start_index = st.number_input("Enter the start index", min_value=int(df.index.min()), max_value=int(df.index.max()),
                              step=1, value=int(df.index.min()))
end_index = st.number_input("Enter the end index", min_value=int(df.index.min()), max_value=int(df.index.max()), step=1,
                            value=int(df.index.max()))

if start_index > end_index:
    st.error("Start index must be less than or equal to end index")

# Column selection for plotting
column1 = st.selectbox("Select the first column for plotting", df.columns)
column2 = st.selectbox("Select the second column for plotting", df.columns)

# Plot type selection
plot_type = st.selectbox("Select the type of plot", ['Line Plot', 'Scatter Plot', 'Bar Plot'])

# Plotting based on user selection
if column1 and column2 and start_index <= end_index:
    df_filtered = df.loc[start_index:end_index]

    if plot_type == 'Line Plot':
        plot, axis = plt.subplots()
        axis.plot(df_filtered[column1], df_filtered[column2])
        axis.set_title("Line Plot")
        axis.set_xlabel(column1)
        axis.set_ylabel(column2)
        st.pyplot(plot)

    elif plot_type == 'Scatter Plot':
        plot, axis = plt.subplots()
        axis.scatter(df_filtered[column1], df_filtered[column2])
        axis.set_title("Scatter Plot")
        axis.set_xlabel(column1)
        axis.set_ylabel(column2)
        st.pyplot(plot)

    elif plot_type == 'Bar Plot':
        plot, axis = plt.subplots()
        axis.bar(df_filtered[column1], df_filtered[column2])
        axis.set_title("Bar Plot")
        axis.set_xlabel(column1)
        axis.set_ylabel(column2)
        st.pyplot(plot)

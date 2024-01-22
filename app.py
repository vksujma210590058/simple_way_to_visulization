import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objs as go
import numpy as np
st.title(":rainbow[Upload a clean data csv ]")
file=st.file_uploader(label=":rainbow[Upload a clean file to visualize]")

if file is not None:
    name=file.name
    if name.endswith(".csv"):
        df=pd.read_csv(file)
        st.write(df)
    else:
        df=pd.read_excel(file)
        st.write(df)
else:
    df=pd.DataFrame({"Name":["vikas_maurya","Radhe_maurya"],"Gender":["male","female"],"Salary":[21,23]})
    st.write(df)
 # st.write(df[f"{selected_column_number}"])


object_columns=df.select_dtypes(include="object").columns
number_columns=df.select_dtypes(include="number").columns

selected_column_object=st.selectbox(":rainbow[Select a object_column]",object_columns)
selected_column_number=st.selectbox(":rainbow[Select a number_column]",number_columns)
df_count=df.groupby(selected_column_object).agg({selected_column_number:"count"})
df_mean=df.groupby(selected_column_object).agg({selected_column_number:"mean"})
# dfs=[df_count,df_sum,df_mean]
# selected_df=st.selectbox("Groupby",dfs)
if st.button(":rainbow[click me count Agg :]"):
    fig1=px.pie(data_frame=df_count,labels=f"{selected_column_object}",values=f"{selected_column_number}",color=df_count.index)
    fig2=px.bar(data_frame=df_count,x=df_count.index,y=selected_column_number,color=df_count.index)
    st.plotly_chart(fig1)
    st.plotly_chart(fig2)
df_sum=df.groupby(selected_column_object).agg({selected_column_number:"sum"})

if st.button(":rainbow[click me sum Agg:]"):
    fig1=px.pie(data_frame=df_sum,labels=f"{selected_column_object}",values=f"{selected_column_number}",color=df_sum.index)
    fig2=px.bar(data_frame=df_sum,x=df_sum.index,y=selected_column_number,color=df_sum.index)
    st.plotly_chart(fig1)
    st.plotly_chart(fig2)
df_mean=df.groupby(selected_column_object).agg({selected_column_number:"mean"})
if st.button(":rainbow[click me mean Agg:]"):
    fig1=px.pie(data_frame=df_mean,labels=f"{selected_column_object}",values=f"{selected_column_number}",color=df_mean.index)
    fig2=px.bar(data_frame=df_mean,x=df_mean.index,y=selected_column_number,color=df_mean.index)
    st.plotly_chart(fig1)
    st.plotly_chart(fig2)
z_col=st.selectbox(":rainbow[Select a z_column]",number_columns)
if st.button(":rainbow[click me to see the 3d graph]"):
    fig3=px.scatter_3d(data_frame=df,x=selected_column_object,y=selected_column_number,z=z_col,color=selected_column_object)
    fig4=px.line_3d(data_frame=df,x=selected_column_object,y=selected_column_number,z=z_col,color=selected_column_object)
    st.plotly_chart(fig4)

    st.plotly_chart(fig3)

st.title(":rainbow[Example To See]")
# Generate data for x and y axes (range of values)
x_values = np.linspace(-5, 5, 100)
y_values = np.linspace(-5, 5, 100)
x_mesh, y_mesh = np.meshgrid(x_values, y_values)

# Calculate z-values for the surface plot
z_values = np.sin(np.sqrt(x_mesh**2 + y_mesh**2))

# Create a 3D surface plot
surface = go.Surface(x=x_values, y=y_values, z=z_values)

# Define layout settings
layout = go.Layout(
    title='3D Surface Plot: z = sin(sqrt(x^2 + y^2))',
    scene=dict(
        xaxis=dict(title='X-axis'),
        yaxis=dict(title='Y-axis'),
        zaxis=dict(title='Z-axis'),
        camera=dict(eye=dict(x=1.2, y=1.2, z=0.6))
    )
)

# Create the figure and display it
fig_example = go.Figure(data=[surface], layout=layout)
st.plotly_chart(fig_example)

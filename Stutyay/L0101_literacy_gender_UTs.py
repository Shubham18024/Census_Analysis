#!/usr/bin/env python
# coding: utf-8

# #Analysis of Literacy Rate by Gender in different states and UTs of India(2011)
# 
# ##AIM
# The objective of this analysis is to visualize the literacy rate of males and females from all the states and UTs of the year 2011 and to compare them with the national average literacy rate of both the genders.
# 
# ##Formula 
# Literacy Rate of Males= Total Male Literacy(age 7 and above)/Total Male population(Age 7 and above)x100
# Literacy Rate of Females= Total Female Literacy(age 7 and above)/Total Female population(age 7 and above)x100
# 
# ##Source for data
# The data for this analysis is sourced from Census of India 2011. The orignal data can be downloaded from the census website:
# [Census_2011](https://censusindia.gov.in/census.website/data/census-tables#)
# 
# ##Refined Data
# The has been Refined to study the of males and females of different states and UT along with the comparison to the national average literacy rate. The refined data can be found here on github:[Refined_data_States](https://github.com/Shubham18024/Census_Analysis/blob/8ca83c15c24210b27af0ab870081158bd02e8814/CSV%20files%20for%201991%2C2001%2C2011/2011%20Gender%20Literacy%20Rate%20(1).xlsx)
# [Refined_data_UTs](https://github.com/Shubham18024/Census_Analysis/blob/8ca83c15c24210b27af0ab870081158bd02e8814/CSV%20files%20for%201991%2C2001%2C2011/UTs%202011%20Literacy%20and%20Gender.xlsx)
# 
# ##Visualisation
# Below is the code written to generate a grouped bar chatof literacy rate of males and females of different states and UTs along with the comparison to the national average literacy rate.

# In[22]:


import pandas as pd
import plotly.graph_objects as go


# In[23]:


df=pd.read_excel(r"C:\Users\stuti\OneDrive\Desktop\temp_1\2011 Gender Literacy Rate (1).xlsx" , engine="openpyxl")
df


# In[24]:


df.columns


# In[25]:


#Extract Relevant data
states=df["Area Name"]
male_lit_rate=df["Male Literacy Rate"]
female_lit_rate=df["Female Literacy Rate"]


# In[26]:


# National average literacy rates (replace these values with actual national averages)
national_avg_male = 80.88
national_avg_female = 64.63
national_avg_total = 72.98

# Create a bar plot for male and female literacy rates
fig = go.Figure()

fig.add_trace(go.Bar(
    x=states,
    y=male_lit_rate,
    name="Male Literacy Rate",
    marker_color='blue'
    
))

fig.add_trace(go.Bar(
    x=states,
    y=female_lit_rate,
    name="Female Literacy Rate",
    marker_color='pink'
))

# Add horizontal lines for national averages with labels
fig.add_shape(
    type="line",
    x0=0,
    y0=national_avg_male,
    x1=1,
    y1=national_avg_male,
    line=dict(color="blue", width=2, dash="dash"),
    xref='paper',
    yref='y'
)
fig.add_annotation(
    x=1.02,
    y=national_avg_male,
    xref='paper',
    yref='y',
    text="National Avg Male Literacy Rate",
    showarrow=False,
    font=dict(color="blue", size=10),
    xanchor='left',
    yanchor='middle'
)

fig.add_shape(
    type="line",
    x0=0,
    y0=national_avg_female,
    x1=1,
    y1=national_avg_female,
    line=dict(color="pink", width=2, dash="dash"),
    xref='paper',
    yref='y'
)
fig.add_annotation(
    x=1.02,
    y=national_avg_female,
    xref='paper',
    yref='y',
    text="National Avg Female Literacy Rate",
    showarrow=False,
    font=dict(color="pink", size=10),
    xanchor='left',
    yanchor='middle'
)

fig.add_shape(
    type="line",
    x0=0,
    y0=national_avg_total,
    x1=1,
    y1=national_avg_total,
    line=dict(color="green", width=2, dash="dash"),
    xref='paper',
    yref='y'
)
fig.add_annotation(
    x=1.02,
    y=national_avg_total,
    xref='paper',
    yref='y',
    text="National Avg Total Literacy Rate",
    showarrow=False,
    font=dict(color="green", size=10),
    xanchor='left',
    yanchor='middle'
)

fig.update_layout(
    title="Literacy Rate by Gender in Different States",
    xaxis_title="States",
    yaxis_title="Literacy Rate (%)",
    barmode='group',
    legend_title="Gender",
    width=1000,
    height=1000,
    # Adjust legend layout
    legend=dict(
        x=1,
        y=1,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)' 
    
   )
    
)
# Show the plot
fig.show()

# Conversion of png image to html to view interactive plot
fig.write_html("literacy_rate_by_gender.html")


# In[14]:


df_ut=pd.read_excel(r"C:\Users\stuti\OneDrive\Desktop\temp_1\UTs 2011 Literacy and Gender.xlsx")
df_ut


# In[15]:


df_ut.columns


# In[16]:


#Extract Relevant data
UT=df_ut["Uts"]
male_lit_rate=df_ut["Male Literacy Rate"]
female_lit_rate=df_ut["Female Literacy Rate"]


# In[20]:


# National average literacy rates (replace these values with actual national averages)
national_avg_male = 80.88
national_avg_female = 64.63
national_avg_total = 72.98

# Create a bar plot for male and female literacy rates
fig = go.Figure()

fig.add_trace(go.Bar(
    x=UT,
    y=male_lit_rate,
    name="Male Literacy Rate",
    marker_color='blue'
))

fig.add_trace(go.Bar(
    x=UT,
    y=female_lit_rate,
    name="Female Literacy Rate",
    marker_color='pink'
))

# Add horizontal lines for national averages with labels
fig.add_shape(
    type="line",
    x0=0,
    y0=national_avg_male,
    x1=1,
    y1=national_avg_male,
    line=dict(color="blue", width=2, dash="dash"),
    xref='paper',
    yref='y'
)
fig.add_annotation(
    x=1.02,
    y=national_avg_male,
    xref='paper',
    yref='y',
    text="National Avg Male Literacy Rate",
    showarrow=False,
    font=dict(color="blue", size=10),
    xanchor='left',
    yanchor='middle'
)

fig.add_shape(
    type="line",
    x0=0,
    y0=national_avg_female,
    x1=1,
    y1=national_avg_female,
    line=dict(color="pink", width=2, dash="dash"),
    xref='paper',
    yref='y'
)
fig.add_annotation(
    x=1.02,
    y=national_avg_female,
    xref='paper',
    yref='y',
    text="National Avg Female Literacy Rate",
    showarrow=False,
    font=dict(color="pink", size=10),
    xanchor='left',
    yanchor='middle'
)

fig.add_shape(
    type="line",
    x0=0,
    y0=national_avg_total,
    x1=1,
    y1=national_avg_total,
    line=dict(color="green", width=2, dash="dash"),
    xref='paper',
    yref='y'
)
fig.add_annotation(
    x=1.02,
    y=national_avg_total,
    xref='paper',
    yref='y',
    text="National Avg Total Literacy Rate",
    showarrow=False,
    font=dict(color="green", size=10),
    xanchor='left',
    yanchor='middle'
)

fig.update_layout(
    title="Literacy Rate by Gender in Different States",
    xaxis_title="Union Territories",
    yaxis_title="Literacy Rate (%)",
    barmode='group',
    legend_title="Gender",
    width=1000,
    height=1000,
    # Adjust legend layout
    legend=dict(
        x=1,
        y=1,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)' 
    
   )
    
)
# Show the plot
fig.show()

# Conversion of png image to html to view interactive plot
fig.write_html("literacy_rate_by_gender_UTs.html")


# [View Output for States](http://localhost:8888/view/literacy_rate_by_gender.html)
# [View Output for UTs](http://localhost:8888/view/literacy_rate_by_gender_UTs.html)

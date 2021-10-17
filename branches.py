import pandas as pd
import plotly.graph_objects as go


closings = pd.read_csv("../../../1_Bankfind_Events_Changes_Downloads/downloaded_data/Branch_Office_Closings_10_7_2021.csv", error_bad_lines=False)
openings = pd.read_csv("../../../1_Bankfind_Events_Changes_Downloads/downloaded_data/Branch_Office_Openings_10_7_2021.csv", error_bad_lines=False)
relos = pd.read_csv("../../../1_Bankfind_Events_Changes_Downloads/downloaded_data/Branch_Office_Relocations_10_7_2021.csv", error_bad_lines=False)
by_inst = pd.read_csv("../../../1_Bankfind_Events_Changes_Downloads/downloaded_data/Branch_Purchases_&_Assumptions_by_Institution_10_7_2021.csv", error_bad_lines=False)

def plot_openings_year(year):

    data_year = openings[openings['EFFYEAR'] == year]

    fig = go.Figure(data=go.Scattergeo(
        lon = data_year['OFF_LONGITUDE'],
        lat = data_year['OFF_LATITUDE'],
#        text = data['text'],
        mode = 'markers',
#        marker_color = data['cnt'],
        ))

    fig.update_layout(
        title = 'Branch Openings in Year' + str(year),
        geo_scope='usa')
    
    fig.show()

def plot_closings_year(year):

    data_year = closings[closings['EFFYEAR'] == year]

    fig = go.Figure(data=go.Scattergeo(
        lon = data_year['LONGITUDE'],
        lat = data_year['LATITUDE'],
#        text = data['text'],
        mode = 'markers',
#        marker_color = data['cnt'],
        ))

    fig.update_layout(
        title = 'Branch Closings in Year' + str(year),
        geo_scope='usa')
    
    fig.show()

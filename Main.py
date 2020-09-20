import plotly.graph_objects as go
import pandas as pd


def main():
    ######################################
    # Mask usage by state
    df = pd.read_csv(r'C:\Users\gleee\OneDrive\Desktop\GeorgiaTech\2020Fall\CS6440\MiniProject2\MaskData_Formatted.csv')
    fig = go.Figure(data=go.Choropleth(
        locations=df['code'],  # Spatial coordinates
        z=df['mask'].astype(float),  # Data to be color-coded
        locationmode='USA-states',  # set of locations match entries in `locations`
        colorscale='Reds',
        colorbar_title="Mask Usage %",
    ))

    fig.update_layout(
        title_text='Mask Usage by State',
        geo_scope='usa',  # limite map scope to USA
    )

    fig.show()

    ######################################
    # Covid cases by state
    df = pd.read_csv(r'C:\Users\gleee\OneDrive\Desktop\GeorgiaTech\2020Fall\CS6440\MiniProject2\DeathData_Formatted.csv')
    fig = go.Figure(data=go.Choropleth(
        locations=df['code'],  # Spatial coordinates
        z=df['cases'].astype(float),  # Data to be color-coded
        locationmode='USA-states',  # set of locations match entries in `locations`
        colorscale='Reds',
        colorbar_title="Covid Deaths",
    ))

    fig.update_layout(
        title_text='Covid Cases by State',
        geo_scope='usa',  # limit map scope to USA
    )

    fig.show()

    ######################################
    # Covid deaths by state
    df = pd.read_csv(r'C:\Users\gleee\OneDrive\Desktop\GeorgiaTech\2020Fall\CS6440\MiniProject2\DeathData_Formatted.csv')
    fig = go.Figure(data=go.Choropleth(
        locations=df['code'],  # Spatial coordinates
        z=df['deaths'].astype(float),  # Data to be color-coded
        locationmode='USA-states',  # set of locations match entries in `locations`
        colorscale='Reds',
        colorbar_title="Covid Deaths",
    ))

    fig.update_layout(
        title_text='Covid Deaths by State',
        geo_scope='usa',  # limit map scope to USA
    )

    fig.show()


if __name__ == "__main__":
    main()

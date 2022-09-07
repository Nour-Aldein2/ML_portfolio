# Create a dashboard of the graph above

# Imports
import pandas as pd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import plotly.express as px

# Prepare the dataset
df = pd.read_csv('../DATA/lending_club_loan_two.csv')
# df = pd.get_dummies(data=df, columns=['loan_status'], drop_first=True)
# df['fully_paid'] = df['loan_status_Fully Paid']
# df.drop(['loan_status_Fully Paid'], axis=1, inplace=True)

# App location
app = dash.Dash()

# Create list of the features that you will be working with
features = ['term', 'grade', 'sub_grade',
            'home_ownership', 'verification_status', 'issue_d', 'purpose']

# The app layout
app.layout = html.Div([
    html.Div([
        dcc.Dropdown(id='huename',  # Dropdown that contains features
                     options=[{'label': i, 'value': i} for i in features],
                     value='loan_status')
    ], style={'width': '20%', 'display': 'inline-block'}),
    dcc.Graph(id='feature-graphic'),  # The graph

], style={'padding': 10})

# Adjust the figures


@app.callback(Output('feature-graphic', 'figure'),
              [Input('huename', 'value')])
def update_graph(huename):
    # return {'data': [go.histogram(x=df["fully_paid"], color=df[huename], text_auto=True, barmode='group')],
    #         'layout': go.Layout(title='Lendding Club', xaxis={'title': 'Fully Paid'})}

    if huename is None:
        huename = "loan_status"
        # raise dash.exceptions.PreventUpdate

    fig = px.histogram(x=df["loan_status"], color=df[huename], text_auto=True, barmode='group')

    fig.update_xaxes(type='category', categoryorder='category ascending')
    fig.update_layout(title='Lendding Club', xaxis={'title': 'Loan Status'})

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)

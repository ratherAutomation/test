import dash
from dash import dcc, html
import plotly.express as px

# Crear una aplicación Dash
app = dash.Dash(__name__)
server = app.server
# Definir el diseño del dashboard
app.layout = html.Div([
    html.H1("Dashboard de Prueba en Render"),
    dcc.Graph(
        id='grafico-de-barras',
        figure=px.bar(
            x=['A', 'B', 'C', 'D'],
            y=[4, 7, 1, 2],
            labels={'x': 'Categoría', 'y': 'Valor'},
            title='Gráfico de Barras'
        )
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

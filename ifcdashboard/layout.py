import dash_ifc
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

from ifcdashboard.fileutils import read_file

class IfcLayout:
    
    def __init__(self):
        self._layout = self.setup_layout()

    def apply_layout(self, app: dash.Dash) -> None:
        """
        Apply layout to app

        Args:
            app (dash.App): app object to apply layout to
        """
        app.layout = self._layout


    def setup_layout(self) -> dbc.Container:
        layout = dbc.Container([
            dcc.ConfirmDialog(
                id='confirm-upload',
            ),
            html.Div([html.Div("Dash IFC viewer")], style={"padding":"20px"}),
            dbc.Row([
                dbc.Col(
                    dcc.Upload(
                        id='upload-data',
                        children=html.Div([
                            'Drag and Drop or ',
                            html.A('Select File')
                        ]),
                        style={
                            'width': '100%',
                            'height': '60px',
                            'lineHeight': '60px',
                            'borderWidth': '1px',
                            'borderStyle': 'dashed',
                            'borderRadius': '5px',
                            'textAlign': 'center',
                        },
                    ),
                    style={"padding":"20px"},
                    width=2
                ),
                dbc.Col(
                    dash_ifc.DashIfc("ifc_viewer", ""),
                    style={"padding":"20px"},
                    width=8
                ),
            ], 
            className="g-0",
            style={
                "height": "90vh",
                "width": "95vw",
                "padding": "20px"
            })

        ])
        return layout

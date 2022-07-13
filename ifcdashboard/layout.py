import dash_ifc
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

from .constants import IFC_TYPES

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
            html.Div(
                id='data-updated',
            ),
            # dcc.Store stores the intermediate value
            dcc.Store(id='session-id'),
            html.Div(
                [html.Div([
                    dcc.Link("Dash", href="https://dash.plotly.com/"),
                    " / ",
                    dcc.Link("IFC.js", href="https://ifcjs.github.io/info/"),
                    " viewer"
                ])],
                style={
                    "padding":"40px",
                    "font-size": "40px"
                }
            ),
            dbc.Row([
                dbc.Col(
                    [
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
                        dbc.DropdownMenu(
                            children=[dbc.DropdownMenuItem(key, id=key) for key in ["All"] + IFC_TYPES],
                            id="dropdown",
                            label="Select Product",
                            style={
                                "padding":"40px",
                                "padding-left":"0px"
                            }
                        ),
                        html.Div([
                            dcc.Graph(
                                id='radar',
                                figure={
                                    'data': [],
                                }
                            )
                        ])
                    ],
                    style={"padding":"20px"},
                    width=4
                ),
                dbc.Col(
                    dash_ifc.DashIfc("ifc_viewer", ""),
                    style={"padding":"20px"},
                    width=8
                ),
            ], 
            className="g-0",
            style={
                "height": "80vh",
                "width": "95vw",
                "padding": "20px"
            })

        ],
        style={
            "maxWidth": "100vw"
        }
        )
        return layout

from dash import no_update, callback_context
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc

import time

from .app import app
from .charts import radar_chart, histogram
from .constants import IFC_TYPES
from .fileutils import parse_contents
from .ifc import IfcFile

@app.callback(Output('confirm-upload', 'message'),
            Output('confirm-upload', 'displayed'),
            Output("ifc_viewer", "ifc_file_contents"),
            Output("ifc_data", "data"),
            Input('upload-data', 'contents'),
            State('upload-data', 'filename'),
            prevent_initial_call=True)
def update_output(file_contents, filename):
    try:
        ifc_data = parse_contents(file_contents, filename)
        return "", False, ifc_data, ifc_data
    except Exception as e:
        return str(e), True, no_update, no_update

@app.callback(Output('radar', 'figure'),
    Output("dropdown", "label"),
    Input("ifc_data", "data"),
    [Input(key.replace(" ", "_"), "n_clicks") for key in ["All"] + IFC_TYPES],
    prevent_initial_call=True)
def update_figure(ifc_data, *args):
    ctx = callback_context

    if not ctx.triggered:
        button_id = "All"
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if button_id == "ifc_data":
        button_id = "All"
    
    # load ifc data
    if ifc_data is None:
        raise PreventUpdate()

    tstart = time.time()
    ifc_file = IfcFile(ifc_data)
    print(f"Took: {time.time() - tstart}s")

    if button_id != "All" and "OverallHeight" in ifc_file.get_product(button_id).columns.values:
        # scatter plot
        fig = histogram(ifc_file.get_product(button_id), "OverallHeight")
        return fig, button_id
    else:
        # radar plot
        fig = radar_chart(ifc_file.product_count)
        return fig, "All"
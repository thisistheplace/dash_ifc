// import './App.css';
import { IfcViewerAPI } from 'web-ifc-viewer';
import React, {Component, setState} from 'react';
import PropTypes from 'prop-types';

export default class DashIfc extends Component {

    constructor(props) {
        super(props);
        this.state = {
            ifc_data: props.ifc_file_contents
        }
        this.handleFileUpdate = this.handleFileUpdate.bind(this);
        this.loadifc = this.loadifc.bind(this);
        this.loader = this.loader.bind(this);
    }

    componentDidUpdate(prevProps){
        const {ifc_file_contents} = this.props;
        if (ifc_file_contents !== prevProps.ifc_file_contents){
            this.handleFileUpdate();
        }
    }

    handleFileUpdate(){
        const {ifc_file_contents} = this.props;
        // Update the viewer
        this.loadifc();
    }

    componentDidMount() {
        const container = document.getElementById(this.props.id);
        const viewer = new IfcViewerAPI({container});
        viewer.addAxes();
        viewer.addGrid();
        viewer.IFC.setWasmPath('../../');
        viewer.IFC.loader.ifcManager.applyWebIfcConfig({
            USE_FAST_BOOLS: true,
            COORDINATE_TO_ORIGIN: true
          });
        viewer.context.renderer.postProduction.active = true;

        this.viewer = viewer;

        window.onmousemove = viewer.prepickIfcItem;
        window.ondblclick = viewer.addClippingPlane
    }

    loadifc(){
        this.loader();
    }

    loader = async() => {
        var blob = new Blob([this.props.ifc_file_contents], { type: 'text/plain', endings: "native" });
        const ifc_file = new File([blob], "file.ifc");
        await this.viewer.IFC.loadIfc(ifc_file, true);
    }

    render() {
        return (
          <div id={this.props.id} style={{ position: 'relative', height: '100%', width: '100%' }} />
        );
    }
}

DashIfc.defaultProps = {};

DashIfc.propTypes = {
    /**
     * The ID used to identify the container for the IFC viewer component.
     */
    id: PropTypes.string,

    /**
     * The contents of the ifc file
     */
     ifc_file_contents: PropTypes.string.isRequired,
};

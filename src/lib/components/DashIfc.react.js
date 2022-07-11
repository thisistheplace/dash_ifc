// import './App.css';
import { IfcViewerAPI } from 'web-ifc-viewer';
import React, {Component} from 'react';
import PropTypes from 'prop-types';

export default class DashIfc extends Component {

    state = {
        loaded: false,
        loading_ifc: false
    };

    constructor(props) {
        super(props);
    }

    componentDidMount() {
        const container = document.getElementById(this.props.id);
        const viewer = new IfcViewerAPI({container});
        viewer.addAxes();
        viewer.addGrid();
        console.log("set wasm path");
        //viewer.IFC.setWasmPath('assets/');

        this.viewer = viewer;
        this.loadifc();

        window.onmousemove = viewer.prepickIfcItem;
        window.ondblclick = viewer.addClippingPlane
    }

    handleToggleClipping = () => {
        this.viewer.clipper.active = !this.viewer.clipper.active;
    };

    handleOpenViewpoint = (viewpoint) => {
        this.viewer.currentViewpoint = viewpoint;
    };

    loadifc(){
      this.loader();
    }

    loader = async() => {
      this.setState({ loading_ifc: true });
      console.log(this.props.ifc_file_contents.slice(0, 100));
      console.log("loading blob");
      var blob = new Blob([this.props.ifc_file_contents], { type: 'text/plain', endings: "native" });
      console.log(blob);
      console.log("creating file");
      const ifc_file = new File([blob], "file.ifc");
      console.log(ifc_file);
      console.log("loading");
      await this.viewer.IFC.loadIfc(ifc_file, true);
      console.log("loaded");
      this.setState({ loaded: true, loading_ifc: false })
    }

    render() {
        const {id, ifc_file_contents} = this.props;
        return (
          <div id={id} style={{ position: 'relative', height: '100%', width: '100%' }} />
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

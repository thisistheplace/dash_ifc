import { IfcViewerAPI } from 'web-ifc-viewer';

const DashIfcViewer = {};

DashIfcViewer.create = (el, url) => {
    // Create viewer from IFC file at url
    const container = document.getElementById(el);
    DashIfcViewer.container = container;
    const viewer = new IfcViewerAPI({container});
    DashIfcViewer.viewer = viewer;
    viewer.axes.setAxes();
    viewer.grid.setGrid();
    const ifcURL = URL.createObjectURL(url);
    viewer.IFC.loadIfcUrl(ifcURL);
};

export {DashIfcViewer};
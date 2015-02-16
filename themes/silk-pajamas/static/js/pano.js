
// <![CDATA[

PanoJS.MSG_BEYOND_MIN_ZOOM = null;
PanoJS.MSG_BEYOND_MAX_ZOOM = null;

var panoViewer = null;

function createViewer (panoInfo, baseUrl) {
    if (panoViewer) return;
  
    var myPyramid = new ZoomifyPyramid(panoInfo.width, panoInfo.height, 256);
    
    var myProvider = new PanoJS.TileUrlProvider('','','');
    myProvider.assembleUrl = function(xIndex, yIndex, zoom) {
        return baseUrl + '/' + panoInfo.id + "/" + myPyramid.tile_filename( zoom, xIndex, yIndex );
    }

    var options = {
        tileUrlProvider : myProvider,
        tileSize        : myPyramid.tilesize,
        maxZoom         : myPyramid.getMaxLevel(),
        imageWidth      : myPyramid.width,
        imageHeight     : myPyramid.height,
        staticBaseURL   : '/theme/js/panojs3/',
        blankTile       : '/theme/js/panojs3/images/blank.gif',
        loadingTile     : '/theme/js/panojs3/images/progress.gif'
    };

    if (typeof(panoInfo.initialZoom) != 'undefined') {
        options.initialZoom = panoInfo.initialZoom;
    }
    
    panoViewer = new PanoJS("viewer", options);

    Ext.EventManager.addListener( window, 'resize', callback(panoViewer, panoViewer.resize) );
    panoViewer.init();
};

function initViewer(panoData) {
	var panoContainer = $("#panoContainer");
	var panoHeader = $("#panoHeader");

	// clear out any existing pano
	destroyViewer();
	
	panoContainer.height($('#overlay').dialog('option', 'height') - 70);

	// set the new one
	if (!panoData) {
		console.log("must pass pano information");
		return
	}
	panoHeader.html(panoData.title);

	var viewer = $("<div></div>");
	viewer.attr({
		id: "viewer",
		style: "width: 100%; height: 100%",
		class: "viewer"
	});
	panoContainer.append(viewer);

	createViewer(panoData, "/panorama/" + panoData.panoGroup);
}

function destroyViewer() {
	$('#panoContainer').empty();
	$('#panoHeader').empty();
	panoViewer = null;
}

function showOverlay() {
	var panoData = $(this).data('panoInfo');
	var dHeight = Math.ceil($(window).height() * .95);
	var dWidth = Math.ceil($(window).width() * .95);
	console.log('height: ' + dHeight + ', width: ' + dWidth);
	$('#overlay').dialog({
		modal: true,
		draggable: false,
		resizable: false,
		height: dHeight,
		width: dWidth,
		title: panoData.title
	});
	initViewer(panoData);
}

function hideOverlay() {
	destroyViewer();
	$('#overlay')
		.height(null)
		.hide();
}
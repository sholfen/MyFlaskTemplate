var maskNum = 0;
var total_show_object_list = [];
function mask(text, isMaskBackground, hide_object_list) {
    // default value
    if (isMaskBackground === undefined) {
        isMaskBackground = false;
    }
    if (hide_object_list === undefined) {
        hide_object_list = [];
    }

    // logic of mask function
    maskNum = maskNum +1;
    var backgroundOpacity = isMaskBackground ? 1: 0;

    // hide object
    for (i=0; i<hide_object_list.length; i++){
        hide_object_list[i].hide();
        // keep object for show when unmask
        total_show_object_list.push(hide_object_list[i]);
    }

    // block
    if (1 == maskNum){
        jQuery.blockUI({
            css: {
                border: 'none',
                padding: '15px',
                backgroundColor: '#000',
                '-webkit-border-radius': '10px',
                '-moz-border-radius': '10px',
                opacity: .5,
                color: '#fff'
            },
            overlayCSS: {
                backgroundColor: 'white',
                opacity: backgroundOpacity
            },
            fadeIn: 0,
            message: text
        });
    }
}

function unmask() {
    maskNum = maskNum -1;
    if (0 == maskNum){
        // show object
        for (i=0; i<total_show_object_list.length; i++){
            total_show_object_list[i].show();
        }
        total_show_object_list = [];
        jQuery.unblockUI();
    }
}

function showMessageDialog(message) {
    var scope = angular.element(jQuery("#messageDialog")).scope();
    scope.$apply(function(){
        scope.message = message; 
    });
    jQuery("#messageDialog").dialog();
}


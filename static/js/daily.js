    $(document).ready(function(){
        $('div.btn.btn-info').click( function() {
                loadPopupBox();
            });

        $('#popupBoxClose').click( function() {
            unloadPopupBox();
        });

        function unloadPopupBox() {    // TO Unload the Popupbox
            $('div#popup_box').fadeOut("slow");
            $("#container").css({ // this is just for style
                "opacity": "1"
            });
        }

        function loadPopupBox() {    // To Load the Popupbox
            $('div#popup_box').fadeIn("slow");
            $("#container").css({ // this is just for style
                "opacity": "0.3"
            });
        }

});
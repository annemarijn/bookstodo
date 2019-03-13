// Found at https://stackoverflow.com/questions/12744145/how-to-remember-scroll-position-of-page/12744617

// When document is ready...
$(document).ready(function() {

    // If cookie is set, scroll to the position saved in the cookie.
    if ( $.cookie("scroll") !== null ) {
        $(document).scrollTop( $.cookie("scroll") );
    }

    // When a button is clicked...
    $('#submit').on("click", function() {

        // Set a cookie that holds the scroll position.
        $.cookie("scroll", $(document).scrollTop() );

    });

});
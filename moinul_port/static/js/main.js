
$(window).scroll(function () {

    if ($(window).width() > 990) {
        $('.navbar').addClass('fixed-top');

    }
    var scroll = $(window).scrollTop();
    if (scroll < 60) {
        $('.fixed-top').css('background', 'transparent');
    } else {
        $('.fixed-top').css('background', 'white').css('border-bottom', '1px solid grey');
    }
});



////contact fetch post

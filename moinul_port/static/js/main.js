
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
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({
    "name": "ok",
    "email": "ok",
    "msg": "ok"
});

var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: raw,
    redirect: 'follow'
};

fetch("http://127.0.0.1:8000/contact/", requestOptions)
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));

//refresh image with current image
function refreshImage() {
    fetch('/static/display_img.jpg')
        .then(function (res) {
            document.getElementById('image').src = res.url;
            console.log(res.ok);
        })
        .catch(err => console.log('error ' + err));
}


///*
//schedule function call every interval ms
window.addEventListener('load', function () {
    var interval = 500;
    setInterval(refreshImage, interval);
});
//*/


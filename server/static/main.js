
//refresh image with current image
function refreshImage() {
    fetch('/static/display_img.jpg')
        .then(function (res) {
            document.getElementById('image').src = res.url;
        })
        .catch(err => console.log('error ' + err));
}


//schedule function call every interval ms if video is being streamed
if (document.getElementById('image') != null) {
    window.addEventListener('load', function () {
        var interval = 500;
        setInterval(refreshImage, interval);
    });
}



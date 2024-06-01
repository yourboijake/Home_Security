
console.log('hello test');

function refreshImage() {
    console.log('refreshing image');
    fetch('/static/display_img.jpg')
        .then(function (res) {
            document.getElementById('image').src = res.url;
            console.log(res.ok);
        })
        .catch(err => console.log('error ' + err));
}


///*
window.addEventListener('load', function () {
    var interval = 500;
    setInterval(refreshImage, interval);
});
//*/


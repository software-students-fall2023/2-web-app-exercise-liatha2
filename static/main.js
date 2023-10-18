const gif = document.getElementById('bouncing-gif');

let x = 0;
let y = 0;
let xSpeed = 5;
let ySpeed = 5;

function animate() {
    if (x + gif.width > window.innerWidth || x < 0) {
        xSpeed = -xSpeed;
    }

    if (y + gif.height > window.innerHeight || y < 0) {
        ySpeed = -ySpeed;
    }

    x += xSpeed;
    y += ySpeed;

    gif.style.left = x + 'px';
    gif.style.top = y + 'px';
    requestAnimationFrame(animate);
}
const imageElement = document.getElementById('dj-cool');
const audioElement = document.getElementById('music');

imageElement.addEventListener('click', function() {
    if (audioElement.paused) {
        audioElement.play();
    } else {
        audioElement.pause();
    }
});

animate();

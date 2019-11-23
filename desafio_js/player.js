const playerElement = document.querySelector('#my_player');
const controls = playerElement.querySelector('.buttons_box');
const audioElement = playerElement.querySelector('audio');
const progressBar = playerElement.querySelector('.progress_bar');
const progressBarLowOpacity = playerElement.querySelector('.progress_bar_low_opacity');

const playBtn = controls.querySelector('.play');
const forwards = controls.querySelector('.forwards');
const backwards = controls.querySelector('.backwards');

function checkStatePlay() {
    const pauseButtonState = playerElement.querySelector('#pauseButton');
    const playButtonState = playerElement.querySelector('#playButton');
    if(audioElement.play() === true){
        pauseButtonState.style.display = pauseButtonState.style.display.flex;
        playButtonState.style.display = none;
    }
}

playBtn.addEventListener('click', () => {
    audioElement.play();
    checkStatePlay();
})

// playBtn.addEventListener('click', () => {
//     audioElement.pause();
// })

forwards.addEventListener('click', () => {
    audioElement.currentTime+=10;
})

backwards.addEventListener('click', () => {
    audioElement.currentTime-=10;
})

audioElement.addEventListener('timeupdate', () => {
    progressBar.style.width = 100 * (audioElement.currentTime) / (audioElement.duration)+'%';
})

// audioElement.addEventListener('click', () => {
//     progressBar.style.width = 100 * () / (progressBarLowOpacity.style.width) + '%';
// })
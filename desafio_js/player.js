const playerElement = document.querySelector('#my_player');
const controls = playerElement.querySelector('.buttons_box');
const audioElement = playerElement.querySelector('audio');
const progressBar = playerElement.querySelector('.progress_bar');
const progressBarLowOpacity = playerElement.querySelector('.progress_bar_low_opacity');

const playBtn = controls.querySelector('.play');
const pauseBtn = controls.querySelector('.pause');
const forwards = controls.querySelector('.forwards');
const backwards = controls.querySelector('.backwards');

function checkStatePlayAdd() {
    playBtn.classList.add('remove_button');
}

function checkStatePlayRemove() {
    playBtn.classList.remove('remove_button');
}

function checkStatePauseRemove() {
    pauseBtn.classList.remove('remove_button');
}

function checkStatePauseAdd() {
    pauseBtn.classList.add('remove_button');
}

playBtn.addEventListener('click', () => {
    audioElement.play();
    checkStatePlayAdd();
    checkStatePauseRemove();
})

pauseBtn.addEventListener('click', () => {
    audioElement.pause();
    checkStatePlayRemove();
    checkStatePauseAdd();
})

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
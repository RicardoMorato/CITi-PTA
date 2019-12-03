const playerElement = document.querySelector('#my_player');
const controls = playerElement.querySelector('.buttons_box');
const audioElement = playerElement.querySelector('audio');
const progressBar = playerElement.querySelector('.progress_bar');
const progressBarLowOpacity = playerElement.querySelector('.progress_bar_low_opacity');
const bolinha = playerElement.querySelector('.bolinha');

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

function detectsMousePosition() {
    const posX = event.offsetX;
    const posY = event.offsetY;
    console.log(posX, posY);
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

audioElement.addEventListener('timeupdate',  () => {
    progressBar.style.width = 100 * (audioElement.currentTime) / (audioElement.duration)+'%';
    bolinha.style.marginLeft = progressBar.style.width;
})

progressBarLowOpacity.addEventListener('click', () => {
    detectsMousePosition();
    progressBar.style.width += event.offsetX + 'px';
    bolinha.style.marginLeft = progressBar.style.width;
    // audioElement.currentTime = audioElement.duration * (progressBar.style.width/progressBarLowOpacity.style.width);
})

progressBar.addEventListener('click', () => {
    detectsMousePosition();

    const bar = progressBar.getBoundingClientRect();
    const x = event.clientX;
    const y = event.clientY;

    console.log('X coords: ${Math.round(((x - bar.left)/(bar.left-bar.right)) * 100)}%');

    // progressBar.style.width =  (progressBar.getBoundingClientRect() - event.offsetX);
})
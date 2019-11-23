const playerElement = document.querySelector('#my_player');
const controls = playerElement.querySelector('.buttons_box');
const audioElement = playerElement.querySelector('audio');
const progressBar = playerElement.querySelector('.progress_bar');

const actionBtn = controls.querySelector('.action');
const forwards = controls.querySelector('.forwards');
const backwards = controls.querySelector('.backwards');

actionBtn.addEventListener('click', () => {
    audioElement.play();
})

// actionBtn.addEventListener('click', () => {
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
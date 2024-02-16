const colors = [
    '#2196f3',
    '#e91e63',
    '#ffeb3b',
    '#74ff1d',
];
function createSquare() {
    const section = document.getElementById('main');
    const square = document.createElement('span');
    var size = Math.random() * 50;
    square.style.width = 20 + size + 'px';
    square.style.height = 20 + size + 'px';
    square.style.top = Math.random() * (innerHeight - size ) + 'px';
    square.style.left = Math.random() * (innerWidth - size / 2) + 'px';
    square.style.background = colors[Math.floor(Math.random() * colors.length)];
    square.style.borderRadius = size / 8 + "px";
    square.style.zIndex = 0;
    section.appendChild(square);
    setTimeout(() => {
        square.remove();
    }, 5000);
}
setInterval(createSquare, 200);
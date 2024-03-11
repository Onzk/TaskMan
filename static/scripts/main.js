const drawer = document.getElementById("drawer-label");
const innerPage = document.getElementById("inner-page");

function goToId(id) {
    // drawer.click()
    scrollToElm(innerPage, document.getElementById(id), 600);
}

/////////////

function scrollToElm(container, elm, duration) {
    var pos = getRelativePos(elm);
    scrollTo(container, pos.top, duration / 1000); // duration in seconds
}

function getRelativePos(elm) {
    var pPos = elm.parentNode.getBoundingClientRect(), // parent pos
        cPos = elm.getBoundingClientRect(), // target pos
        pos = {};

    pos.top = cPos.top - pPos.top + elm.parentNode.scrollTop,
        pos.right = cPos.right - pPos.right,
        pos.bottom = cPos.bottom - pPos.bottom,
        pos.left = cPos.left - pPos.left;

    return pos;
}

function scrollTo(element, to, duration, onDone) {
    var start = element.scrollTop,
        change = to - start,
        startTime = performance.now(),
        val, now, elapsed, t;

    function animateScroll() {
        now = performance.now();
        elapsed = (now - startTime) / 1000;
        t = (elapsed / duration);

        element.scrollTop = start + change * easeInOutQuad(t);

        if (t < 1)
            window.requestAnimationFrame(animateScroll);
        else
            onDone && onDone();
    };

    animateScroll();
}

function easeInOutQuad(t) {
    return t < .5 ? 2 * t * t : -1 + (4 - 2 * t) * t
};

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
    square.style.top = (Math.random() * innerHeight) + 'px';
    square.style.left = (Math.random() * innerWidth) + 'px';
    square.style.background = colors[Math.floor(Math.random() * colors.length)];
    square.style.borderRadius = size / 8 + "px";
    square.style.zIndex = 0;
    section.appendChild(square);
    setTimeout(() => {
        square.remove();
    }, 5000);
}
setInterval(createSquare, 200);
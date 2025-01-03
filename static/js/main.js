let clicked = true;

show_nav_bar = () => {
    if (clicked) {
        document.querySelector('#nav').style.display = 'block';
        clicked = false;
    } else {
        document.querySelector('#nav').style.display = 'none';
        clicked = true;
    }
};


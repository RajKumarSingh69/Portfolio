var typed1 = new Typed(".text", {
    strings: ["Data Science Enthusiast", "Junior ML Engineer"],
    typeSpeed: 100,
    backSpeed: 100,
    backDelay: 1000,
    loop: true
});
console.log("Typed.js for .text is initialized");

var typed2 = new Typed(".text2", {
    strings: ["Data Science Enthusiast", "Junior ML Engineer"],
    typeSpeed: 100,
    backSpeed: 100,
    backDelay: 1000,
    loop: true
});
console.log("Typed.js for .text2 is initialized");

var tablinks = document.getElementsByClassName("tab-links");
var tabcontents = document.getElementsByClassName("tab-contents");

function opentab(tabname) {
    for (var tablink of tablinks) {
        tablink.classList.remove("active-link");
    }
    for (var tabcontent of tabcontents) {
        tabcontent.classList.remove("active-tab");
    }
    event.currentTarget.classList.add("active-link");
    document.getElementById(tabname).classList.add("active-tab");
    console.log("Opened tab: " + tabname);
}

document.addEventListener('DOMContentLoaded', function () {
    const seeMoreBtn = document.getElementById('see-more');
    const hideBtn = document.getElementById('hide');
    const additionalProjects = document.querySelector('.additional-projects');

    seeMoreBtn.addEventListener('click', function (e) {
        e.preventDefault();
        additionalProjects.style.display = 'grid';
        seeMoreBtn.style.display = 'none';
        hideBtn.style.display = 'inline-block'; // Show Hide button
    });

    hideBtn.addEventListener('click', function (e) {
        e.preventDefault();
        additionalProjects.style.display = 'none';
        seeMoreBtn.style.display = 'inline-block';
        hideBtn.style.display = 'none'; // Hide Hide button
    });
});



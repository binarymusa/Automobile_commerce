const btn = document.querySelector('#side');
const btncol = document.querySelector('#sc');
const sidebar = document.querySelector('#fix');
const mainContent = document.querySelector('#mainContent');
const dayNight = document.querySelector('#daynight');
const bgclr = document.querySelector('#bodyclr');

dayNight.addEventListener('click', function(){
    bgclr.classList.toggle('white');
});

btn.addEventListener('click', function(){
    sidebar.classList.toggle('show');
    btn.classList.toggle('move');

    if (sidebar.classList.contains('show')) {
        mainContent.classList.remove('col-lg-10');
        mainContent.classList.add('col-lg-9');         
        mainContent.classList.add('ms-auto');       
        // mainContent.style.marginLeft = 'auto'
    } else {
        mainContent.classList.remove('col-lg-9');
        mainContent.classList.add('col-lg-10');
        mainContent.classList.remove('ms-auto');
        mainContent.style.marginLeft = '';
    }   
});

btncol.addEventListener('mouseover', function() {
    btncol.style.backgroundColor = '#e2e2e2bb';
});
btncol.addEventListener('mouseleave', function() {
    btncol.style.backgroundColor = ''; 
    btncol.style.display = ''
});

sidebar.addEventListener('mouseover', function(){
    sidebar.style.opacity = '1';
});
sidebar.addEventListener('mouseleave', function(){
    sidebar.style.opacity = '';
});



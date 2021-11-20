const nextBtn = document.querySelector('#nextPicture');
const prevBtn = document.querySelector('#prevPicture');
const picturesTab = [];
document.querySelectorAll('li').forEach(function(li){
    picturesTab.push(li);
})
let currentPic = 0;

picturesTab[currentPic].className = 'visible';

nextBtn.addEventListener('click', function(){
    picturesTab[currentPic].className = '';
    if(currentPic < picturesTab.length - 1){
        currentPic++;
    }
    picturesTab[currentPic].className = 'visible';
});

prevBtn.addEventListener('click', function (){
    picturesTab[currentPic].className = '';
    if(currentPic > 0){
        currentPic--;
    }
    picturesTab[currentPic].className = 'visible';
});

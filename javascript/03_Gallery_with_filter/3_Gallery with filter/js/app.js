const gallery = [];

document.querySelectorAll('img').forEach(function(image){
    gallery.push(image);
});

const showButton = document.querySelector('#showButton');
const hideButton = document.querySelector('#hideButton');
const input = document.querySelector('#tagInput');

showButton.addEventListener('click', function(){
   input.value = '';
   gallery.forEach(function(img){
       // console.log(img.getAttribute('data-tag').indexOf('sport'));
       if(!(img.getAttribute('data-tag').indexOf(input.value) < 0)){
           console.log('success');
           console.log(img.getAttribute('data-tag'));
       }
   });
});

hideButton.addEventListener('click', function(){
   console.log(input.value);
   input.value = '';
   gallery.forEach(function(img){
       console.log(img.getAttribute('data-tag'));
   });
});
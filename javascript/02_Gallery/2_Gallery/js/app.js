const imgList = []
document.querySelectorAll('li').forEach(function(li){
    imgList.push(li);
});
const body = document.querySelector('body');

imgList.forEach(function(img){
    img.addEventListener('click', function(){
        const imgDiv = document.createElement('div')
        imgDiv.className = 'fullScreen';
        body.appendChild(imgDiv);

        const imgSource = this.querySelector('img').getAttribute('src');
        const image = document.createElement('img');
        image.setAttribute('src', imgSource);
        imgDiv.appendChild(image);

        const btn = document.createElement('button');
        btn.className = 'close';
        btn.innerText = 'Close';
        imgDiv.appendChild(btn);

        document.querySelector('.fullScreen').addEventListener('click', function(){
            this.remove();
        });

        document.querySelector('.close').addEventListener('click', function(){
            document.querySelector('.fullScreen').remove();
        });
    });
});


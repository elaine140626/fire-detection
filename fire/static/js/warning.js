function rebind(){
    // 给所有img 都绑定点击全屏事件
    let img =
        document.getElementById('warning-table').getElementsByTagName('img');
    let len = img.length;
    let popup = document.getElementById('popup');


    for(let i=0;i<len ;i++){

        img[i].onclick = ((event)=>{
            // alert(12333);
            // event = event|window.event;
            // alert(event);
            // let target = document.elementsFromPoint(event.clientX, event.clientY);
            showBig(img[i].src);
        })
    }


    popup.onclick = function () {
        popup.style.display = "none";
    };

    function showBig(src) {
        popup.getElementsByTagName('img')[0].src = src;
        popup.style.display = "block";
    }
}


let makeTrue = document.getElementById('make-true'),
    makkeFalse = document.getElementById('make-false');





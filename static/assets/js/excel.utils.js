function loadImages() {
    let images = document.querySelectorAll('#excel-image')
    console.log(images.length);
    images.forEach((img) => {
        let src = img.getAttribute('src-load')
        img.src = src
    })
}

btn_loadImg = document.getElementById('btn-loadImg')
btn_refresh = document.getElementById('btn-refresh')

if (btn_loadImg != null) {
    btn_loadImg.addEventListener("click", (e) => {
        loadImages()
    })
}
btn_refresh.addEventListener("click", (e) => {
    let excel_name = e.target.getAttribute('excel-name')
    e.target.href = `/excel/refresh/${excel_name}`
})

let btn_copy = document.querySelectorAll('#btn-copy')
let tabla = document.getElementById("example5").rows

btn_copy.forEach(element => {
    element.addEventListener("click", (e) => {
        let col = element.getAttribute('clipboard-target')
        copyColumn(col)
    })
})

function copyColumn(col) {
    let paragraph = document.createElement("div")
    for (let index = 0; index < tabla.length; index++) {
        let p = document.createElement("span")
        p.innerHTML = tabla[index].cells[col].innerText
        paragraph.appendChild(p)
    }
    const body = document.querySelector('body');
    const area = document.createElement('textarea');
    body.appendChild(area);
    body.appendChild(paragraph)

    paragraph.classList.add("d-flex")
    paragraph.classList.add("flex-column")

    area.value = paragraph.innerText
    area.select();
    document.execCommand('copy');

    body.removeChild(area);
    body.removeChild(paragraph)
}

let copyBtn = document.querySelector('#btn-copy-all');
copyBtn.addEventListener('click', function () {
  selectElementContents(document.querySelector('#example5'))
});

function selectElementContents(el) {
    let body = document.body, range, sel;
    if (document.createRange && window.getSelection) {
        range = document.createRange();
        sel = window.getSelection();
        sel.removeAllRanges();
        try {
            range.selectNodeContents(el);
            sel.addRange(range);
        } catch (e) {
            range.selectNode(el);
            sel.addRange(range);
        }
    } else if (body.createTextRange) {
        range = body.createTextRange();
        range.moveToElementText(el);
        range.select();
    }
    document.execCommand("copy");
}
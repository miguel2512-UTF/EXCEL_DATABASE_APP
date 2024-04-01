let text = document.getElementById('codigos')
let resp = document.querySelectorAll('#resp')

text.addEventListener("change", () => {
    resp[0].innerHTML = ""
    resp[1].innerHTML = ""

    let codigos_sin_formato = []
    let codigos_con_formato = []

    codigos_sin_formato = text.value.split('\n')
    codigos_sin_formato.forEach(element => {
        if (element != "") {
            code = `INSTALACION_ORIGEN_V10 = ${element} OR`
            codigos_con_formato.push(String(code))
        }
    });

    codigos_con_formato[codigos_con_formato.length - 1] = codigos_con_formato[codigos_con_formato.length - 1].replace(' OR', '')

    codigos_con_formato.forEach(element => {
        let p = document.createElement("span")
        p.innerHTML = element
        p.classList.add('remove')
        resp[0].appendChild(p)
    })

    codigos_con_formato.forEach(element => {
        let p = document.createElement("span")
        p.innerHTML = element.replace('_V10', '')
        p.classList.add('remove')
        resp[1].appendChild(p)
    })
})

let btn_copy = document.querySelectorAll('.btn-copy')
btn_copy.forEach(element => {
    element.addEventListener("click", (e) => {
        console.log("aaaa", e.target.getAttribute('clipboard-target'));
        handleCopyTextFromParagraph(element.getAttribute('clipboard-target'))
    })
})

function handleCopyTextFromParagraph(clipboard_target) {
    const body = document.querySelector('body');
    const paragraph = document.querySelector(`.${clipboard_target}`);
    const area = document.createElement('textarea');
    body.appendChild(area);

    area.value = paragraph.innerText;
    area.select();
    document.execCommand('copy');

    body.removeChild(area);
}
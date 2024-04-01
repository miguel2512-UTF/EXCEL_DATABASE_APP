// Column Toggle
checkboxes = document.getElementsByName('col');

function toggle(source) {
    for(var i=0, n=checkboxes.length;i<n;i++) {
        checkboxes[i].checked = source.checked;
        checkboxes[i].click()
    }
}	

checkboxes.forEach(boton => {
    boton.addEventListener('click', columnaToggle)
    boton.checked=true
})	

let name = checkboxes[0].getAttribute('excel-name')

function columnaToggle(e) {
    let columns = localStorage.getItem(name)
    columns = JSON.parse(columns)

    if (e.target.checked == false) {
        document.querySelectorAll(`.${e.target.id}`).forEach((element)=>{
            element.setAttribute('hidden','')
        })
        columns[e.target.id] = false   
    }else{
        document.querySelectorAll(`.${e.target.id}`).forEach((element)=>{
            element.removeAttribute('hidden','')
        })
        columns[e.target.id] = true
    }

    columns = JSON.stringify(columns)
    localStorage.setItem(name, columns)
}

if (localStorage.getItem(name) == null){
    let configColumns = {}
    checkboxes.forEach((element)=>{
        configColumns[element.id] = true
    })
    localStorage.setItem(name, JSON.stringify(configColumns))
}

if (localStorage.getItem(name)){
    let columns = localStorage.getItem(name)
    columns = JSON.parse(columns)

    checkboxes.forEach((element)=>{
        if (columns[element.id]){
            document.querySelectorAll(`.${element.id}`).forEach((element)=>{
                element.removeAttribute('hidden','')
            })
            document.getElementById(`${element.id}`).checked=true
        }else{
            document.querySelectorAll(`.${element.id}`).forEach((element)=>{
                element.setAttribute('hidden','')
            })
            document.getElementById(`${element.id}`).checked=false
        }
})
}
// Column Toggle
checkboxes = document.getElementsByName('col');

function toggle(source) {
    for (let i = 0, n = checkboxes.length; i < n; i++) {
        checkboxes[i].checked = source.checked;
        checkboxes[i].click()
    }
}

checkboxes.forEach(boton => {
    boton.addEventListener('click', columnaToggle)
    boton.checked = true
})

let name = checkboxes[0].getAttribute('excel-name')

function columnaToggle(e) {
    let columns = localStorage.getItem(name)
    columns = JSON.parse(columns)

    let rows = document.getElementById('example5').rows;

    let do_show = e.target.checked;
    let col_no = parseInt(e.target.getAttribute("data-column"))
    for (let row = 0; row < rows.length; row++) {
        let cols = rows[row].cells;
        if (col_no >= 0 && col_no < cols.length) {
            cols[col_no].style.display = do_show ? '' : 'none';
        }
    }
    columns[e.target.id] = do_show

    columns = JSON.stringify(columns)
    localStorage.setItem(name, columns)
}

if (localStorage.getItem(name) == null) {
    let configColumns = {}
    checkboxes.forEach((element) => {
        configColumns[element.id] = true
    })
    localStorage.setItem(name, JSON.stringify(configColumns))
}
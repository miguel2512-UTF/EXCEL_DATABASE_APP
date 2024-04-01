let excel_name = document.querySelector('.excel-title').textContent
let checkboxes = document.getElementsByName('col');

$(document).ready(function () {
    let columns = []
    let req = new XMLHttpRequest()

    req.open("GET", `/excel/test/${excel_name}`)

    req.onload = () => {
        let column_names = JSON.parse(req.response);
        column_names.column_names.forEach(column => {
            columns.push({
                "data": String(column),
                "defaultContent": "",
                "render": function (data, type, row, meta) {
                    if (typeof data == "string") {
                        if (data.startsWith("http")) {
                            return '<div class="modal-container"><img src-load="' + data + '" id="excel-image"></div>';
                        }
                    }

                    if (typeof data == "string") {
                        if (data == "None") {
                            return ""
                        }
                    }

                    return data
                }
            })
        })

        let excel_table = $("#example5").DataTable({
            deferRender: true,
            scrollCollapse: true,
            scroller: true,
            order: [],
            searchDelay: 350,
            serverSide: true,
            processing: true,
            "ajax": (data, callback, settings) => {
                let columna_filtro = ""
                if (data.order.length > 0) {
                    columna_filtro = data.columns[data.order[0].column].data
                }
                let reverse = ""
                if (data.order.length > 0) {
                    reverse = data.order[0].dir
                }
                $.get(`/excel/test/${excel_name}`, {
                    limite: data.length,
                    inicio: data.start,
                    filtro: data.search.value,
                    order_by: columna_filtro,
                    dir: reverse
                }, (res) => {
                    console.log(data);
                    console.log(res);
                    console.log(columns);

                    setTimeout(()=>{
                        refreshColumns()
                        modalImages()
                    }, 0)

                    callback({
                        recordsTotal: res.length,
                        recordsFiltered: res.length,
                        data: res.data
                    });
                })
            },
            "columns": columns
        })

        let table = document.getElementById('example5');
        let parent = table.parentNode;
        let div_scroll = document.createElement('div');

        div_scroll.classList.add('table-scroll')
        parent.replaceChild(div_scroll, table);
        div_scroll.appendChild(table);
    }

    req.send()
})

function refreshColumns() {
    if (localStorage.getItem(excel_name)) {
        let columns = localStorage.getItem(excel_name)
        columns = JSON.parse(columns)

        let rows = document.getElementById('example5').rows;

        checkboxes.forEach((element) => {
            let do_show = columns[element.id];
            let col_no = parseInt(element.getAttribute("data-column"))
            for (let row = 0; row < rows.length; row++) {
                let cols = rows[row].cells;
                if (col_no >= 0 && col_no < cols.length) {
                    cols[col_no].style.display = do_show ? '' : 'none';
                }
            }

            document.getElementById(`${element.id}`).checked = columns[element.id];
        })
    }
}

function modalImages() {      
    function zoomEvent(e) {
        e.target.classList.toggle("zoom")
    }

    document.querySelectorAll(".modal-container img").forEach(el => {
        el.addEventListener("click", function (ev) {
            ev.stopPropagation();
            this.parentNode.classList.add("active")
            document.querySelector(".modal-container.active img").addEventListener("click", zoomEvent)
        })
    });

    document.querySelectorAll(".modal-container").forEach(el => {
        el.addEventListener("click", function (ev) {
            document.querySelector(".modal-container.active img").removeEventListener("click", zoomEvent)
            this.classList.remove("active")
        })
    });
}
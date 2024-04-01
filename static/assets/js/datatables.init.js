let table_excel = $('#example5').DataTable({
    deferRender:    true,
    scrollCollapse: true,
    scroller:       true,
    order: []
});

let table = document.getElementById('example5')
let parent = table.parentNode;
let div_scroll = document.createElement('div');

div_scroll.classList.add('table-scroll')
parent.replaceChild(div_scroll, table);
div_scroll.appendChild(table);
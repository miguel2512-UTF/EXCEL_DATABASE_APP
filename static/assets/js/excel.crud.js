$(document).ready(function() {
    $(".btn-edit").on("click", function(e) {
        e.preventDefault();
        let href = $(this).attr("href");
        $.get(href, (excel) => {
            $("#edit-excel #id_excel").val(excel.id)
            $("#edit-excel #id_name").val(excel.name)
            $("#edit-excel #id_url").val(excel.url)
            $("#edit-excel #id_load_images").prop("checked", excel.loadImages)
            $("#edit-excel").modal("show")
        })
    })
})
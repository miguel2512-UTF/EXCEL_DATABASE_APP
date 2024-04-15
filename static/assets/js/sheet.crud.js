$(document).ready(function() {
    $(".btn-edit").on("click", function(e) {
        e.preventDefault();
        let href = $(this).attr("href");
        $.get(href, (excel) => {
            $("#edit-sheet #id_sheet").val(excel.id)
            $("#edit-sheet #id_name").val(excel.name)
            $("#edit-sheet #id_url").val(excel.url)
            $("#edit-sheet #id_load_images").prop("checked", excel.loadImages)
            $("#edit-sheet").modal("show")
        })
    })
})
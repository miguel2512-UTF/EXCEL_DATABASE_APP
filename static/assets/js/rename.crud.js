$(document).ready(function(){
    $('.btn-edit').on('click', function(event) {
        event.preventDefault();
        var href = $(this).attr('href');

        $.get(href, function (task) {
            $("#edit-task #id_task").val(task.id)
            $("#edit-task #id_name").val(task.name)
            $("#edit-task #id_folder").val(task.folder)
            if (task.is_reverse == true) {
                $("#edit-task #id_is_reverse").parent().removeAttr("hidden", "")
                $("#edit-task #id_reverse").parent().removeAttr("hidden", "")
                $("#edit-task #id_is_reverse").prop("checked", true)
                $("#edit-task #id_reverse").val(task.reverse)
                $("#edit-task #id_replace").parent().attr("hidden", "")
                $("#edit-task #id_replace").val("")
                $("#edit-task #id_insert").parent().attr("hidden", "")
                $("#edit-task #id_insert").val("")
            }else{
                $("#edit-task #id_reverse").parent().attr("hidden", "")
                $("#edit-task #id_reverse").val("")
                $("#edit-task #id_is_reverse").prop("checked", false)
                $("#edit-task #id_replace").val(task.replace)
                $("#edit-task #id_insert").val(task.insert)
                $("#edit-task #id_replace").parent().removeAttr("hidden", "")
                $("#edit-task #id_insert").parent().removeAttr("hidden", "")
            }
                
            $("#edit-task").modal("show")
        })
    })
})
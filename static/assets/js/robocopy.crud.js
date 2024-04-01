$(document).ready(function(){
    $('.btn-edit').on('click', function(event) {
        event.preventDefault();
        var href = $(this).attr('href');

        $.get(href, function (task) {
            $("#edit-task #id_task").val(task.id)
            $("#edit-task #id_name").val(task.name)
            $("#edit-task #id_source_folder").val(task.source_folder)
            $("#edit-task #id_destination_folder").val(task.destination_folder)
            $("#edit-task #id_group").val(task.group)
            $("#edit-task").modal("show")
        })
    })

    $('.btn-log').on('click', function(event) {
        event.preventDefault();
        var href = $(this).attr('href');

        $.get(href, function (task_log) {
            $("#exampleModal #date-init").text(task_log.date_init)
            $("#exampleModal #date-finish").text(task_log.date_finish)
            $("#exampleModal #copied-files").text(task_log.copied_files)
            $("#exampleModal #skiped-files").text(task_log.skiped_files)
            $("#exampleModal #history").attr("href", `/robocopy/history/${task_log.task}`)
            $("#exampleModal").modal("show")
        })
    })
})
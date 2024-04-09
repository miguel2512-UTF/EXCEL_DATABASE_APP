document.querySelectorAll(".btn-connect").forEach(btn => {
    btn.addEventListener("click", (e) => {
        e.preventDefault()

        fetch(btn.href).then(res => res.json()).then(data => {
            document.querySelector("#connect-excel #id_sheet").value = data.id
            document.querySelector("#connect-excel #id_url_api").value = data.api_url

            if (data.api_isactive) {
                document.querySelector("#connect-excel #id_url_api").parentElement.removeAttribute("hidden", "")
                document.querySelector("#connect-excel #id_api_password").parentElement.setAttribute("hidden", "")
                document.querySelector("#connect-excel .modal-footer").firstElementChild.textContent = "Close"
                document.querySelector("#connect-excel .modal-footer").lastElementChild.setAttribute("hidden", "")
            } else {
                document.querySelector("#connect-excel #id_url_api").parentElement.setAttribute("hidden", "")
                document.querySelector("#connect-excel #id_api_password").parentElement.removeAttribute("hidden", "")
                document.querySelector("#connect-excel .modal-footer").firstElementChild.textContent = "Cancel"
                document.querySelector("#connect-excel .modal-footer").lastElementChild.removeAttribute("hidden", "")
            }
            $("#connect-excel").modal("show")
        })
    })
})
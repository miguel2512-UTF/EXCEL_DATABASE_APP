let status = document.querySelectorAll('.status')

function checkStatus() {
    status.forEach(element => {
        let req = new XMLHttpRequest()
        req.open('GET', `/rename/status/${element.id}`)
        req.send()
        req.onload = () => {
            console.log(req.response);
            if (req.response == "True") {
                element.innerHTML = `
                <span class="badge text-bg-success align">
                <div class="spinner-border spinner-border-sm text-light mr-5" role="status"></div>
                Ejecutando
                </span>
                `
            } else {
                element.innerHTML = `
                <span class="badge text-bg-danger align">
                    <i class='bx bx-stop f-14'></i>
                    Detenida
                </span>
                `
            }
        }
    });
}
checkStatus()
setInterval(()=>checkStatus(), 10000)

let toast = document.querySelector("#liveToastBtn")
toast.style.display = "none"
toast.onclick = function() {
  $('#liveToast').toast("show");
}

let btn_task = document.querySelectorAll('#btn-task')
btn_task.forEach(element => {
    element.addEventListener("click", (e) => {
        e.preventDefault()
        let req = new XMLHttpRequest()
        req.open('GET', element.href)
        req.send()
        req.onload = () => {
            data = JSON.parse(req.response)
            if (data.error) {
                document.querySelector(".me-auto").innerHTML = data.task
                document.querySelector(".toast-error").innerHTML = data.error
                document.querySelector(".toast-message").innerHTML = data.message
                toast.click()
            }
        }
    })
})

let btn_stop_task = document.querySelectorAll('#btn-stop-task')
btn_stop_task.forEach(element => {
    element.addEventListener("click", (e) => {
        e.preventDefault()

        let req = new XMLHttpRequest()
        req.open('GET', element.href)
        req.send()
        req.onload = () => {
            data = JSON.parse(req.response)
            if (data.error) {
                document.querySelector(".me-auto").innerHTML = data.task
                document.querySelector(".toast-error").innerHTML = data.error
                document.querySelector(".toast-message").innerHTML = data.message
                toast.click()
            }
        }
        setTimeout(() => checkStatus(), 1000)
    })
})

let is_reverse = document.getElementsByName("is_reverse")
let reverse = document.getElementsByName("reverse")
let replace = document.getElementsByName("replace")
let insert = document.getElementsByName("insert")

reverse[0].parentElement.setAttribute("hidden", "")

is_reverse.forEach((element, index) => {
    element.addEventListener("click", (e) => {
        e.target.value = e.target.checked
        if (e.target.checked) {
            reverse[index].parentElement.removeAttribute("hidden", "")
            replace[index].parentElement.setAttribute("hidden", "")
            insert[index].parentElement.setAttribute("hidden", "")
        } else {
            replace[index].parentElement.removeAttribute("hidden", "")
            insert[index].parentElement.removeAttribute("hidden", "")
            reverse[index].parentElement.setAttribute("hidden", "")
        }
    })
})

open_folder_buttons = document.querySelectorAll(".btn-open-folder")

open_folder_buttons.forEach(element => {
    element.addEventListener("click", (e) => {
        e.preventDefault()
        let href = element.getAttribute("href")

        let req = new XMLHttpRequest()
        req.open('GET', href)
        req.send()
    })
})
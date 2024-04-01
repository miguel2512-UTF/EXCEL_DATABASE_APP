let status = document.querySelectorAll('.status')

function checkStatus() {
    status.forEach(element => {
        let req = new XMLHttpRequest()
        req.open('GET', `/robocopy/status/${element.id}`)
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
setInterval(() => checkStatus(), 30000)

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
        setTimeout(() => checkStatus(), 1000)
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

groups = document.querySelectorAll(".task-group-head i");

groups.forEach(element => {
    element.addEventListener("click", (e) => {
        element.parentElement.parentElement.classList.toggle("active")
    })
})

groupSelect = document.getElementById("id_group")

let new_group_opt = document.createElement("option")
new_group_opt.value = ""
new_group_opt.innerHTML = ("&#x2b; Nuevo grupo")
groupSelect.appendChild(new_group_opt)


function popupwindow(url, title, w, h) {
    let left = (screen.width/2)-(w/2);
    let top = (screen.height/2)-(h/2);
    return window.open(url, title, 'toolbar=no, location=no, directories=no, status=no, menubar=no, scrollbars=no, resizable=no, copyhistory=no, width='+w+', height='+h+', top='+top+', left='+left);
} 

groupSelect.addEventListener("change", (e) => {
    if (groupSelect.options[groupSelect.selectedIndex] == groupSelect.options[groupSelect.options.length - 1]) {
        let group_window = popupwindow("http://localhost:7000/robocopy/create/group/", "popup", 600, 600)

        group_window.onunload = function(){
            setTimeout(()=>{
                if (group_window.closed) {
                    let req  = new XMLHttpRequest()
                    req.open("GET", "http://localhost:7000/robocopy/group/get")
                    req.onload = () => {
                        Object.values(groupSelect).forEach(element => {
                            element != groupSelect[0] ? groupSelect.removeChild(element) : ""
                        })
                        groups = JSON.parse(req.response)
                        groups.forEach(element => {
                            opt = document.createElement("option")
                            opt.innerHTML = element.name
                            opt.value = element.id
                            groupSelect.appendChild(opt)
                        })
                        groupSelect.appendChild(new_group_opt)
                    }
                    req.send();
                }
            })
        };
    }
})
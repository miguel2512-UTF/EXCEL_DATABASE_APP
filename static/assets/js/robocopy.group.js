let groups = document.querySelectorAll(".task-group-head i");

groups.forEach(element => {
    element.addEventListener("click", (e) => {
        element.parentElement.parentElement.classList.toggle("active")
    })
})

let groupSelect = document.getElementById("id_group")

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
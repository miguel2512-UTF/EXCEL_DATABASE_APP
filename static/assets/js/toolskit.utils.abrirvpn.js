let btn_vpn = document.querySelectorAll('#btn-vpn')
btn_vpn.forEach(element => {
    element.addEventListener("click", (e)=>{
        e.preventDefault()
        let req = new XMLHttpRequest()
        req.open('GET', element.href)
        req.send()
    })
})

let btn_memento = document.querySelectorAll('#btn-memento')
btn_memento.forEach(element => {
    element.addEventListener("click", (e)=>{
        e.preventDefault()
        let req = new XMLHttpRequest()
        req.open('GET', element.href)
        req.send()
    })
});
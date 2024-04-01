const btn_menu = document.getElementById('menu');
const sidebar = document.querySelector('.sidebar');
const backdrop = document.querySelector('.backdrop')

btn_menu.addEventListener('click', ()=>{
    sidebar.classList.toggle('active')
    backdrop.classList.toggle('active')
})

let plus = document.querySelectorAll(".arrow")      
plus.forEach((plusBtn)=>{
    plusBtn.addEventListener("click",(e)=>{
        let plusParent = e.target.parentElement.parentElement
        plusParent.classList.toggle("show")
    })
})
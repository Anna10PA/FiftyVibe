// verify_code.html
document.addEventListener('DOMContentLoaded', () => {
    const codeInput = document.querySelector('#code')
    const message = document.querySelector('#message')
    let prevValue = ''

    if (!codeInput) return

    codeInput.addEventListener('paste', (e) => {
        e.preventDefault()
        message.textContent = 'You cannot paste the code! Please type it manually.'
    })
})

// user_profile.html
let new_post = document.querySelector('#new_post')
let nav = document.querySelector('#nav')
let open = true

new_post.addEventListener('click', (e)=> {
    if (open) {
        new_post.className = 'fa-solid fa-minus absolute top-5 right-2 text-gray-800 text-2xl duration-100 hover:text-[#5B0E14] cursor-pointer '
        nav.className = 'bg-[#A3202A] absolute translate-x-[0px] right-0 z-[100] top-[60px] w-max px-3 py-5 rounded flex flex-col items-center gap-[15px] opacity-100 duration-300'
    } else {
        new_post.className = 'fa-solid fa-plus absolute top-5 right-2 text-gray-800 text-2xl duration-100 hover:text-[#5B0E14] cursor-pointer '
        nav.className = 'bg-[#A3202A] absolute right-0 z-[100] translate-x-[100px] top-[60px] w-max px-3 py-5 rounded flex flex-col items-center gap-[15px] duration-300 opacity-0'
    }
    open = !open
})
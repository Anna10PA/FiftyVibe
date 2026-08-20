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


// user_profile.html / nav
let new_post = document.querySelector('#new_post')
let nav = document.querySelector('#nav')
let open = true

new_post.addEventListener('click', (e) => {
    if (open) {
        new_post.className = 'fa-solid fa-minus absolute top-5 right-2 text-gray-800 text-2xl duration-100 hover:text-[#5B0E14] cursor-pointer '
        nav.className = 'bg-[#A3202A] absolute translate-x-[0px] right-0 z-[100] top-[60px] w-max px-3 py-5 rounded flex flex-col items-center gap-[15px] opacity-100 duration-300'
    } else {
        new_post.className = 'fa-solid fa-plus absolute top-5 right-2 text-gray-800 text-2xl duration-100 hover:text-[#5B0E14] cursor-pointer '
        nav.className = 'bg-[#A3202A] absolute right-0 z-[100] translate-x-[100px] top-[60px] w-max px-3 py-5 rounded flex flex-col items-center gap-[15px] duration-300 opacity-0'
    }
    open = !open
})


// user_profile.html (add post)
let filesInput = document.querySelector('#files')
let show_posts = document.querySelector('#show_posts')

let fileContainer = new DataTransfer()

filesInput.addEventListener('change', (e) => {
    let newFiles = e.target.files

    for (let i = 0; i < newFiles.length; i++) {
        let currentFile = newFiles[i]
        fileContainer.items.add(currentFile)
        let fileUrl = URL.createObjectURL(currentFile)

        if (currentFile.type.includes('image')) {
            show_posts.innerHTML += `
            <div class="last:odd:col-span-2 w-full h-full">
            <img src='${fileUrl}' class='w-full object-cover h-full' />
            </div>
            `
        } else if (currentFile.type.includes('video')) {
            show_posts.innerHTML += `
            <div class="last:odd:col-span-2 w-full h-full">
                <video class="h-full">
                    <source src='${fileUrl}'>
                </video>
            </div>
        `
        }

    }

    filesInput.files = fileContainer.files
})


// user_profile.html (add tags)
let tagInput = document.querySelector('#tag_input')
let tagsContainer = document.querySelector('#tag_container')
let hiddenTagsInput = document.querySelector('#hidden-tags')

let tagsArray = []


function addTag() {
    let tagValue = tagInput.value.trim()

    if (tagValue !== "") {
        if (!tagValue.startsWith('#')) {
            tagValue = '#' + tagValue
        }

        tagsArray.push(tagValue)

        tagsContainer.innerHTML += `
            <span class="bg-red-200 text-red-800 px-2 py-1 rounded-full text-sm">
                ${tagValue.toLowerCase()}
            </span>
        `

        hiddenTagsInput.value = tagsArray.join(',')
        tagInput.value = ''
    }
}


tagInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        e.preventDefault()
        addTag()
    }
})
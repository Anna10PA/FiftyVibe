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
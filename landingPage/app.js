let navbar = document.querySelector('nav')
let signIn = document.querySelector('#sign-inbtn')
let signUp = document.querySelector('#sign-upbtn')
let navLinks = document.querySelectorAll('.nav-link')
let humburger = document.querySelector('.navbar-toggler')
let main = document.querySelector('main')
let upArrow = document.querySelector('.up')

navLinks.forEach(navlink => navlink.addEventListener(('click'), () => {
    humburger.click()
}))

window.addEventListener('resize', () => {
    if (window.innerWidth >= 550 && window.innerWidth <= 1145) {
        signIn.innerHTML = 'Login'
        signUp.innerHTML = 'Join'

    } else {
        signIn.innerHTML = 'Sign In'
        signUp.innerHTML = 'Sign Up'
    }
})
window.addEventListener('scroll', () => {
    let top = main.getBoundingClientRect().top
    if (top > 282) {
        upArrow.classList.remove('show')
        upArrow.classList.add('hide')
        console.log('work')
    } else {
        upArrow.classList.remove('hide')
        upArrow.classList.add('show')
        console.log('not-working')
    }

})
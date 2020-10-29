let navbar = document.querySelector('nav')
let signIn = document.querySelector('#sign-inbtn')
let signUp = document.querySelector('#sign-upbtn')
let navLinks = document.querySelectorAll('.nav-link')
let humburger = document.querySelector('.navbar-toggler')

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
window.addEventListener(('scroll'), () => {
    let top = navbar.getBoundingClientRect().top

})
function validate(e) {
    e.preventDefault();
    const email = document.getElementById("email").value;
    const pass = document.getElementById("password").value;
    const age = document.getElementById("age").value;
    const msgBox = document.getElementById("message").value;
 

    if(email === " ") {
        message = "please enter an email.";
        msgBox.style.color = "red";
    } else if (pass === " "){
        message = "password  8 chracters. must be at least";
        msgBox.style.color = "red";
    }

}
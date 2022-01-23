var labels = document.querySelectorAll("label");
var form = document.getElementsByClassName("form-content")[0];
form.style.marginTop = "20px";

for (let index = 0; index < labels.length; index++) {
    labels[index].style.fontWeight = "bold";
    labels[index].style.fontSize = "18px";
    labels[index].style.fontFamily = "Manrope";
    var brTag = document.createElement("br");
    labels[index].parentNode.insertBefore(brTag, labels[index].nextSibling);
    if(index == 2)
        labels[index].innerHTML = "Password: ";
    if(index == 3)
        labels[index].innerHTML = "Confirm Password: ";
}

var usernameInput = document.getElementById("id_username");
usernameInput.style.border = "1px solid grey";
usernameInput.style.borderRadius = "5px";
usernameInput.style.fontSize = "16px";
usernameInput.style.boxSizing = "border-box";
usernameInput.style.width = "300px";
usernameInput.setAttribute("placeholder", "");
var brTag = document.createElement("br");
usernameInput.parentNode.insertBefore(brTag, usernameInput.nextSibling);

var emailInput = document.getElementById("id_email");
emailInput.style.border = "1px solid grey";
emailInput.style.borderRadius = "5px";
emailInput.style.fontSize = "16px";
emailInput.style.boxSizing = "border-box";
emailInput.style.width = "300px";
emailInput.setAttribute("placeholder", "");
var brTag = document.createElement("br");
emailInput.parentNode.insertBefore(brTag, emailInput.nextSibling);

var passwordInput = document.getElementById("id_password1");
passwordInput.style.border = "1px solid grey";
passwordInput.style.borderRadius = "5px";
passwordInput.style.fontSize = "16px";
passwordInput.style.boxSizing = "border-box";
passwordInput.style.width = "300px";
passwordInput.setAttribute("placeholder", "");
var brTag = document.createElement("br");
passwordInput.parentNode.insertBefore(brTag, passwordInput.nextSibling);

var passwordInput = document.getElementById("id_password2");
passwordInput.style.border = "1px solid grey";
passwordInput.style.borderRadius = "5px";
passwordInput.style.fontSize = "16px";
passwordInput.style.boxSizing = "border-box";
passwordInput.style.width = "300px";
passwordInput.setAttribute("placeholder", "");
var brTag = document.createElement("br");
passwordInput.parentNode.insertBefore(brTag, passwordInput.nextSibling);
var labels = document.querySelectorAll("label");
var form = document.getElementsByClassName("form-content")[0];

for (let index = 0; index < labels.length; index++) {
    labels[index].style.fontWeight = "bold";
    labels[index].style.fontSize = "18px";
    labels[index].style.marginTop = "20px";
    labels[index].style.fontFamily = "Manrope";
    var brTag = document.createElement("br");
    labels[index].parentNode.insertBefore(brTag, labels[index].nextSibling);
}

var emailInput = document.getElementById("id_username");
var passwordInput = document.getElementById("id_password");

emailInput.style.border = "1px solid grey";
emailInput.style.borderRadius = "5px";
emailInput.style.fontSize = "16px";
emailInput.style.boxSizing = "border-box";
emailInput.style.width = "300px";
emailInput.setAttribute("placeholder", "");
var brTag = document.createElement("br");
emailInput.parentNode.insertBefore(brTag, emailInput.nextSibling);

passwordInput.style.border = "1px solid grey";
passwordInput.style.borderRadius = "5px";
passwordInput.style.fontSize = "16px";
passwordInput.style.boxSizing = "border-box";
passwordInput.style.width = "300px";
passwordInput.setAttribute("placeholder", "");
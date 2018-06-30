function mainf(){
if(document.getElementById('rem').checked)
{
user = document.getElementById("user").value;
name ="userId";
document.cookie=name+"="+user+";expires=Sat,30 Jun 2018 12:00:00 UTC";
}
}

function validate(){
console.log("function active");
user = document.regform.username.value
pass = document.regform.password.value
rpass = document.regform.rpassword.value
fullname = document.regform.fullname.value
email = document.regform.email.value
var error = new Array();
var format = /[ !@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/;
if (user.length<5 || user.length > 10)
{
	error.push("Username must be within 5 to 10 chars<br>")
}
else
{
	error.push("")
}

if(fullname.length==0)
{
	error.push("Fullname can't be empty<br>")
}
else
{
	error.push("")
}

var atpos=email.indexOf("@");
var dotpos=email.lastIndexOf(".");
if (atpos<1 || dotpos<atpos+2 || dotpos+2>=email.length)
{
	error.push("enter a valid email id<br>")
}
else
{
	error.push("")
}

if( !pass.match(/[a-z]/i) || pass.length<4 || !pass.match(/[0-9]/) || !format.test(pass))
{
	error.push("Password must contain atleast one alphabet,one digit,one special character and have a minimum length of 5<br>")
}
else
{
	error.push("")
}

if(pass !=rpass)
{
	error.push("Passwords don't match")
}
else
{
	error.push("")
}

console.log(error);
var f=0;
for(var i=0;i<5;i++)
{
if(error[i]=="")
{
	f=1
}
else{
	f=0
	break;
}
}
if(f==1)
{
console.log('true');
return true;
}

else
{
if(!document.getElementById("div0"))
{
div = document.createElement("div")
div.id="div0"
div.style.color="red"
document.getElementById("username").appendChild(div)
}
div = document.getElementById("div0")
div.innerHTML=error[0];
document.getElementById("username").appendChild(div)
if(!document.getElementById("div1"))
{
div = document.createElement("div")
div.id="div1"
div.style.color="red"
document.getElementById("fullname").appendChild(div)
}
div = document.getElementById("div1")
div.innerHTML=error[1];
document.getElementById("fullname").appendChild(div)

if(!document.getElementById("div2"))
{
div = document.createElement("div")
div.id="div2"
div.style.color="red"
document.getElementById("email").appendChild(div)
}
div = document.getElementById("div2")
div.innerHTML=error[2];
document.getElementById("email").appendChild(div)

if(!document.getElementById("div3"))
{
div = document.createElement("div")
div.id="div3"
div.style.color="red"
document.getElementById("password").appendChild(div)
}
div = document.getElementById("div3")
div.innerHTML=error[3];
document.getElementById("password").appendChild(div)

if(!document.getElementById("div4"))
{
div = document.createElement("div")
div.id="div4"
div.style.color="red"
document.getElementById("rpassword").appendChild(div)
}
div = document.getElementById("div4")
div.innerHTML=error[4];
document.getElementById("rpassword").appendChild(div)

}
console.log('false');
return false;
}

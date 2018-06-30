x = document.getElementById("logout").innerHTML
user = x.slice(8,);
d = new Date();
d.setTime(d.getTime() - (1000*60*60*24));
expires = "expires=" + d.toGMTString();
document.cookie = "userId="+user+"; "+expires;

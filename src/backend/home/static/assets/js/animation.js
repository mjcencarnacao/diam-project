function doThis(id) {
  var str0 = id + "-0star";
  var strnota = id + "-nota";
  var str1 = id + "-1star";
  var str2 = id + "-2star";
  var str3 = id + "-3star";
  var str4 = id + "-4star";
  var str5 = id + "-5star";
  var str6 = id + "-6star";
  var str7 = id + "-7star";
  var str8 = id + "-8star";
  var str9 = id + "-9star";
  var str10 = id + "-10star";

  document.getElementById(str0).style.display = "inline";
  document.getElementById(strnota).style.display = "inline";
  document.getElementById(str1).style.display = "inline";
  document.getElementById(str1).style.color = "orange";
  document.getElementById(str2).style.display = "inline";
  document.getElementById(str2).style.color = "orange";
  document.getElementById(str3).style.display = "inline";
  document.getElementById(str3).style.color = "orange";
  document.getElementById(str4).style.display = "inline";
  document.getElementById(str4).style.color = "orange";
  document.getElementById(str5).style.display = "inline";
  document.getElementById(str5).style.color = "orange";
  document.getElementById(str6).style.display = "inline";
  document.getElementById(str6).style.color = "orange";
  document.getElementById(str7).style.display = "inline";
  document.getElementById(str7).style.color = "orange";
}

function doThat(id) {
  var str0 = id + "-0star";
  var strnota = id + "-nota";
  var str1 = id + "-1star";
  var str2 = id + "-2star";
  var str3 = id + "-3star";
  var str4 = id + "-4star";
  var str5 = id + "-5star";
  var str6 = id + "-6star";
  var str7 = id + "-7star";

  document.getElementById(strnota).style.display = "none";
  document.getElementById(str1).style.display = "none";
  document.getElementById(str2).style.display = "none";
  document.getElementById(str3).style.display = "none";
  document.getElementById(str4).style.display = "none";
  document.getElementById(str5).style.display = "none";
  document.getElementById(str6).style.display = "none";
  document.getElementById(str7).style.display = "none";
}

function doHeart(id) {
  var strheart = id + "-heart";
  document.getElementById(strheart).style.color = "red";
}

function paintheart(id) {
  var strheart = id + "-heart";
  document.getElementById(strheart).style.color = "red";
}

function unpaintheart(id) {
  var strheart = id + "-heart";
  document.getElementById(strheart).style.color = "black";
}

function hoverplus(id){
  var strplus = id;
  document.getElementById(strplus).style.transform = 'scale(1.5)';
}

function hoverplusout(id){
  var strplus = id;
  document.getElementById(strplus).style.transform = 'scale(1)';
}
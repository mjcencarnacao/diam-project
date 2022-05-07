function doThis(id, feedback) {
  var evaluation;
  var strnota = id + "-nota";
  if(feedback == 0) {
    evaluation = "Negativo ";
    document.getElementById(strnota).style.color = "red";
  }
    else {
      evaluation = "Positivo ";
      document.getElementById(strnota).style.color = "green";
    }
  
  var aifeedback = id + "-aifeedback";
  var aiscore = id + "-aiscore";

  document.getElementById(aifeedback).style.display = "inline";
  document.getElementById(strnota).innerHTML = evaluation;
  document.getElementById(strnota).style.display = "inline";
  document.getElementById(aiscore).style.display = "inline";
}

function doThat(id) {
  var aiscore = id + "-aiscore";
  var strnota = id + "-nota";
 
  document.getElementById(aiscore).style.display = "none";
  document.getElementById(strnota).style.display = "none";
}

function doThumbsup(id, likes_value) {
  var thumbsup = id + "-thumbsup";
  var likes = id + "-likes";
  //var likes_evaluation = likes_value + " likes"
  document.getElementById(thumbsup).style.color = "green";
  //document.getElementById(likes).innerHTML = likes_evaluation;
  document.getElementById(likes).style.display = "inline";
}

function paintthumbsup(id) {
  var thumbsup = id + "-thumbsup";
  document.getElementById(thumbsup).style.color = "green";
}

function unpaintthumbsup(id) {
  var thumbsup = id + "-thumbsup";
  document.getElementById(thumbsup).style.color = "black";
}

function doThumbsdown(id, likes_value) {
  var thumbsdown = id + "-thumbsdown";
  var likes = id + "-likes";
  //var likes_evaluation = likes_value + " likes"

  //document.getElementById(likes).innerHTML = likes_evaluation;
  document.getElementById(thumbsdown).style.color = "red";
  document.getElementById(likes).style.display = "inline";
}

function paintthumbsdown(id) {
  var thumbsdown = id + "-thumbsdown";
  document.getElementById(thumbsdown).style.color = "red";
}

function unpaintthumbsdown(id) {
  var thumbsdown = id + "-thumbsdown";
  document.getElementById(thumbsdown).style.color = "black";
}



function hoverfilter(id){
  var strfilter = id;
  document.getElementById(strfilter).style.transform = 'scale(1.5)';
}

function hoverfilterout(id){
  var strfilter = id;
  document.getElementById(strfilter).style.transform = 'scale(1)';
}


function hoverplus(id){
  var strplus = id;
  document.getElementById(strplus).style.transform = 'scale(1.5)';
}

function hoverplusout(id){
  var strplus = id;
  document.getElementById(strplus).style.transform = 'scale(1)';
}

function clickplus(){
  document.getElementById('form_comment').style.display = 'block';
  document.getElementById('form_comment').style.paddingTop = '4rem';
  document.getElementById('comment_hr').style.display = 'block';
  document.getElementById('form_comment_in').style.display = 'block';
  document.getElementById('slide_up').style.display = 'inline';
}

function slideup(){
  document.getElementById('form_comment').style.display = 'none';
  document.getElementById('form_comment').style.paddingTop = '0rem';
  document.getElementById('form_comment_in').style.display = 'none';
  document.getElementById('comment_hr').style.display = 'none';
  document.getElementById('slide_up').style.display = 'none';
}

function slideupover(){
  document.getElementById('slide_up').style.transform = 'scale(2)';
}

function slideupout(){
  document.getElementById('slide_up').style.transform = 'scale(1)';
}

function doThisThumbsup(id){
  var str_thumbsup = id + "-likesprofile";
  document.getElementById(str_thumbsup).style.display = "inline";
}

function searchbuttonover(id){
  document.getElementById(id).style.color = "#18bfef";
}

function searchbuttonout(id){
  document.getElementById(id).style.color = "#ffffff";
}
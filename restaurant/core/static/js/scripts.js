
  const input = document.querySelector("#phone");
  const error_msg = document.getElementById('error_msg');
  const aa=window.intlTelInput(input, {
    initialCountry:'np' ,
    loadUtils: () => import("https://cdn.jsdelivr.net/npm/intl-tel-input@26.0.6/build/js/utils.js"),

});

document.getElementById('contactForm').addEventListener('submit',function(e){

  if (aa.isValidNumber()){
    input.value=aa.getNumber();
    error_msg.style.display='none'
  }
  else{
    e.preventDefault();
    error_msg.style.display='inline'
  }

})
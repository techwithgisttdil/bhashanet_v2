
$('#captcha-img').attr('src', '/media/captcha_images/CAPTCHA.png' + "?t="+new Date().getTime())

   function refresh_button() {
      console.log("refresh button clicked")
      $.ajax({
            type: "GET",
            url: '/captcha_refresh/'
      }).done(function (result){
            let image = result.captcha_url
            $('#captcha-img').attr('src', '/media'+image+"?t="+new Date().getTime())
            //$('#captcha-img').attr('src', '/static'+image)
            $('input[name="captcha_value"]').val('')
            $('#id_captcha_hidden').val(result.captcha_value)
      })
      return false;
   }


   function readaudio(){
    console.log("inside read audio")
    let audio = new Audio('media/captcha_audio/CAPTCHA.wav?t='+new Date().getTime())
    audio.play()
   }

   selectAnyLanguage = () => {
    console.log("language changed")
    if(document.getElementById("gistFK_kbdBox")!=null)
    document.getElementById("keyboardClicked").click()
 }


function addDiv(){
  let divcount = $(".generateddiv").length
  console.log("div count : " + divcount)

  let newDiv = 
      `<div class="col-lg-12 mb-1 generateddiv" id='request${divcount+1}'>
        <div class="input-group mb-3">
          <select class="form-select1" oninput="checklanguage(${divcount+1})" id="selectedLang${divcount+1}" name="selectedLang">
            <option value='' selected>Select Language</option>
            <option value="Hindi">Hindi</option>
            <option value="Marathi">Marathi</option>
            <option value="Malayalam">Malayalam</option>
            <option value="Kannada">Kannada</option>
            <option value="Gujarati">Gujarati</option>
            <option value="Bengali">Bengali</option>
            <option value="Urdu">Urdu</option>
            <option value="Manipuri">Manipuri</option>
            <option value="Telugu">Telugu</option>
            <option value="Punjabi">Punjabi</option>
            <option value="Tamil">Tamil</option>
            <option value="Konkani">Konkani</option>
            <option value="Kashmiri">Kashmiri</option>
            <option value="Assamese">Assamese</option>
            <option value="Sindhi">Sindhi</option>
            <option value="Oriya">Oriya</option>
            <option value="Sanskrit">Sanskrit</option>
            <option value="Maithili">Maithili</option>
            <option value="Santali">Santali</option>
            <option value="Bodo">Bodo</option>
            <option value="Dogri">Dogri</option>
            <option value="Nepali">Nepali</option>
          </select>
          <input type="text" id="myInput${divcount+1}" oninput="checkinput(${divcount+1})" name="inputData" class="form-control" placeholder="Enter URL" aria-label="Text input with dropdown button">
          <a class="btn btn-danger mx-2 " id="deleteDiv${divcount+1}" onclick="deleteDiv(${divcount+1})">Delete</a>
        </div>
      </div>`
  

  // nimber of div need to be created
  let numberOfDiv = 22
  if(divcount+1 <= numberOfDiv){
    $("#divinput").append(newDiv)
    // delete previous div delete button
    $(`#deleteDiv${divcount}`).hide()

    $('.submit-button').prop('disabled', true)
    $('#adddiv').prop('disabled', true)
    if(divcount+1 == numberOfDiv){
      $("#adddiv").hide()
    }
  }else{
    // let errorDiv = `<div class="my-3 alert alert-danger">Maximum </div>`
    $("#adddiv").hide()
  }
}

function deleteDiv(count){
  console.log("deleteDiv number : ", count)
  $("#adddiv").show()
  $(`#request${count}`).remove()
  $(`#deleteDiv${count-1}`).show()
  

  let divcount = $(".generateddiv").length + 1
  console.log("generated count : ", divcount)
  for (let i = 1; i <= divcount; i++){
    if(count !== i){
      console.log("count : ", i)
      checkinput(i)
      checklanguageondelete(i)
    }
  }

}

function checkinput(value){
  console.log("input check")
  let selectedLang = $(`#selectedLang${value}`).val()
  let inputValue = $(`#myInput${value}`).val()
  console.log("selected language ", selectedLang)
  console.log("input value ", inputValue)

  if(selectedLang !== '' && inputValue.trim() !==''){
    $('.submit-button').prop('disabled', false)
    $('#adddiv').prop('disabled', false)
  }else{
    $('.submit-button').prop('disabled', true)
    $('#adddiv').prop('disabled', true)
  }
}


function checklanguageondelete(value){
  console.log("language check")
  $('#max-error').html('')
  let selectedLang = $(`#selectedLang${value}`).val()
  let inputValue = $(`#myInput${value}`).val()
  console.log("selected language ", selectedLang)
  console.log("input value ", inputValue)


  if(selectedLang !== '' && inputValue.trim() !==''){
    $('.submit-button').prop('disabled', false)
    $('#adddiv').prop('disabled', false)
  }else{
    $('.submit-button').prop('disabled', true)
    $('#adddiv').prop('disabled', true)
  }
}

function checklanguage(value){
  console.log("language check")
  $('#max-error').html('')

  let selectedLang = $(`#selectedLang${value}`).val()
  let inputValue = $(`#myInput${value}`).val()
  console.log("selected language ", selectedLang)
  console.log("input value ", inputValue)

    // check langguaeg already selected or not 
    $('select[name="selectedLang"]').each(function(count) {
      console.log('Checked status:', $(this).val());
      console.log("value : " , value)
      console.log("count : " , count+1)
      if(selectedLang == ''){
        let errorDiv = `<div class="my-3 alert alert-danger">Please select language</div>`
        $('#max-error').append(errorDiv)
        $(`#selectedLang${value}`).val('')
        return false;
      }
      else if(value !== count+1 && selectedLang == $(this).val()){
        let errorDiv = `<div class="my-3 alert alert-danger">Language already selected</div>`
        $('#max-error').append(errorDiv)
        $(`#selectedLang${value}`).val('')
      }
      // if(selectedLang == $(this).val() && value !== count+1){
      //   let errorDiv = `<div class="my-3 alert alert-danger">Language already selected</div>`
      //   $('#max-error').append(errorDiv)
      //   $(`#selectedLang${value}`).val('')
      // }
    });

  if(selectedLang !== '' && inputValue.trim() !==''){
    $('.submit-button').prop('disabled', false)
    $('#adddiv').prop('disabled', false)
  }else{
    $('.submit-button').prop('disabled', true)
    $('#adddiv').prop('disabled', true)
  }
}

function submitForm() {
  $("#errorCode").removeClass('alert-danger')
  $("#errorMessage").text('')
  console.log("Submit button clicked")

  var formData = $('#myForm').serialize();
  console.log("form data ", formData)
  // Send AJAX POST request
  $.ajax({
    type: 'POST',
    url: '/idn_websites_request',
    data: formData,
    // contentType: 'application/json',
    success: function(response) {
        console.log('Success:', response.message);
        // Handle success response here
        // Refresh captcha after submitting the form
        refresh_button()
        $("#errorCode").addClass('alert-success')
        $("#errorMessage").text(response.message)
        
        $('html, body').animate({
          scrollTop: $('#errorCode').offset().top
      }, 100); // You can adjust the animation duration
    },
    error: function(error) {
        console.log('Error:', error);
        // Refresh captcha after submitting the form
        refresh_button()
        if(error.status == 400) {
          $("#errorCode").addClass('alert-danger')
          $("#errorMessage").text(error.responseJSON.message)
        }
        $('html, body').animate({
          scrollTop: $('#errorCode').offset().top
      }, 100); // You can adjust the animation duration
    }
  });
}
    

// on click assistance button
$('input[name="assistance"]').click(function(){
  console.log("Clicked on assistance radio buttons")
  let resp = $('input[name="assistance"]:checked').val()
  console.log("response : " , resp)

  if(resp == 'yes'){
    // display input box
    $('#assist').show()
  }else{
    $('#assist').hide()
    $('input[name="assistLang"]').val('')
    $('textarea[name="remark"]').val('')

  }
})

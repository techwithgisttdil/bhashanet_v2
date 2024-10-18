function addDiv(){
  let divcount = $(".generateddiv").length

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
  

  
  if(divcount < 5){
    $("#divinput").append(newDiv)
    $('.submit-button').prop('disabled', true)
    $('#adddiv').prop('disabled', true)
  }else{
    // let errorDiv = `<div class="my-3 alert alert-danger">Maximum </div>`
    $("#adddiv").hide()
  }
}

function deleteDiv(count){
  console.log("deleteDiv number : ", count)
  $("#adddiv").show()
  $(`#request${count}`).remove()
}

function checkinput(value){
  console.log("input check")
  let selectedLang = $(`#selectedLang${value}`).val()
  let inputValue = $(`#myInput${value}`).val()
  console.log("selected language ", selectedLang)
  console.log("input value ", inputValue)

  if(selectedLang !== '' && inputValue !==''){
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

    if(selectedLang == $(this).val() && value !== count+1){
      let errorDiv = `<div class="my-3 alert alert-danger">Language already selected</div>`
      $('#max-error').append(errorDiv)
      $(`#selectedLang${value}`).val('')
    }
});

  if(selectedLang !== '' && inputValue !==''){
    $('.submit-button').prop('disabled', false)
    $('#adddiv').prop('disabled', false)
  }else{
    $('.submit-button').prop('disabled', true)
    $('#adddiv').prop('disabled', true)
  }
}

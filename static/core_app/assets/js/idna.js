$(function () {
    $("#CheckEmailButton").click(function () {
        console.log("sfnyudgub")
        let email = $("#emailText").val()
        console.log(email)
        $.ajax({
            url: "/idna/checkIdnEmail",
            type: "POST",
            dataType: "json",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify({ email: email }),
            success: function (result) {
                // when call is sucessfull
                console.log("Resul ", result.message)
                $("#result").html(`<div class="card w-100 p-2 shadow "><h3 class="fw-bold text-dark">Result</h3><hr style="width:50%; margin: auto; border:2px solid;"/><h4 class="mt-3 fw-bold ">${result.message}</h4></div>`)
             },
             error: function (err) {
                console.log("dfnhuidf")
             }
          });

    })
})

$(function () {
    $("#CheckDomainButton").click(function () {
        console.log("sfnyudgub")
        let domain = $("#domainText").val()
        console.log(domain)

        $.ajax({
            url: "/idna/domain",
            type: "POST",
            dataType: "json",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify({ domain: domain }),
            success: function (result) {
                // when call is sucessfull
                console.log("Resul ", result.message)
                $("#result").html(`<div class="card w-100 p-2 shadow "><h3 class="fw-bold text-dark">Result</h3><hr style="width:50%; margin: auto; border:2px solid;"/><h4 class="mt-3 fw-bold ">${result.message}</h4></div>`)
             },
             error: function (err) {
                console.log("dfnhuidf")
             }
          });
        
    })
})

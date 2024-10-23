/* 
Version: 2.1
Organisation : CDAC| GIST| PUNE
Author Name: Tanvi Nitin Patil,Shivam Sharma, Shubhangni Asati
Date: 25-03-2023
Description: Below script rendering data elastic search
*/

$("document").ready(function () {
  console.log("clicked");
  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);
  const search = urlParams.get("search");
  const pageNo = Number(urlParams.get("pageNo"));

  console.log("search term ", search);

  if (search) {
    console.log("Searched ", search);
    console.log("Searched ", pageNo);
    
    // check search term validation
    let pattern = /^[^\^<>%*!\\\/+=\[\]{};.:"'~|`]*$/
    if(pattern.test(search)){
      callService(search, pageNo);
    }else{
      document.getElementsByClassName("searchresult")[0].innerHTML = "<div class='text-danger fw-semibold '>'Special characters other than  @ $ , - _ ( ) # ?  not allowed.'</div>";
      document.getElementById("searchTerm").value = search;
    }
    
  }else if(search == "") {
    document.getElementsByClassName("searchresult")[0].innerHTML = "<div class='text-danger fw-semibold '>Please Enter Search Term</div>";
  }

  function callService(inputstring, pageNo) {
    console.log("calling callService", inputstring)
    // set input value
    document.getElementById("searchTerm").value = inputstring;
    document.getElementsByClassName("searchresult")[0].innerHTML = "Searching...";
    document.getElementById("myPagination").innerHTML = "";
    document.getElementById("Totalsearchresult").innerHTML = "";
  
    var fromResult = 10 * pageNo + 1;
    var toResult = 9 + fromResult;
  
    //   inputstring = document.getElementById("searchTerm").value;
  
    if (inputstring.length == 0) {
      document.getElementById("myPagination").innerHTML = "";
    }
  
    let params = {
      searchTerm: document.getElementById("searchTerm").value,
      resultsPerPage: 10,
      pageNumber: pageNo,
    };
  
    console.log(params)
  
    $(function () {
      $.ajax({
        type: "get",
        url: "/search/search",
        async: true,
        dataType: "json",
        data: params,
        timeout: 2000,
        success: function (response) {
          if (response.status == "error") {
            document.getElementsByClassName(
              "searchresult"
            )[0].innerHTML = `<br/><br/><h2>${response.errorMessage}</h2><br/><br/>`;
            document.getElementById("myPagination").innerHTML = "";
            document.getElementById("Totalsearchresult").innerHTML = "";
          } else {
  
              console.log("Resp ", response)
            var state = {
              totalPages: response.result.total.value,
              querySet: response.result.hits,
              rows: 10,
              page: pageNo,
              window: 5,
            };
  
            function pagination(querySet, page, rows, totalPages) {
              //  var trimStart = (page) * rows
              //  var trimEnd = trimStart + rows
  
              //  var trimmedData = querySet.slice(trimStart, trimEnd)
              var trimmedData = querySet;
  
              var pages = Math.ceil(totalPages / rows);
  
              return {
                querySet: trimmedData,
                pages: pages,
              };
            }
  
            function pageButtons(pages) {
              var wrapper = document.getElementById("myPagination");
  
              wrapper.innerHTML = "";
              var maxLeft = state.page - Math.floor(state.window / 2) + 1;
              var maxRight = state.page + Math.floor(state.window / 2) + 1;
  
              if (maxLeft < 2) {
                maxLeft = 1;
                maxRight = state.window;
              }
  
              if (maxRight > pages) {
                maxLeft = pages - (state.window - 1);
                maxRight = pages;
  
                if (maxLeft < 1) {
                  maxLeft = 1;
                }
              }
  
              for (var page = maxLeft; page <= maxRight; page++) {
                wrapper.innerHTML += `<button id="testButton" value=${page} class="page btn btn-sm ${
                  state.page === page - 1 ? "active" : ""
                }">${page}</button> `;
              }
              if (state.page != 0) {
                wrapper.innerHTML =
                  `<button   value=${state.page} class="page1 btn btn-sm " style="margin-left:3px;">&#171; <b>Prev</b></button>` +
                  wrapper.innerHTML;
              }
  
              if (state.page != 0) {
                wrapper.innerHTML =
                  `<button id="testButton" value=${1} class="page btn btn-sm"> <b>First</b> </button>` +
                  wrapper.innerHTML;
              }
  
              if (state.page != pages - 1) {
                wrapper.innerHTML += `<button  value=${
                  state.page + 1 + 1
                } class="page2 btn btn-sm " style="margin-right:3px;"><b>Next</b> &#187; </button>`;
              }
  
              if (state.page != pages - 1) {
                wrapper.innerHTML += `<button id="testButton" value=${pages} class="page btn btn-sm "><b>Last</b> </button> `;
              }
              if (state.page != pages) {
                wrapper.innerHTML += `<br><br> <p style="color:grey; font-size:15px;"> Showing ${fromResult} to ${toResult} results</p>`;
              }
  
              $(".page").on("click", function () {
                console.log("page", $(this).val())
                window.location.href = window.location.origin + window.location.pathname + "?id=search&search=" + inputstring + "&pageNo=" + Number($(this).val() - 1);
                // callService(Number($(this).val() - 1), "elasticSearch");
              });
              $(".page1").on("click", function () {
                console.log("page1", $(this).val())
                window.location.href = window.location.origin + window.location.pathname + "?id=search&search=" + inputstring + "&pageNo=" + Number($(this).val() - 1);
                // callService(Number($(this).val() - 1), "elasticSearch");
              });
              $(".page2").on("click", function () {
                console.log("page2", $(this).val())
                        window.location.href = window.location.origin + window.location.pathname + "?id=search&search=" + inputstring + "&pageNo=" + Number($(this).val() - 1);
                // callService(Number($(this).val() - 1), "elasticSearch");
              });
            }
            var data2 = pagination(
              state.querySet,
              state.page,
              state.rows,
              state.totalPages
            );
  
            if (pageNo + 1 == data2.pages) {
              toResult = response.result.total.value;
            }
  
            var result = "";
  
            for (const key in data2.querySet) {
              var title = data2.querySet[key]._source.title;
              var url = data2.querySet[key]._source.url;

              if(!data2.querySet[key].highlight){
                console.log("highlight not found")
                desc = title
              }else{
                var desc = data2.querySet[key].highlight.desc;
              }

  
              result +=
                `<div class="search-title">
                  <a href=${url}> ${title}</a>
                </div>
                <a class="search-link" href=${url}>${url}</a>
                <div class="search-desc">${desc}</div>
                `
            }
  
            if (response.result.total.value == 0) {
              console.log("no records found")
              document.getElementsByClassName("searchresult")[0].innerHTML =
                "<br/><br/><h2>No Result Found</h2><br/><br/>";
              document.getElementById("myPagination").innerHTML = "";
              document.getElementById("Totalsearchresult").innerHTML = "";
              document.getElementById(testButton).hide();
              document.getElementById(wrapper).hide();
            } else {
              total = response.result.total.value;
              document.getElementById("Totalsearchresult").innerHTML =
                "<small>Total records found : " + total + "</small>";
              document.getElementsByClassName("searchresult")[0].innerHTML =
                result;
            }
  
            pageButtons(data2.pages);
          }
        },
  
        error: function (error, textStatus) {
          if (textStatus == "timeout") {
            callService(search, pageNo);
            console.log("timeout")
          }
          console.log("errro message ", error)
  
          document.getElementsByClassName("searchresult")[0].innerHTML =
            "<br/><br/><h2>Service is down</h2><br/><br/>";
          document.getElementById("myPagination").innerHTML = "";
          document.getElementById("Totalsearchresult").innerHTML = "";
        },
      });
    });
  }
});


function exit() {
  document.getElementById("searchTerm").value = "";
  document.getElementsByClassName("searchresult")[0].innerHTML = "";
  document.getElementById("myPagination").innerHTML = "";
  document.getElementById("Totalsearchresult").innerHTML = "";
}

// end of elastic search call

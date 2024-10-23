/*
 This transliteration service is hosted to be used by MMPs only.
 Author - Mukul Saini // Version : 1.5.1
 
 
 Moddifications:
 
 Added Reverse Support.
 Moved /aptrans to root.
 added nvsp languages.
 
Author: Sagar Aradwad 
 
 
 
 
 Copyright (c) 2015 GIST at CDAC (http://www.cdac.in/)
 */
//Google Analytics Script :Start

(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
    (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
    m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
    })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');
  
    ga('create', 'UA-26415849-1', 'auto');
    ga('send', 'pageview');
  
  
  //Google Analytics Script : End
  
  var Service_Url = 'https://trans.tdil-dc.gov.in/'  //Main server Service_Url (ONLY CHANGE THIS IF NEEDED)
  var Service_Url_Arr = ["https://gisttransserver.in/", "https://gisttransserver.in/"];
  var jsFolderPath = Service_Url + 'js';
  //var jsFolderPath = './js';
  var cssFolderPath = jsFolderPath + '/css';
  var imageFolderPath = jsFolderPath + '/images';
  var glocale = ""; //Default locale
  var languageName = ""; //To store full name of language
  var maxTypingLength = 15; //Setting max typing length
  
  if ((typeof jQuery === 'undefined') && !window.jQuery) {
      document.write(("<script type='text/javascript' src='" + jsFolderPath + "/jquery.min.js'></script>"));
  } else {
      if ((typeof jQuery === 'undefined') && window.jQuery) {
          jQuery = window.jQuery;
      } else if ((typeof jQuery !== 'undefined') && !window.jQuery) {
          window.jQuery = jQuery;
      }
  }
  //document.write("<script type='text/javascript' src='" + jsFolderPath + "/jquery.caret.min.js'></script>");
  document.write("<script type='text/javascript' src='" + jsFolderPath + "/jquery.caret.js'></script>");
  document.write("<link href='" + cssFolderPath + "/CDAC-Typing-Script-Style.min.css' rel='stylesheet' type='text/css' />");
  document.write("<script type='text/javascript' src='" + jsFolderPath + "/KeyboardScript.min.js'></script>");
  
  var $ = jQuery.noConflict();
  
  var typingLayout = "transliteration", //Setting default typing layout
      suggestionsPerPage = 5, //Setting suggestions per page
      totalTopPos = 27, //Stores Gist_Typing_Popup_MainBX Top position
      totalLeftPos = 2, //Stores Gist_Typing_Popup_MainBX Left position
      totalRightPos = 3,
      element_Id = "", //To store id of input element
      content_Id = "", //To store id of Popup Input Box element
      popbox_Id = "", //To store whole Pop Box Id
      suggestion_Id = "", //To store suggestion box id
      container_Id = "", //To store clonediv id
      pagingdiv_Id = "", //To store page div id
      imageDiv_Id = "",
      currentElementId = "", //To store id of clicked element,
      targetID = "", //To Store Target Ids
      behavior = "", // To set name or address variable
      storePreviousID = "",  //To store previous clicked id
      originalText = "",
      beforeText = "",
      afterText = "",
      storeResult = "", //To store result from the service
      engContainSpace = true, //to check if the selected text contain space or not
      selectionFlag = 0, //0: isSelected, 1: isDoubleClick, -1: No selection
      //isNotDblClick = false,
      multiTypingEnabled = false,
      caretPos = 0, //Contain the current cursor position
      tempLength = 0, //Temp variable for length
      arrSugg = new Array(), //array for storing the suggestions of any word.
      browserName = "", //To store browser name
      suggestions = "", //Stores suggestions
      selectedText = "",
      selectedTextStart = -1,
      selectedTextEnd = -1,
      totalSuggestionsCount = 0, //To contain count of the suggestions
      totalPageCount = 0, //Stores total pages count
      currentSelectedIndex = 0,
      currentPosition = 0,
      suggestionsToShow = 0, //To store how much suggestion showed on each page
      currentPageCounter = 1, //Store current Page count
      firstLimit = 0, //To store First Limit of page
      lastLimit = 0,
      previousFont = "",
      uniqueSymbols = ["#~1#", "#~2#", "#~3#", "#~4#", "#~5#", "#~6#", "#~7#", "#~8#", "#~9#", "#~10#", "#~11#", "#~12#"],
      serverCounter = -1,    //Stores count of the server in use
      enableOnBlurTransliteration = true;
  
  
  var addressIDs = new Array();
  var nameIDs = new Array();
  var sourceAddressIDs = new Array();
  var targetAddressIDs = new Array();
  var sourceNameIDs = new Array();
  var targetNameIDs = new Array();
  var revFlag = false;
  var hashtableHI_IN = new Hashtable();
  var hashtableGJ_IN = new Hashtable();
  var hashtableMR_IN = new Hashtable();
  var hashtablePN_IN = new Hashtable();
  var hashtableML_IN = new Hashtable();
  var hashtableBN_IN = new Hashtable();
  var hashtableTM_IN = new Hashtable();
  var hashtableTL_IN = new Hashtable();
  var hashtableKN_IN = new Hashtable();
  var hashtableOR_IN = new Hashtable();
  var hashtableUR_IN = new Hashtable();
  
  var hashTableName = hashtableHI_IN;
  var hashTableForDblClick = new Hashtable();
  var hashTableAddress = new Hashtable();
  //var languageSupportForTyping = new Array("hin", "hi_in", "hindi", "mar", "mr_in", "marathi", "guj", "gj_in", "gujarati", "ben", "bn_in", "bengali", "pan", "pn_in", "punjabi", "mal", "ml_in", "malayalam", "tam", "tamil", "kan", "kannada", "tel", "telugu", "asm", "assamese", "urd", "urdu");
  var supportedLangCode1 = new Array("hin", "mar", "guj", "ben", "pan", "mal", "tam", "tel", "kan", "ory", "urd","asm");
  var supportedLangCode2 = new Array("hi_in", "mr_in", "gj_in", "bn_in", "pn_in", "ml_in", "tm_in", "tl_in", "kn_in", "or_in", "ur_in","as_in");
  var supportedLangCode3 = new Array("hindi", "marathi", "gujarati", "bengali", "punjabi", "malayalam", "tamil", "telugu", "kannada", "oriya", "urdu", "assamese");
  
  /*PUBLIC FUNCTION TO GIVE TO CLIENT FOR IMPLEMENTATION INTO THERE PAGE*/
  //To add suggestion functionality on the textbox
  function enableTyping(idArraySource, idArrayTarget, type, locale, revFlag, autoTransliteration) {
      try {
          revTrans = revFlag;
          if (typeof (autoTransliteration) != "undefined")
              enableOnBlurTransliteration = autoTransliteration;
  
          if (glocale != locale) {
              if (locale.toLowerCase() == "eng" || locale.toLowerCase() == "en_in") {
                  return;
              }
              else {
                  setLanguage(locale);
                  setHashTableName();
              }
          }
  
          if (idArrayTarget === null || typeof (idArrayTarget) == undefined)//for typing on same textbox
              typingOnSameTextbox(idArraySource, type, glocale);
          else if (idArraySource != null || idArraySource.length > 0 || typeof (idArraySource) != undefined && idArrayTarget != null || idArrayTarget.length > 0 || typeof (idArrayTarget) != undefined)//for typing on source target textbox
              typingOnMultiTextbox(idArraySource, idArrayTarget, type, glocale);
  
          browserName = getBrowserName();
      } catch (e) { }
  }
  
  //To change typing layout 1: Inscript 2: transliteration
  function setTypingLayout(layout) { //Setting Typing Layout
      try {
          if ($.trim(layout).length > 0) {
              typingLayout = $.trim(layout);
              if (typingLayout.toLowerCase() == "inscript")
                  g_EnableTypingOnlyOnKBDOpen = 0;
              else
                  g_EnableTypingOnlyOnKBDOpen = 1;
          }
          browserName = getBrowserName();
      } catch (e) { }
  }
  
  //To change language
  function setLanguage(changed_locale) {
      try {
          changed_locale = changed_locale.toLowerCase();
          var languageIndex = checkLanguageSupport(changed_locale);
  
          if (languageIndex != -1)
              changed_locale = supportedLangCode2[languageIndex];
          else if (changed_locale == "en_in")
              changed_locale = "eng";
  
          //switch (changed_locale.toLowerCase()) {
          //    case "en_in":
          //        changed_locale = "eng";
          //        break;
          //    case "hin":
          //    case "hindi":
          //        changed_locale = "hi_in";
          //        break;
          //    case "guj":
          //    case "gujarati":
          //        changed_locale = "gj_in";
          //        break;
          //    case "mar":
          //    case "marathi":
          //        changed_locale = "mr_in";
          //        break;
          //    case "pan":
          //    case "panjabi":
          //    case "punjabi":
          //        changed_locale = "pn_in";
          //        break;
          //    case "mal":
          //    case "malayalam":
          //        changed_locale = "ml_in";
          //        break;
          //    case "ben":
          //    case "bengali":
          //        changed_locale = "bn_in";
          //        break;
          //    //default:
          //    //    setTypingLayout("inscript");
          //    //    break;
          //}
  
          if (changed_locale != glocale) {
              glocale = changed_locale;
              hashTableName.clear();
              hashTableAddress.clear();
          }
  
          if (languageIndex != -1)
              languageName = supportedLangCode3[languageIndex];
          else if (changed_locale == "eng")
              languageName = "english";
          else
              languageName = glocale;
  
          //switch (glocale) {
          //    case "eng":
          //        languageName = "english";
          //        break;
          //    case "hi_in":
          //        languageName = "hindi";
          //        break;
          //    case "gj_in":
          //        languageName = "gujarati";
          //        break;
          //    case "mr_in":
          //        languageName = "marathi";
          //        break;
          //    case "pn_in":
          //        languageName = "punjabi";
          //        break;
          //    case "ml_in":
          //        languageName = "malayalam";
          //        break;
          //    case "bn_in":
          //        languageName = "bengali";
          //        break;
          //    case "tam":
          //        languageName = "tamil";
          //        break;
          //    case "kan":
          //        languageName = "kannada";
          //        break;
          //    case "tel":
          //        languageName = "telugu";
          //        break;
          //    case "asm":
          //        languageName = "assamese";
          //        break;
          //    case "urd":
          //        languageName = "urdu";
          //        break;
          //    default:
          //        languageName = glocale;
          //        break;
          //}
  
          if (glocale == 'pn_in')
              totalTopPos = 43;
          else if (glocale == 'ml_in')
              totalTopPos = 35;
          else
              totalTopPos = 27;
  
          if (languageName == "english")
              closeKeyboard();
          else
              changeKeyboardLanguage(languageName);
  
      } catch (e) {
          //console.log( e.message + "\nError In : setLanguage" );
      }
  }
  
  //To call transliteration on button click
  function provideTransliteration(elementID, isReverseTrans) {
      try {
          if (!enableOnBlurTransliteration && glocale != "eng" && checkLanguageSupport(glocale) > -1) {
              $("#" + elementID).focus();
  
              var isReverseTransEnabled = false;
              if (typeof (isReverseTrans) != "undefined" && isReverseTransEnabled != isReverseTrans)
                  isReverseTransEnabled = isReverseTrans;
  
              if (typingLayout == 'transliteration' && ((jQuery.inArray(elementID, sourceNameIDs) > -1 || jQuery.inArray(elementID, sourceAddressIDs) > -1 || isReverseTransEnabled)) && multiTypingEnabled) {
                  currentElementId = elementID;
                  var inputBoxID = '#' + currentElementId;
  
                  if (behavior === 'name') {
                      if (sourceNameIDs.length != targetNameIDs.length) {
                          alert("Error in defining the Source ID or its Target ID for Name Translations");
                          return;
                      }
                      else {
                          var checkForIdInArray = jQuery.inArray(currentElementId, sourceNameIDs);
                          if (checkForIdInArray > -1)
                              targetID = targetNameIDs[checkForIdInArray];
                          else if (isReverseTransEnabled) {
                              checkForIdInArray = jQuery.inArray(currentElementId, targetNameIDs);
                              if (checkForIdInArray > -1)
                                  targetID = sourceNameIDs[checkForIdInArray];
                          }
                          else
                              return;
                      }
                  }
                  else
                      if (behavior === 'address') {
                          if (sourceAddressIDs.length != targetAddressIDs.length) {
                              alert("Error in defining the Source ID or its Target ID for Address Translations");
                              return;
                          }
  
                          var checkForIdInArray = jQuery.inArray(currentElementId, sourceAddressIDs);
                          if (checkForIdInArray > -1)
                              targetID = targetAddressIDs[checkForIdInArray];
                          else if (isReverseTransEnabled) {
                              checkForIdInArray = jQuery.inArray(currentElementId, targetAddressIDs);
                              if (checkForIdInArray > -1)
                                  targetID = sourceAddressIDs[checkForIdInArray];
                          }
                          else
                              return;
                      }
                  var english_text = $.trim($(inputBoxID).val());
  
                  $('#' + targetID).text = ""; // trying to clear text in textarea
                  $('#' + targetID).val(""); // trying to clear text in textbox
  
                  if (english_text.length > 0) {
                      resetValues();
                      iSuggest(inputBoxID, '#' + targetID, english_text, isReverseTransEnabled);
                  }
                  else
                      return;
              }
              else
                  return;
  
          }
          else {
              resetValues();
              removePreviousContainers();
              return;
          }
      }
      catch (e) {
          ////console.log(e.message + "\nError In : focus");
      }
  }
  /*PUBLIC FUNCTION TO GIVE TO CLIENT FOR IMPLEMENTATION INTO THERE PAGE*/
  
  $(document).ready(function () {
      var keyText = ""; //To store key values;
      //Handling focus event on text-area or text-field starts
      $("input[type='text'], textarea").focus(function (event) {
          try {
              if (glocale != "eng" && checkLanguageSupport(glocale) > -1) {
                  currentElementId = this.id;
  
                  if (jQuery.inArray(currentElementId, nameIDs) > -1 || jQuery.inArray(currentElementId, addressIDs) > -1)
                      multiTypingEnabled = false;
                  else if (jQuery.inArray(currentElementId, sourceNameIDs) > -1 || jQuery.inArray(currentElementId, sourceAddressIDs) > -1 || jQuery.inArray(currentElementId, targetNameIDs) > -1 || jQuery.inArray(currentElementId, targetAddressIDs) > -1)
                      multiTypingEnabled = true;
  
                  //if (jQuery.inArray(currentElementId, nameIDs) > -1 || jQuery.inArray(currentElementId, addressIDs) > -1)
                  //    multiTypingEnabled = false;
                  //else
                  //    multiTypingEnabled = true;
  
                  behavior = (checkIDS(currentElementId)).toLowerCase();
  
                  if (storePreviousID != currentElementId) {
                      removePreviousContainers();
  
                      if (jQuery.inArray(currentElementId, sourceNameIDs) == -1 && jQuery.inArray(currentElementId, sourceAddressIDs) == -1 && behavior != "") {
                          //if (navigator.appVersion.indexOf("MSIE 7.") != -1 && navigator.appVersion.indexOf("MSIE 8.") != -1 && navigator.appVersion.indexOf("MSIE 9.") != -1 && navigator.appName == "Netscape")
                          if (navigator.appVersion.indexOf("MSIE 8.") != -1 || (navigator.appName == "Microsoft Internet Explorer" && navigator.appVersion.indexOf("Trident/7.0") == -1 && navigator.appVersion.indexOf("MSIE 10") == -1 && navigator.appVersion.indexOf("MSIE 9") == -1 && navigator.appVersion.indexOf("Chrome") == -1))
                              $('body').wrap("<span id='democontainer_" + currentElementId + "' class='element'></span>");
                          else
                              $("body").prepend("<elem id='democontainer_" + currentElementId + "' class='element'></elem>");
  
  
                          executeAfterClickOnTextBox(currentElementId);
                          storePreviousID = currentElementId;
                          setFont(element_Id);
                          $(event.target).focus();
                      }
                      else {
                          storePreviousID = currentElementId;
                          $(event.target).focus();
                      }
                  }
                  else {
                      setFont(element_Id);
                      return;
                  }
              }
              else {
                  resetValues();
                  removePreviousContainers();
                  return;
              }
          }
          catch (e) {
              ////console.log( e.message + "\nError In : focus" );
          }
      });
      //Handling focus event on text-area or text-field starts
  
      //Handling on blur event to provide tab like functionality STARTS//
      $("input[type='text'], textarea").blur(function (e) {
          try {
              if (glocale != "eng" && checkLanguageSupport(glocale) > -1) {
  
                  if (typingLayout == 'transliteration' && (jQuery.inArray(this.id, nameIDs) > -1 || jQuery.inArray(this.id, addressIDs) > -1 || jQuery.inArray(this.id, sourceNameIDs) > -1 || jQuery.inArray(this.id, sourceAddressIDs) > -1))
                      //if (typingLayout == 'transliteration')
                  {
                      if (!multiTypingEnabled && behavior === 'address') {
                          if (jQuery.inArray(currentElementId, addressIDs) > -1) {
                              var inputBoxID = '#' + currentElementId;
                              var textToTranslate = $.trim($('#' + currentElementId).val());
                              iSuggest(inputBoxID, null, textToTranslate, revTrans);
                          }
                      }
                      else if (enableOnBlurTransliteration && multiTypingEnabled) {
                          currentElementId = this.id;
                          var inputBoxID = '#' + currentElementId;
                          //removePreviousContainers();
  
                          if (behavior === 'name') {
                              if (sourceNameIDs.length != targetNameIDs.length) {
                                  alert("Error in defining the Source ID or its Target ID for Name Translations");
                                  return;
                              }
                              else {
                                  var checkForIdInArray = jQuery.inArray(currentElementId, sourceNameIDs);
                                  if (checkForIdInArray > -1)
                                      targetID = targetNameIDs[checkForIdInArray];
                                  else
                                      return;
                              }
                          }
                          else
                              if (behavior === 'address') {
                                  if (sourceAddressIDs.length != targetAddressIDs.length) {
                                      alert("Error in defining the Source ID or its Target ID for Address Translations");
                                      return;
                                  }
  
                                  var checkForIdInArray = jQuery.inArray(currentElementId, sourceAddressIDs);
                                  if (checkForIdInArray > -1)
                                      targetID = targetAddressIDs[checkForIdInArray];
                                  else
                                      return;
                              }
                          var english_text = $.trim($(inputBoxID).val());
  
                          $('#' + targetID).text = ""; // trying to clear text in textarea
                          $('#' + targetID).val(""); // trying to clear text in textbox
  
                          if (english_text.length > 0) {
                              resetValues();
                              iSuggest(inputBoxID, '#' + targetID, english_text, revTrans);
                          }
                          else
                              return;
                          //isNotDblClick = true;
                      }
                      else {
                          return;
                      }
                  }
                  else
                      return;
  
              }
              else {
                  resetValues();
                  removePreviousContainers();
                  return;
              }
          }
          catch (e) {
              ////console.log(e.message + "\nError In : focus");
          }
      });
      //Handling on blur event to provide tab like functionality ENDS//
  
      //Handling selection event on text-area or text-field STARTS
      $("input[type='text'], textarea").select(function (e) {
          try {
              if (glocale != "eng" && checkLanguageSupport(glocale) > -1) {//jQuery.inArray(glocale, languageSupportForTyping) > -1                    
                  currentElementId = e.target.id;
                  behavior = (checkIDS(currentElementId)).toLowerCase();
  
                  if ($(popbox_Id).is(':visible'))
                      resetValues();
  
                  if (multiTypingEnabled) {
                      if (jQuery.inArray(currentElementId, sourceNameIDs) > -1 || jQuery.inArray(currentElementId, sourceAddressIDs) > -1) {
                          resetValues();
                          return;
                      }
                  }
  
                  //Uncomment this one when suggestion on address feature in available
                  //if ( ( jQuery.inArray( currentElementId, nameIDs ) > -1 || jQuery.inArray( currentElementId, targetNameIDs ) > -1 ) && behavior === "name" || ( jQuery.inArray( currentElementId, addressIDs ) > -1 || jQuery.inArray( currentElementId, targetAddressIDs ) > -1 ) && behavior === "address")
                  if ((jQuery.inArray(currentElementId, nameIDs) > -1 || jQuery.inArray(currentElementId, targetNameIDs) > -1) && behavior === "name" && !$(popbox_Id).is(':visible')) {
                      selectionFlag = 1;
                      getSuggestionsForSelectedText($(this).attr("id"));
                  }
                  else {
                      selectionFlag = 0;
                      resetValues();
                      return;
                  }
  
  
                  //if(jQuery.inArray( currentElementId, nameIDs ) > -1 || jQuery.inArray( currentElementId, addressIDs ) > -1 || jQuery.inArray( currentElementId, targetNameIDs ) > -1 || jQuery.inArray( currentElementId, targetAddressIDs ) > -1)
                  //{
                  //    if (!$(popbox_Id).is(':visible'))
                  //        getSuggestionsForSelectedText($( this ).attr( "id" ));
                  //    selectionFlag = 1;
                  //}
                  //else
                  //{
                  //    resetValues();
                  //    return;
                  //}
  
              }
              else {
                  resetValues();
                  removePreviousContainers();
                  return;
              }
  
          } catch (e) {
              ////console.log( e.message + "\nError In : select" );
          }
      });
      //Handling selection event on text-area or text-field ENDS
  
      //Handling click event on document STARTS //
      $(document).on("mousedown", "*", function (e) {
          try {
              if (glocale != "eng" && checkLanguageSupport(glocale) > -1) {
  
                  if ($(popbox_Id).is(':visible') && $(e.target).hasClass("Gist_Typing_Popup_PagingBtn") == false && $(e.target).hasClass("optional-suggestion") == false) {
                      putWord("");//to reset the selected text variables that got set.
                      resetValues();
                  }
  
                  if (g_EnableTypingOnlyOnKBDOpen == 1 && isKBDOpen && multiTypingEnabled) {
                      if (jQuery.inArray(e.target.id, sourceNameIDs) > -1 || jQuery.inArray(e.target.id, sourceAddressIDs) > -1)
                          closeKeyboard();
                  }
  
              }
              else {
                  resetValues();
                  removePreviousContainers();
                  return;
              }
          } catch (e) {
              ////console.log( e.message + "\nError In : click" );
          }
      });
      //Handling click event on document ENDS
  
      //Handling Click Event for PopupInput box STARTS//
      $(document).on('click', '.Gist_Typing_Popup_PopupTypingBox', function () {
          try {
              if (glocale != "eng" && checkLanguageSupport(glocale) > -1) {
  
                  resetValues();
                  $(element_Id).focus();
                  setCursorToPosition(caretPos);
  
              }
              else {
                  resetValues();
                  removePreviousContainers();
                  return;
              }
          } catch (e) {
              ////console.log( e.message + "\nError In : Click on popupTypingBox" );
          }
      });
      //Handling Click Event for PopupInput box ENDS//
  
      //Handling Click Event on Suggestions STARTS//
      $(document).on("click", ".optional-suggestion", function (e) {
          if (glocale != "eng" && checkLanguageSupport(glocale) > -1) {
              funClick($(this).text());
          }
          else {
              resetValues();
              removePreviousContainers();
              return;
          }
      });
      //Handling Click Event on Suggestions ENDS//
  
      //Handling double click event on text-area or text-field STARTS
      //$( document ).on( "dblclick", "input,textarea", function ( e )
      //{
      //    try
      //    {
      //        currentElementId = $( this ).attr( "id" );
      //        behavior = ( checkIDS( currentElementId ) ).toLowerCase();
  
      //        if ( $( popbox_Id ).is( ':visible' ) )
      //            resetValues();
  
      //        if ( multiTypingEnabled )
      //        {
      //            /*if ( jQuery.inArray( currentElementId, sourceNameIDs ) == -1 )
      //                if ( jQuery.inArray( currentElementId, sourceAddressIDs ) > -1 )
      //                    return;*/
  
      //            if ( jQuery.inArray( currentElementId, sourceNameIDs ) > -1 || jQuery.inArray( currentElementId, sourceAddressIDs ) > -1 )
      //            {
      //                resetValues();
      //                return;
      //            }
      //        }
      //        selectionFlag = 1;
  
      //        //Uncomment this one when suggestion on address feature in available
      //        //if ( ( jQuery.inArray( currentElementId, nameIDs ) > -1 || jQuery.inArray( currentElementId, targetNameIDs ) > -1 ) && behavior === "name" || ( jQuery.inArray( currentElementId, addressIDs ) > -1 || jQuery.inArray( currentElementId, targetAddressIDs ) > -1 ) && behavior === "address")
      //        if ( ( jQuery.inArray( currentElementId, nameIDs ) > -1 || jQuery.inArray( currentElementId, targetNameIDs ) > -1 ) && behavior === "name")
      //            getSuggestionsForSelectedText( $( this ).attr( "id" ) );
  
      //        //isNotDblClick = false;
      //    } catch ( e )
      //    {
      //        ////console.log( e.message + "\nError In : dblclick" );
      //    }
      //} );
      //Handling double click event on text-area or text-field ENDS
  
      //Handling KeyDown Event for InputTextBox STARTS//
      $(document).on('keydown', element_Id, function (e) {
          try {
              if (glocale != "eng" && checkLanguageSupport(glocale) > -1) {
  
                  if (!e.ctrlKey) {
                      if (typingLayout == "transliteration" && !isKBDOpen) {
                          if (!multiTypingEnabled && behavior === 'name') {
                              suggestions = "";
                              //For Alphabets typing on main text box
                              if (e.keyCode > 64 && e.keyCode < 91) {//If the key pressed is an alphabet eg: from A to Z and not combo key
                                  e.preventDefault();
                                  keyText = String.fromCharCode(e.keyCode); //Getting key value in upper case by default
                                  if (e.shiftKey) //Checking for shift key and caps lock to manage upper and lower cases starts
                                      keyText = keyText.toUpperCase();
                                  else
                                      if (!e.shiftKey)
                                          keyText = keyText.toLowerCase(); //Checking for shift key and caps lock to manage upper and lower cases ends
  
                                  if ($(content_Id).text().length < maxTypingLength)
                                      $(content_Id).html($(content_Id).html() + keyText);
                                  else
                                      return;
  
                                  if (typeof $(content_Id).html() == "undefined")
                                      tempLength = $(content_Id).text().length;
                                  else
                                      tempLength = $(content_Id).html().length;
                              }
                          }
  
                          /*if(e.keyCode == 9)//On Tab
                          {
                              if(!multiTypingEnabled && behavior === 'address')
                              {
                                  //e.preventDefault();
                                  if (jQuery.inArray(currentElementId, addressIDs) > -1)
                                  {
                                      var inputBoxID = '#' + currentElementId;
                                      var textToTranslate = $.trim($('#' + currentElementId).val());
                                      iSuggest( inputBoxID, null, textToTranslate, false );
                                  }
                              }
      
                              if(multiTypingEnabled)
                              {
                                  if(behavior === 'name')
                                  {
                                      if ( sourceNameIDs.length != targetNameIDs.length )
                                      {
                                          alert( "Error in defining the Source ID or its Target ID for Name Translations" );
                                          return;
                                      }
                                      else
                                      {
                                          var checkForIdInArray = jQuery.inArray( currentElementId, sourceNameIDs );
                                          if ( checkForIdInArray > -1 )
                                              targetID = targetNameIDs[checkForIdInArray];
                                          else
                                              return;
                                      }
                                  }
      
                                  if(behavior === 'address')
                                  {
                                      if ( sourceAddressIDs.length != targetAddressIDs.length )
                                      {
                                          alert( "Error in defining the Source ID or its Target ID for Address Translations" );
                                          return;
                                      }
      
                                      var checkForIdInArray = jQuery.inArray( currentElementId, sourceAddressIDs );
                                      if ( checkForIdInArray > -1 )
                                          targetID = targetAddressIDs[checkForIdInArray];
                                      else
                                          return;
                                  }
      
                                  iSuggest( '#' + currentElementId, '#' + targetID, $.trim($('#' + currentElementId).val()), false );
                                  isNotDblClick = true;
                              }
                          }*/
                      }
                      if (typingLayout == "inscript") {
                          resetValues();
                      }
                  }
                  else if (e.ctrlKey) {
                      if (e.keyCode == 89) {
                          if (document.getElementById("keyBrd") == null)
                              $("body").append('<div id="keyBrd"> </div>');
  
                          openKeyboard(languageName);
                          hashtable_clear();
                          $(element_Id).focus();
                      }
                      resetValues();
                      return;
                  }
  
                  //To handel how things happen after Gist_Typing_Popup_MainBX is visible
                  if ($(popbox_Id).is(':visible')) {
                      if ($(content_Id).text() == "" && e.keyCode == 8) {//For Backspace + no value in Gist_Typing_Popup_MainBX
                          e.preventDefault();
                          resetValues();
                      }
                      else if ((e.keyCode == 32 || e.keyCode == 13) && $(suggestion_Id).html() != "") { //space key //Enter Key //****key which sets the suggestions to the textbox
                          e.preventDefault();
                          setSuggestionToTextbox();
                      }
                      else if (e.keyCode == 8) {//For backspace key only if Gist_Typing_Popup_MainBX is visible
                          if (!multiTypingEnabled) {
                              e.preventDefault();
                              var tempText = $(content_Id).html();
                              var len = tempText.length;
                              tempText = tempText.substr(0, len - 1);
                              $(content_Id).html(tempText);
                          }
                          else {
                              resetValues();
                          }
                      }
                      else if (e.keyCode == 27) {//Esc Key
                          //var str = $( element_Id ).text().replace( text, "" );
                          //$( element_Id ).text( str );
                          resetValues();
                      }
                      else if (e.keyCode == 37) { //Left Arrow Key
                          e.preventDefault();
                          prevPage();
                          return;
                      }
                      else if (e.keyCode == 39) { //Right Arrow Key
                          e.preventDefault();
                          nextPage();
                          return;
                      }
                      else if (e.keyCode == 38) { //Up Arrow Key
                          e.preventDefault();
                          unSelectSuggestion(currentSelectedIndex); //removing selection previous element
  
                          if (currentSelectedIndex > firstLimit) // if current element is not at first position then move up
                              currentSelectedIndex--;
                          selectSuggestion(currentSelectedIndex);
                      }
                      else if (e.keyCode == 40) { //Down Arrow Key
                          e.preventDefault();
                          unSelectSuggestion(currentSelectedIndex); //removing selection previous element
  
                          if (currentSelectedIndex < lastLimit)// if current element is not at first position then move down
                              currentSelectedIndex++;
                          selectSuggestion(currentSelectedIndex);
                      }
                      else if (e.keyCode == 46) {//Del key
                          resetValues();
                      }
                      else if (((e.keyCode > 47 && e.keyCode < 58) || (e.keyCode > 185 && e.keyCode < 193) || (e.keyCode > 218 && e.keyCode < 223) || (e.keyCode >= 109 && e.keyCode <= 111) && (e.keyCode == 106 || e.keyCode == 107)) && e.keyCode != 16) { //For Keys Except all the above and shift key
                          setSuggestionToTextbox();
                          resetValues();
                      }
                  }
  
              }
              else {
                  resetValues();
                  removePreviousContainers();
                  return;
              }
          }
          catch (e) {
              ////console.log( e.message + "\nError In : keydown" );
          }
      });
      //Handling KeyDown Event for InputTextBox ENDS//
  
      //Handling KeyUp Event for InputTextBox STARTS//
      $(document).on('keyup', element_Id, function (e) {
          try {
              if (glocale != "eng" && checkLanguageSupport(glocale) > -1) {
  
                  if (!e.ctrlKey && !isKBDOpen && typingLayout == "transliteration" && !multiTypingEnabled && behavior == "name") {
                      if (e.keyCode > 64 && e.keyCode < 91) {//For Alphabets typed on main text box A to Z
                          $(suggestion_Id).html(""); //Important Otherwise suggestion will repeat itself
                          setPopupBox();
                          iSuggest(content_Id, null, $.trim($(content_Id).text()), false);
                          if (tempLength < maxTypingLength) { //to check the typing limit
                              //$( popbox_Id ).show();
                              //$( content_Id ).show();
                              tempLength = 0;
                          }
                          else { //if user types more then the limit no change will occur (Currently removed)
                              return;
                          }
                      }
                      else if ($(popbox_Id).is(':visible')) {
                          if (e.keyCode == 8) { //for backspace if Gist_Typing_Popup_MainBX is visible
                              if ($(content_Id).text() == "") {
                                  resetValues();
                                  return;
                              }
                              setPopupBox();
                              $(suggestion_Id).html("");
                              iSuggest(content_Id, null, $.trim($(content_Id).text()), false);
                              //$( popbox_Id ).show();
                          }
  
                          if (((e.keyCode > 47 && e.keyCode < 58) || (e.keyCode > 185 && e.keyCode < 193) || (e.keyCode > 218 && e.keyCode < 223) || (e.keyCode >= 109 && e.keyCode <= 111) && (e.keyCode == 106 || e.keyCode == 107)) && e.keyCode == 16) { //For Keys Except all the above and shift key
                              var symbol = String.fromCharCode(e.keyCode);
                              e.preventDefault();
                              putSingleChar(symbol);
                              return;
                          }
                      }
                  }
                  /*else if(e.ctrlKey)
                  {
                      resetValues();
                      return;
                  }*/
  
              }
              else {
                  resetValues();
                  removePreviousContainers();
                  return;
              }
          }
          catch (e) {
              ////console.log( e.message + "\nError In : keyup" );
          }
  
      });
      //Handling KeyUp Event for InputTextBox ENDS//
  
      //Handling MouseEnter Leave events for suggestion box STARTS//
      $(document).on('mouseenter', '.Gist_Typing_Popup_SuggestnBox', function () {
          unSelectSuggestion(currentSelectedIndex);
      }).on('mouseleave', '.Gist_Typing_Popup_SuggestnBox', function () {
          selectSuggestion(currentSelectedIndex);
      });
      //Handling MouseEnter Leave events for suggestion box ENDS//
  });
  
  if (window.onresize) {
      window.onresize = function () {
          resetValues();
      };
  }
  
  function nextPage() {
      try {
          if (totalSuggestionsCount > suggestionsPerPage && currentPageCounter < totalPageCount) //To check if it is not the first page
          {
              $(suggestion_Id).html(""); //First set the html of suggestion div to null
              currentPosition++; //Increasing current index
              currentPageCounter++; //Increasing page counter
              $("#prev").removeAttr("disabled"); //Enabling previous page button
  
              //Calculating total no of suggestion to show on each page
              var totalSuggestionOnThisPage = suggestionsPerPage;
              suggestionsToShow = 0;
  
              if ((currentPosition + totalSuggestionOnThisPage) > totalSuggestionsCount)
                  totalSuggestionOnThisPage = totalSuggestionsCount - currentPosition; //calculating how much suggestion to show on next page
  
              var counter = 0; //Start from begning to loop among all suggestions
              firstLimit = currentPosition; //Setting first limit of page
              while (counter < totalSuggestionOnThisPage) //Loop till the suggestion limit reached
              {
                  appendSuggestion(arrSugg[currentPosition]); //Calling appendSuggestion method to create a suggestion list
                  currentPosition++;
                  suggestionsToShow++;
                  counter++;
              }
              currentPosition--;
              lastLimit = currentPosition; //Setting last limit of page
              selectSuggestion(firstLimit); //Selecting first suggestion on each page
  
              currentSelectedIndex = firstLimit;
  
              if (currentPosition == (totalSuggestionsCount - 1)) //If last page reached disable the next button
              {
                  $("#next").attr("disabled", "disabled");
              }
              //            $(element_Id).focus();
              //            setCursorToPosition( caretPos );
          }
      } catch (e) {
          ////console.log( e.message + "\nError In : nextPage" );
      }
  }
  
  function prevPage() {//Code for previous button inside Gist_Typing_Popup_MainBX
      try {
          if (totalSuggestionsCount > suggestionsPerPage && currentPageCounter > 1) //To check if it is not the first page
          {
              $(suggestion_Id).html(""); //First set the html of suggestion div to null
              if (currentPageCounter > 1)
                  currentPageCounter--; //decreasing page count
  
              $("#next").removeAttr("disabled"); //enabling next button
  
              //Calculation suggestions to show on current page
              var totalSuggestionOnThisPage = suggestionsPerPage;
              if (currentPageCounter > 1)
                  currentPosition = currentPosition - suggestionsToShow - suggestionsPerPage + 1; //Calculating last limit on each page
              else if (currentPageCounter == 1)
                  currentPosition = 0;
  
              suggestionsToShow = 0;
              firstLimit = currentPosition; //Setting firstLimit of page
              var counter = 0;
              while (counter < totalSuggestionOnThisPage) {
                  appendSuggestion(arrSugg[currentPosition]); //Calling appendSuggestion method to create a suggestion list
                  currentPosition++;
                  suggestionsToShow++;
                  counter++;
              }
              currentPosition--;
              lastLimit = currentPosition; //Setting lastLimit of page
              selectSuggestion(firstLimit); //Selecting first suggestion on each page
              currentSelectedIndex = firstLimit;
  
              if ((currentPosition - suggestionsPerPage) <= 0) //If first page reached disable the prev button
              {
                  $("#prev").attr("disabled", "disabled");
              }
              //            $(element_Id).focus();
              //            setCursorToPosition( caretPos );
          }
      } catch (e) {
          ////console.log( e.message + "\nError In : prevPage" );
      }
  }
  
  /*Called threw enable typing function*/
  function typingOnSameTextbox(idArray, type) {
      try {
          if (type == "ADDRESS") {
              addressIDs = idArray;
          }
          else if (type == "NAME") {
              nameIDs = idArray
          }
          storePreviousID = "";
      } catch (e) {
          //console.log( e.message + "\nError In : EnableTyping" );
      }
  }
  /*Called threw enable typing function*/
  function typingOnMultiTextbox(sourceIdArray, targetIdArray, type) {
      try {
          if (type == "ADDRESS") {
              sourceAddressIDs = sourceIdArray;
              targetAddressIDs = targetIdArray;
          }
          else if (type == "NAME") {
              sourceNameIDs = sourceIdArray;
              targetNameIDs = targetIdArray;
          }
          storePreviousID = "";
      } catch (e) {
          //console.log( e.message + "\nError In : EnableMultiTyping" );
      }
  }
  
  function checkLanguageSupport(langName) {
      var languageIndex = -1;
      try {
          var tempIndex = jQuery.inArray(langName, supportedLangCode1);
          if (tempIndex != -1)
              languageIndex = tempIndex;
          else {
              tempIndex = jQuery.inArray(langName, supportedLangCode2);
              if (tempIndex != -1)
                  languageIndex = tempIndex;
              else {
                  tempIndex = jQuery.inArray(langName, supportedLangCode3);
                  if (tempIndex == -1)
                      languageIndex = tempIndex;
              }
          }
      } catch (e) {
          //console.log( e.message + "\nError In : checkLanguageSupport" );
      }
      return languageIndex;
  }
  
  function formatSuggestion(suggestion) {
      suggestion = suggestion.replace(/-/gi, "-#~1#-").replace(/\{/gi, "{#~2#{").replace(/\}/gi, "}#~3#}").replace(/\(/gi, "(#~4#(")
          .replace(/\)/gi, ")#~5#)").replace(/\[/gi, "[#~6#[").replace(/\]/gi, "]#~7#]").replace(/_/gi, "_#~8#_")
          .replace(/\&/gi, "&#~9#&").replace(/,/gi, ",#~10#,").replace(/\"/gi, "\"#~11#\"").replace(/'/gi, "#~12#");
  
      var finalSuggestion = "";
      try {
          var mainWords = suggestion.split(/[\s\{\}\(\)\[\]\-_\&,'"]/gi);//( " " );
          for (var i = 0; i < mainWords.length; i++) {
              var word = mainWords[i];
  
              if (jQuery.inArray(word, uniqueSymbols) == -1) {
                  word += " ";
              }
  
              var temp = mainWords[i].split(";$;");
              if (temp.length > 1) {
                  word = temp[0] + " ";
                  //var tempArray = $.grep( temp, function ( n, i ) { return i > 0; } );
                  hashTableAddress.put(temp[0], temp);
              }
  
              finalSuggestion += word;
          }
          finalSuggestion = finalSuggestion.replace(/#~1#/gi, "-").replace(/#~2#/gi, "{").replace(/#~3#/gi, "}").replace(/#~4#/gi, "(")
              .replace(/#~5#/gi, ")").replace(/#~6#/gi, "[").replace(/#~7#/gi, "]").replace(/#~8#/gi, "_")
              .replace(/#~9#/gi, "&").replace(/#~10#/gi, ",").replace(/#~11#/gi, "\"").replace(/#~12#/gi, "'");
  
          finalSuggestion = finalSuggestion.replace(/\s-/gi, "-").replace(/\s\{/gi, "{").replace(/\s\}/gi, "}").replace(/\(/gi, "(")
              .replace(/\s\)/gi, ")").replace(/\s\[/gi, "[").replace(/\s\]/gi, "]").replace(/\s_/gi, "_")
              .replace(/\s\&/gi, "&").replace(/\s,/gi, ",").replace(/\s"/gi, "\"").replace(/\s'/gi, "'");
  
          return finalSuggestion;
      }
      catch (ex) {
          ////console.log( ex.message );
      }
      return finalSuggestion;
  }
  
  function removePreviousContainers() // In case of Multityping
  {
      try {
          var cnt = $(".element").contents();
          $(".element").replaceWith(cnt);
          resetValues();
      } catch (e) {
          ////console.log( e.message + "\nError In : removePreviousContainers" );
      }
  }
  
  function executeAfterClickOnTextBox(controlIds) {
      //To Hide the div id="cloneBox" Using it to calculate the position//
      try {//To make all variables generic type so they will work on each and every textbox on the page
  
          $(popbox_Id).remove();
  
          element_Id = "#" + controlIds;
          popbox_Id = "#popupBox_" + controlIds;
          content_Id = "#PopUpInputBox_" + controlIds;
          suggestion_Id = "#Suggestions_" + controlIds;
          container_Id = "#democontainer_" + controlIds;
          pagingdiv_Id = "#page_" + controlIds;
          imageDiv_Id = "#cdacImage_" + controlIds;
          var pageid = "page_" + controlIds;
  
          if (document.getElementById("popupBox_" + controlIds) == null) {
              var popupBx = $("<div class='Gist_Typing_Popup_MainBX' id='popupBox_" + controlIds + "'></div>");
              var popupIOBx = $("<div id='PopUpInputBox_" + controlIds + "' class='Gist_Typing_Popup_PopupTypingBox'></div>");
              var popupSuggBx = $("<div id='Suggestions_" + controlIds + "' class='Gist_Typing_Popup_SuggestnBox'></div>");
              var popupPaggingBx = $("<div id='" + pageid + "' class='Gist_Typing_Popup_PagingDiv'><input type='button' value='<' id='prev' class='Gist_Typing_Popup_PagingBtn' style='float:left;' onclick='prevPage()'/><input type='button' value='>' id='next' class='Gist_Typing_Popup_PagingBtn' style='float:right;' onclick='nextPage()'/></div>");
              var popupImageBx = $("<div id='imageDiv_Id' class='Gist_Typing_Popup_CdacImgDiv'><img src='" + imageFolderPath + "/CDAC-GIST.bmp' alt='CDAC Gist' class='Gist_Typing_Popup_CdacImg'/></div>");
  
              $(popupBx).append(popupIOBx);
              $(popupBx).append(popupSuggBx);
              $(popupBx).append(popupPaggingBx);
              $(popupBx).append(popupImageBx);
  
              $(container_Id).append($(popupBx));
          }
          resetValues();
          $(element_Id).attr("autocomplete", "off");
      }
      catch (e) {
          //console.log( e.message + "\nError In : executeAfterClickOnTextBox" );
      }
  }
  
  function setFont(idOfCurrentElement) {
      previousFont = $(idOfCurrentElement).css('font-family');
      $(idOfCurrentElement).css("font-family", "gist_" + languageName + "_font");
      //$(suggestion_Id).css("font-family","gist_" + languageName + "_font");
  }
  
  function checkIDS(elemID) {
      try {
          var mainFlag = "";
  
          if (!multiTypingEnabled) {
              if (nameIDs.length != undefined) {
                  var checkForIdInArray = jQuery.inArray(elemID, nameIDs);
                  if (checkForIdInArray > -1) {
                      mainFlag = "NAME";
                      return mainFlag;
                  }
              }
  
              if (addressIDs.length != undefined) {
                  var checkForIdInArray = jQuery.inArray(elemID, addressIDs);
                  if (checkForIdInArray > -1) {
                      mainFlag = "ADDRESS";
                      return mainFlag;
                  }
              }
          }
          else {
              //For source
              if (sourceNameIDs.length != undefined) {
                  var checkForIdInArray = jQuery.inArray(elemID, sourceNameIDs);
                  if (checkForIdInArray > -1) {
                      mainFlag = "NAME";
                      return mainFlag;
                  }
              }
              if (sourceAddressIDs.length != undefined) {
                  var checkForIdInArray = jQuery.inArray(elemID, sourceAddressIDs);
                  if (checkForIdInArray > -1) {
                      mainFlag = "ADDRESS";
                      return mainFlag;
                  }
              }
  
              //For Target
              if (targetNameIDs.length != undefined) {
                  var checkForIdInArray = jQuery.inArray(elemID, targetNameIDs);
                  if (checkForIdInArray > -1) {
                      mainFlag = "NAME";
                      return mainFlag;
                  }
              }
              if (targetAddressIDs.length != undefined) {
                  var checkForIdInArray = jQuery.inArray(elemID, targetAddressIDs);
                  if (checkForIdInArray > -1) {
                      mainFlag = "ADDRESS";
                      return mainFlag;
                  }
              }
          }
          return mainFlag;
      } catch (e) {
          //console.log( e.message + "\nError In : checkIDS" );
      }
  }
  
  function setPopupBox() {//Setting POPUP BOX below the new character inserted
      try {
          currentSelectedIndex = 0;
          gettypingCaretPositionForPopup(); //Setting Caret Position variable
  
          var tmpPosition = $(element_Id).caret('offset');
          var finalLeftPos = tmpPosition.left + totalLeftPos;
          var finalTopPos = tmpPosition.top + totalTopPos;
          var finalRightPos = tmpPosition.left + totalRightPos;  
          
          if(glocale === "ur_in") {    
            $(".Gist_Typing_Popup_MainBX").css('right', finalRightPos + 'px');
            $(".Gist_Typing_Popup_MainBX").css('top', finalTopPos + 'px');
            $(".Gist_Typing_Popup_MainBX").css('z-index', "999999999");            
            $(".Gist_Typing_Popup_MainBX").css("left","unset");
        } else {
            $(".Gist_Typing_Popup_MainBX").css('left', finalLeftPos + 'px');
            $(".Gist_Typing_Popup_MainBX").css('top', finalTopPos + 'px');
            $(".Gist_Typing_Popup_MainBX").css('z-index', "999999999");
            $(".Gist_Typing_Popup_MainBX").css("right","unset");
        }
      }
      catch (e) {
          //console.log( e.message + "\nError In : setPopupBox" );
      }
  }
  
  function typingCaretPosition(txtRef) {//To find cursor position in all browser
      try {
          /* CS - 11th Apr,22 */
          var languagueDirection = getLanguageDirection(glocale);      
          txtRef.setAttribute("dir", languagueDirection);  

          var i = txtRef.value.length;
          if (txtRef.createTextRange && !isBrowserAboveIE9()) {
              if (txtRef.tagName == "TEXTAREA") {                  
                  //Complete if condition For handling typing support in TextArea as caret position retrieved is incorrect.
                  //create a range object and save off it's text
                  var objRange;
                  if (document.selection != undefined) {
                      if (document.selection.type == "Text") {
                          var tempRange = document.selection.createRange();
                          var cPos = caretPosExtFun(txtRef);
                          if (cPos != undefined) {
                              cursorPos = caretPos + tempRange.text.length;
                              selectedTextStart = cPos;
                              selectedTextEnd = cursorPos;
                              return cPos;
                          }
                          else {
                              var theCaret = document.selection.createRange().duplicate();
                              while (theCaret.parentElement() == txtRef && theCaret.move("character", 1) == 1)
                                  --i;
                              selectedTextStart = i + 1;
                              selectedTextEnd = i + tempRange.text.length;
                              return i + 1;
                          }
                      }
                      else
                          objRange = document.selection.createRange();
  
                      var sOldRange = objRange.text;
                      if (sOldRange == "") {
                          var sWeirdString = '#%~';
                          objRange.text = sOldRange + sWeirdString;
                          objRange.moveStart('character', (0 - sOldRange.length - sWeirdString.length));
                          var sNewText = txtRef.value;
                          objRange.text = sOldRange;
                          for (i = 0; i <= sNewText.length; i++) {
                              var sTemp = sNewText.substring(i, i + sWeirdString.length);
                              if (sTemp == sWeirdString) {
                                  var cursorPos = (i - sOldRange.length);
                                  return cursorPos;
                              }
                          }
                      }
                  }
              }
              else {                
                  var theCaret = document.selection.createRange().duplicate();
                  while (theCaret.parentElement() == txtRef
                  && theCaret.move("character", 1) == 1)--i;
                  return i == txtRef.value.length + 1 ? -1 : i;
              }
          }
          else if (txtRef.selectionStart || (txtRef.selectionStart == '0')) {
              return txtRef.selectionStart;
          }
      }
      catch (e) {
          //console.log( e.message + "\nError In : typingCaretPosition" );
      }
  }
  
  function gettypingCaretPositionForPopup() {
      try {
          originalText = $(element_Id).val() || $(element_Id).text();
          var totalTextLength = originalText.length; //Calculating total text length
          var tempId = element_Id.substring(1, element_Id.length);
          caretPos = typingCaretPosition(document.getElementById(tempId)); //Calculating caret position
          beforeText = originalText.substring(0, caretPos); //Calculating text before cursor position
          afterText = originalText.substring(caretPos, totalTextLength); //Calculating text after cursor position
      } catch (e) {
          //console.log( e.message + "\nError In : gettypingCaretPositionForPopup" );
      }
  }
  
  function resetSpan() { //Method to reset span element so ass it will not add up in UI of webpage
      try {
          $("#widthcalc").html("");
          $("#widthcalc").remove();
      } catch (e) {
          //console.log( e.message + "\nError In : resetSpan" );
      }
  }
  
  function setSuggestionToTextbox() { //Method to set the selected suggestion to the textbox
      try {
          if ($(suggestion_Id).text() != "") {
              var divID = '#' + arrSugg[currentSelectedIndex];
              var selectedTranslation = $(divID).text();
              putWord(selectedTranslation);
              resetValues();
          }
          resetSpan();
      }
      catch (e) {
          //console.log( e.message + "\nError In : setSuggestionToTextbox" );
      }
  }
  
  function putWord(word) {
      try {
          if (word != "") {
              var finalText = "";
              if (selectedTextStart != selectedTextEnd && selectionFlag != 0) {
                  var val = $(element_Id).val();
                  if (engContainSpace)
                      finalText = val.slice(0, selectedTextStart) + word + " " + val.slice(selectedTextEnd);
                  else
                      finalText = val.slice(0, selectedTextStart) + word + val.slice(selectedTextEnd);
  
                  selectedTextStart = -1;
                  selectedTextEnd = -1;
  
                  caretPos = caretPos + word.length;
              }
              else {
                  if (beforeText.length == 0 && afterText.length == 0) //If there is no text in the textarea
                  {
                      finalText = word + " "; //append an space after the word
                  }
                  else if (afterText.length == 0 && beforeText.length != 0) //if there is no text after the cursor i.e cursor is at last
                  {
                      //checking for the space in the text before the cursor
                      if (beforeText.lastIndexOf(" ") <= (beforeText.length - 1)) //appending space after the word but there is space before the word
                          finalText = beforeText + word + " "; //append an space after the word
                      else
                          finalText = beforeText + " " + word + " "; //appending space after and before the word
                  }
                  else if (afterText.length != 0 && beforeText.length == 0) //if there is text after the cursor and cursor is at the start position in the textarea
                  {
                      //checking for the space in the text after the cursor
                      if (afterText.indexOf(" ") == 0) //if space is at first position
                          finalText = word + afterText; //No need to append extra space
                      else
                          finalText = word + " " + afterText; //append an extra space before appending the word
                  }
                  else if (afterText.length != 0 && beforeText.length != 0) //if there is text before and after the cursor
                  {
                      //check for the space in the before text
                      if (beforeText.lastIndexOf(" ") <= (beforeText.length - 1)) //if space was found at the last of the before text
                          finalText = beforeText + word; //No need to append an extra space
                      else
                          finalText = beforeText + " " + word; //else append an space before the word
  
                      if (afterText.indexOf(" ") == 0) //if space is there before the text
                          finalText += afterText; //no need to append an extra space
                      else //there is no space before the text
                          finalText += " " + afterText; //else append an space after the word
                  }
                  caretPos = caretPos + word.length + 1;
              }
  
              $(element_Id).val(finalText);
  
              if (behavior === "name") {
                  changeSuggestionSequence(word);
              }
              else if (behavior === "address") {
                  var requiredArray = hashTableAddress.get($.trim(selectedText));
                  if (requiredArray != "undefined" && requiredArray != null) {
                      hashTableAddress.remove($.trim(selectedText));
                      hashTableAddress.put($.trim(word), requiredArray);
                  }
              }
              setCursorToPosition(caretPos);
          }
          selectionFlag = 0;
      }
      catch (e) {
          //console.log( e.message + "\nError In : putWord" );
      }
  }
  
  function changeSuggestionSequence(selectedSuggestion) {
      try {
          selectedSuggestion = $.trim(selectedSuggestion);
          var englishWord = $.trim($(content_Id).html());
          if (englishWord != selectedSuggestion) {
              var previousSuggestions = hashTableName.get(englishWord);
              var selectedSuggRemovedString = previousSuggestions.replace(selectedSuggestion + '^', "");
              var reformedSuggestions = selectedSuggestion + "^" + selectedSuggRemovedString;
              var suggCount = reformedSuggestions.split('^').length - 1;
  
              if (previousSuggestions != reformedSuggestions || suggCount == 1) {
                  hashTableName.remove(englishWord);
                  hashTableName.put(englishWord, reformedSuggestions);
                  //updating suggestion frequency via service
                  updateSuggestionsFrequency("NAME", englishWord, selectedSuggestion, glocale);
              }
          }
          hashTableForDblClick.put(selectedSuggestion, englishWord);
      } catch (e) {
          //console.log( e.message + "\nError In : changeSuggestionSequence" );
      }
  }
  
  function putSingleChar(word) {
      try {
          gettypingCaretPositionForPopup();
  
          if (word != "") {
              var finalText = beforeText + word + afterText;
  
              $(element_Id).val(finalText);
              caretPos = caretPos + word.length + 1;
              setCursorToPosition(caretPos);
          }
      }
      catch (e) {
          //console.log( e.message + "\nError In : putSingleChar" );
      }
  }
  
  function setCursorToPosition(pos) {
      try {
          if ($(element_Id).get(0).setSelectionRange) {
              $(element_Id).get(0).setSelectionRange(pos, pos);
          }
          else if ($(element_Id).get(0).createTextRange) {
              var range = $(element_Id).get(0).createTextRange();
              range.collapse(true);
              range.moveEnd('character', pos);
              range.moveStart('character', pos);
              range.select();
          }
      }
      catch (e) {
          //console.log( e.message + "\nError In : setCursorToPosition" );
      }
  }
  
  function selectSuggestion(indx) { //Changing the look and feel of selected suggestion
      try {
          var divID = '#' + arrSugg[indx];
          $(divID).attr('class', 'Gist_Typing_Popup_SelectedText');
      } catch (e) {
          //console.log( e.message + "\nError In : selectSuggestion" );
      }
  }
  
  function unSelectSuggestion(indx) { //Changing the look and feel of unselected suggestion
      try {
          var divID = '#' + arrSugg[indx];
          $(divID).attr('class', 'Gist_Typing_Popup_UnSelectedText')
      } catch (e) {
          //console.log( e.message + "\nError In : unSelectSuggestion" );
      }
  }
  
  function getBrowserName() { //To find out which browser
      //This function detects the browser and returns the browser name.
      try {
          var browserName = "";
          var ua = navigator.userAgent.toLowerCase();
          if (ua.indexOf("opera") != -1)
              browserName = "opera";
          else if (ua.indexOf("msie") != -1)
              browserName = "msie";
          else if (ua.indexOf("safari") != -1)
              browserName = "safari";
          else if (ua.indexOf("mozilla") != -1) {
              if (ua.indexOf("firefox") != -1)
                  browserName = "firefox";
              else
                  browserName = "mozilla";
          }
          return browserName;
      } catch (e) {
          //console.log( e.message + "\nError In : getBrowserName" );
      }
  }
  
  function isBrowserAboveIE9() {
      try {
          var navAppVer = navigator.appVersion;
          var versionInfo = parseInt(navigator.appVersion);
          if (versionInfo <= 4) {
              return false;
          }
          return true;
      } catch (e) {
          //console.log( e.message + "\nError In : isBrowserAboveIE9" );
      }
  }
  
  function getSuggestionsForSelectedText(elementID) {
      try {
          var textComponent = document.getElementById(elementID);
  
          // IE version
          if (document.selection) {
              var bookmark = document.selection.createRange().getBookmark();
              var sel = textComponent.createTextRange();
              var bfr = sel.duplicate();
              sel.moveToBookmark(bookmark);
              bfr.setEndPoint("EndToStart", sel);
              selectedTextStart = bfr.text.length;
              selectedTextEnd = selectedTextStart + sel.text.length;
              selectedText = sel.text;
          }
              // Rest Of Browser
          else if (textComponent.selectionStart != undefined) {
              var startPos = textComponent.selectionStart;
              selectedTextStart = startPos;
              var endPos = textComponent.selectionEnd;
              selectedTextEnd = endPos;
              selectedText = textComponent.value.substring(startPos, endPos);
          }
  
          //Not to process further if selected text is empty
          if ($.trim(selectedText) == null || $.trim(selectedText) == undefined || $.trim(selectedText) == "") {
              resetValues();
              return;
          }
  
          var checkSpace = selectedText.split(' ');
          if (checkSpace.length > 1)
              engContainSpace = true;
          else
              engContainSpace = false;
  
          if (behavior == 'name') {
              var selectedEnglishText = hashTableForDblClick.get($.trim(selectedText)); //getting english text from hindi text
              if (selectedEnglishText != undefined && selectedEnglishText != "") {
                  setPopupBox();
                  resetValues();
  
                  var res = hashTableName.get($.trim(selectedEnglishText))
                  if ($.trim(res).length > 0)
                      showSuggestions(res);
                  else
                      iSuggest('#' + elementID, null, $.trim(selectedEnglishText), false);
  
                  $(content_Id).html(selectedEnglishText);
              }
          }
          else if (behavior == 'address') {
              var cachedSuggestion = hashTableAddress.get($.trim(selectedText)); //getting english text from hindi text
              if (cachedSuggestion != undefined && cachedSuggestion != "" && $.trim(cachedSuggestion).length > 0) {
                  setPopupBox();
                  resetValues();
                  showSuggestions(cachedSuggestion);
              }
              else
                  iSuggest('#' + elementID, null, $.trim(selectedText), true);
          }
      } catch (e) {
          //console.log( e.message + "\nError In : getSuggestionsForSelectedText" );
      }
  }
  
  function iSuggest(sourceID, targetID, transText, isReverseTrans =  false) {
      try {
          isReverseTrans = (typeof isReverseTrans === "number") ? ((["eng", "en_in"].indexOf(glocale) === -1) ? false : true) : isReverseTrans;
          if ($.trim(transText).length > 0) {
              var input_eng_text = $.trim(transText);
              transText = encodeURIComponent(transText);
              var mainService_Url = "";
              var tempResult = "";
              var tFlag = 0;
              //0: For no behavior and Multityping not set
              //1: For Not Multityping and Name
              //2: For Not Multityping and Address
              //3: For Multityping and Name
              //4: For Multityping and Address
              //5: For Reverse Translation
  
              //if (isReverseTrans) {
              //    mainService_Url = Service_Url + 'Transliteration.aspx?itext=' + transText + '&transliteration=NAME&locale=' + 'eng' + '&direction=REVERSE';
  
              //    if (navigator.appVersion.indexOf("MSIE 7.") == -1 && navigator.appVersion.indexOf("MSIE 8.") == -1 && navigator.appVersion.indexOf("MSIE 9.") == -1 && navigator.appVersion.indexOf("MSIE 10.") == -1 && !navigator.userAgent.match(/Trident\/7\./))// && navigator.appName != "Netscape"
              //        //if (navigator.appVersion.indexOf("MSIE 11.") != -1 || (navigator.appName.toLowerCase() != "netscape" && navigator.appName.toLowerCase() != "microsoft internet explorer"))
              //    {
              //        //Calling service
              //        storeResult = "";//Resetting Suggestions
              //        $.ajax({
              //            type: "GET",
              //            url: mainService_Url,
              //            async: true,
              //            success: function (response) {
              //                storeResult = decodeURIComponent(response);
              //            },
              //            complete: function () {
              //                $(targetID).val("");
              //                $(targetID).val($.trim(storeResult));
              //            }
              //        });
              //        storeResult;
              //    }
              //    else // For MSIE V 7 and 8
              //    {
              //        //mainService_Url = mainService_Url.replace("https", "http");
              //        //Implemented AJAX.
              //        var httpRequest;
              //        if (window.XMLHttpRequest)
              //            httpRequest = new XMLHttpRequest();
              //        else// code for IE6, IE5
              //            httpRequest = new ActiveXObject("Microsoft.XMLHTTP");
              //        if (!httpRequest) {
              //            alert('Cannot create an XMLHTTP instance');
              //            return;
              //        }
              //        try {
              //            httpRequest.onreadystatechange = function () {
              //                if (httpRequest.readyState == 4 && httpRequest.status == 200) {
              //                    storeResult = decodeURIComponent(httpRequest.responseText);
              //                    $(targetID).val("");
              //                    $(targetID).val($.trim(storeResult));
              //                }
              //            };
              //            httpRequest.open("GET", mainService_Url, true);
              //            httpRequest.send();
              //        }
              //        catch (err) {
              //            if (XDomainRequest) {// IE8
              //                httpRequest = new XDomainRequest();
              //                httpRequest.onload = function () {
              //                    storeResult = decodeURIComponent(httpRequest.responseText);
              //                    $(targetID).val("");
              //                    $(targetID).val($.trim(storeResult));
              //                };
              //                httpRequest.open("GET", mainService_Url);
              //                httpRequest.send();
              //            }
              //        }
              //    }
              //}
              //else {
                  if (behavior === "name") {
                      mainService_Url = Service_Url + 'Transliteration.aspx?itext=' + transText + '&transliteration=NAME&locale=' + glocale + '&transRev=' + isReverseTrans;
  
                      tempResult = hashTableName.get(input_eng_text);
  
                      if (!multiTypingEnabled && ($.trim(targetID).length == 0 && $.trim(sourceID).length != 0)) {//if single text box
                          if ($.trim(tempResult).length != 0) {
                              showSuggestions(tempResult);
                              return;
                          }
                          else
                              tFlag = 1;
                      }
                      else if (multiTypingEnabled && ($.trim(sourceID).length != 0 && $.trim(targetID).length != 0)) {//if multiple textbox
                          if ($.trim(tempResult).length != 0) {
                              setResultInTarget(targetID, input_eng_text, tempResult);
                              return;
                          }
                          else
                              tFlag = 3;
                      }
                  }
                  else if (behavior === "address") {
                      mainService_Url = Service_Url + 'Transliteration.aspx?itext=' + transText + '&transliteration=ADDRESS&locale=' + glocale + '&transRev=' + isReverseTrans;
  
                      tempResult = hashTableAddress.get(input_eng_text);
                      if (!multiTypingEnabled && ($.trim(targetID).length == 0 && $.trim(sourceID).length != 0)) {
                          if ($.trim(tempResult).length != 0) {
                              $(sourceID).val(tempResult);
                              return;
                          }
                          else
                              tFlag = 2;
                      }
                      else if (multiTypingEnabled && ($.trim(sourceID).length != 0 && $.trim(targetID).length != 0)) {
                          if ($.trim(tempResult).length != 0) {
                              $(targetID).val(tempResult);
                              return;
                          }
                          else
                              tFlag = 4;
                      }
                  }
  
  
                  try {
                      if (navigator.appVersion.indexOf("MSIE 7.") == -1 && navigator.appVersion.indexOf("MSIE 8.") == -1 && navigator.appVersion.indexOf("MSIE 9.") == -1 && navigator.appVersion.indexOf("MSIE 10.") == -1 && !navigator.userAgent.match(/Trident\/7\./))// && navigator.appName != "Netscape"
                          //if (navigator.appVersion.indexOf("MSIE 11.") != -1 || (navigator.appName.toLowerCase() != "netscape" && navigator.appName.toLowerCase() != "microsoft internet explorer"))
                      {
                          //Calling service
                          storeResult = "";//Resetting Suggestions
                          $.ajax({
                              type: "GET",
                              url: mainService_Url,
                              async: true,
                              success: function (response) {
                                  storeResult = formatSuggestion(decodeURIComponent(response));
                              },
                              complete: function () {
                                  processSuggestions(sourceID, targetID, input_eng_text, tFlag);
                              }
                          });
                      }
                      else // For MSIE V 7 and 8
                      {
                          //mainService_Url = mainService_Url.replace("https", "http");
                          //Implemented AJAX.
                          var httpRequest;
                          if (window.XMLHttpRequest)
                              httpRequest = new XMLHttpRequest();
                          else// code for IE6, IE5
                              httpRequest = new ActiveXObject("Microsoft.XMLHTTP");
                          if (!httpRequest) {
                              alert('Cannot create an XMLHTTP instance');
                              return;
                          }
                          try {
                              httpRequest.onreadystatechange = function () {
                                  if (httpRequest.readyState == 4 && httpRequest.status == 200) {
                                      storeResult = formatSuggestion(decodeURIComponent(httpRequest.responseText));
                                      processSuggestions(sourceID, targetID, input_eng_text, tFlag);
                                  }
                              };
                              httpRequest.open("GET", mainService_Url, true);
                              httpRequest.send();
                          }
                          catch (err) {
                              if (XDomainRequest) {// IE8
                                  httpRequest = new XDomainRequest();
                                  httpRequest.onload = function () {
                                      storeResult = decodeURIComponent(formatSuggestion(httpRequest.responseText));
                                      processSuggestions(sourceID, targetID, input_eng_text, tFlag);
                                  };
                                  httpRequest.open("GET", mainService_Url);
                                  httpRequest.send();
                              }
                          }
                      }
                  }
                  catch (err) {
                      //console.log("Error In : iSuggest\n" + "Error Message: " + err.message);
                  }
              }
         // }
          else
              return;
      }
      catch (e) {
          //console.log(e.message + "\nError In : iSuggest");
      }
  }
  
  function processSuggestions(sourceID, targetID, e_text, tFlag)//To process suggestions
  {
      try {
          storeResult = $.trim(storeResult);
          e_text = $.trim(e_text);
  
          if ($.trim(storeResult) === "Empty Value." || $.trim(storeResult) === "") {
              if (serverCounter < Service_Url_Arr.length)
                  serverCounter++;
              else {
                  resetValues();
                  return;
              }
  
              Service_Url = Service_Url_Arr[serverCounter];
              if (Service_Url) {
                  iSuggest(sourceID, targetID, e_text, tFlag);
              } else {
                  serverCounter = -1;
              }
              
              //return;
          }
          else {
              if (tFlag == 1) {//For Not Multityping and Name
                  //storeResult = storeResult + e_text;
                  storeResult = storeResult;
                  hashTableName.put(e_text, storeResult);
                  showSuggestions(storeResult);
                  //feedback method cannot be called here due to suggestion on each keypress
              }
              else if (tFlag == 2) {//For Not Multityping and Address
                  $(sourceID).val(storeResult);
                  updateSuggestionsFrequency("Address", e_text, storeResult, glocale);
              }
              else if (tFlag == 3) {//For Multityping and Name
                  setResultInTarget(targetID, e_text, storeResult);
              }
              else if (tFlag == 4) {//For Multityping and Address
                  $(targetID).val(storeResult);
                  updateSuggestionsFrequency("Address", e_text, storeResult, glocale);
              }
              else if (tFlag == 5) {//For Reverse Translation
                  hashTableAddress.put(e_text, storeResult);
                  showSuggestions(storeResult);
                  // Here target id will get changed as the source id
                  //setResultInTarget(sourceID, e_text, storeResult);
              }
          }
      }
      catch (e) {
          //console.log(e.message + "\nError In : processSuggestions");
      }
  }
  
  function updateSuggestionsFrequency(transType, engWord, transWord, langLocale) {
      try {
          var url = window.location.hostname;
          var Updation_Service_Url = "https://gisttransserver.in/Feedback.aspx?webUrl=" + url + "&trnsType=" + transType + "&inText=" + engWord + "&outText=" + transWord + "&loc=" + langLocale;
  
          $.ajax({
              type: "GET",
              url: Updation_Service_Url,
              async: true,
              success: function (response) {
                  //console.log( response );
              },
              complete: function () {
                  //console.log( "Error" );
              }
          });
      } catch (e) {
          //console.log( e.message + "\nError In : updateSuggestionsFrequency" );
      }
  }
  
  function setResultInTarget(targetid, engText, transResult) {
      try {
          var resultToAppend = "";
          var cacheFlag = false;
          var trText = "";
          var enText = "";
  
          if (transResult.length - 1 == transResult.lastIndexOf(';'))
              cacheFlag = true;
  
          var englishTextArray = engText.split(" ");
  
          transResult = transResult.replace(/;$/, '');
          var transTextArray = transResult.split(';');
  
          if (englishTextArray.length > 1) {
              for (var indexCount = 0; indexCount < englishTextArray.length; indexCount++) {
                  if (hashTableName.containsKey(englishTextArray[indexCount])) {
                      //var new_Trns_Txt = transTextArray[indexCount] + englishTextArray[indexCount];
                      var new_Trns_Txt = transTextArray[indexCount];
                      var old_Trans_Text = hashTableName.get(englishTextArray[indexCount]);
                      if (new_Trns_Txt != old_Trans_Text)
                          transTextArray[indexCount] = old_Trans_Text;
                  }
              }
          }
          if (englishTextArray.length > 1 && transTextArray.length > 1 && (englishTextArray.length == transTextArray.length)) {
              for (var indexCounter = 0; indexCounter < englishTextArray.length; indexCounter++) {
                  enText = $.trim(englishTextArray[indexCounter]);
                  if (cacheFlag)
                      trText = $.trim(transTextArray[indexCounter]);
                  else
                      trText = $.trim(transTextArray[indexCounter]);
                  //trText = $.trim(transTextArray[indexCounter]) + enText;
  
                  var firstSuggestion = trText.substring(0, trText.indexOf("^"));
                  resultToAppend += firstSuggestion + " ";
  
                  if (!hashTableName.containsKey(enText))
                      hashTableName.put(enText, trText);
                  hashTableForDblClick.put(firstSuggestion, enText);
              }
          }
          else {
              if (cacheFlag)
                  trText = transResult;
              else
                  trText = transResult;
              //trText = transResult + engText;
              var firstSuggestion = trText.substring(0, trText.indexOf("^"));
              resultToAppend += firstSuggestion + " ";
  
              if (!hashTableName.containsKey(engText))
                  hashTableName.put(engText, trText);
              hashTableForDblClick.put(firstSuggestion, engText);
          }
  
          if (resultToAppend) {
              
              $(targetid).val("");
              $(targetid).val($.trim(resultToAppend));
          }
          updateSuggestionsFrequency("Name", engText, resultToAppend, glocale);
      } catch (e) {
          //console.log( e.message + "\nError In : setResultInTarget" );
      }
  }
  
  function showSuggestions(suggs) { //Setting UI dynamically for the new suggestions and showing them inside a box ///changed
      //This function is added to tokenize the suggestion list and add to div Gist_Typing_Popup_MainBX ,then display the Gist_Typing_Popup_MainBX
      try {
          totalSuggestionsCount = 0;
          if (suggs) {
              $(suggestion_Id).html("");
  
              if (suggs.split(';').length > 1) {
                  var tempArr = suggs.split(';');
                  arrSugg = tempArr[0].split('^');
                  arrSugg.push(tempArr[1]);
              }
              else
                  arrSugg = suggs.split('^');
  
              arrSugg = $.grep(arrSugg, function (value) { return value != ""; });
              totalSuggestionsCount = arrSugg.length;
              totalPageCount = Math.ceil(totalSuggestionsCount / suggestionsPerPage);
              if (totalPageCount == 1)//if only one page
              {
                  /*$( "#prev" ).css( "background-color", "#E6E6E6" );
                  $( "#next" ).css( "background-color", "#E6E6E6" );*/
                  $("#prev").css("cursor", "default");
                  $("#next").css("cursor", "default");
                  $("#next").attr("disabled", "disabled");
                  $("#prev").attr("disabled", "disabled");
              }
              else {
                  $("#prev").css("cursor", "pointer");
                  $("#next").css("cursor", "pointer");
                  $("#prev").attr("disabled", "disabled");
                  $("#next").removeAttr("disabled");
              }
  
              currentPosition = 0;
              currentPageCounter = 1;
  
              var counter = 0;
              firstLimit = 0;
              while (counter < totalSuggestionsCount) {
                  appendSuggestion(arrSugg[currentPosition]);
                  currentPosition++;
                  counter++;
                  suggestionsToShow++;
                  if (counter == suggestionsPerPage)
                      break;
              }
              currentPosition--;
              lastLimit = currentPosition;
              currentSelectedIndex = firstLimit;
              selectSuggestion(0);
  
              $(suggestion_Id).show();
              $(content_Id).show();
              $(imageDiv_Id).show();
              $(popbox_Id).show();
  
              if (totalPageCount == 1)
                  $(pagingdiv_Id).hide();
              else
                  $(pagingdiv_Id).show();
          }
      } catch (e) {
          //console.log( e.message + "\nError In : showSuggestions" );
      }
  }
  
  function appendSuggestion(suggestion) {
      try {
          var newdiv = $("<div id='" + suggestion + "' class='Gist_Typing_Popup_UnSelectedText'></div>");
          $(newdiv).html("<p style='color:black;margin:0em;' class='optional-suggestion'>" + suggestion + "</p>");
          $(newdiv).css("margin", "2px 0px 2px 0px");
          $(newdiv).css("font-family", "gist_" + languageName + "_font");
          $(suggestion_Id).append(newdiv);
      } catch (e) {
          //console.log( e.message + "\nError In : appendSuggestion" );
      }
  }
  
  function funClick(txt) {
      try {
          $(element_Id).focus();
          putWord(txt);
          resetValues();
      } catch (e) {
          //console.log( e.message + "\nError In : funClick" );
      }
  }
  
  function resetValues() {
      try {
          $(suggestion_Id).html("");
          $(suggestion_Id).hide();
          $(content_Id).text("");
          $(content_Id).hide();
          $(pagingdiv_Id).hide();
          $(imageDiv_Id).hide();
          $(popbox_Id).hide();
          suggestions = null;
          storeResult = null;
          serverCounter = -1;
          //selectedTextStart = 0;
          //selectedTextEnd = 0;
          //selectionFlag = 0;
      } catch (e) {
          //console.log( e.message + "\nError In : resetValues" );
      }
  }
  
  function caretPosExtFun(txtRef) {
      try {
          var i = txtRef.value.length;
          if (txtRef.createTextRange && !isBrowserAboveIE9()) {
              if (txtRef.tagName == "TEXTAREA") {//Complete if condition added by AnupK on 23-11-2012 For handling typing support in TextArea as caret position retrieved is incorrect.
                  //create a range object and save off it's text
                  var objRange = document.selection.createRange();
                  var sOldRange = objRange.text;
                  if (sOldRange == "") {
                      //set this string to a small string that will not normally be encountered
                      var sWeirdString = '#%~';
                      //insert the weirdstring where the cursor is at
                      objRange.text = sOldRange + sWeirdString;
                      objRange.moveStart('character', (0 - sOldRange.length - sWeirdString.length));
                      //save off the new string with the weirdstring in it
                      var sNewText = txtRef.value;
                      //set the actual text value back to how it was
                      objRange.text = sOldRange;
                      //look through the new string we saved off and find the location of
                      //the weirdstring that was inserted and return that value
                      for (i = 0; i <= sNewText.length; i++) {
                          var sTemp = sNewText.substring(i, i + sWeirdString.length);
                          if (sTemp == sWeirdString) {
                              var cursorPos = (i - sOldRange.length);
                              return cursorPos;
                          }
                      }
                  }
              }
              else {
                  var theCaret = document.selection.createRange().duplicate();
                  while (theCaret.parentElement() == txtRef
                      && theCaret.move("character", 1) == 1)--i;
                  return i == txtRef.value.length + 1 ? -1 : i;
              }
          }
          else if (txtRef.selectionStart || (txtRef.selectionStart == '0')) {
              return txtRef.selectionStart;
          }
      }
      catch (e) {
          //console.log( e.message + "\nError In : caretPosExtFun" );
      }
  }
  
  /*Default functionalities of hash table no need to change*/
  function setHashTableName() {
      try {
          if (glocale == "hi_in") {
              hashTableName = hashtableHI_IN;
          } else if (glocale == "gj_in") {
              hashTableName = hashtableGJ_IN;
          } else if (glocale == "mr_in") {
              hashTableName = hashtableMR_IN;
          } else if (glocale == "pn_in") {
              hashTableName = hashtablePN_IN;
          } else if (glocale == "ml_in") {
              hashTableName = hashtableML_IN;
          } else if (glocale == "bn_in") {
              hashTableName = hashtableBN_IN;
          } else if (glocale == "tm_in") {
              hashTableName = hashtableTM_IN;
          } else if (glocale == "tl_in") {
              hashTableName = hashtableTL_IN;
          } else if (glocale == "kn_in") {
              hashTableName = hashtableKN_IN;
          } else if (glocale == "or_in") {
              hashTableName = hashtableOR_IN;
          } else if (glocale == "ur_in") {
              hashTableName = hashtableUR_IN;
          }
      } catch (e) {
          //console.log( e.message + "\nError In : setHashTableName" );
      }
  }
  
  function Hashtable() {
      this.clear = hashtable_clear;
      this.containsKey = hashtable_containsKey;
      this.containsValue = hashtable_containsValue;
      this.get = hashtable_get;
      this.isEmpty = hashtable_isEmpty;
      this.keys = hashtable_keys;
      this.put = hashtable_put;
      this.remove = hashtable_remove;
      this.size = hashtable_size;
      this.toString = hashtable_toString;
      this.values = hashtable_values;
      this.hashtable = new Array();
  }
  
  function hashtable_clear() {
      this.hashtable = new Array();
  }
  
  function hashtable_containsKey(key) {
      var exists = false;
      for (var i in this.hashtable) {
          if (i == key && this.hashtable[i] != null) {
              exists = true;
              break;
          }
      }
      return exists;
  }
  
  function hashtable_containsValue(value) {
      var contains = false;
      if (value != null) {
          for (var i in this.hashtable) {
              if (this.hashtable[i] == value) {
                  contains = true;
                  break;
              }
          }
      }
      return contains;
  }
  
  function hashtable_get(key) {
      return this.hashtable[key];
  }
  
  function hashtable_isEmpty() {
      return (parseInt(this.size()) == 0) ? true : false;
  }
  
  function hashtable_keys() {
      var keys = new Array();
      for (var i in this.hashtable) {
          if (this.hashtable[i] != null)
              keys.push(i);
      }
      return keys;
  }
  
  function hashtable_put(key, value) {
      if (key == null || value == null) {
          this.hashtable[key] = value;
      } else {
          this.hashtable[key] = value;
      }
  }
  
  function hashtable_size() {
      var size = 0;
      for (var i in this.hashtable) {
          if (this.hashtable[i] != null)
              size++;
      }
      return size;
  }
  
  function hashtable_toString() {
      var result = "";
      for (var i in this.hashtable) {
          if (this.hashtable[i] != null)
              result += "{" + i + "},{" + this.hashtable[i] + "}\n";
      }
      return result;
  }  
  
  function hashtable_values() {
      var values = new Array();
      for (var i in this.hashtable) {
          if (this.hashtable[i] != null)
              values.push(this.hashtable[i]);
      }
      return values;
  }
  
  function hashtable_remove(key) {
      var rtn = this.hashtable[key];
      this.hashtable[key] = null;
      return rtn;
  }

  /* CS- 11th Apr,22 */
  function getLanguageDirection(glocale){
    switch (glocale) { 
    case "ur_in":  
    case "ks_in":
    case "sd_in":
      return "rtl";
    default:
      return "ltr";
    } 
  }
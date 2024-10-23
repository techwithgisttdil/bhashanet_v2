

   
         (function ($) {
         "use strict";
         if ($(".get-visions-resourceance__progress-range").length) {
            $(".get-visions-resourceance__progress-range").each(function () {
               let balanceTag = $(this).find(".get-visions-resourceance__balance span");
               let balanceInput = $(this).find(".get-visions-resourceance__balance__input");
               $(this).find(".balance-range-slider").ionRangeSlider({
               onStart: function (data) {
                  balanceTag.html(data.from);
                  balanceInput.prop("value", data.from);
               },
               onChange: function (data) {
                  balanceTag.html(data.from);
                  balanceInput.prop("value", data.from);
               }
               });
            });
         }



            if ($(".tabs-box").length) {
               $(".tabs-box .tab-buttons .tab-btn").on("click", function (e) {
                  e.preventDefault();
                  var target = $($(this).attr("data-tab"));

                  if ($(target).is(":visible")) {
                  return false;
                  } else {
                  target
                     .parents(".tabs-box")
                     .find(".tab-buttons")
                     .find(".tab-btn")
                     .removeClass("active-btn");
                  $(this).addClass("active-btn");
                  target
                     .parents(".tabs-box")
                     .find(".tabs-content")
                     .find(".tab")
                     .fadeOut(0);
                  target
                     .parents(".tabs-box")
                     .find(".tabs-content")
                     .find(".tab")
                     .removeClass("active-tab");
                  $(target).fadeIn(300);
                  $(target).addClass("active-tab");
                  }
               });
            }

            //Single Vertical Carousel
            if ($(".single-vertical-carousel").length) {
               $(".single-vertical-carousel").slick({
                  dots: true,
                  autoplay: false,
                  loop: true,
                  autoplaySpeed: 5000,
                  infinite: true,
                  responsive: true,
                  slidesToShow: 2,
                  vertical: true,
                  slidesToScroll: 1,
                  prevArrow: "<div class='prev-btn'><span class='fa fa-angle-up'></span></div>",
                  nextArrow: "<div class='next-btn'><span class='fa fa-angle-down'></span></div>"
               });
            }

            if ($(".circle-progress").length) {
               $(".circle-progress").appear(function () {
                  let circleProgress = $(".circle-progress");
                  circleProgress.each(function () {
                  let progress = $(this);
                  let progressOptions = progress.data("options");
                  progress.circleProgress(progressOptions);
                  });
               });
            }

            function SmoothMenuScroll() {
               var anchor = $(".scrollToLink");
               if (anchor.length) {
                  anchor.children("a").bind("click", function (event) {
                  if ($(window).scrollTop() > 10) {
                     var headerH = "90";
                  } else {
                     var headerH = "90";
                  }
                  var target = $(this);
                  $("html, body")
                     .stop()
                     .animate({
                        scrollTop: $(target.attr("href")).offset().top - headerH + "px"
                        },
                        1200,
                        "easeInOutExpo"
                     );
                  anchor.removeClass("current");
                  anchor.removeClass("current-menu-ancestor");
                  anchor.removeClass("current_page_item");
                  anchor.removeClass("current-menu-parent");
                  target.parent().addClass("current");
                  event.preventDefault();
                  });
               }
            }
            SmoothMenuScroll();

            function OnePageMenuScroll() {
               var windscroll = $(window).scrollTop();
               if (windscroll >= 117) {
                  var menuAnchor = $(".one-page-scroll-menu .scrollToLink").children("a");
                  menuAnchor.each(function () {
                  var sections = $(this).attr("href");
                  $(sections).each(function () {
                     if ($(this).offset().top <= windscroll + 100) {
                        var Sectionid = $(sections).attr("id");
                        $(".one-page-scroll-menu").find("li").removeClass("current");
                        $(".one-page-scroll-menu")
                        .find("li")
                        .removeClass("current-menu-ancestor");
                        $(".one-page-scroll-menu")
                        .find("li")
                        .removeClass("current_page_item");
                        $(".one-page-scroll-menu")
                        .find("li")
                        .removeClass("current-menu-parent");
                        $(".one-page-scroll-menu")
                        .find("a[href*=\\#" + Sectionid + "]")
                        .parent()
                        .addClass("current");
                     }
                  });
                  });
               } else {
                  $(".one-page-scroll-menu li.current").removeClass("current");
                  $(".one-page-scroll-menu li:first").addClass("current");
               }
            }



            })(jQuery);
  
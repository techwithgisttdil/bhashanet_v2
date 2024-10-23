/*=============================
Portal Name: Bhashanet     
Portal URI: https://Bhashanet.in
Author: Rahul Borade  
Version: 1.0.0 ================== */

(function($) {
    "use strict";
    if ($(window).width() > 767) {
        if ($('.theiaStickySidebar').length > 0) {
            $('.theiaStickySidebar').theiaStickySidebar({
                additionalMarginTop: 70
            });
        }
    }
    if ($('.toggle-password').length > 0) {
        $(document).on('click', '.toggle-password', function() {
            $(this).toggleClass("feather-eye feather-eye-off");
            var input = $(".pass-input");
            if (input.attr("type") == "password") {
                input.attr("type", "text");
            } else {
                input.attr("type", "password");
            }
        });
    }
    if ($(window).width() <= 991) {
        var Sidemenu = function() {
            this.$menuItem = $('.main-nav a');
        };

        function init() {
            var $this = Sidemenu;
            $('.main-nav a').on('click', function(e) {
                if ($(this).parent().hasClass('has-submenu')) {
                    e.preventDefault();
                }
                if (!$(this).hasClass('submenu')) {
                    $('ul', $(this).parents('ul:first')).slideUp(350);
                    $('a', $(this).parents('ul:first')).removeClass('submenu');
                    $(this).next('ul').slideDown(350);
                    $(this).addClass('submenu');
                } else if ($(this).hasClass('submenu')) {
                    $(this).removeClass('submenu');
                    $(this).next('ul').slideUp(350);
                }
            });
        }
        init();
    }
    $('.ua-share .fa-heart').on('click', function(e) {
        e.preventDefault();
        $(this).toggleClass('color-active');
    });
    
   
    $('.header-fixed').append('<div class="sidebar-overlay"></div>');
    $(document).on('click', '#mobile_btn', function() {
        $('main-wrapper').toggleClass('slide-nav');
        $('.sidebar-overlay').toggleClass('opened');
        $('html').addClass('menu-opened');
        return false;
    });
    $(document).on('click', '.sidebar-overlay', function() {
        $('html').removeClass('menu-opened');
        $(this).removeClass('opened');
        $('main-wrapper').removeClass('slide-nav');
    });
    $(document).on('click', '#menu_close', function() {
        $('html').removeClass('menu-opened');
        $('.sidebar-overlay').removeClass('opened');
        $('main-wrapper').removeClass('slide-nav');
    });
    if ($('.select').length > 0) {
        $('.select').select2({
            minimumResultsForSearch: -1,
            width: '100%'
        });
    }
    $(document).ready(function() {
        $('[data-bs-toggle="tooltip"]').tooltip();
    });
    
   
    if ($('.owl-carousel.ua-support-slider').length > 0) {
        var owl = $('.owl-carousel.ua-support-slider');
        owl.owlCarousel({
            margin: 30,
            nav: false,
            nav: true,
            loop: true,
            autoplay: true,
            autoplaySpeed: 2000,
            responsive: {
                0: {
                    items: 1
                },
                768: {
                    items: 4
                },
                1170: {
                    items: 4
                }
            }
        });
    }
    if ($('.owl-carousel.ua1s-ua').length > 0) {
        var owl = $('.owl-carousel.ua1s-ua');
        owl.owlCarousel({
            margin: 24,
            nav: false,
            nav: true,
            loop: true,
            autoplay: true,
            autoplaySpeed: 3000,
            responsive: {
                0: {
                    items: 1
                },
                768: {
                    items: 2
                },
                1170: {
                    items: 4
                }
            }
        });
    }
    if ($('.owl-carousel.event-slide').length > 0) {
        var owl = $('.owl-carousel.event-slide');
        owl.owlCarousel({
            margin: 24,
            nav: false,
            nav: true,
            loop: true,
            responsive: {
                0: {
                    items: 1
                },
                768: {
                    items: 1
                },
                1170: {
                    items: 1
                }
            }
        });
    }
    if ($('.owl-carousel.login-slide').length > 0) {
        var owl = $('.owl-carousel.login-slide');
        owl.owlCarousel({
            margin: 24,
            nav: false,
            nav: true,
            loop: true,
            responsive: {
                0: {
                    items: 1
                },
                768: {
                    items: 1
                },
                1170: {
                    items: 1
                }
            }
        });
    }
   
    $(window).scroll(function() {
        var sticky = $('.scroll-sticky'),
            scroll = $(window).scrollTop();
        if (scroll >= 100) sticky.addClass('add-header-bg');
        else sticky.removeClass('add-header-bg');
    });
    if ($('.countdown-container').length > 0) {
        const daysEl = document.getElementById("days");
        const hoursEl = document.getElementById("hours");
        const minsEl = document.getElementById("mins");
        const newYears = "1 Jan 2023";

        function countdown() {
            const newYearsDate = new Date(newYears);
            const currentDate = new Date();
            const totalSeconds = (newYearsDate - currentDate) / 1000;
            const days = Math.floor(totalSeconds / 3600 / 24);
            const hours = Math.floor(totalSeconds / 3600) % 24;
            const mins = Math.floor(totalSeconds / 60) % 60;
            daysEl.innerHTML = days;
            hoursEl.innerHTML = formatTime(hours);
            minsEl.innerHTML = formatTime(mins);
        }

        function formatTime(time) {
            return time < 10 ? `0${time}` : time;
        }
        countdown();
        setInterval(countdown, 1000);
    }

    function animateElements() {
        $('.circle-bar1').each(function() {
            var elementPos = $(this).offset().top;
            var topOfWindow = $(window).scrollTop();
            var percent = $(this).find('.circle-graph1').attr('data-percent');
            var animate = $(this).data('animate');
            if (elementPos < topOfWindow + $(window).height() - 30 && !animate) {
                $(this).data('animate', true);
                $(this).find('.circle-graph1').circleProgress({
                    value: percent / 100,
                    size: 400,
                    thickness: 40,
                    startAngle: -1.6,
                    fill: {
                        color: '#159f46'
                    }
                });
            }
        });
    }
    if ($('.circle-bar').length > 0) {
        animateElements();
    }
    $(window).scroll(animateElements);
    $('.digit-group').find('input').each(function() {
        $(this).attr('maxlength', 1);
        $(this).on('keyup', function(e) {
            var parent = $($(this).parent());
            if (e.keyCode === 8 || e.keyCode === 37) {
                var prev = parent.find('input#' + $(this).data('previous'));
                if (prev.length) {
                    $(prev).select();
                }
            } else if ((e.keyCode >= 48 && e.keyCode <= 57) || (e.keyCode >= 65 && e.keyCode <= 90) || (e.keyCode >= 96 && e.keyCode <= 105) || e.keyCode === 39) {
                var next = parent.find('input#' + $(this).data('next'));
                if (next.length) {
                    $(next).select();
                } else {
                    if (parent.data('autosubmit')) {
                        parent.submit();
                    }
                }
            }
        });
    });
    $('.digit-group input').on('keyup', function() {
        var self = $(this);
        if (self.val() != '') {
            self.addClass('active');
        } else {
            self.removeClass('active');
        }
    });
    if ($('.main-wrapper .aos').length > 0) {
        AOS.init({
            duration: 1200,
            once: true
        });
    }

    
    $(document).ready(function() {
        let progressVal = 0;
        let businessType = 0;
        $(".next_btn").click(function() {
            $(this).parent().parent().parent().next().fadeIn('slow');
            $(this).parent().parent().parent().css({
                'display': 'none'
            });
            progressVal = progressVal + 1;
            $('.progress-active').removeClass('progress-active').addClass('progress-activated').next().addClass('progress-active');
        });
        $(".prev_btn").click(function() {
            $(this).parent().parent().parent().prev().fadeIn('slow');
            $(this).parent().parent().parent().css({
                'display': 'none'
            });
            progressVal = progressVal - 1;
            $('.progress-active').removeClass('progress-active').prev().removeClass('progress-activated').addClass('progress-active');
        });
    });
    if ($('#editor').length > 0) {
        ClassicEditor.create(document.querySelector('#editor'), {
            toolbar: {
                items: ['heading', '|', 'fontfamily', 'fontsize', '|', 'alignment', '|', 'fontColor', 'fontBackgroundColor', '|', 'bold', 'italic', 'strikethrough', 'underline', 'subscript', 'superscript', '|', 'link', '|', 'outdent', 'indent', '|', 'bulletedList', 'numberedList', 'todoList', '|', 'code', 'codeBlock', '|', 'insertTable', '|', 'uploadImage', 'blockQuote', '|', 'undo', 'redo'],
                shouldNotGroupWhenFull: true
            }
        }).then(editor => {
            window.editor = editor;
        }).catch(err => {
            console.error(err.stack);
        });
    }
})(jQuery);

document.addEventListener('DOMContentLoaded', function () {
    const togglePanel = document.getElementById('toggle-panel');
    const toggleButton = document.createElement('button');
    toggleButton.textContent = 'Toggle';
    document.body.appendChild(toggleButton);
    
    toggleButton.addEventListener('click', function () {
        togglePanel.style.display = togglePanel.style.display === 'block' ? 'none' : 'block';
    });
});

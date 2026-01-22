;(function($) {
    "use strict"; 
    
    //* Navbar Fixed  
    function navbarFixed(){
        if ( $('.main_header_area').length ){ 
            $(window).on('scroll', function() {
                var scroll = $(window).scrollTop();   
                if (scroll >= 295) {
                    $(".main_header_area").addClass("navbar_fixed");
                } else {
                    $(".main_header_area").removeClass("navbar_fixed");
                }
            });
        };
    };  
    
    /* Main Slider js */
    function main_slider(){
        if ( $('#main_slider').length ){
            $("#main_slider").revolution({
                sliderType:"standard",
                sliderLayout:"auto",
                delay:9000,
                disableProgressBar:"off", 
                navigation: {
                    keyboardNavigation: "on",
                    keyboard_direction: "horizontal",
                    mouseScrollNavigation: "off",
                    onHoverStop: "off",
                    touch: {
                        touchenabled: "on",
                        swipe_threshold: 75,
                        swipe_min_touches: 50,
                        swipe_direction: "horizontal",
                        drag_block_vertical: false
                    },
                    bullets: {
                        enable: true,
                        hide_onmobile: true,
                        hide_under: 640,
                        style: "zeus",
                        hide_onleave: false,
                        direction: "horizontal", 
                        v_align: "bottom",
                        h_offset: 0,
                        v_offset: 48,
                        space: 10, 
                        tmp: '<span class="tp-bullet-image"></span><span class="tp-bullet-imageoverlay"></span><span class="tp-bullet-title">{{title}}</span>'
                    }
                },
                responsiveLevels:[4096,1199,992,767,540],
                gridwidth:[1170,1000,750,700,500],
                gridheight:[830,830,650,500,500],
                lazyType:"smart", 
                fallbacks: {
                    simplifyAll:"off",
                    nextSlideOnWindowFocus:"off",
                    disableFocusListener:false,
                }
            })
        }
    };
    
    //* Round Circle js
    $(".quick_help_need").each(function() {
        $(this).waypoint(function() { 
            $('.pie_chart').pieChart({
                barColor: '#ff9e1c',
                trackColor: '#fff',
                lineCap: 'butt',
                size: 110, 
                lineWidth: 10, 
                onStep: function(from, to, percent) {
                    $(this.element).find('.pie-value').text(Math.round(percent) + '%');
                },
                animate: {
                    duration: 1500,
                    enabled: true
                },
            });  
        }, {
          triggerOnce: true,
          offset: 'bottom-in-view'
        });
    }); 
    $(".latest_causes_area, .donations_details").each(function() {
        $(this).waypoint(function() { 
            //* smpie_chart
            $('.smpie_chart').pieChart({
                barColor: '#ff9e1c',
                trackColor: '#dadada',
                lineCap: 'butt',
                size: 71, 
                lineWidth: 9, 
                onStep: function(from, to, percent) {
                    $(this.element).find('.pie-value').text(Math.round(percent) + '%');
                },
                animate: {
                    duration: 1500,
                    enabled: true
                },
            });
            
        }, {
          triggerOnce: true,
          offset: 'bottom-in-view'
        });
    });
    
    //* Counter Js 
    function counterUp(){
        if ( $('.charity_organizations').length ){ 
            $('.counter').counterUp({
                delay: 10,
                time: 400
            });
        };
    }; 
    
    /* childrenCare and client_logo */ 
    function childrenCare(){
        if ( $('.children_care, .client_logo').length ){ 
            $('.children_care').owlCarousel({
                loop: false,
                margin: 30, 
                autoplay: true,
                items: 4,
                responsiveClass: true,
                responsive: {
                    0: {
                        items: 1, 
                    },
                    500: {
                        items: 2, 
                    },
                    800: {
                        items: 3, 
                    },
                    1000: {
                        items: 4, 
                    }
                }
            }); 
            $('.client_logo').owlCarousel({
                loop: false,
                margin: 0, 
                autoplay: true,
                items: 4,
                responsiveClass: true,
                responsive: {
                    0: {
                        items: 1, 
                    },
                    500: {
                        items: 2, 
                    },
                    800: {
                        items: 3, 
                    },
                    1000: {
                        items: 4, 
                    }
                }
            });
        };
    }; 
    
    //* Progressbar Js 
    function progressbar(){
        if ( $('.latest_causes_inner, .causes_area').length ){  
           $('.progress progress').each(function () {
                $(".progress label[for='" + $(this).attr('id') + "']")
                .text(this.value + "%")
                .animate({
                    'margin-left': $(this).width() * $(this).attr("value") / 100 -
                        $(".progress label[for='" + $(this).attr('id') + "']").width() / 2 + "px"
                }, 2000, 'easeOutQuad');
            });
        };
    }; 
    
    //* CounDown Js 
    function counDown(){
        if ( $('.donations_details').length ){  
            $('.timer').dsCountDown({
                endDate: new Date("December 24, 2020 23:59:00")
            });
        };
    };  
    
    //* Isotope js
    function gallery_isotope(){
        if ( $('.grid_gallery_area').length ){ 
            // Activate isotope in container
            $(".grid_gallery_item_inner").imagesLoaded( function() {
                $(".grid_gallery_item_inner").isotope({
                    layoutMode: 'fitRows',  
                }); 
            }); 
            
            // Add isotope click function 
            $(".gallery_filter li").on('click',function(){
                $(".gallery_filter li").removeClass("active");
                $(this).addClass("active"); 
                var selector = $(this).attr("data-filter");
                $(".grid_gallery_item_inner").isotope({
                    filter: selector,
                    animationOptions: {
                        duration: 450,
                        easing: "linear",
                        queue: false,
                    }
                });
                return false;
            }); 
            
            //*  Simple LightBox js 
            $('.imageGallery1 .light').simpleLightbox()
        };
    }; 
    
    //* Select js
    function selectmenu(){
        if ( $('.selectmenu').length ){ 
            $('select').niceSelect();
        };
    };
    
    //* Select js
    function datepicker(){
        if ( $('.datepicker').length ){ 
            $( ".datepicker" ).datepicker();
        };
    };
    
    //*  Google map js 
    if ( $('#mapBox').length ){
        var $lat = $('#mapBox').data('lat');
        var $lon = $('#mapBox').data('lon');
        var $zoom = $('#mapBox').data('zoom');
        var $marker = $('#mapBox').data('marker');
        var $info = $('#mapBox').data('info');
        var $markerLat = $('#mapBox').data('mlat');
        var $markerLon = $('#mapBox').data('mlon');
        var map = new GMaps({
        el: '#mapBox',
        lat: $lat,
        lng: $lon,
        scrollwheel: false,
        scaleControl: true,
        streetViewControl: false,
        panControl: true,
        disableDoubleClickZoom: true,
        mapTypeControl: false,
        zoom: $zoom,
            styles: [
                {
                    "featureType": "water",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "color": "#dcdfe6"
                        }
                    ]
                },
                {
                    "featureType": "transit",
                    "stylers": [
                        {
                            "color": "#808080"
                        },
                        {
                            "visibility": "off"
                        }
                    ]
                },
                {
                    "featureType": "road.highway",
                    "elementType": "geometry.stroke",
                    "stylers": [
                        {
                            "visibility": "on"
                        },
                        {
                            "color": "#dcdfe6"
                        }
                    ]
                },
                {
                    "featureType": "road.highway",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "color": "#ffffff"
                        }
                    ]
                },
                {
                    "featureType": "road.local",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "visibility": "on"
                        },
                        {
                            "color": "#ffffff"
                        },
                        {
                            "weight": 1.8
                        }
                    ]
                },
                {
                    "featureType": "road.local",
                    "elementType": "geometry.stroke",
                    "stylers": [
                        {
                            "color": "#d7d7d7"
                        }
                    ]
                },
                {
                    "featureType": "poi",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "visibility": "on"
                        },
                        {
                            "color": "#ebebeb"
                        }
                    ]
                },
                {
                    "featureType": "administrative",
                    "elementType": "geometry",
                    "stylers": [
                        {
                            "color": "#a7a7a7"
                        }
                    ]
                },
                {
                    "featureType": "road.arterial",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "color": "#ffffff"
                        }
                    ]
                },
                {
                    "featureType": "road.arterial",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "color": "#ffffff"
                        }
                    ]
                },
                {
                    "featureType": "landscape",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "visibility": "on"
                        },
                        {
                            "color": "#efefef"
                        }
                    ]
                },
                {
                    "featureType": "road",
                    "elementType": "labels.text.fill",
                    "stylers": [
                        {
                            "color": "#696969"
                        }
                    ]
                },
                {
                    "featureType": "administrative",
                    "elementType": "labels.text.fill",
                    "stylers": [
                        {
                            "visibility": "on"
                        },
                        {
                            "color": "#737373"
                        }
                    ]
                },
                {
                    "featureType": "poi",
                    "elementType": "labels.icon",
                    "stylers": [
                        {
                            "visibility": "off"
                        }
                    ]
                },
                {
                    "featureType": "poi",
                    "elementType": "labels",
                    "stylers": [
                        {
                            "visibility": "off"
                        }
                    ]
                },
                {
                    "featureType": "road.arterial",
                    "elementType": "geometry.stroke",
                    "stylers": [
                        {
                            "color": "#d6d6d6"
                        }
                    ]
                },
                {
                    "featureType": "road",
                    "elementType": "labels.icon",
                    "stylers": [
                        {
                            "visibility": "off"
                        }
                    ]
                },
                {},
                {
                    "featureType": "poi",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "color": "#dadada"
                        }
                    ]
                }
            ]
        });

        map.addMarker({
            lat: $markerLat,
            lng: $markerLon,
            icon: $marker,    
            infoWindow: {
              content: $info
            }
        })
    }; 
        
    // Product value
    function productValue() {
        var inputVal = $("#product-value");
        if (inputVal.length) {
            $('#value-decrease').on('click', function () {
                inputVal.html(function (i, val) {
                    return val * 1 - 1
                });
            });
            $('#value-increase').on('click', function () {
                inputVal.html(function (i, val) {
                    return val * 1 + 1
                });
            });
        }
    }
    
    // Scroll to top
    function scrollToTop() {
        if ($('.scroll-top').length) {  
            $(window).on('scroll', function () {
                if ($(this).scrollTop() > 200) {
                    $('.scroll-top').fadeIn();
                } else {
                    $('.scroll-top').fadeOut();
                }
            }); 
            //Click event to scroll to top
            $('.scroll-top').on('click', function () {
                $('html, body').animate({
                    scrollTop: 0
                }, 1000);
                return false;
            });
        }
    }
    
    // Preloader JS
    function preloader(){
        if( $('.preloader').length ){
            $(window).on('load', function() {
                $('.preloader').fadeOut();
                $('.preloader').delay(50).fadeOut('slow');  
            })   
        }
    }
    
    /*Function Calls*/ 
    new WOW().init();
    main_slider (); 
    navbarFixed ();
    counterUp ();
    childrenCare ();
    progressbar (); 
    counDown ();
    gallery_isotope ();
    datepicker ();
    selectmenu ();
    productValue ();
    scrollToTop ();
    preloader();
    
})(jQuery);
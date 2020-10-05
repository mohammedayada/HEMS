  ///<reference path="./typings/globals/jquery/index.d.ts">
  

  // var element = document.getElementById('input-date-time-picker');
  // var picker = new Picker(element, {
  //   format: 'YYYY/MM/DD HH:mm',
  //   headers : true
  // });

  $(document).ready(function(){

    // ==========================home page==================================

    // sidenav
    $('.sidenav').sidenav({
      preventScrolling:false
    });
    // dropdown menue
    $(".dropdown-trigger").dropdown({
      coverTrigger: false,
      inDuration: 300,
      outDuration: 225,
      // constrainWidth: false,
      hover: false, // Activate on hover
      // gutter: 0, // Spacing from edge
      belowOrigin: true, // Displays dropdown below the button
      stopPropogation: true
    });

    // select box
    $('select').formSelect();


    // slick slider
    if($('.specialities-slider').length > 0) {
      $('.specialities-slider').slick({
        dots: true,
        autoplay:false,
        infinite: true,
        variableWidth: true,
        prevArrow: false,
        nextArrow: false
      });
    }

    // sticky navbar
    $(window).scroll(function(){
      if($(this).scrollTop() > 10){
        $("nav").addClass('sticky-nav');
      }else{
        $("nav").removeClass('sticky-nav');
      }
    })

    // =================login page ============================================

    // customize height
    var winh = $(window).height();
    var navh = $("nav").innerHeight();
    $(".login-pic").height(winh-navh);
    
     // =================searsh page ============================================

    // datetimepicker
    if($('.datetimepicker').length > 0) {
      $('.datetimepicker').datetimepicker({
        format: 'DD/MM/YYYY',
        icons: {
          up: "fas fa-chevron-up",
          down: "fas fa-chevron-down",
          next: 'fas fa-chevron-right',
          previous: 'fas fa-chevron-left'
        }
      });
    }

    if ($(window).width() > 767) {
      if($('.theiaStickySidebar').length > 0) {
        $('.theiaStickySidebar').theiaStickySidebar({
          // Settings
          additionalMarginTop: 30
        });
      }
    }

    // collapse
    $('.collapsible').collapsible();

      //doctor educations
    var doctorEducationAndWork = $(".doctor-education ul li");
    doctorEducationAndWork.each(function(index){
      $(this).on("mouseover", function(){
        $(this).addClass('color-li-education')
      })
      $(this).on("mouseleave", function(){
        $(this).removeClass('color-li-education')
      })
    });  


   

    // preventdefault the submit input patient dashboard
     var pSettingDas = document.querySelector(".save-changes");
    $(pSettingDas).click(function(e){
      e.preventDefault();
    })


    var ChangePassword = document.querySelector(".save-new-password");
    $(ChangePassword).click(function(e){
      e.preventDefault();
    })



    // Toglle visibiltiy opassword
    var togPasswordVisi  = document.querySelectorAll('.togle-passwod-vis');
    togPasswordVisi.forEach((tog)=>{
      $(tog).click(function (e) {
        e.preventDefault();
        var n = tog.previousSibling;
        // console.log(n);
        // console.log(n.type);
        if(n.type === "password"){
          n.type = "text";
          tog.innerHTML = "<i class='material-icons'>visibility_off</i>";
        }else{
          n.type = "password";
          tog.innerHTML = "<i class='material-icons'>visibility</i>";
        }
      })
    })

    $(".p-setting .save-changes").click(function(e){
      e.preventDefault();
      $(".p-setting  input[type = 'text'], input[type = 'number'], input[type = 'date']").val("");
    })

    $(".cilnic-upload-photo").click(function(e){
      e.preventDefault();
    })

    var custom  = document.querySelector(".custom-price");
    var custom2  = document.querySelector(".custom-price2");
    var  inputPrice = document.querySelector(".price-per-hour");  
    $(custom).click(function (e) {
      $(inputPrice).css("display", "block");
    })

    $(custom2).click(function (e) {
      $(inputPrice).css("display", "none");
    })


    $('#tags').tagsInput({
      'height':'50px',
      'width':'100%',
      'interactive':true,
      'removeWithBackspace' : true,
      'placeholderColor' : '#09e5ab'
    });

    $('#tags2').tagsInput({
      'height':'50px',
      'width':'100%',
      'interactive':true,
      'removeWithBackspace' : true,
      'placeholderColor' : '#09e5ab'
    });

    $(".social-dotor .save-changes").click(function(e){
      e.preventDefault();
    })
  
});



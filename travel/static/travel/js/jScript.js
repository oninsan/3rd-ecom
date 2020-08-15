$(window).scroll(function(){
	if($(this).scrollTop() > 150){
		$("#up-bt").fadeIn();
		// $(".showcase").css("-webkit-filter","blur(2px)");
	}else{
		$("#up-bt").fadeOut();
	  	// $(".showcase").css("-webkit-filter","blur(0px)");
  	}
})

$("#up-bt").click(function(e){
	$("html, body").animate({scrollTop: 0}, 800);
})

// Search Button Part
$(".search-box input").addClass("form-control")
$("#id_destination__icontains").attr("placeholder","Search by Places")
$("#id_continent__icontains").attr("placeholder","Search by Continents")


// sign_up part
$(".signup input").addClass("form-control mb-2")
$(".signup #id_first_name").attr("placeholder","First Name")
$(".signup #id_last_name").attr("placeholder","Last Name")
$(".signup ul").detach()
$(".signup label").detach()
$(".signup br").detach()
$(".signup #error_1_id_first_name").detach()
$(".signup #error_1_id_last_name").detach()
//$(".signup #error_1_id_password1").detach()
//$(".signup #error_1_id_password2").detach()
//$(".signup #error_1_id_email").detach()
//$(".signup #error_1_id_username").detach()
$(".signup #hint_id_password2").detach()
$(".signup #hint_id_username").detach()
//$(".errorlist li").addClass("fa fa-info-circle text-warning shadow-lg")
$(".signup #id_username").attr("placeholder","Username")
$(".signup #id_first_name").attr("autofocus","")
$(".signup #id_username").removeAttr("autofocus")
$(".signup #id_email").attr("placeholder","Email")
$(".signup #id_password1").attr("placeholder","Password")
$(".signup #id_password2").attr("placeholder","Confirm Password")

//webview
$(window).mouseenter(function(e){
    $(".signup #error_1_id_password1").detach()
    $(".signup #error_1_id_password2").detach()
    $(".signup #error_1_id_password3").detach()

    $(".signup #error_2_id_password1").detach()
    $(".signup #error_2_id_password2").detach()
    $(".signup #error_2_id_password3").detach()

    $(".signup #error_3_id_password1").detach()
    $(".signup #error_3_id_password2").detach()
    $(".signup #error_3_id_password3").detach()

    $(".signup #error_1_id_email").detach()
    $(".signup #error_1_id_username").detach()
})

//mobile view
$(window).click(function(e){
    $(".signup #error_1_id_password1").detach()
    $(".signup #error_1_id_password2").detach()
    $(".signup #error_1_id_password3").detach()

    $(".signup #error_2_id_password1").detach()
    $(".signup #error_2_id_password2").detach()
    $(".signup #error_2_id_password3").detach()

    $(".signup #error_3_id_password1").detach()
    $(".signup #error_3_id_password2").detach()
    $(".signup #error_3_id_password3").detach()

    $(".signup #error_1_id_email").detach()
    $(".signup #error_1_id_username").detach()
})

// sign_in part
$(".signin input").addClass("form-control mb-3")
$(".signin label").detach()
$(".signin ul").css("list-style","none")
$(".signin #id_username").attr("placeholder","Username")
$(".signin #id_password").attr("placeholder","Password")



// Filtering Part
$("#id_continent__icontains").css("display","none")

function selectFilterChange(change){
    if(change.value === "continent"){
        $("#id_continent__icontains").fadeIn()
        $("#id_destination__icontains").css("display","none")
    }else{
         $("#id_destination__icontains").fadeIn()
         $("#id_continent__icontains").css("display","none")
    }
}

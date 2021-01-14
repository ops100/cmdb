
$(document).ready(function () {
    // $("#menu>ul>li>ul").addClass('disconfnone');


    // 左侧菜单
    $("u").click(function () {
        $('#menu').find('ul>li>ul').hide();
        $('u').css("border-bottom","");
        $(this).css("border-bottom","1px solid #ffe8a1");
        // $(this).css('color','red');
        // $(this).next('ul').first().css('border-top','thick solid #ff0000');
        $(this).next('ul').css( "box-shadow","1px 1px 1px #aaaaaa");
        $(this).next('ul').toggle(20);
    });
    $('.switch').click(function () {
        $(".sm").toggle(500);
    });


});
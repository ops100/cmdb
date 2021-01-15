
$(document).ready(function () {


    // 左侧菜单
    $("u").click(function () {
        // $(this).toggleClass({'text-shadow': '0px 5px 5px' });
        // $(this).next('ul').css( "box-shadow","1px 1px 1px #aaaaaa");
        $(this).next('ul').toggle(20);
    }
    );
    $('.switch').click(function () {
        $(".sm").toggle(500);
    });


});
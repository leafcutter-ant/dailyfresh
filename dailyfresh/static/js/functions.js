$(function () {
    var $before_login = $('.login_info');
    var $after_login = $('.login_btn');
    $.get('/user/loginstatus/',function (data) {
        if(data.res == 1){
            $before_login.hide();
            $after_login.show();
        }else{
            $before_login.show();
            $after_login.hide();
        }
    });

    var $quit_login = $('#quitlogin');
    $quit_login.click(function () {
        $.get('/user/quitlogin/',function (data) {
            if(data.res == 1){
                $before_login.hide();
                $after_login.show();
            }else{
                alert('quit login failure');
            }
        })
    })

});
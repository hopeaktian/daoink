/**
 * Created by hopeaktian on 2018/10/26.
 */


if(UserName === 'null'){
    $(function() {
        $.login({
            title: '登陆',
            text: '请输入手机号和密码',
            onOK: function (username, password) {
                console.log(username, password);
                var data = {};
                data['tel'] = username;
                data['password'] = password;
                $.ajax({								// 提交POST请求给后端
                    type: 'POST',
                    url: /login/,
                    data: data,
                    dataType: 'json',
                    success: function() {
                        // window.location.reload();
                        // window.location.href='/select';
                        $.getJSON('/login'
                            , function(data) {                    // 从Flask返回的数据
                                alert(data.flag)                     // 浏览器弹窗显示 后端返回的dict["a"]的值，此次是1
                            }
                        )

                    },
                    error: function() {
                        // window.location.reload();
                        // window.location.href='/select';
                        $.getJSON('/login'
                            , function(data) {                    // 从Flask返回的数据
                                alert(data.flag)                     // 浏览器弹窗显示 后端返回的dict["a"]的值，此次是1
                            }
                        )

                    }
                    // success:function() {
                    //     $("#finally").show();
                    // }
                    //
                    //
                    // });

                // if(!flags){
                //     $.toast('登陆失败!');
                //     window.location.href='/select';
                // }else{
                //     $.toast('登陆成功!');
                // }


            },
            onCancel: function () {
                $.confirm("手机一键注册", "没有账号?", function() {
                    // function skip(){
                    window.location.href='/register';
                    // }
                    // setInterval(skip,50);
                }, function() {
                    window.location.href='/';
                    //取消操作
                    // function skip(){
                    //     window.location.href='/';
                    // }
                    // setInterval(skip,50);
                });
            }
        });


    });



}else if(flag === '1'){
    $(function() {
        $.alert("您已经登陆", "提示",
            function () {
            window.location.href='/';
        });

    });
    function skip() {
        window.location.href='/';
    }
    setTimeout("skip()", 3000)

}else if(flag === '2') {
    $(function() {
        $.alert("登陆失败,请重试", "警告",
            function () {
                window.location.href='/login';
            });

    });
}
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
                        window.location.href='/select';
                    },
                    error: function() {
                        window.location.href='/select';
                    }
                });

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



}


$("#page1").change(function(){
    var page1 = $('#page1').val();
    var page2 = $('#page2').val();
    var copies = $('#copies').val();
    $("#fee").text("￥");
    var cost=(page2-page1+1)*copies*0.15;
    var textNode = document.createTextNode(cost.toFixed(2));
    $(fee).append(textNode);
});
$("#page2").change(function(){
    var page1 = $('#page1').val();
    var page2 = $('#page2').val();
    var copies = $('#copies').val();
    $("#fee").text("￥");
    var cost=(page2-page1+1)*copies*0.15;
    var textNode = document.createTextNode(cost.toFixed(2));
    $(fee).append(textNode);
});
$("#copies").change(function(){
    var page1 = $('#page1').val();
    var page2 = $('#page2').val();
    var copies = $('#copies').val();
    $("#fee").text("￥");
    var cost=(page2-page1+1)*copies*0.15;
    var textNode = document.createTextNode(cost.toFixed(2));
    $(fee).append(textNode);
});

$("#place").select({
    title: "打印点",
    items: ["西安理工大学教六2楼西"],
    onChange: function(d) {
        console.log(this, d);
    },
    onClose: function() {
        console.log("close");
    },
    onOpen: function() {
        console.log("open");
    },
});
// var date = new Date();
// var year = date.getFullYear();
// var month = date.getMonth()+1;
// var day = date.getDate();
// var hour = date.getHours();
// var minute = date.getMinutes();
// var second = date.getSeconds();
// time_now = year+'-'+month+'-'+day+' '+hour+':'+minute
$("#time").datetimePicker({
    title: '预约时间',
    min: time_now,
    max: "2019-12-12 12:12",
    onChange: function (picker, values, displayValues) {
        console.log(values);
    }
});

var MAX = 99, MIN = 1;
$('.weui-count__decrease').click(function (e) {
    var $input = $(e.currentTarget).parent().find('.weui-count__number');
    var number = parseInt($input.val() || "0") - 1
    if (number < MIN) number = MIN;
    $input.val(number)
    var page1 = $('#page1').val();
    var page2 = $('#page2').val();
    var copies = $('#copies').val();
    $("#fee").text("￥");
    var cost=(page2-page1+1)*copies*0.15;
    var textNode = document.createTextNode(cost.toFixed(2));
    $(fee).append(textNode);
})
$('.weui-count__increase').click(function (e) {
    var $input = $(e.currentTarget).parent().find('.weui-count__number');
    var number = parseInt($input.val() || "0") + 1
    if (number > MAX) number = MAX;
    $input.val(number)
    var page1 = $('#page1').val();
    var page2 = $('#page2').val();
    var copies = $('#copies').val();
    $("#fee").text("￥");
    var cost=(page2-page1+1)*copies*0.15;
    var textNode = document.createTextNode(cost.toFixed(2));
    $(fee).append(textNode);
})

$("#showTooltips").click(function() {
    var uploaderInput = $('#uploaderInput').val();
    if(uploaderInput==""){
        $.toptip('未上传文件');
        return false;
    }
    var place = $("#place").val();
    if(place==""){
        $.toptip('请选择打印点');
        return false;
    }
    var page1 = $('#page1').val();
    if(page1==""){
        $.toptip('未正确设置起始页');
        return false;
    }
    var page2 = $('#page2').val();
    if(page2==""){
        $.toptip('未正确设置结束页');
        return false;
    }
    if(page1>page2){
        $.toptip('未正确设置打印页数');
        return false;
    }
    else $.modal({
        title: "Success",
        text: "请选择支付方式",
        buttons: [
            { text: "支付宝", onClick: function(){ $.alert("你选择了支付宝"); } },
            { text: "微信支付", onClick: function(){ $.alert("你选择了微信支付"); } },
            { text: "取消", className: "default"},
        ]
    });
});
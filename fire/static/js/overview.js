"use strict";

let option = {
    // backgroundColor: '#2c343c',
    title:{
        // text:'设备安装数量统计图'
    },
    tooltip:{},
    legend:{
        data:['用户来源']
    },
    xAxis:{
        data:["110","110kV","220kV"]
    },
    yAxis:{
        name:'Amount',
    },
    series:[{
        name:'设备数量',
        type:'bar',
        data:[22,3,16],
        itemStyle:{
            color:'rgb(9, 38, 78)',
            barBorderRadius:[5,5,0,0],
            opacity:0.5,
        },
        labelLine: {
            normal: {
                lineStyle: {
                    color: 'rgba(255, 255, 255, 0.3)'
                },
                smooth: 0.2,
                length: 10,
                length2: 20
            }
        },
    }],
    barWidth:30
};
let option2 = {
    // backgroundColor: transparent,
    optical:0.5,

    title: {
        // text:'装备在线统计图',
        // left: 'center',
        // top: 20,
        // textStyle: {
        //     color: '#ccc'
        // }
    },

    tooltip : {
        trigger: 'item',
        formatter: "{a}  --- {b} : {c} ({d}%)"
    },

    visualMap: {
        show: false,
        min: 80,
        max: 600,
        inRange: {
            colorLightness: [0, 1]
        }
    },
    series : [
        {
            name:'设备数量',
            type:'pie',
            radius : ['55%','10%'],
            minAngle:3,
            center: ['50%', '50%'],
            data:[
                {value:335, name:'在线'},
                {value:0, name:'离线'},
            ].sort(function (a, b) { return a.value - b.value; }),
            label: {
                normal: {
                    textStyle: {
                        color: 'rgba(255, 255, 255, 0.3)'
                    }
                }
            },
            labelLine: {
                normal: {
                    lineStyle: {
                        color: 'rgba(255, 255, 255, 0.3)'
                    },
                    smooth: 0.2,
                    length: 20,
                    length2: 50
                }
            },
            itemStyle: {
                normal: {
                    color: 'rgba(48, 228, 183,0.2)',
                    shadowBlur: 200,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            },
            // animationType: 'scale',
            // animationEasing: 'elasticOut',
        }
    ]
};
let option3 = {
    // title: {
    //     text: '微气象'
    // },
    tooltip: {},
    legend: {
        data: ['此刻 ( Present )', '昨天 ( Yesterday )']
    },
    radar: {
        // shape: 'circle',
        radius:'70%',
        name: {
            textStyle: {
                color: '#fff',
                backgroundColor: '#999',
                borderRadius: 3,
                padding: [3, 5]
            }
        },
        indicator: [
            { name: '风向', max: 360},
            { name: '雨量', max: 50},
            { name: '风速', max: 10},
            { name: '气压', max: 1500}
        ]
    },
    series: [{
        name: '昨日 vs 此刻（Yesterday vs At present）',
        type: 'radar',
        // areaStyle: {normal: {}},
        data : [
            {
                value : [15, 1.1, 0.5 , 1230],
                name : '此刻 ( Present )'
            },
            {
                value : [285, 10,0.7, 1300],
                name : '昨天 ( Yesterday )'
            }
        ]
    }]
};
//初始化echarts实例
var myChart = echarts.init(document.getElementById('vol-chart'));
var myChart2 = echarts.init(document.getElementById('online-chart'));
var myChart3 = echarts.init(document.getElementById('sensor-chart'));

//使用制定的配置项和数据显示图表
myChart.setOption(option);
myChart2.setOption(option2);
myChart3.setOption(option3);

window.onresize = function () {

    myChart.resize();
    myChart2.resize();
    myChart3.resize();
};


// slide part

var wrapper = document.getElementById('wrap');
var aBanner = wrapper.getElementsByClassName('banner');
var aSpan = wrapper.getElementsByClassName('tab')[0].getElementsByTagName('span');
var oNext = wrapper.getElementsByClassName('next');
var oPrev = wrapper.getElementsByClassName('prev');

aBanner[0].style.opacity = "1";
var num =0;

function timeSlide(){
    aBanner[num].style.opacity = '0';
    aSpan[num].className = "";
    // alert("This is "+num);
    num = (num+1)%aBanner.length;
    aBanner[num].style.opacity = '1';
    aSpan[num].className = "on";
}

var timer = setInterval(timeSlide,2000);



oNext.onclick = function () {
    clearInterval(timer);
    timeSlide();
    timer = setInterval(timeSlide,2000);
};
oPrev.onclick = function () {
    clearInterval(timer);
    aBanner[num].style.opacity = '0';
    aSpan[num].className = "";
    num = (num-1+aBanner.length)%aBanner.length;
    aBanner[num].style.opacity = '1';
    aSpan.className = 'on';

};

wrapper.onmouseover = function () {
    clearInterval(timer);
};
wrapper.onmouseout = function () {
    clearInterval(timer);
    timer = setInterval(timeSlide,2000);
};
alert("I've worked");

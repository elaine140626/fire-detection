webpackJsonp([1],{"+kPp":function(e,t){},"1L2X":function(e,t){},"6QvN":function(e,t){},NHnr:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var a=n("7+uW"),i={render:function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("el-row",{attrs:{id:"the-base-header"}},[n("el-row",{staticClass:"hidden-lg-and-up"},[n("h2",[e._v("\n      山大i-Learn智能烟火检测系统\n    ")])]),e._v(" "),n("el-row",{staticClass:"hidden-sm-and-down",attrs:{type:"flex",align:"middle"}},[n("el-col",{staticClass:"hidden-md-and-down",attrs:{span:14}},[n("h2",[e._v("\n        山大i-Learn智能烟火检测系统\n      ")])]),e._v(" "),n("el-col",{staticClass:"hidden-sm-and-down"},[n("el-button",{on:{click:function(t){return e.routeTo("overview")}}},[e._v("\n        系统总览\n      ")]),e._v(" "),n("el-button",{on:{click:function(t){return e.routeTo("monitor")}}},[e._v("\n        监控可视化\n      ")]),e._v(" "),n("el-button",{on:{click:function(t){return e.routeTo("warning")}}},[e._v("\n        告警分析\n      ")]),e._v(" "),n("el-button",[e._v("\n        日志管理\n      ")]),e._v(" "),n("el-button",[e._v("\n        推送系统\n      ")]),e._v(" "),n("el-button",{on:{click:function(t){return e.routeTo("config")}}},[e._v("\n        系统配置\n      ")])],1),e._v(" "),n("el-col",{attrs:{span:4}},[n("el-dropdown",{attrs:{trigger:"hover"}},[n("span",[e._v("\n        username "),n("i",{staticClass:"el-icon-user el-icon--right"})]),e._v(" "),n("el-dropdown-menu",[n("el-dropdown-item",[e._v("\n            aaa\n          ")])],1)],1)],1)],1),e._v(" "),n("el-row",[n("el-col",{staticClass:"hidden-md-and-up",attrs:{span:2}},[n("el-dropdown",{staticClass:"el-dropdown-link",attrs:{trigger:"click"},on:{command:e.routeTo}},[n("el-button",[n("i",{staticClass:"el-icon-menu"})]),e._v(" "),n("el-dropdown-menu",{attrs:{slot:"dropdown"},slot:"dropdown"},[n("el-dropdown-item",{attrs:{icon:"el-icon-info",command:"overview"}},[e._v("系统总览")]),e._v(" "),n("el-dropdown-item",{attrs:{icon:"el-icon-video-camera",command:"monitor"}},[e._v("监控可视化")]),e._v(" "),n("el-dropdown-item",{attrs:{icon:"el-icon-edit-outline",command:"warning"}},[e._v("告警分析")]),e._v(" "),n("el-dropdown-item",{attrs:{icon:"el-icon-notebook-1"}},[e._v("日志管理")]),e._v(" "),n("el-dropdown-item",{attrs:{icon:"el-icon-connection"}},[e._v("推送系统")]),e._v(" "),n("el-dropdown-item",{attrs:{icon:"el-icon-setting",command:"conf"}},[e._v("系统配置")]),e._v(" "),n("el-dropdown-item",{attrs:{icon:"el-icon-switch-button"}},[e._v("退出系统")])],1)],1)],1)],1)],1)},staticRenderFns:[]};var r={name:"App",components:{BaseHeader:n("VU/8")({name:"BaseHeader",data:function(){return{}},methods:{routeTo:function(e){this.$router.push(e)}}},i,!1,function(e){n("+kPp")},null,null).exports}},o={render:function(){var e=this.$createElement,t=this._self._c||e;return t("div",{attrs:{id:"app"}},[t("el-container",{staticStyle:{height:"100%"}},[t("el-header",{staticStyle:{height:"auto"}},[t("base-header")],1),this._v(" "),t("el-main",{staticStyle:{display:"flex","justify-content":"center","align-items":"center"}},[t("router-view")],1)],1)],1)},staticRenderFns:[]};var s=n("VU/8")(r,o,!1,function(e){n("1L2X")},null,null).exports,l=n("/ocq"),c={render:function(){var e=this.$createElement;return(this._self._c||e)("el-card",{style:{background:"rgba(255, 255, 255, "+this.oo+")",padding:this.thePadding}},[this._t("default")],2)},staticRenderFns:[]};var d={name:"Login",components:{BlurCard:n("VU/8")({name:"BlurCard",props:{oo:.3,thePadding:0},data:function(){return{}}},c,!1,function(e){n("ZDTP")},"data-v-64c8b628",null).exports},data:function(){return{user:"",password:""}},methods:{OnLogin:function(){var e=this;this.$axios.post(this.urlHead+"/api/user/login/",{username:this.user,password:this.password,withcredential:!0}).then(function(t){console.log(t),e.$notify({title:"成功",message:t.data,type:"success",duration:2500}),e.$router.push("test")}).catch(function(t){e.$notify({title:"失败",message:t.data,type:"warning",duration:2500})})}}},u={render:function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("el-card",[n("h2",[e._v("登录")]),e._v(" "),n("el-form",{attrs:{"label-position":"left"}},[n("el-form-item",{attrs:{label:"用户名"}},[n("el-input",{model:{value:e.user,callback:function(t){e.user=t},expression:"user"}})],1),e._v(" "),n("el-form-item",{attrs:{label:"密码"}},[n("el-input",{attrs:{"show-password":""},model:{value:e.password,callback:function(t){e.password=t},expression:"password"}})],1)],1),e._v(" "),n("el-button",{attrs:{type:"primary"},on:{click:e.OnLogin}},[e._v("登录")])],1)},staticRenderFns:[]};var v=n("VU/8")(d,u,!1,function(e){n("6QvN")},"data-v-68705866",null).exports,m={render:function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"hello"},[n("h1",[e._v(e._s(e.msg))]),e._v(" "),n("h2",[e._v("Essential Links")]),e._v(" "),e._m(0),e._v(" "),n("h2",[e._v("Ecosystem")]),e._v(" "),e._m(1)])},staticRenderFns:[function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("ul",[n("li",[n("a",{attrs:{href:"https://vuejs.org",target:"_blank"}},[e._v("\n        Core Docs\n      ")])]),e._v(" "),n("li",[n("a",{attrs:{href:"https://forum.vuejs.org",target:"_blank"}},[e._v("\n        Forum\n      ")])]),e._v(" "),n("li",[n("a",{attrs:{href:"https://chat.vuejs.org",target:"_blank"}},[e._v("\n        Community Chat\n      ")])]),e._v(" "),n("li",[n("a",{attrs:{href:"https://twitter.com/vuejs",target:"_blank"}},[e._v("\n        Twitter\n      ")])]),e._v(" "),n("br"),e._v(" "),n("li",[n("a",{attrs:{href:"http://vuejs-templates.github.io/webpack/",target:"_blank"}},[e._v("\n        Docs for This Template\n      ")])])])},function(){var e=this.$createElement,t=this._self._c||e;return t("ul",[t("li",[t("a",{attrs:{href:"http://router.vuejs.org/",target:"_blank"}},[this._v("\n        vue-router\n      ")])]),this._v(" "),t("li",[t("a",{attrs:{href:"http://vuex.vuejs.org/",target:"_blank"}},[this._v("\n        vuex\n      ")])]),this._v(" "),t("li",[t("a",{attrs:{href:"http://vue-loader.vuejs.org/",target:"_blank"}},[this._v("\n        vue-loader\n      ")])]),this._v(" "),t("li",[t("a",{attrs:{href:"https://github.com/vuejs/awesome-vue",target:"_blank"}},[this._v("\n        awesome-vue\n      ")])])])}]};var h=n("VU/8")({name:"HelloWorld",data:function(){return{msg:"Welcome to Your Vue.js App"}}},m,!1,function(e){n("RqNW")},"data-v-3b884edb",null).exports,_=n("jkKj"),p=n.n(_),g=n("XLwt"),f={name:"Overview",data:function(){return{drawer:!1,device:[],messages:[{id:1,content:"这是一条告警信息",img_url:"http://188.131.241.21/static/untrack/1558428914.6071951.jpg",device_number:1,device_hint:"n3",deal:!0,c_time:"2019-06-26"},{id:2,content:"这是一条告警信息",img_url:"http://188.131.241.21/static/untrack/1558428914.6071951.jpg",device_number:1,device_hint:"n3",deal:!1,c_time:"2019-06-26"},{id:3,content:"这是一条告警信息",img_url:"http://188.131.241.21/static/untrack/1558428915.6183162.jpg",device_number:1,device_hint:"n3",deal:!1,c_time:"2019-06-26"},{id:4,content:"这是一条告警信息",img_url:"http://188.131.241.21/static/untrack/1558428921.801521.jpg",device_number:1,device_hint:"n3",deal:!0,c_time:"2019-06-26"},{id:5,content:"这是一条告警信息",img_url:"http://188.131.241.21/static/untrack/1558428922.8135169.jpg",device_number:1,device_hint:"n3",deal:!0,c_time:"2019-06-26"},{id:6,content:"这是一条告警信息",img_url:"http://188.131.241.21/static/untrack/",device_number:1,device_hint:"n3",deal:!1,c_time:"2019-06-26"},{id:7,content:"这是一条告警信息",img_url:"http://188.131.241.21/static/untrack/1558428923.8265727.jpg",device_number:1,device_hint:"n3",deal:!1,c_time:"2019-06-26"},{id:8,content:"这是一条告警信息",img_url:"http://188.131.241.21/static/untrack/1558428924.8973463.jpg",device_number:1,device_hint:"n3",deal:!1,c_time:"2019-06-26"},{id:9,content:"这是一条告警信息",img_url:"http://188.131.241.21/static/untrack/1558428925.974638.jpg",device_number:1,device_hint:"n3",deal:!1,c_time:"2019-06-26"},{id:10,content:"这是一条告警信息",img_url:"http://188.131.241.21/static/untrack/1558428928.0553596.jpg",device_number:1,device_hint:"n3",deal:!1,c_time:"2019-06-26"}],deviceOnShow:{serial_number:void 0,hint:void 0,location_x:void 0,location_y:void 0,video_url:void 0},videoOnShow:"",autoPlay:!0,messageUnread:0,messageAmount:0,deviceOnline:0,deviceAmount:0}},mounted:function(){var e=this,t=g.init(document.getElementById("voltage-chart")),n=g.init(document.getElementById("install-chart")),a=g.init(document.getElementById("wheather-chart")),i={optical:.5,title:{},tooltip:{trigger:"item",formatter:"{a}  --- {b} : {c} ({d}%)"},visualMap:{show:!1,min:80,max:600,inRange:{colorLightness:[0,1]}},series:[{name:"设备数量",type:"pie",radius:["55%","10%"],minAngle:3,center:["50%","50%"],data:[{value:335,name:"在线"},{value:0,name:"离线"}].sort(function(e,t){return e.value-t.value}),label:{normal:{textStyle:{color:"rgba(255, 255, 255, 0.3)"}}},labelLine:{normal:{lineStyle:{color:"rgba(255, 255, 255, 0.3)"},smooth:.2,length:20,length2:50}},itemStyle:{normal:{color:"rgba(48, 228, 183,0.2)",shadowBlur:200,shadowColor:"rgba(0, 0, 0, 0.5)"}}}]};t.setOption({title:{},tooltip:{},legend:{data:["用户来源"]},xAxis:{data:["110","110kV","220kV"]},yAxis:{name:"Amount"},series:[{name:"设备数量",type:"bar",data:[22,3,16],itemStyle:{color:"rgb(9, 38, 78)",barBorderRadius:[5,5,0,0],opacity:.5},labelLine:{normal:{lineStyle:{color:"rgba(255, 255, 255, 0.3)"},smooth:.2,length:10,length2:20}}}],barWidth:30}),n.setOption(i),a.setOption({tooltip:{},legend:{data:["此刻 ( Present )","昨天 ( Yesterday )"]},radar:{radius:"70%",name:{textStyle:{color:"#fff",backgroundColor:"#999",borderRadius:3,padding:[3,5]}},indicator:[{name:"风向",max:360},{name:"雨量",max:50},{name:"风速",max:10},{name:"气压",max:1500}]},series:[{name:"昨日 vs 此刻（Yesterday vs At present）",type:"radar",data:[{value:[15,1.1,.5,1230],name:"此刻 ( Present )"},{value:[285,10,.7,1300],name:"昨天 ( Yesterday )"}]}]}),window.onresize=function(){t.resize(),n.resize(),a.resize()},this.$refs["popover-message"].doClose();var r=new p.a.Map("map-chart"),o=new p.a.Point(120.697792,36.369133);r.centerAndZoom(o,15),this.$axios.get(this.urlHead+"/api/devices/all").catch(function(){e.$notify({message:"无法获取设备信息",type:"warning"})}).then(function(t){e.device=t.data.data,console.log(t);for(var n=function(t){var n=new p.a.Point(e.device[t].location_x,e.device[t].location_y),a=new p.a.Marker(n);r.addOverlay(a),a.addEventListener("mouseover",function(){e.deviceOnShow=e.device[t],e.$refs["popover-message"].doShow(),console.log(e.$refs["popover-message"])}),a.addEventListener("mouseout",function(){e.$refs["popover-message"].doClose()}),a.addEventListener("click",function(){e.ShowVideo(e.device[t].video_url)})},a=0;a<e.device.length;a++)n(a)}),this.GetMessages()},methods:{MessageFormat:function(e){return 0===e?"无":e+"%"},ShowVideo:function(e){this.drawer=!0,this.videoOnShow=e},InitVideo:function(){var e=document.getElementById("myPlayer"),t=document.createElement("source");t.setAttribute("src",this.videoOnShow),e.appendChild(t),console.log(EZUIPlayer),new EZUIPlayer("myPlayer").play()},GetMessages:function(){var e=this;this.$axios.get(this.urlHead+"/api/messages/?limit=10&type=all",{withcredentials:!0}).then(function(t){console.log(t.data),0===t.data.code?e.messages=t.data.data:e.$notify({message:t.data.msg,type:"warning"})}).catch(function(t){console.log(t),e.$notify({message:"无法获取报警信息",type:"warning"})})},HandleChange:function(e,t){this.$refs.imgCarousel.setActiveItem(e),this.$refs.messageCarousel.setActiveItem(e)}},computed:{devicePercentage:function(){return 0===this.deviceAmount?0:Math.ceil(100*this.deviceOnline/this.deviceAmount)},messagePercentage:function(){return 0===this.messageAmount?0:Math.ceil(100*this.messageUnread/this.messageAmount)}}},w={render:function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"overview-main"},[n("el-card",{staticClass:"overview-voltage-card",attrs:{slot:"header"},slot:"header"},[n("span",[e._v("设备安装")]),e._v(" "),n("div",{staticStyle:{height:"100%"},attrs:{id:"voltage-chart"}})]),e._v(" "),n("el-card",{staticClass:"overview-install-card",attrs:{slot:"header"},slot:"header"},[n("span",[e._v("设备在线")]),e._v(" "),n("div",{attrs:{id:"install-chart"}})]),e._v(" "),n("el-card",{staticClass:"overview-map-card",staticStyle:{margin:"0",padding:"0"}},[n("el-popover",{ref:"popover-message",attrs:{trigger:"manual"}},[n("el-card",[n("h4",[e._v("设备序列号")]),e._v("\n        "+e._s(e.deviceOnShow.serial_number)+"\n        "),n("h4",[e._v("提示信息")]),e._v("\n        "+e._s(e.deviceOnShow.hint)+"\n        "),n("h4",[e._v("视频地址")]),e._v("\n        "+e._s(e.deviceOnShow.video_url)+"\n        "),n("h4",[e._v("经纬度")]),e._v("\n        ("+e._s(e.deviceOnShow.location_x)+", "+e._s(e.deviceOnShow.location_y)+")\n      ")]),e._v(" "),n("div",{attrs:{slot:"reference",id:"map-chart"},slot:"reference"})],1)],1),e._v(" "),n("el-card",{staticClass:"overview-amount-card",attrs:{slot:"header"},slot:"header"},[n("span",[e._v("装置数量")]),e._v(" "),n("div",{staticClass:"flex-center",attrs:{id:"amount-chart"}},[n("div",{staticStyle:{display:"block","align-items":"center",height:"auto"}},[n("div",{staticStyle:{display:"block","align-items":"center",height:"auto"}},[n("h4",[e._v("未读消息: "+e._s(e.messageUnread))]),e._v(" "),n("el-progress",{staticStyle:{height:"auto"},attrs:{percentage:e.messageUnread,format:e.MessageFormat,color:"red"}})],1),e._v(" "),n("div",{staticStyle:{display:"block","align-items":"center",height:"auto"}},[n("h4",[e._v("设备在线: "+e._s(e.deviceOnline))]),e._v(" "),n("el-progress",{staticStyle:{height:"auto"},attrs:{percentage:e.devicePercentage,color:"green"}})],1)])])]),e._v(" "),n("el-card",{staticClass:"overview-wheather-card",attrs:{slot:"header"},slot:"header"},[n("span",[e._v("微气象")]),e._v(" "),n("div",{attrs:{id:"wheather-chart"}})]),e._v(" "),n("el-card",{staticClass:"overview-message-card",attrs:{slot:"header"},slot:"header"},[n("span",[e._v("报警信息")]),e._v(" "),n("el-carousel",{ref:"messageCarousel",attrs:{height:"30%",autoplay:!1,type:"card",direction:"vertical","indicator-position":"outside"},on:{change:e.HandleChange}},e._l(e.messages,function(t){return n("el-carousel-item",{key:t.id,staticClass:"flex-center"},[e._v("\n        "+e._s(t.content)+"\n        "),n("span",{staticStyle:{"font-size":"13px"}},[e._v(e._s(t.c_time))])])}),1)],1),e._v(" "),n("el-card",{staticClass:"overview-img-card"},[n("span",[e._v("预警图片")]),e._v(" "),n("el-carousel",{ref:"imgCarousel",attrs:{autoplay:e.autoPlay},on:{change:e.HandleChange}},e._l(e.messages,function(e){return n("el-carousel-item",{key:e.id,staticClass:"flex-center"},[n("el-image",{staticStyle:{"max-height":"80%"},attrs:{src:e.img_url,fit:"cover"}})],1)}),1)],1),e._v(" "),n("el-drawer",{ref:"videoDrawer",attrs:{title:"设备实时监控",visible:e.drawer,size:"85%","destroy-on-close":!0,direction:"btt"},on:{"update:visible":function(t){e.drawer=t},opened:e.InitVideo}},[n("div",{attrs:{id:"myPlayer",controls:"",playsInline:"","webkit-playsinline":""}})])],1)},staticRenderFns:[]};var y=n("VU/8")(f,w,!1,function(e){n("tPIW")},"data-v-26fe8bca",null).exports,b={render:function(){var e=this.$createElement,t=this._self._c||e;return t("div",{staticStyle:{height:"100%",width:"100%"}},[t("el-row",[t("el-col",{attrs:{span:4}},[this._v("\n      1\n    ")]),this._v(" "),t("el-col",{attrs:{span:20}},[this._v("\n      2\n    ")])],1)],1)},staticRenderFns:[]};var k=n("VU/8")({name:"Monitor",data:function(){return{videos:[]}},mounted:function(){this.$axios.get("").catch().then()}},b,!1,function(e){n("jrOz")},"data-v-5c0446ca",null).exports;a.default.use(l.a);var x=new l.a({routes:[{path:"/",redirect:"/login"},{path:"/login",name:"Login",component:v},{path:"/test",name:"Test",component:h},{path:"/monitor",name:"Monitor",component:k},{path:"/overview",name:"Overview",component:y}]}),C=n("mtWM"),S=n.n(C),j=n("zL8q"),$=n.n(j);n("tvR6"),n("sfy8"),n("rqsT");a.default.use($.a),a.default.prototype.$axios=S.a,a.default.prototype.urlHead="http://127.0.0.1:8000",a.default.config.productionTip=!1,new a.default({el:"#app",router:x,components:{App:s},template:"<App/>"})},RqNW:function(e,t){},ZDTP:function(e,t){},jkKj:function(e,t){e.exports=BMap},jrOz:function(e,t){},rqsT:function(e,t){},sfy8:function(e,t){},tPIW:function(e,t){},tvR6:function(e,t){}},["NHnr"]);
//# sourceMappingURL=app.c63a1b5118fb3e433a4a.js.map
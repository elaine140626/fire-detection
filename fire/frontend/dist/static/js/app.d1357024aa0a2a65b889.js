webpackJsonp([1],{"07rD":function(t,e){},"1uuo":function(t,e){},"5xUT":function(t,e){},NHnr:function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var r=n("7+uW"),a={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("el-row",{attrs:{id:"the-base-header"}},[n("el-row",{staticClass:"hidden-lg-and-up"},[n("h2",[t._v("\n      山大i-Learn智能烟火检测系统\n    ")])]),t._v(" "),n("el-row",{staticClass:"hidden-sm-and-down",attrs:{type:"flex",align:"middle"}},[n("el-col",{staticClass:"hidden-md-and-down",attrs:{span:14}},[n("h2",[t._v("\n        山大i-Learn智能烟火检测系统\n      ")])]),t._v(" "),n("el-col",{staticClass:"hidden-sm-and-down"},[n("el-button",[t._v("\n        系统总览\n      ")]),t._v(" "),n("el-button",[t._v("\n        监控可视化\n      ")]),t._v(" "),n("el-button",[t._v("\n        告警分析\n      ")]),t._v(" "),n("el-button",[t._v("\n        日志管理\n      ")]),t._v(" "),n("el-button",[t._v("\n        推送系统\n      ")]),t._v(" "),n("el-button",[t._v("\n        系统配置\n      ")])],1),t._v(" "),n("el-col",{attrs:{span:4}},[n("el-dropdown",{attrs:{trigger:"hover"}},[n("span",[t._v("\n        username "),n("i",{staticClass:"el-icon-user el-icon--right"})]),t._v(" "),n("el-dropdown-menu",[n("el-dropdown-item",[t._v("\n            aaa\n          ")])],1)],1)],1)],1),t._v(" "),n("el-row",[n("el-col",{staticClass:"hidden-md-and-up",attrs:{span:2}},[n("el-dropdown",{staticClass:"el-dropdown-link",attrs:{trigger:"click"}},[n("el-button",[n("i",{staticClass:"el-icon-menu"})]),t._v(" "),n("el-dropdown-menu",{attrs:{slot:"dropdown"},slot:"dropdown"},[n("el-dropdown-item",{attrs:{icon:"el-icon-info",command:"f"}},[t._v("系统总览")]),t._v(" "),n("el-dropdown-item",{attrs:{icon:"el-icon-video-camera"}},[t._v("监控可视化")]),t._v(" "),n("el-dropdown-item",{attrs:{icon:"el-icon-edit-outline"}},[t._v("告警分析")]),t._v(" "),n("el-dropdown-item",{attrs:{icon:"el-icon-notebook-1"}},[t._v("日志管理")]),t._v(" "),n("el-dropdown-item",{attrs:{icon:"el-icon-connection"}},[t._v("推送系统")]),t._v(" "),n("el-dropdown-item",{attrs:{icon:"el-icon-setting"}},[t._v("系统配置")]),t._v(" "),n("el-dropdown-item",{attrs:{icon:"el-icon-switch-button"}},[t._v("退出系统")])],1)],1)],1)],1)],1)},staticRenderFns:[]};var s={name:"App",components:{BaseHeader:n("VU/8")({name:"BaseHeader",data:function(){return{}}},a,!1,function(t){n("5xUT")},null,null).exports}},o={render:function(){var t=this.$createElement,e=this._self._c||t;return e("div",{attrs:{id:"app"}},[e("el-container",{staticStyle:{height:"100%"}},[e("el-header",[e("base-header")],1),this._v(" "),e("el-main",{staticStyle:{display:"flex","justify-content":"center","align-items":"center"}},[e("router-view")],1)],1)],1)},staticRenderFns:[]};var i=n("VU/8")(s,o,!1,function(t){n("nTmJ")},null,null).exports,l=n("/ocq"),u={render:function(){var t=this.$createElement;return(this._self._c||t)("el-card",{style:{background:"rgba(255, 255, 255, "+this.oo+")",padding:this.thePadding}},[this._t("default")],2)},staticRenderFns:[]};var c={name:"Login",components:{BlurCard:n("VU/8")({name:"BlurCard",props:{oo:.3,thePadding:0},data:function(){return{}}},u,!1,function(t){n("Z9P2")},"data-v-63eb8dae",null).exports},data:function(){return{user:"",password:""}},methods:{OnLogin:function(){var t=this;this.$axios.post("check_user",{params:{username:this.user,password:this.password}}).then(function(){t.$router.push("test")}).catch(function(){alert("WWWW")})}}},d={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("el-card",[n("h2",[t._v("登录")]),t._v(" "),n("el-form",{attrs:{"label-position":"left"}},[n("el-form-item",{attrs:{label:"用户名"}},[n("el-input",{model:{value:t.user,callback:function(e){t.user=e},expression:"user"}})],1),t._v(" "),n("el-form-item",{attrs:{label:"密码"}},[n("el-input",{attrs:{"show-password":""},model:{value:t.password,callback:function(e){t.password=e},expression:"password"}})],1)],1),t._v(" "),n("el-button",{attrs:{type:"primary"},on:{click:t.OnLogin}},[t._v("登录")])],1)},staticRenderFns:[]};var v=n("VU/8")(c,d,!1,function(t){n("07rD")},"data-v-e51bbbce",null).exports,_={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"hello"},[n("h1",[t._v(t._s(t.msg))]),t._v(" "),n("h2",[t._v("Essential Links")]),t._v(" "),t._m(0),t._v(" "),n("h2",[t._v("Ecosystem")]),t._v(" "),t._m(1)])},staticRenderFns:[function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("ul",[n("li",[n("a",{attrs:{href:"https://vuejs.org",target:"_blank"}},[t._v("\n        Core Docs\n      ")])]),t._v(" "),n("li",[n("a",{attrs:{href:"https://forum.vuejs.org",target:"_blank"}},[t._v("\n        Forum\n      ")])]),t._v(" "),n("li",[n("a",{attrs:{href:"https://chat.vuejs.org",target:"_blank"}},[t._v("\n        Community Chat\n      ")])]),t._v(" "),n("li",[n("a",{attrs:{href:"https://twitter.com/vuejs",target:"_blank"}},[t._v("\n        Twitter\n      ")])]),t._v(" "),n("br"),t._v(" "),n("li",[n("a",{attrs:{href:"http://vuejs-templates.github.io/webpack/",target:"_blank"}},[t._v("\n        Docs for This Template\n      ")])])])},function(){var t=this.$createElement,e=this._self._c||t;return e("ul",[e("li",[e("a",{attrs:{href:"http://router.vuejs.org/",target:"_blank"}},[this._v("\n        vue-router\n      ")])]),this._v(" "),e("li",[e("a",{attrs:{href:"http://vuex.vuejs.org/",target:"_blank"}},[this._v("\n        vuex\n      ")])]),this._v(" "),e("li",[e("a",{attrs:{href:"http://vue-loader.vuejs.org/",target:"_blank"}},[this._v("\n        vue-loader\n      ")])]),this._v(" "),e("li",[e("a",{attrs:{href:"https://github.com/vuejs/awesome-vue",target:"_blank"}},[this._v("\n        awesome-vue\n      ")])])])}]};var p=n("VU/8")({name:"HelloWorld",data:function(){return{msg:"Welcome to Your Vue.js App"}}},_,!1,function(t){n("1uuo")},"data-v-d8ec41bc",null).exports;r.default.use(l.a);var h=new l.a({routes:[{path:"/",redirect:"/login"},{path:"/login",name:"Login",component:v},{path:"/test",name:"Test",component:p}]}),m=n("mtWM"),f=n.n(m),g=n("zL8q"),w=n.n(g);n("tvR6"),n("sfy8");r.default.use(w.a),r.default.prototype.$axios=f.a,r.default.config.productionTip=!1,new r.default({el:"#app",router:h,components:{App:i},template:"<App/>"})},Z9P2:function(t,e){},nTmJ:function(t,e){},sfy8:function(t,e){},tvR6:function(t,e){}},["NHnr"]);
//# sourceMappingURL=app.d1357024aa0a2a65b889.js.map
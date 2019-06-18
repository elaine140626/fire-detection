"use strict";

function toOverview() {
    let curHref = window.location.href.split('/');
    let strLength = window.location.href.length;

    window.location.href = window.location.href.substr(0,strLength-curHref[curHref.length-1].length) + "overview.html";
}
function toMonitor() {
    let curHref = window.location.href.split('/');
    let strLength = window.location.href.length;

    window.location.href = window.location.href.substr(0,strLength-curHref[curHref.length-1].length) + "monitor.html";
}

function toLogin() {
    let curHref = window.location.href.split('/');
    let strLength = window.location.href.length;

    window.location.href = window.location.href.substr(0,strLength-curHref[curHref.length-1].length) + "monitor.html";
}
function toConf() {
    let curHref = window.location.href.split('/');
    let strLength = window.location.href.length;

    window.location.href = window.location.href.substr(0,strLength-curHref[curHref.length-1].length) + "conf.html";
}

function toWarning() {
    let curHref = window.location.href.split('/');
    let strLength = window.location.href.length;

    window.location.href = window.location.href.substr(0,strLength-curHref[curHref.length-1].length) + "warning.html";
}

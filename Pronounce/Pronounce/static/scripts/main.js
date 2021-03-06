/*
*  Copyright (c) 2015 The WebRTC project authors. All Rights Reserved.
*
*  Use of this source code is governed by a BSD-style license
*  that can be found in the LICENSE file in the root of the source
*  tree.
*/

// This code is adapted from
// https://rawgit.com/Miguelao/demos/master/mediarecorder.html

'use strict';

/* globals MediaRecorder */

var mediaSource = new MediaSource();
mediaSource.addEventListener('sourceopen', handleSourceOpen, false);
var mediaRecorder;
var recordedBlobs;
var sourceBuffer;

var gumVideo = document.querySelector('audio#gum');
var recordedVideo = document.querySelector('audio#recorded');

var recordButton = document.querySelector('button#record');
var playButton = document.querySelector('button#play');
var downloadButton = document.querySelector('button#download');
var submitButton = document.querySelector('button#submit');
recordButton.onclick = toggleRecording;
playButton.onclick = play;
downloadButton.onclick = download;
submitButton.onclick = upload;


// window.isSecureContext could be used for Chrome
var isSecureOrigin = location.protocol === 'https:' ||
    location.hostname === 'localhost';
if (!isSecureOrigin) {
    alert('getUserMedia() must be run from a secure origin: HTTPS or localhost.' +
        '\n\nChanging protocol to HTTPS');
    location.protocol = 'HTTPS';
}

var constraints = {
    audio: true,
    video: false
};

function handleSuccess(stream) {
    recordButton.disabled = false;
    console.log('getUserMedia() got stream: ', stream);
    window.stream = stream;
    if (window.URL) {
        gumVideo.src = window.URL.createObjectURL(stream);
    } else {
        gumVideo.src = stream;
    }
}

function handleError(error) {
    console.log('navigator.getUserMedia error: ', error);
}

navigator.mediaDevices.getUserMedia(constraints).
    then(handleSuccess).catch(handleError);

function handleSourceOpen(event) {
    console.log('MediaSource opened');
    sourceBuffer = mediaSource.addSourceBuffer('audio/mp3');
    console.log('Source buffer: ', sourceBuffer);
}

recordedVideo.addEventListener('error', function (ev) {
    console.error('MediaRecording.recordedMedia.error()');
    alert('Your browser can not play\n\n' + recordedVideo.src
        + '\n\n media clip. event: ' + JSON.stringify(ev));
}, true);

function handleDataAvailable(event) {
    if (event.data && event.data.size > 0) {
        recordedBlobs.push(event.data);
    }
}

function handleStop(event) {
    console.log('Recorder stopped: ', event);
}

function toggleRecording() {
    if (recordButton.textContent === 'Opnemen ') {
        
        startRecording();
    } else {
        $("#stoptext").show();
        $("#starttext").hide();
        stopRecording();
        recordButton.textContent = 'Opnemen ';
        playButton.disabled = false;
        downloadButton.disabled = false;
        submitButton.disabled = false;
    }
}


function startRecording() {
    recordedBlobs = [];
    var options = { mimeType: 'audio/opus' };
    if (!MediaRecorder.isTypeSupported(options.mimeType)) {
        console.log(options.mimeType + ' is not Supported');
        options = { mimeType: 'audio/ogg' };
        if (!MediaRecorder.isTypeSupported(options.mimeType)) {
            console.log(options.mimeType + ' is not Supported');
            options = { mimeType: 'audio/webm' };
            if (!MediaRecorder.isTypeSupported(options.mimeType)) {
                console.log(options.mimeType + ' is not Supported');
                options = { mimeType: '' };
            }
        }
    }
    try {
        mediaRecorder = new MediaRecorder(window.stream, options);
        $("#starttext").show();
        $("#stoptext").hide();
        $("#submittext").hide();
    } catch (e) {
        console.error('Exception while creating MediaRecorder: ' + e);
        alert('Oeps, zorg dat je de toegang tot de microfoon opent'
            );
        return;
    }
    console.log('Created MediaRecorder', mediaRecorder, 'with options', options);
    recordButton.textContent = 'Stop met opnemen';
    playButton.disabled = true;
    downloadButton.disabled = true;
    submitButton.disabled = true;
    mediaRecorder.onstop = handleStop;
    mediaRecorder.ondataavailable = handleDataAvailable;
    mediaRecorder.start(10); // collect 10ms of data
    console.log('MediaRecorder started', mediaRecorder);
}

function stopRecording() {
    mediaRecorder.stop();
    console.log('Recorded Blobs: ', recordedBlobs);
    recordedVideo.controls = true;
}

function play() {
    var superBuffer = new Blob(recordedBlobs, { type: 'audio/webm' });
    recordedVideo.src = window.URL.createObjectURL(superBuffer);
}

function download() {
    var blob = new Blob(recordedBlobs, { type: 'audio/webm' });
    console.log(blob);
    var url = window.URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.style.display = 'none';
    a.href = url;
    a.download = 'test.webm';
    document.body.appendChild(a);
    a.click();
    setTimeout(function () {
        document.body.removeChild(a);
        window.URL.revokeObjectURL(url);
    }, 100);
}

function upload() {
    var browserInfo = getBrowserInfo();
    console.log(browserInfo);
    var x = document.getElementById("langtext").innerHTML;
    var splitx = x.split(" ");
    console.log(browserInfo + "Hi" + splitx[0].toString());
    if (browserInfo.slice(0,5) == 'Firef')
    {
        var blob = new Blob(recordedBlobs, { type: 'audio/ogg' });
        var fd = new FormData();
        fd.append('fname', splitx[0].toString());
        fd.append('data', blob, "test.ogg");
    }
    else if (browserInfo.slice(0, 5) == 'Chrom') {
        var blob = new Blob(recordedBlobs, { type: 'audio/webm' });
        var fd = new FormData();
        fd.append('fname', splitx[0].toString()); 
        fd.append('data', blob, "test.webm");
    }
    else if (browserInfo.slice(0, 5) == 'Edge ') {
        var blob = new Blob(recordedBlobs, { type: 'audio/ogg' });
        var fd = new FormData();
        fd.append('fname', splitx[0].toString());
        fd.append('data', blob, "test.ogg");
    }
    else if (browserInfo.slice(0, 5) == 'Safar') {
        var blob = new Blob(recordedBlobs, { type: 'audio/ogg' });
        var fd = new FormData();
        fd.append('fname', splitx[0].toString());
        fd.append('data', blob, "test.ogg");
    }
    console.log(fd)
    console.log(browserInfo);
    var request = new XMLHttpRequest();
    request.open("POST", "/assemblies");
    request.send(fd);
    $("#submittext").show();

}

function getBrowserInfo() {
    var ua = navigator.userAgent, tem,
        M = ua.match(/(opera|chrome|safari|firefox|msie|trident(?=\/))\/?\s*(\d+)/i) || [];
    if (/trident/i.test(M[1])) {
        tem = /\brv[ :]+(\d+)/g.exec(ua) || [];
        return 'IE ' + (tem[1] || '');
    }
    if (M[1] === 'Chrome') {
        tem = ua.match(/\b(OPR|Edge)\/(\d+)/);
        if (tem != null) return tem.slice(1).join(' ').replace('OPR', 'Opera');
    }
    M = M[2] ? [M[1], M[2]] : [navigator.appName, navigator.appVersion, '-?'];
    if ((tem = ua.match(/version\/(\d+)/i)) != null)
        M.splice(1, 1, tem[1]);
    return M.join(' ');
}




function getBlob() {
    var blob = new Blob(recordedBlobs, { type: 'audio/ogg' });
    //var blobs = window.URL.createObjectURL(blob)
    console.log(blob);
    return blob
}

//document.getElementById('myField').value = getBlob();
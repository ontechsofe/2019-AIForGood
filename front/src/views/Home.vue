<template>
    <v-app dark id="app-home">
        <v-toolbar color="primary" dark fixed app>
            <v-toolbar-title>TrashSORT</v-toolbar-title>
        </v-toolbar>
        <v-content>
            <div id="camera">
                <video id="camera--view" autoplay playsinline></video>
                <canvas id="camera--sensor" style="display: none"></canvas>
                <button id="camera--trigger" @click="clickTrigger">Take a picture</button>
            </div>
        </v-content>
    </v-app>
</template>

<script>
    export default {
        name: "Home",
        data: () => ({
            constraints: { video: { facingMode: "user" }, audio: false },
            cameraView: null,
            cameraOutput: null,
            cameraSensor: null,
            cameraTrigger: null
        }),
        mounted() {
            this.cameraView = document.querySelector("#camera--view")
            this.cameraSensor = document.querySelector("#camera--sensor")
            this.cameraTrigger = document.querySelector("#camera--trigger")
            window.addEventListener("load", () => {
                navigator.mediaDevices.getUserMedia({video: true}).then(mediaStream => { this.cameraView.srcObject = mediaStream; })
            }, false)
        },
        methods: {
            clickTrigger() {
                this.cameraSensor.width = this.cameraView.videoWidth
                this.cameraSensor.height = this.cameraView.videoHeight
                this.cameraSensor.getContext("2d").drawImage(this.cameraView, 0, 0)
                console.log(this.cameraSensor.toDataURL("image/jpeg"))
            }
        }
    }
</script>

<style>
    #camera, #camera--view, #camera--sensor{
        position: fixed;
        height: 100%;
        width: 100%;
        object-fit: cover;
    }

    #camera--view, #camera--sensor {
        transform: scaleX(-1);
    }

    #camera--trigger{
        width: 200px;
        background-color: black;
        color: white;
        font-size: 16px;
        border-radius: 30px;
        border: none;
        padding: 15px 20px;
        text-align: center;
        box-shadow: 0 0 10px 2px rgba(0,0,0,0.5);
        position: fixed;
        bottom: 30px;
        left: calc(50% - 100px);
    }
</style>

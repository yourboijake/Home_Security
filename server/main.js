//https://medium.com/@supersjgk/building-a-live-streaming-app-using-flask-opencv-and-webrtc-8cc8b521fa44

let pc = new RTCPeerConnection();

async function createOffer() {
    console.log("Sending offer request");

    const offerResponse = await fetch("/offer", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            sdp: "",
            type: "offer",
        }),
    });

    //trigger the process by creating and sending an offer
    createOffer();

    const offer = await offerResponse.json();
    console.log("Recieved offer response:", offer);

    await pc.setRemoteDescription(new RTCSessionDescription(offer));
    const answer = await pc.createAnswer();
    await pc.setLocalDescription(answer);
}
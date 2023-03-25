const APP_ID = "d025a07a47a4421db20529206dba7b3b"
const CHANNEL = "mynewchannel"
const TOKEN = "006d025a07a47a4421db20529206dba7b3bIAAPKAhqIs2iCXbaZlkvYYleXuRraWQwCLCvKKeW5+hlKmf+nQh4pRwwIgASB0MAQFD+YwQAAQBAUP5jAgBAUP5jAwBAUP5jBABAUP5j"
UID

console.log("In stream.js")

const client = AgoraRTC.createClient({mode:'rtc', codec : 'vp8'})

let localTracks=[]
let remoteUsers ={}

let joinAndDisplayStream = async () =>{

    client.on("user-published", handleUserJoined)
    await client.join(APP_ID, CHANNEL, TOKEN, UID)
    localTracks = await AgoraRTC.createMicrophoneAndCameraTracks()

    let player =  `<div  class="video-container" id="user-container-${UID}">
    <div class="video-player" id="user-${UID}"></div>
    <div class="username-wrapper"><span class="user-name">MyName</span></div>
 </div>`

    document.getElementById('video-streams').insertAdjacentHTML('beforeend',player)
    localTracks[1].play(`user-${UID}`)
    await client.publish(localTracks[0],localTracks[1])
}
let handleUserJoined = async (user, mediaType) => {
    remoteUsers[user.uid] = user
    await client.subscribe(user, mediaType)

    if (mediaType === 'video'){
        let player = document.getElementById(`user-container-${user.uid}`)
        if (player != null){
            player.remove()
        }
        player =  `<div  class="video-container" id="user-container-${user.uid}">
                        <div class="video-player" id="user-${user.uid}}"></div>
                        <div class="username-wrapper"><span class="user-name">MyName</span></div>
                    </div>`
        document.getElementById('video-streams').insertAdjacentHTML('beforeend',player)  
        user.videoTrack.play(`user-${user.uid}`)
    }

    if (mediaType === 'audio'){
        user.audioTrack.play()
    }
}
joinAndDisplayStream()
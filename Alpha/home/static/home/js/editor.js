console.log("in editor.js")

var editor = ace.edit('editor');
editor.setTheme("ace/theme/twilight");
document.getElementById('editor').style.fontSize='14px';
editor.session.setMode("ace/mode/python");

let cursorPos = null;
let lock = false

//send updates from text editor to other people connected using websocket
//this will be done as soon as a keystroke is made
// editor.session.on('change', function(delta) {
//     // console.log(lock)
//     if(lock) return;
// // delta.start, delta.end, delta.lines, delta.action
// // console.log(delta)
// // editor.getSession().getDocument().applyDeltas(delta)
// chatSocket.send(JSON.stringify({"type": "editor", "text": delta, "cursor": editor.selection.getCursor()}))
// });

chatSocket.onmessage = function (e) {
    let data = JSON.parse(e.data);

    if(data['type']=='chat'){
        if(data.username){
            document.querySelector('#chat-text').innerHTML += ('<span class="text-danger">' + data.username + '</span>'+ ': ' + data.message + '<br/>')
        }
        else{
            document.querySelector('#chat-text').innerHTML += ('<span class="font-weight-bold">' + data.message + '</span>' + '<br/>') 
        }
        var xH = chatWindow.scrollHeight
        chatWindow.scrollTo(0, xH)
    }
    else if(data['type']=='editor'){
        if(userName!=data.username){
            cursorPos = editor.selection.getCursor();
            // console.log(cursorPos, 'is the cursor at')
            lock = true;
            if(data['sync']){
                editor.setValue(data['text'])
                editor.clearSelection() // This will remove the highlight over the text
            }
            else if(data['text']!=null){
                editor.getSession().getDocument().applyDeltas([data['text']])
                // editor.moveCursorTo(5,5);
                // editor.moveCursorToPosition(3,0);
    
            }
            lock = false;
            editor.moveCursorToPosition(cursorPos)
            
    
        }
        // else{
        //     // console.log("no username")
        // }
    }
    else if(data['type']=='canvas'){
        // console.log('got canvas data')
        // console.log(data['data'])
        drawQueue.push(data['data'])
    }
    else if(data['type']=='output'){
        console.log("HERE")
        showOutput(data['data'])
        console.log(data)
    }
    // console.log(data)
   
}

// $(document).ready(() => {
//     // $("#editor").on('input change keyup', () => {
//     //     console.log(editor.getValue())
//     //     console.log(editor.selection.getCursor())
//     //     chatSocket.send(JSON.stringify({"text": editor.getValue(), "cursor": editor.selection.getCursor()}))                
//     // })
// })

function changeFontSize(e) {
    let val = e.value
    let ele = document.getElementById('editor')
    ele.style.fontSize=`${val}px`
}

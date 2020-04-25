
// Create medium editors
var editor = new MediumEditor('.editable_title', {
    placeholder: {
        text: 'Enter title...',
        hideOnClick: true
    },
    toolbar: false,
});

var editor = new MediumEditor('.editable_body', {
    placeholder: {
        text: 'Type your text...',
        hideOnClick: true
    }
});

// Copy the text and send it

function submit() {
var title = ""
var body = ""
title = document.getElementById('title').innerText
body  = document.getElementById('body').innerHTML

if (title != "" && body != "") {
        document.getElementsByClassName('hidden_title').value = title
        document.getElementsByClassName('hidden_body').value = body
        document.getElementById('hidden_form').submit()
        console.log('Submitted')
    }
}
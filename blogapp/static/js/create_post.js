
// Create medium editors
var editor1 = new MediumEditor('.editable_title', {
    placeholder: {
        text: 'Enter title...',
        hideOnClick: true
    },
    toolbar: false,
});

var editor = new MediumEditor('.editable_description', {
    placeholder: {
        text: 'Type a short description...',
    },
    toolbar: false,
})

var editor3 = new MediumEditor('.editable_body', {
    placeholder: {
        text: 'Type your text...',
        hideOnClick: true
    },
    anchor: {
        linkValidation: true,
    }
});

// Copy the text and send it

function submit() {
var title = ""
var body = ""
var description = ""
title = document.getElementById('title').innerText
description = document.getElementById('description').innerText
body  = document.getElementById('body').innerHTML

if (title != "" && body != "" && description != "") {
        document.getElementById('hidden_title').value = title
        document.getElementById('hidden_body').value = body
        document.getElementById('hidden_description').value = description
        document.getElementById('hidden_form').submit()
        console.log('Submitted')
    }
}
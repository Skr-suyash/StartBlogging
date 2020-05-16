  
  var quill1 = new Quill('#title', {
    modules: {
      toolbar: false,
    },
    placeholder: 'Enter a title...',
    theme: 'snow'  // or 'bubble'
  });


  var quill2 = new Quill('#description', {
    modules: {
      toolbar: false,
    },
    placeholder: 'Enter a short description...',
    theme: 'snow'  // or 'bubble'
  });


var quill3 = new Quill('#body', {
    modules: {
      toolbar: [
        [{ header: [2, 3, false] }],
        ['bold', 'italic', 'underline'],
        ['link', 'code-block', 'blockquote']
      ]
    },
    placeholder: 'Type your text...',
    theme: 'snow'  // or 'bubble'
  });


// Copy the text and send it

function publish() {
var title = ""
var body = ""
var description = ""
title = document.getElementById('title').innerText
description = document.getElementById('description').innerText
body  = quill3.root.innerHTML

console.log(title, description, body)

if (title != "" && body != "" && description != "") {
        document.getElementById('hidden_title').value = title
        document.getElementById('hidden_body').value = body
        document.getElementById('hidden_description').value = description
        document.getElementById('is_draft').value = "False"
        document.getElementById('hidden_form').submit()
        console.log('Submitted')
    }
}

function save() {
    var title = ""
    var body = ""
    var description = ""
    title = document.getElementById('title').innerText
    description = document.getElementById('description').innerText
    body  = quill3.root.innerHTML
    document.getElementById('hidden_title').value = title
    document.getElementById('hidden_body').value = body
    document.getElementById('hidden_description').value = description
    document.getElementById('is_draft').value = "True"
    document.getElementById('hidden_form').submit()
    print("Submitted Draft")
}

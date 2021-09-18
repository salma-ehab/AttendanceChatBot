const messages = document.querySelector('.messages');
const form = document.querySelector('form');
const input = document.querySelector('input');

form.addEventListener('submit',(e) =>{
    e.preventDefault();
    userMessage(input.value);
    input.value = '';});

function userMessage(message){
    messages.innerHTML += `<div class="self">${message}</div>`
    location.href = '#edge';
    $.ajax({
        data: {Usermessage: message },
        type : "POST",
        url : '/chat'
    })
    .done(function(data){
        if(data.reply){
            botMessage(data.reply); }

        else{
            botMessage("No response was found");}
});
}

function botMessage(message){
    messages.innerHTML += `<div class="bot">${message}</div>`;
    location.href = '#edge';
}
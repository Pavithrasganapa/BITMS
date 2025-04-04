function listen() {
    let inputArea = document.getElementById('input-area')
    let outputArea = document.getElementById('output-area')
  
    var recognition = new webkitSpeechRecognition();
    recognition.lang = "en-GB";
    recognition.start();
  
    recognition.onresult = function(event) {
      let transcript = event.results[0][0].transcript;
      .innerHTML = event.results[0][0].transcript;
    }
  }
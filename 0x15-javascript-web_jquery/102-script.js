$(document).ready(function(){
    $('#btn_translate').click(function(){
      let languageCode = $('#language_code').val();
      let proxyUrl = 'https://cors-anywhere.herokuapp.com/'; // Proxy server to bypass CORS
      let apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/';
      $.ajax({
        url: proxyUrl + apiUrl,
        type: 'GET',
        dataType: 'json',
        data: { lang: languageCode },
        success: function(response){
          $('#hello').text(response.hello);
        }
      });
    });
  });
  
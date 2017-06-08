  var seconds_left = 20;
            var interval = setInterval(function () {
                document.getElementById('timerdiv').innerHTML = --seconds_left;

            }, 1000);
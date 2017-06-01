  var seconds_left = 10;
            var interval = setInterval(function () {
                document.getElementById('timerdiv').innerHTML = --seconds_left;

            }, 1000);
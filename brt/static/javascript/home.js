var chart = document.getElementById('myChart').getContext('2d');


var gradient = this.chart.createLinearGradient(  0, document.getElementById('myChart').width, 0,0);
    gradient.addColorStop(0, '#ffffff');
     gradient.addColorStop(0.25, '#ffffff');
    gradient.addColorStop(1, '#aaaaaa');
    document.getElementById('myChart').style.backgroundColor = 'transparent';

Chart.defaults.global.legend.display = false;
Chart.defaults.global.defaultFont = "Poppins";
var testchart = new Chart(chart, {
	type: 'line',
	scaleOverride : true,
	scaleStartValue : 0 ,
	data: {
		labels:['Mon', 'Tue', 'Wed', 'Thurs', 'Fri'],
		datasets:[{
			backgroundColor: gradient,
			label:'Amount',
			borderColor: "#000000",
			pointBackgroundColor: "#000000",
   			pointBorderColor: "#BEC2CD",
   			pointRadius: 7,
			data:[
				{
					x:10,
					y:20000
				},
				{
					x:15,
					y:30000
				},
				{
					x:20,
					y:20000
				},
				{
					x:25,
					y:10
				},
				{
					x:30,
					y:40000
				}

			]
		}],
	},
	options:{
		scales: {
        	xAxes: [{
        		ticks: {
        			padding: 20
        			
        		},
            	gridLines: {
            		drawTicks: false,
            		color:"transparent",
                	display: true,
                	drawBorder: false,
  					zeroLineColor: "#BEC2CD",
  					zeroLineWidth: 3
            	}
        	}],
        	yAxes: [{
        		ticks: {
        			beginAtZero:true,
        			padding: 20,
        			
        		},
            	gridLines: {
            		borderDash: [8, 4],
            		drawTicks: false,
            		color:"rgba(190, 194, 205, 0.5)",
                	display: true,
                	drawBorder: false,
  					zeroLineColor: "#BEC2CD",
  					zeroLineWidth: 3
                	
            	}   
        	}]
    }
	},

	

})


$(".dropdown-toggle").dropdown();

$('.dropdown-menu').on( 'click', 'a', function() {
    var text = $(this).html();
    var htmlText = text + ' <<i class="fas fa-chevron-down"></i>';
    $(this).closest('.dropdown').find('.drop btn').html(htmlText);
});
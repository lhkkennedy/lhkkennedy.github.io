function loadcontent() {
	document.getElementById("1-Embedding-content").innerHTML += 
    "<!doctype html>

    <div class="cd-panel__content">
        <div class="col-blogEntry panel">
    
            <!-- Blog entry 1 -->
            <div class="card-blogEntry panel">
                <div id="firstChart" class="chart center">
                    <script>
                    var myChart1 = "html/json/1_Embedding/chart1_covidUKRegions.json";
                    vegaEmbed('#firstChart', myChart1);
                    </script>
                </div>
                <div class="blog-details">
                    <h3><b>Example Graph</b></h3></div>
                <div class="blog-description">
                    <h5>Given to show how to use vega to display graph <br>
                        <span class="date">4th October, 2021</span></h5>
                </div>
            </div>
            <hr>
            
            <!-- Blog entry 2 -->
            <div class="card-blogEntry panel">
                <div id="secondChart" class="chart center">
                    <script>
                    var myChart2 = "html/json/1_Embedding/chart2_ukProductivity.json";
                    vegaEmbed('#secondChart', myChart2);
                    </script>
                </div>
                <div class="blog-details">
                    <h3><b>Historical Data</b></h3>
                </div>
                <div class="blog-description">
                    <h5>Data was sourced from ONS as csv file</h5>
                </div>
            </div>
            <hr>
    
            <!-- Blog entry 3 -->
            <div class="card-blogEntry panel">
                <div class="chart center" id="thirdChart">
                    <script>
                    var myChart3 = "html/json/1_Embedding/chart3_givenBitcoin.json";
                    vegaEmbed('#thirdChart', myChart3);
                    </script>
                </div>
                <div class="blog-details">
                    <h3><b>Bitcoin chart taken from rapidcharts.io</b></h3></div>
                <div class="blog-0description">
                    <h5>Data was sourced from Coinbase via FRED</h5>
                </div>
            </div>
            <hr>
        <!-- END BLOG ENTRIES -->
        </div>";
}
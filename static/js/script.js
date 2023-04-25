// server address
var server = 'http://127.0.0.1:5000';

function formatDate(date) {
    var date = new Date(date);
    var year = date.getFullYear()
    var month = date.getMonth() + 1
    var day = date.getDate()
    var dateString = `${year}-${month}-${day}`
    return dateString
}

function formatTemprature(temperature){
    // convert "5" to "5°"
    var t = temperature + '°'
    return t
}

// 使用echarts的折线显示天气数据,横坐标是时间,纵坐标是温度
function showWeatherChart(data) {
    var myChart = echarts.init(document.getElementById('weatherChart'));
    // 指定图表的配置项和数据
    // 鼠标移动到折线上,显示日期,最高气温,最低气温,天气,风向,风力,空气指数,空气信息,空气等级
    var option = {
        title: {
            text: '天气数据'
        },
        tooltip: {
        },
        legend: {
            data:['温度']
        },
        xAxis: {
            data: data.map(function(item) {
                return formatDate(item.date);
            })
        },
        // set yAxis unit to °
        yAxis: {
            axisLabel: {
                formatter: formatTemprature
            }
        },
        // display hight and low temperature
        series: [{
            name: '最高温度',
            type: 'line',
            data: data.map(function(item) {
                return item.high_temp;
            })
        }, {
            name: '最低温度',
            type: 'line',
            data: data.map(function(item) {
                return item.low_temp;
            })
        }]
    };
    //鼠标移动到折线上,显示日期,最高气温,最低气温,天气,风向,风力,空气指数,空气信息,空气等级
    myChart.on('mouseover', function (params) {
        var index = params.dataIndex
        var date = formatDate(data[index].date)
        var high = formatTemprature(data[index].high_temp)
        var low =  formatTemprature(data[index].low_temp)
        var type = data[index].weather
        var fengxiang = data[index].wind_direction
        var fengli = data[index].wind_power
        var aqi = data[index].air_index
        var quality = data[index].air_info
        var pm25 = data[index].air_level
        var tips = `日期: ${date}`
        tips += `<br>最高气温: ${high}`
        tips += `<br>最低气温: ${low}`
        tips += `<br>天气: ${type}`
        tips += `<br>风向: ${fengxiang}`
        tips += `<br>风力: ${fengli}`
        tips += `<br>空气指数: ${aqi}`
        tips += `<br>空气信息: ${quality}`
        tips += `<br>空气等级: ${pm25}`
        option.tooltip.formatter = tips
        myChart.setOption(option)
    })
    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
}


// 使用echarts的折线显示人口数据，横坐标是时间，纵坐标是人口
function showPopulationChart(data) {
    var myChart = echarts.init(document.getElementById('populationChart'));
    console.log('data', data)
    // 指定图表的配置项和数据
    var option = {
        title: {
            text: '人口数据'
        },
        tooltip: {},
        legend: {
            data:['人口']
        },
        xAxis: {
            data: data.map(function(item) {
                return item.year;
            }
        )},
        yAxis: {},
        series: [{
            name: '人口',
            type: 'line',
            data: data.map(function(item) {
                return item.population;
            }
        )}]
    };
    myChart.on('mouseover', function (params) {
        var index = params.dataIndex
        var year = data[index].year
        var population = data[index].population
        var tips = `年份: ${year}`
        tips += `<br>人口: ${population}`
        option.tooltip.formatter = tips
        myChart.setOption(option)
    })
    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
}


// 使用echarts的折线显示GDP数据，横坐标是时间，纵坐标是GDP
function showIndustrialChart(data) {
    var myChart = echarts.init(document.getElementById('industrialChart'));
    console.log('data', data)
    // 指定图表的配置项和数据
    var option = {
        title: {
            text: '工业生产总值数据'
        },
        tooltip: {},
        legend: {
            data:['production']
        },
        xAxis: {
            data: data.map(function(item) {
                return item.year;
            }
        )},
        yAxis: {},
        series: [{
            name: 'production',
            type: 'line',
            data: data.map(function(item) {
                return item.production;
            }
        )}]
    };
    myChart.on('mouseover', function (params) {
        var index = params.dataIndex
        var year = data[index].year
        var gdp = data[index].production
        var tips = `年份: ${year}`
        tips += `<br>Production: ${gdp}`
        option.tooltip.formatter = tips
        myChart.setOption(option)
    })
    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
}

// 使用echarts的折线显示finance数据，横坐标是年份，纵坐标是金额,单位是(万元)
function showFinanceChart(data) {
    var myChart = echarts.init(document.getElementById('financeChart'));
    console.log('data', data)
    // 指定图表的配置项和数据
    var option = {
        title: {
            text: '财政收入数据'
        },
        tooltip: {},
        legend: {
            data:['finance']
        },
        xAxis: {
            data: data.map(function(item) {
                return item.year;
            }
        )},
        yAxis: {},
        series: [{
            name: 'finance',
            type: 'line',
            data: data.map(function(item) {
                return item.money;
            }
        )}]
    };
    myChart.on('mouseover', function (params) {
        var index = params.dataIndex

        var year = data[index].year
        var finance = data[index].money;
        var tips = `年份: ${year}`
        tips += `<br>Finance: ${finance}`
        option.tooltip.formatter = tips
        myChart.setOption(option)
    })
    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
}



// append data in table
function appendDataInTable(data) {
    // append data in table
    var table = document.getElementById('table')
    for(var i in data) {
        var row = `<tr>
                        <td>${data[i].name}</td>
                        <td>${data[i].age}</td>
                        <td>${data[i].city}</td>
                  </tr>`
        table.innerHTML += row
    }
}
// when click the button,then delete the row
function deleteRow(row) {
    var i = row.parentNode.parentNode.rowIndex;
    document.getElementById("table").deleteRow(i);
}

// when click the button,then add the row
function addRow() {
    var table = document.getElementById('table')
    var row = `<tr>
                    <td><input type="text" id="name"></td>
                    <td><input type="text" id="age"></td>
                    <td><input type="text" id="city"></td>
                    <td><button onclick="saveRow(this)">Save</button></td>
                    <td><button onclick="deleteRow(this)">Delete</button></td>
              </tr>`
    table.innerHTML += row
}


// user jquery to get data from server the url is "weather",the method is "POST",the data is "startDatetime, endDatetime"
function getDataFromServer(startDatetime, endDatetime) {
    return $.ajax({
        url: server + '/weather',
        type: 'POST',
        dataType: 'json',
        data: {
            startDatetime: startDatetime,
            endDatetime: endDatetime
        },
        success: function(data) {
            return data
        },
        error: function(err) {
            console.log(err)
        }
    })
}

// get post data from server by city id
function getPopulationFromServer(cityId) {
    return $.ajax({
        url: server + '/population',
        type: 'POST',
        dataType: 'json',
        data: {
            cityId: cityId
        },
        success: function(data) {
            return data
        },
        error: function(err) {
            console.log(err)
        }
    })
}

// get industrial data from server
function getIndustrialFromServer() {
    return $.ajax({
        url: server + '/industrial',
        type: 'POST',
        dataType: 'json',
        success: function(data) {
            return data
        },
        error: function(err) {
            console.log(err)
        }
    })
}

// get finance data from server
function getFinanceFromServer() {
    return $.ajax({
        url: server + '/finance',
        type: 'POST',
        dataType: 'json',
        success: function(data) {
            return data
        },
        error: function(err) {
            console.log(err)
        }
    })
}


jQuery(document).ready(function($) {
    // add one day and get data from server every 1 second
    var startDatetime = '2015-01-01'
    var endDatetime = '2015-01-31'
    setInterval(function() {
        getDataFromServer(startDatetime,endDatetime).then(function(data) {
            showWeatherChart(data);
        })

        // if endDatetime > startDatetime + 60 days,then startDatetime = endDatetime - 60 days
        var startDate = new Date(startDatetime)
        var endDate = new Date(endDatetime)

        startDate.setDate(startDate.getDate() + 60)
        if (startDate < endDate) {
            startDate = endDate;
            startDatetime =formatDate(new Date(startDatetime).setDate(startDate.getDate() + 1))
        }

        endDate.setDate(endDate.getDate() + 1)
        endDatetime = formatDate(endDate)
    }, 1000)

    // 显示人口数据
    var cityId = 0
    getPopulationFromServer(cityId).then(function(data) {
        showPopulationChart(data)
    })

    // 显示工业数据
    getIndustrialFromServer().then(function(data) {
        console.log('data', data);
        showIndustrialChart(data)
    })

    // 显示财政数据
    getFinanceFromServer().then(function(data) {
        console.log('data', data);
        showFinanceChart(data)
    })
})
import React from "react";
// import {Card} from "antd";
import ReactEcharts from "echarts-for-react";
import heatMap from "./pic"

const echarts = require('./echarts.min.js');
// const echarts = require('echarts');
const tree = require("./data.json");

const Chart: React.FC<{}> = props => {

  // const ref = React.useRef(null);
  let myChart = echarts.init(document.getElementById('heatmap'));

  let app = {title:'股价热力图'};
  myChart.showLoading();

  heatMap(tree, myChart, echarts);
  return (
    <div>
      <ReactEcharts option={this.getOption()} />
    </div>
  )
};

export default Chart;

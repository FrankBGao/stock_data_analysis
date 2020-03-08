import echarts from "./echarts.min"

function heatMap(data, name) {
  convertData(data);

  function convertData(originList) {
    let min = Infinity;
    let max = -Infinity;

    for (let i = 0; i < originList.length; i++) {
      const node = originList[i];
      if (node) {
        let value = node.value;
        value[2] != null && value[2] < min && (min = value[2]);
        value[2] != null && value[2] > max && (max = value[2]);
      }
    }

    for (let i = 0; i < originList.length; i++) {
      let node = originList[i];
      if (node) {
        if (node.children) {
          convertData(node.children);
        }
      }
    }
  }


  function isValidNumber(num) {
    return num != null && isFinite(num);
  }

  // myChart.setOption(option = );
  const option = {
    title: {
      left: 'center',
      text: name + '-热力图',
      subtext: '面积大小与市值成正比，颜色与当日涨跌有关'
    },
    tooltip: {
      formatter: function (info) {
        let value = info.value;

        let change = value[1];
        change = isValidNumber(change)
          ? change.toFixed(2) + '%'
          : '-';
        let open = value[2];
        open = isValidNumber(open)
          ? echarts.format.addCommas(open) + ''
          : '-';
        let high = value[3];
        high = isValidNumber(high)
          ? echarts.format.addCommas(high) + ''
          : '-';
        let low = value[4];
        low = isValidNumber(low)
          ? echarts.format.addCommas(low) + ''
          : '-';

        return [
          '<div class="tooltip-title">' + echarts.format.encodeHTML(info.name) + '</div>',
          '涨幅: &nbsp;&nbsp;' + change + '<br>',
          '开盘: &nbsp;&nbsp;' + open + '<br>',
          '最高: &nbsp;&nbsp;' + high + '<br>',
          '最低: &nbsp;&nbsp;' + low + '<br>',
        ].join('');
      }
    },
    series: [{
      name: '股价',
      top: 80,
      type: 'treemap',
      label: {
        show: true,
        formatter: "{b}",
        color: '#cccccc',
        normal: {
          textStyle: {
            ellipsis: true
          }
        }
      },
      upperLabel: {
        normal: {
          show: true,
          height: 30,
          color: '#cccccc'
        }
      },
      itemStyle: {
        normal: {
          borderColor: 'grey',

        }
      },
      levels: [
        {
          upperLabel: {
            normal: {
              show: false,
              height: 30,
              color: '#cccccc'
            }
          },
          itemStyle: {
            normal: {
              borderWidth: 3,
              gapWidth: 3
            }
          }

        },


      ],
      data: data
    }]
  };
  return (option);

}

export default heatMap;

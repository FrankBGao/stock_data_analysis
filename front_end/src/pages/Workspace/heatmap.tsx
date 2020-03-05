import React from 'react';
import {
  Chart,
  Geom,
  Axis,
  Tooltip,
  Label,
} from 'bizcharts';
import DataSet from "@antv/data-set";

class Heatmap extends React.Component {
  render() {
    const data =
      [{'row': 0, 'col': 0, 'label': 'in_freq', 'color': 3, 'freq': 1}, {'row': 0, 'col': 1, 'label': '1.|2|', 'color': 6, 'freq': 1}, {'row': 0, 'col': 2, 'label': '2.|2|', 'color': 2, 'freq': 1}, {'row': 0, 'col': 3, 'label': '3.|2|', 'color': 7, 'freq': 1}, {'row': 0, 'col': 4, 'label': '4.|4|', 'color': 1, 'freq': 1}, {'row': 0, 'col': 5, 'label': '1', 'color': 5, 'freq': 1}, {'row': 0, 'col': 6, 'label': '2', 'color': 0, 'freq': 1}, {'row': 0, 'col': 7, 'label': '3', 'color': 4, 'freq': 1}]    ;
    const cols = {
      row: {
        type: 'cat',
      },
      col: {
        type: 'cat',
        values: ["0","1","2","3","4","5","6","7","8","9"]
      },
    };
    // row 是反的
    return (
      <div>
        <Chart
          height={window.innerHeight}
          data={data}
          scale={cols}
          padding={[20, 80, 120, 85]}
          forceFit
        >
          <Axis
            name="row"
            grid={{
              align: 'center',
              lineStyle: {
                lineWidth: 1,
                lineDash: null,
                stroke: '#f0f0f0',
              },
              showFirstLine: true,
            }}
          />
          <Axis
            name="col"
            grid={{
              align: 'center',
              lineStyle: {
                lineWidth: 1,
                lineDash: null,
                stroke: '#f0f0f0',
              },
            }}
          />
          <Tooltip
            showTitle={false}
            containerTpl= {
              '<div class="g2-tooltip">'
              + '<div class="g2-tooltip-title" style="margin-bottom: 4px;"></div>'
              + '<ul class="g2-tooltip-list"></ul>'
              + '</div>'
            }
            itemTpl= {
              '<li data-index=1>'
              + '<span style="background-color:{color};width:8px;height:8px;border-radius:50%;display:inline-block;margin-right:8px;"></span>{label}</br>'
              + '数量' + ': {freq}</br>'
              + '</li>'
            }
          />
          <Geom
            type="polygon"
            position="col*row"
            tooltip={[
              "label*freq",
              (label, freq) => {
                return {
                  label: label,
                  freq: freq,
                };
              }
            ]}
            color={['color', '#BAE7FF-#1890FF-#0050B3']}
            style={{
              stroke: '#fff',
              lineWidth: 1,
            }}
          >
            <Label
              content="label"
              offset={-2}
              textStyle={{
                fill: '#fff',
                fontWeight: 'bold',
                shadowBlur: 2,
                shadowColor: 'rgba(0, 0, 0, .45)',
              }}
            />
          </Geom>
        </Chart>
      </div>
    );
  }
}

export default Heatmap;

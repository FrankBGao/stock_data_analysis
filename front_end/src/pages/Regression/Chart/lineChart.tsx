import React from "react";
import {
  G2,
  Chart,
  Geom,
  Axis,
  Tooltip,
  Coord,
  Label,
  Legend,
  View,
  Guide,
  Shape,
  Facet,
  Util
} from "bizcharts";

interface ChartState {

}

interface ChartProps {
  data: any
}

class Curved extends React.Component<ChartProps, ChartState> {

  constructor(props: { data: any, }) {//dispatch: Dispatch
    super(props);

    this.state = {
      data: props.data
    };
  }

  render() {
    const data = [
      {
        "start": 23.99,
        "max": 24.21,
        "end": 23.4,
        "min": 23.28,
        "volumn": 2914357.25,
        "price_change": -1.37,
        "p_change": -5.53,
        "time": "2020-02-28",
        "point": 23.99,
        "ptype": "in_trend",
        "cash": 1015.0,
        "stock_value": 149760.0,
        "all": 150775.0,
        "earn": 50775.0,
        "earn_percentage": 0.50775,
        "stock": "600030",
        "quantity": null,
        "type_is": null,
        "option": null,
        "money": 69915430.4274999946
      },
      // {
      //   month: "Dec",
      //   city: "London",
      //   temperature: 4.8
      // }
    ];
    const cols = {
      time: {
        type: "timeCat",
        nice: false,
        range: [0, 1]
      },
      earn_percentage: {
        alias: "盈利率"
      },
    };
    return (
      <div>
        <Chart height={400} data={this.props.data} scale={cols} forceFit>
          <Legend/>
          <Axis name="time"/>
          <Axis
            name="earn_percentage"
            // label={{
            //   formatter: val => `${val}°C`
            // }}
          />
          <Tooltip
            crosshairs={{
              type: "y"
            }}
          />
          <Geom
            type="line"
            position="time*earn_percentage"
            size={2}
            color='#0ea7ff'
            shape={"smooth"}
          />
          <Geom
            type="point"
            position="time*earn_percentage"
            size={['type_is', (type_is) => {
              if (type_is === "sell") return 4;
              if (type_is === "buy") return 4;
              return 2
            }]}
            shape={"circle"}
            color={['type_is', (type_is) => {
              if (type_is === null) return '#0ea7ff';
              if (type_is === "sell") return 'green';
              if (type_is === "buy") return 'red';
              return '#0ea7ff'
            }]}
            style={{
              lineWidth: 1
            }}
          />
        </Chart>
      </div>
    );
  }
}

export default Curved;
